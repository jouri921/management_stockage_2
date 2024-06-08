# from django.contrib.auth import REDIRECT_FIELD_NAME
# from django.contrib.auth.decorators import user_passes_test
# from functools import wraps

# def login_admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='hod_views'):
#     actual_decorator = user_passes_test(
#         lambda u: u.user_type == 'Admin',
#         login_url=login_url,
#         redirect_field_name=redirect_field_name
#     )
#     if function:
#         return wraps(function)(actual_decorator(function))
#     return actual_decorator

# def login_employee_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='employee_views'):
#     actual_decorator = user_passes_test(
#         lambda u: u.user_type == 'Employee',
#         login_url=login_url,
#         redirect_field_name=redirect_field_name
#     )
#     if function:
#         return wraps(function)(actual_decorator(function))
#     return actual_decorator

# def login_supplier_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='supplier_views'):
#     actual_decorator = user_passes_test(
#         lambda u: u.user_type == 'Supplier',
#         login_url=login_url,
#         redirect_field_name=redirect_field_name
#     )
#     if function:
#         return wraps(function)(actual_decorator(function))
#     return actual_decorator
