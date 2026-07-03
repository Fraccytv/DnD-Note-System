from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import CampaignForm, NoteForm
from .models import Campaign, Note

# Create your views here.


## Home page
class MainView(View):
    def get(self, request):
        campaigns = Campaign.objects.all()
        return render(request, "notes/home.html", {"campaigns": campaigns})


## Campaign Views
class MakeCampaignView(View):
    def get(self, request):
        form = CampaignForm()
        context = {"form": form}
        return render(request, "notes/make_campaign.html", context)

    def post(self, request):
        form = CampaignForm(request.POST)
        campaigns = Campaign.objects.all()
        context = {"form": form, "campaigns": campaigns}
        if form.is_valid():
            form.save()
            return redirect("campaign_detail", campaign_id=form.instance.id)
        else:
            print("Form is not valid", form.errors)

        return render(request, "notes/home.html", context)


class CampaignDetailView(View):
    def get(self, request, campaign_id):
        campaign_obj = Campaign.objects.get(id=campaign_id)
        notes = Note.objects.filter(campaign=campaign_obj)
        context = {
            "campaign": campaign_obj,
            "notes": notes,
        }
        return render(request, "notes/campaign_detail.html", context)


class DeleteCampaignView(View):
    def post(self, request, campaign_id):
        campaign_obj = Campaign.objects.get(id=campaign_id)
        campaign_obj.delete()
        return redirect("home")


## Note Views
class MakeNoteView(View):
    def get(self, request, campaign_id):
        form = NoteForm()
        context = {"form": form, "campaign_id": campaign_id}
        return render(request, "notes/make_notes.html", context)

    def post(self, request, campaign_id):
        campaign_obj = Campaign.objects.get(id=campaign_id)
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.campaign = campaign_obj
            note.save()
        return redirect("campaign_detail", campaign_id=campaign_id)


class EditNoteView(View):
    def get(self, request, note_id):
        note_obj = Note.objects.get(id=note_id)
        form = NoteForm(instance=note_obj)
        context = {
            "form": form,
            "note": note_obj,
        }
        return render(request, "notes/edit_note.html", context)

    def post(self, request, note_id):
        note_obj = Note.objects.get(id=note_id)
        form = NoteForm(request.POST, instance=note_obj)
        if form.is_valid():
            form.save()
            return redirect("campaign_detail", campaign_id=note_obj.campaign.id)
        else:
            print("Form is not valid", form.errors)
            context = {
                "form": form,
                "note": note_obj,
            }
            return render(request, "notes/edit_note.html", context)


class DeleteNoteView(View):
    def post(self, request, note_id):
        note_obj = Note.objects.get(id=note_id)
        campaign_id = note_obj.campaign.id
        note_obj.delete()
        return redirect("campaign_detail", campaign_id=campaign_id)


## Login / Logout / Register Views
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

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect("login")


class LoginView(View):
    def get(self, request):
        return render(request, "registration/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request,
                "registration/login.html",
                {"error": "Invalid credentials."},
            )


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
