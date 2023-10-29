from django.shortcuts import render
from rest_framework.views import APIView
from data.standard_response import InvalidDataResponse, CreatedResponse
from account.serializers import EmployeeSerializer
from account.models import Employee

# Create your views here.
class RegisterEmployee(APIView):

    def post(self, request, format=None):
        data = request.data

        serializer = EmployeeSerializer(data=data)
        if not serializer.is_valid():
            return InvalidDataResponse("Invalid Data")
        
        employee = Employee(**serializer.validated_data)
        employee.save()

        return CreatedResponse(EmployeeSerializer(employee).data)
