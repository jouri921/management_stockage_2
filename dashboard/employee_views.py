from django.shortcuts  import HttpResponse
from .decorators import login_employee_required
# Create your views here.
def employee_views(request):
    return HttpResponse("employeeoyee")
