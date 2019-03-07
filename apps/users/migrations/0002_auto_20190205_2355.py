# Generated by Django 2.1 on 2019-02-05 23:55
import os
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    def generate_superuser(apps, schema_editor):
        from apps.users.models import User

        DJANGO_DB_NAME = os.environ.get('DJANGO_DB_NAME', "default")
        DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME', "admin")
        DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL', "")
        DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD', "admin")
        
        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD)
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]