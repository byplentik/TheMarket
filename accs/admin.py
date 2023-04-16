from django.contrib import admin

from accs.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass