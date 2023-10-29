from django.db import models
from account.models import Employee
from task.constants import TaskStatus
from data.models import TimeStampModel

# Create your models here.
class Task(TimeStampModel):
    STATUS_CHOICE = (
        (TaskStatus.TODO, "To Do"),
        (TaskStatus.IN_PROGRESS, "In Progress"),
        (TaskStatus.DONE, "Done")
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    assignee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="assignee_task")
    reporter = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="reporter_task")
    status = models.PositiveBigIntegerField(choices=STATUS_CHOICE)
