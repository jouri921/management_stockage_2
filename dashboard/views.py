from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .EmailBackEnd import *

@login_required
def index(request):
    return HttpResponse('request')
def login_page(request):
    return render(request, 'registration/login.html')

def doLogin(request):
    if request.method != "POST":
        return HttpResponseRedirect("/")
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == "Admin":
                return HttpResponseRedirect(reverse("hod_views"))
            elif user.user_type == "Employee":
                return HttpResponseRedirect(reverse("employee_views"))
            elif user.user_type == "Supplier":
                return HttpResponseRedirect(reverse("supplier_views"))
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/login_page")

def logout_user(request):
    if request.user.is_authenticated:
        email = request.user.email
        logout(request)
        logger.info(f"User {email} logged out successfully")
    return redirect("login_page")
