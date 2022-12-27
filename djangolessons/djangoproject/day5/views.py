from django.http import Http404
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics

# Create your views here.
from . import models, serializer

class EmployeeList(mixins.ListModelMixin, mixins.CreateModeMixin, generics.GenericAPIView):
    """
    List all Employee, or create a new Employee.
    """
    queryset = models.Employee.objects.all()
    serializer_class = serializer.EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, format=None):
        return self.create(request, *args, **kwargs)


# class EmployeeList(APIView):
class EmployeeDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModeMixin,
                mixins.DestroyModeMixin.
                generics.GenericAPIView):
    """
    Retriece, update or delete an Employee instance
    """
    queryset = models.Employee.objects.all()
    serializer_class = serializer.EmployeeSerializer

    # def get_object(self, pk):
    #     try:
    #         return models.Employee.objects.get(pk=pk)
    #     except models.Employee.DoesNotExist:
    #         raise Http404
    # def get(self, request, pk, format=None):
    #     employee = self.get_object(pk)
    #     employeeSerializer = serializer.EmployeeSerializer(employee)
    #     return Response(employeeSerializer)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
