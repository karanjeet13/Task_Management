from django.contrib import admin


from task.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "assignee"]
    raw_id_fields = ["assignee"]


admin.site.register(Task, TaskAdmin)
