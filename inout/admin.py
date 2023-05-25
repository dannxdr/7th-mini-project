from django.contrib import admin
from .models import User_info

# Register your models here.
#@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=(
        'username',
        'password',
    )

admin.site.register(User_info, UserAdmin)