from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def index(request):
    return render(request, 'about.html')
def index(request):
    return render(request, 'contact_us.html')