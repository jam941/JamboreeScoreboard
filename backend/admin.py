from django.contrib import admin

# Register your models here.
from backend.models import Troop, Patrol

admin.site.register(Troop)
admin.site.register(Patrol)

