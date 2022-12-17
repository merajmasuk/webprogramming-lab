from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from . import forms, models


# Create your views here.
def CreateStudent(request):
    if request.method == "POST":
        form = forms.CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.CreateStudentForm()
    else:
        form = forms.CreateStudentForm()

    students = models.Student.objects.all().order_by("-id")
    context = {'form': form, 'students': students}
    return render(request, 'index.html', context)


def GetStudent(request, **kwargs):
    reg = kwargs.get('reg')
    student = get_object_or_404(models.Student, reg_no=reg)

    if request.method == "POST":
        form = forms.CreateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:
        form = forms.CreateStudentForm(instance=student)

    context = {'student': student, 'form': form}
    return render(request, 'std_detail.html', context)


def DeleteStudent(request, **kwargs):
    reg = kwargs.get('reg')
    student = models.Student.objects.get(reg_no=reg)
    student.delete()
    return redirect(CreateStudent)


def UpdateStudent(request, **kwargs):
    Id = kwargs.get('id')
    student = models.Student.objects.get(id=Id)
    if request.method == "POST":
        form = forms.CreateStudentForm(instance=student)
        student.name = request.POST['name']
        student.present_address = request.POST['present_address']
        student.reg_no = request.POST['reg_no']
        student.save()
        print(student)
        print(request)
        return redirect(reverse('.views.GetStudent', kwargs=dict(student)))
    else:
        form = forms.CreateStudentForm(instance=student)
        context = {'student': student, 'form': form}
        return render(request, 'update.html', context)
