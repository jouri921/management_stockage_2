from django.shortcuts  import HttpResponse
from .decorators import  login_supplier_required
# Create your views here.
def supplier_views(request):
    return HttpResponse("supplier")
