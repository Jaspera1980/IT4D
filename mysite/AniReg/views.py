from django.shortcuts import render

def AniRegForm(request):
    return render(request, 'AniReg/AniRegForm.html', {})