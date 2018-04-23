

# Create your views here.
from django.http import HttpResponse


def AniRegForm(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#from .forms import PostForm

#def post_new(request):
#    form = PostForm()
#    return render(request, 'blog/post_edit.html', {'form': form})

from django.shortcuts import render

#def AniRegForm(request):
#    return render(request, 'AniReg/index.html')