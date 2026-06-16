from django.shortcuts import render

# Create your views here.

class mainview():
    def home(request):
        return render(request, 'home.html')
    
    def make_campaign(request):
        return render(request, 'make_campaign.html')