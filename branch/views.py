from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from .models import Employee, Branch, Car
from .serializer import EmployeeSerializer, CarSerializer
from django.http import HttpResponse


def main(request):
    return HttpResponse('You entered successfully')

@api_view(['GET'])
def workers(request, branch_id):
    employees = Employee.objects.filter(branch__id=branch_id)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def car(request, branch_id, car_name):
    print(f'Branch ID: {branch_id}, Car Type: {car_name}')
    car_count = Car.objects.filter(branch__id=branch_id, name=car_name).count()
    return Response({'car_count': car_count})


@api_view(['GET'])
def cars(request, branch_id):
    cars = Car.objects.filter(branch__id=branch_id)
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)
