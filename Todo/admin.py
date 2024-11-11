from django.contrib import admin
from .models import Todo

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=('task','is_completed',)
    search_fields=('task',)
    list_editable = ("is_completed",) 

admin.site.register(Todo,TaskAdmin)

