from django.shortcuts import render


from .models import AniRegForm
from django.utils import timezone
from django.contrib.auth.models import User


def AniRegFormView(request):
#    posts = User.objects.all()
#    posts = AniRegForm.objects.all()
    posts = AniRegForm.objects.filter(registration_date__lte=timezone.now()).order_by('registration_date')

    return render(request, 'AniReg/AniRegForm.html', {})


from .forms import webform
def form_new(request):
    form = webform()
    return render(request, 'AniReg/web_form.html', {'form': form})