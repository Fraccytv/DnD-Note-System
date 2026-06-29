
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('make_campaign/', views.MakeCampaignView.as_view(), name='make_campaign'),
    path('campaign/<int:campaign_id>/', views.CampaignDetailView.as_view(), name='campaign_detail'),
    path('note/<int:campaign_id>/', views.MakeNoteView.as_view(), name='make_note'),
]
