from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from data.standard_response import CreatedResponse, InvalidDataResponse, SuccessResponse
from task.serializers import TaskSerializer, TaskUpdateSerializer, TaskAsssignSerializer
from task.models import Task
from task.constants import TaskStatus
from account.models import Employee
from api.v1.decorators import access_control_decorator
from account.constants import UserType


class TaskViewset(ViewSet):
    permission_classes = (AllowAny, )
    parser_classes = (JSONParser, )

    @access_control_decorator(allowed=[UserType.MANAGER])
    def create(self, request):
        serializer = TaskSerializer(data=request.data)

        if not serializer.is_valid():
            return InvalidDataResponse("Invalid Data")
        
        data = serializer.validated_data

        if data.get("assignee"):
            assignee = Employee.objects.filter(email=serializer.validated_data["assignee"], is_active=True).first()
            data["assignee"] = assignee

        task = Task(**data)
        task.reporter = request.employee
        task.status = TaskStatus.TODO
        task.save()

        return CreatedResponse(TaskSerializer(task).data)
    
    @action(detail=False, methods=["post"], url_path="assign-task", url_name="assign_task")
    def assign_task(self, request):
        serializer = TaskAsssignSerializer(data=request.data)
        
        if not serializer.is_valid():
            return InvalidDataResponse("Invalid Data")

        data = serializer.validated_data
        task = Task.objects.get(pk=data["id"])
        assignee = Employee.objects.get(email=data["assignee"])

        task.assignee = assignee
        task.save()
        return SuccessResponse("Record saved successfully.")

    def list(self, request):
        # for the time being no pagination
        return SuccessResponse(TaskSerializer(Task.objects.all(), many=True).data)
    
    @action(detail=False, methods=["post"], url_path="update-task", url_name="update_task")
    def update_task(self, request):
        serializer = TaskUpdateSerializer(data=request.data)

        if not serializer.is_valid():
            return InvalidDataResponse("Invalid data")
        
        validated_data = serializer.validated_data
        
        if validated_data.get("assignee"):
            validated_data["assignee"] = Employee.objects.get(email=validated_data["assignee"])
        
        Task.objects.update_or_create(pk=validated_data["id"], defaults=validated_data)

        return SuccessResponse("Record saved successfully.")
