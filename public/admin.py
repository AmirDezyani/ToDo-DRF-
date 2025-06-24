from django.contrib import admin

from public.models import Todos


@admin.register(Todos)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status')