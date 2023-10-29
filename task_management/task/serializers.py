from rest_framework import serializers
from task.models import Task
from task.constants import TaskStatus
from account.models import Employee


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    assignee = serializers.CharField(required=False)
    status = serializers.SerializerMethodField()
    reporter = serializers.CharField(required=False)
    
    class Meta():
        model = Task
        fields = ["id", "title", "content", "assignee", "status", "reporter"]

    def get_status(self, task):
        return task.get_status_display()
    
    def validate_assignee(self, assignee):
        try:
            Employee.objects.get(email=assignee)
        except Exception:
            raise serializers.ValidationError("Invalid assignee")
        return assignee

class TaskAsssignSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    assignee = serializers.CharField(required=True)

    def validate_id(self, id):
        try:
            Task.objects.get(pk=id)
        except (Task.DoesNotExist, Task.MultipleObjectsReturned):
            raise serializers.ValidationError("Invalid Task ID")
        return id
    
    def validate_assignee(self, assignee):
        try:
            Employee.objects.get(email=assignee)
        except (Employee.DoesNotExist, Employee.MultipleObjectsReturned):
            raise serializers.ValidationError("Invalid Employee")
        return assignee


class TaskUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    assignee = serializers.CharField(required=False)
    status = serializers.IntegerField(required=False)

    def validate_id(self, id):
        try:
            Task.objects.get(id=id)
        except (Task.DoesNotExist, Task.MultipleObjectsReturned):
            raise serializers.ValidationError("Invalid Task ID")
        return id

    def validate_status(self, status):
        if status not in [TaskStatus.IN_PROGRESS, TaskStatus.TODO, TaskStatus.DONE]:
            raise serializers.ValidationError("Invalid status code.")
        return status

    def validate_assignee(self, assignee):
        try:
            Employee.objects.get(email=assignee)
        except Exception:
            raise serializers.ValidationError("Invalid assignee")
        return assignee
