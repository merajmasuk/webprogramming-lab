from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from . import models, serializer

@csrf_exempt
def employee_list(request):
    if request.method == 'GET':
        emps = models.Employee.objects.all()
        serializer = serializer.EmployeeSerializer(emps, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializer.EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def employee_detail(request,pk):
    try:
        employee = models.Employee.objects.get(pk=pk)
    except models.Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = serializer.EmployeeSerializer(employee)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = serializer.EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status=204)
