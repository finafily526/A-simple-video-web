from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def houtai(request):
    return render(request, 'index.html')
def houtai1(request):
    return render(request, 'index1.html')
def video(request):
    return render(request, 'video.html')
