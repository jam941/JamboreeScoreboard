from django.contrib import admin

# Register your models here.
from backend.models import Troop, Patrol, Scout, Score

admin.site.register(Troop)
admin.site.register(Patrol)
admin.site.register(Scout)

admin.site.register(Score)

