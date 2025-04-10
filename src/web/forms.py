from django import forms
from .models import OpportunityRequest

class OpportunityRequestForm(forms.ModelForm):
    opportunity_type = forms.CharField(widget=forms.HiddenInput())  # Hidden field for opportunity type

    class Meta:
        model = OpportunityRequest
        fields = ['full_name', 'email', 'message', 'opportunity_type']