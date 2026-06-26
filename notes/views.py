from django.shortcuts import render
from django.views import View
from .forms import campaignForm
from .models import campaign, note

# Create your views here.


class MainView(View):
    def get(self, request):
        campaigns = campaign.objects.all()
        return render(request, "home.html", {"campaigns": campaigns})


class MakeCampaignView(View):
    def get(self, request):
        form = campaignForm()
        campaigns = campaign.objects.all()
        context = {"form": form, "campaigns": campaigns}
        return render(request, "make_campaign.html", context)

    def post(self, request):
        form = campaignForm(request.POST)
        campaigns = campaign.objects.all()
        context = {"form": form, "campaigns": campaigns}
        if form.is_valid():
            print("Form is valid")
            form.save()
        else:
            print("Form is not valid", form.errors)

        return render(request, "home.html", context)

class campaignDetailView(View):
    def get(self, request, campaign_id):
        campaign_obj = campaign.objects.get(id=campaign_id)
        notes = note.objects.filter(campaign=campaign_obj)
        context = {"campaign": campaign_obj, "notes": notes}
        return render(request, "campaign.html", context)