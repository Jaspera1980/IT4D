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
    if request.method == "POST":
        form = webform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.veterinarian = request.user
            post.registration_date = timezone.now()
            post.treatment_date = timezone.now()
            post.save()
    else:
        form = webform()

    return render(request, 'AniReg/web_form.html', {'form': form})


#def form_new(request):
#    form = webform()
#    return render(request, 'AniReg/web_form.html', {'form': form})