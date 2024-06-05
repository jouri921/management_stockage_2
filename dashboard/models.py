from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save

class CustM(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractUser):
    username = None
    user_type_data=(('Admin',"Admin"),('Employee',"Employee"),('Supplier',"Supplier"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=50)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)  # Changed default value to False
    objects = CustM()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    class Meta:
        verbose_name = _("My User")  # Human-readable singular name
        verbose_name_plural = _("My Users")





class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin = models.OneToOneField(MyUser, on_delete=models.CASCADE)


class Supplier(models.Model):
    id=models.AutoField(primary_key=True)
    admin = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=15)
    address = models.TextField()
    company_Name=models.CharField(max_length=225)
    city = models.CharField(max_length=255, )  # Provide a default value for city
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return str(self.admin)


class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    admin = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    status = models.CharField(max_length=10, choices=(('Active', 'Active'), ('Inactive', 'Inactive')))
    notify_by_email = models.BooleanField(default=True)

    def __str__(self):
        return self.phone_number



@receiver(post_save, sender=MyUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'Admin':
            Admin.objects.create(admin=instance)
        elif instance.user_type == 'Employee':
            Employee.objects.create(admin=instance)
        elif instance.user_type == 'Supplier':
            Supplier.objects.create(admin=instance)

@receiver(post_save, sender=MyUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 'Admin':
        instance.admin.save()
    elif instance.user_type == 'Employee':
        instance.employee.save()
    elif instance.user_type == 'Supplier':
        instance.supplier.save()
