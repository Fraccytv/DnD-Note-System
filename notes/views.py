from django.shortcuts import render, redirect
from django.views import View
from .forms import CampaignForm, NoteForm
from .models import Campaign, Note

# Create your views here.


class MainView(View):
    def get(self, request):
        campaigns = Campaign.objects.all()
        return render(request, "notes/home.html", {"campaigns": campaigns})


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
