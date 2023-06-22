from django import forms
from .models import JoinCode

class JoinCodeForm(forms.ModelForm):
    class Meta:
        model = JoinCode
        fields = ['code']
