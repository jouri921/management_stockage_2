from django.contrib import admin
from .models import  MyUser, Admin, Supplier, Employee

# Register your models here


admin.site.register(MyUser)
admin.site.register(Admin)
admin.site.register(Supplier)
admin.site.register(Employee)
