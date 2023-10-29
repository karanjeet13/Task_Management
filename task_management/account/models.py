from django.db import models
from account.constants import UserType
from data.models import TimeStampModel
import uuid

# Create your models here.
class Employee(TimeStampModel):
    USER_TYPE_CHOICES = (
        (UserType.DEVELOPER, "Developer"),
        (UserType.MANAGER, "Manager")
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    # for the time being token will be constant
    token = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.token:
            self.token = str(uuid.uuid4())
        super(Employee, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.email
    
    def __repr__(self) -> str:
        return self.email
