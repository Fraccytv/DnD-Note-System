from .models import campaign, note
from django import forms

class campaignForm(forms.ModelForm):
    class Meta:
        model = campaign
        fields = ['name', 'description']