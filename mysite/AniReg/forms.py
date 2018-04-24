from django.forms import ModelForm
from .models import AniRegForm

class webform(ModelForm):
    class Meta:
        model = AniRegForm
        exclude = ['registration_date', 'veterinarian', 'treatment_date']

