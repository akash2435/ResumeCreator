from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def create(request):
    return render(request, 'createResume.html')

def steptwo(request):
    return render(request, 'create_next2.html')