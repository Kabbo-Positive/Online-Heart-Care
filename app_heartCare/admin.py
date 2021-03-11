from django.contrib import admin

# Register your models here.

from .models import Nurse, Hospital

admin.site.register(Nurse)
admin.site.register(Hospital)