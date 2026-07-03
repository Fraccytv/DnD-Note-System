from django.urls import path, include
from . import views

urlpatterns = [
    ## Home page
    path("", views.MainView.as_view(), name="home"),
    ##Campaign page / delete campaign
    path("make_campaign/", views.MakeCampaignView.as_view(), name="make_campaign"),
    path(
        "campaign/<int:campaign_id>/",
        views.CampaignDetailView.as_view(),
        name="campaign_detail",
    ),
    path(
        "delete_campaign/<int:campaign_id>/",
        views.DeleteCampaignView.as_view(),
        name="delete_campaign",
    ),
    ## Make note / Edit note pages / delete note
    path("note/<int:campaign_id>/", views.MakeNoteView.as_view(), name="make_note"),
    path("edit_note/<int:note_id>/", views.EditNoteView.as_view(), name="edit_note"),
    path(
        "delete_note/<int:note_id>/", views.DeleteNoteView.as_view(), name="delete_note"
    ),
    ## Login / Logout / Register
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
]
