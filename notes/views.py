from django.shortcuts import render
from django.views import View
from .forms import campaignForm

# Create your views here.


class MainView(View):
    def get(self, request):
        print("MainView GET")
        return render(request, "home.html")


class MakeCampaignView(View):
    def get(self, request):
        form = campaignForm()
        return render(request, "make_campaign.html", {"form": form})

    def post(self, request):
        form = campaignForm(request.POST)
        print("MakeCampaignView POST", form)
        if form.is_valid():
            print("Form is valid")
            form.save()
        else:
            print("Form is not valid", form.errors)

        return render(request, "home.html", {"form": form})
