from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def content_1(request):
    return render(request, 'contents/content_1.html')

def content_2(request):
    return render(request, 'contents/content_2.html')