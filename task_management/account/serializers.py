from rest_framework import serializers
from account.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    user_type = serializers.IntegerField(required=True)
    email = serializers.CharField(required=True)
    token = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)
    
    class Meta():
        model = Employee
        fields = ["user_type", "email", "token", "is_active"]
