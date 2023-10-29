from api.v1.routers import v1_router
from task_management.routers import TaskManagementRouter

api_router = TaskManagementRouter()

api_router.extend('v1', v1_router)
# in future we can add multiple version of apis, by changing it's version
# ex: api_router.extend('v2', v2_router)

