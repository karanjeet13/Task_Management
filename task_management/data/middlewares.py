from account.models import Employee


class UserInvokeMiddleare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', "").replace("Token ", "")
            if token:
                employee = Employee.objects.filter(token=token, is_active=True).first()
                request.employee = employee
            else:
                request.employee = None
        except Employee.DoesNotExist:
            request.employee = None
        response = self.get_response(request)
        return response
