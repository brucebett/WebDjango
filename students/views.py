from django.contrib import messages
from django.shortcuts import render, redirect

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

    if request.method == 'POST':
        form = NewStudentComplainForm(request.POST)
    if form.is_valid():
        # print("VALID")
        form.save()
        NewStudentComplainForm()
        messages.success(request, 'User Registered Successfully')
        return redirect('register')
    else:
        form = NewStudentComplainForm()
    return render(request, 'register.html', {'form': form})
