from django.urls import path
from .views import *
from .employee_views import *
from .supplier_views import *
from .hod_views import *
urlpatterns = [
    path("", index, name='index'),
    path("login_page", login_page, name='login_page'),
    path("doLogin/", doLogin, name='user_login'),
    path("logout_user/", logout_user, name='user_logout'),
    path("employee_views/", employee_views, name='employee_views'),
    path("supplier_views/", supplier_views, name='supplier_views'),
    # pages admin
    path("hod_views/", hod_views, name='hod_views'),
    path("page_add_supplier",page_add_supplier,name="page_add_supplier"),
]
