from django.contrib import admin

# Register your models here.
from .models import User, Event

admin.site.register(Event)
# admin.site.register(User)
