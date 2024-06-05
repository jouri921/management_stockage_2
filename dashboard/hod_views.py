from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import login_admin_required
from .forms import SupplierForm
from .models import Supplier

def hod_views(request):
    return render(request,"dashboard/index.html")

def page_add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            if Supplier.objects.filter(email=email).exists():
                messages.error(request, 'Supplier with this email already exists!')
            else:
                form.save()
                messages.success(request, 'Supplier added successfully!')
                return redirect('page_add_supplier')
    else:
        form = SupplierForm()
    return render(request, "people/page_add_supplier.html", {'form': form})
