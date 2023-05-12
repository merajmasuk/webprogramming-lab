# Create your views here.
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models


class EmployeeBaseView(View):
    model = models.Employee
    fields = '__all__'
    success_url = reverse_lazy('day3:all')


class EmployeeListView(EmployeeBaseView, ListView):
    """_summary_"""


class EmployeeDetailView(EmployeeBaseView, DetailView):
    """_summary_"""


class EmployeeCreateView(EmployeeBaseView, CreateView):
    """_summary_"""


class EmployeeUpdateView(EmployeeBaseView, UpdateView):
    """View to update a Day3"""


class EmployeeDeleteView(EmployeeBaseView, DeleteView):
    """View to delete a Day3"""
