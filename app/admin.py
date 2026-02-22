from django.contrib import admin

from app import models
from .models import Blog

# Register your models here.

admin.site.register(Blog)


