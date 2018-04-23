from django import forms
from .models import AniRegForm

class webform(forms.ModelForm):
    class Meta:
        model = AniRegForm
        fields = ('treatment_1', 'comments')
