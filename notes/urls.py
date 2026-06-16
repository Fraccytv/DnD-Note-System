
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('make_campaign/', views.MakeCampaignView.as_view(), name='make_campaign'),
]
