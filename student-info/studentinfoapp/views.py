from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Student


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = ''
        if user != None:
            login(request, user)
            user_type = user.user_type

            if user_type == '1':
                return redirect('admin_home')

            elif user_type == '2':
                return redirect('staff_home')

            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            # return HttpResponseRedirect("/")
            return redirect('login')


def insert(request):
    return render(request, 'insert.html')


def view_student(request):
    return render(request, 'view.html')


def view_student(request, student_id):
    a_list = Student.objects.filter(id=student_id)
    context = {'id': student_id, 'student': a_list}
    return render(request, 'view.html', context)
