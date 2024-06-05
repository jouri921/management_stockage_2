# Generated by Django 5.0.6 on 2024-06-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_myuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Employee', 'Employee'), ('Supplier', 'Supplier')], default=1, max_length=50),
        ),
    ]
