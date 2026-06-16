
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.mainview.home, name='home'),
]
