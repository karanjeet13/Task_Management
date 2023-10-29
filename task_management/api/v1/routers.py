from task_management.routers import TaskManagementRouter
from api.v1 import viewsets

v1_router = TaskManagementRouter()

v1_router.register(r'task', viewsets.TaskViewset, basename="task")
