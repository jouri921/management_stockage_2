import logging
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin



class LoginCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            if request.user.user_type == 'Admin':
                if request.path != reverse('hod_views'):
                    return HttpResponseRedirect(reverse('hod_views'))
            elif request.user.user_type == 'Employee':
                if request.path != reverse('employee_views'):
                    return HttpResponseRedirect(reverse('employee_views'))
            elif request.user.user_type == 'Supplier':
                if request.path != reverse('supplier_views'):
                    return HttpResponseRedirect(reverse('supplier_views'))

        return response
