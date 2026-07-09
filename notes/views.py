from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CampaignForm, NoteForm
from .models import Campaign, Note

from django.db.models import Q

# -----------------------
# Helpers
# -----------------------


def user_has_campaign_access(campaign, user):
    is_dm = campaign.created_by == user
    is_member = campaign.members.filter(id=user.id).exists()

    return is_dm or is_member


# -----------------------
# Home
# -----------------------


class MainView(View):
    def get(self, request):
        if request.user.is_authenticated:
            campaigns = Campaign.objects.filter(created_by=request.user)
            members_campaigns = Campaign.objects.filter(members=request.user)
        else:
            campaigns = []
            members_campaigns = []

        context = {"campaigns": campaigns, "members_campaigns": members_campaigns}
        return render(
            request,
            "notes/home.html",
            context,
        )


# -----------------------
# Campaign Views
# -----------------------


class MakeCampaignView(LoginRequiredMixin, View):
    def get(self, request):
        form = CampaignForm()

        return render(
            request,
            "notes/make_campaign.html",
            {"form": form},
        )

    def post(self, request):
        form = CampaignForm(request.POST)

        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.created_by = request.user
            campaign.save()

            return redirect(
                "campaign_detail",
                campaign_id=campaign.id,
            )

        return render(
            request,
            "notes/make_campaign.html",
            {"form": form},
        )


class CampaignDetailView(LoginRequiredMixin, View):
    def get(self, request, campaign_id):
        campaign = get_object_or_404(
            Campaign,
            id=campaign_id,
        )

        if not user_has_campaign_access(campaign, request.user):
            return redirect("home")

        notes = Note.objects.filter(campaign=campaign)

        search = request.GET.get("search".strip())
        sort = request.GET.get("sort")

        if search:
            notes = notes.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )

        if sort == "oldest":
            notes = notes.order_by("created_at")
        else:
            notes = notes.order_by("-created_at")

        users = [campaign.created_by]
        users.extend(campaign.members.all())

        return render(
            request,
            "notes/campaign_detail.html",
            {
                "campaign": campaign,
                "notes": notes,
                "users": users,
                "is_dm": campaign.created_by == request.user,
                "is_member": campaign.members.filter(id=request.user.id).exists(),
            },
        )


class DeleteCampaignView(LoginRequiredMixin, View):
    def post(self, request, campaign_id):
        campaign = get_object_or_404(
            Campaign,
            id=campaign_id,
            created_by=request.user,
        )

        campaign.delete()

        return redirect("home")


class AddMemberView(LoginRequiredMixin, View):
    def post(self, request, campaign_id):
        campaign = get_object_or_404(
            Campaign,
            id=campaign_id,
            created_by=request.user,
        )

        username = request.POST.get("username")

        try:
            user_to_add = User.objects.get(username=username)
        except User.DoesNotExist:
            return redirect(
                "campaign_detail",
                campaign_id=campaign.id,
            )

        if user_to_add != campaign.created_by:
            campaign.members.add(user_to_add)

        return redirect(
            "campaign_detail",
            campaign_id=campaign.id,
        )


# -----------------------
# Note Views
# -----------------------


class MakeNoteView(LoginRequiredMixin, View):
    def get(self, request, campaign_id):
        campaign = get_object_or_404(
            Campaign,
            id=campaign_id,
        )

        if not user_has_campaign_access(campaign, request.user):
            return redirect("home")

        form = NoteForm()

        return render(
            request,
            "notes/make_notes.html",
            {
                "form": form,
                "campaign": campaign,
                "campaign_id": campaign_id,
            },
        )

    def post(self, request, campaign_id):
        campaign = get_object_or_404(
            Campaign,
            id=campaign_id,
        )

        if not user_has_campaign_access(campaign, request.user):
            return redirect("home")

        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.campaign = campaign
            note.created_by = request.user
            note.save()

        return redirect(
            "campaign_detail",
            campaign_id=campaign.id,
        )


class EditNoteView(LoginRequiredMixin, View):
    def get(self, request, note_id):
        note = get_object_or_404(
            Note,
            id=note_id,
            created_by=request.user,
        )

        campaign = note.campaign

        form = NoteForm(instance=note)

        return render(
            request,
            "notes/edit_note.html",
            {
                "form": form,
                "note": note,
                "campaign": campaign,
            },
        )

    def post(self, request, note_id):
        note = get_object_or_404(
            Note,
            id=note_id,
            created_by=request.user,
        )

        campaign = note.campaign

        form = NoteForm(
            request.POST,
            instance=note,
        )

        if form.is_valid():
            form.save()

            return redirect(
                "campaign_detail",
                campaign_id=campaign.id,
            )

        return render(
            request,
            "notes/edit_note.html",
            {
                "form": form,
                "note": note,
                "campaign": campaign,
            },
        )


class DeleteNoteView(LoginRequiredMixin, View):
    def post(self, request, note_id):
        note = get_object_or_404(
            Note,
            id=note_id,
        )

        campaign_id = note.campaign.id
        campaign = note.campaign

        is_dm = campaign.created_by == request.user
        is_note_owner = note.created_by == request.user

        if not (is_dm or is_note_owner):
            return redirect("home")

        note.delete()

        return redirect(
            "campaign_detail",
            campaign_id=campaign_id,
        )


# -----------------------
# Authentication
# -----------------------


class RegisterView(View):
    def get(self, request):
        return render(request, "registration/register.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if password != password_confirm:
            return render(
                request,
                "registration/register.html",
                {"error": "Passwords do not match."},
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "registration/register.html",
                {"error": "Username already exists."},
            )

        User.objects.create_user(
            username=username,
            password=password,
        )

        return redirect("login")


class LoginView(View):
    def get(self, request):
        return render(request, "registration/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        return render(
            request,
            "registration/login.html",
            {"error": "Invalid credentials."},
        )


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")
