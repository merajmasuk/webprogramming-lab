from django.http import Http404
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from . import models, serializer


class EmployeeList(APIView):
    """
    List all Employee, or create a new Employee.
    """

    def get(self, request, format=None):
        Employees = models.Employee.objects.all()
        employeeSerializer = serializer.EmployeeSerializer(Employees, many=True)
        return Response(employeeSerializer.data)

    def post(self, request, format=None):
        employeeSerializer = serializer.EmployeeSerializer(data=request, many=True)
        if employeeSerializer.is_valid():
            employeeSerializer.save()
            return Response(employeeSerializer.data, status=status.HTTP_201_CREATED)
        return Response(employeeSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    """
    Retriece, update or delete an Employee instance
    """

    def get_object(self, pk):
        try:
            return models.Employee.objects.get(pk=pk)
        except models.Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Employee = self.get_object(pk)
        employeeSerializer = serializer.EmployeeSerializer(Employee)
        return Response(employeeSerializer.data)

    def put(self, request, pk, format=None):
        Employee = self.get_object(pk)
        employeeSerializer = serializer.EmployeeSerializer(Employee, data=request.data)
        if employeeSerializer.is_valid():
            employeeSerializer.save()
            return Response(employeeSerializer.data)
        return Response(employeeSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Employee = self.get_object(pk)
        Employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
