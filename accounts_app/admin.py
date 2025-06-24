from django.contrib import admin

from accounts_app.models import Profile


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'name', 'email', 'image', 'password')