from django.shortcuts import render

from students.forms import StudentForm, NewStudentComplainForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def login(request):
    form = StudentForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    form = NewStudentComplainForm()
    return render(request, 'register', {'form', 'boby'})
