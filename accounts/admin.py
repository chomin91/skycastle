from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import SignupForm

class UserAdmin(BaseUserAdmin):
    model = User
    add_from = SignupForm
    list_display = ('email', 'user_type', 'coordiInfo')
    list_filter = ('user_type', 'email')
    ordering = ('email', 'user_type')

    def coordiInfo(self, obj):
        try:
            return obj.coordi_info.university
        except AttributeError:
            return 'null'

admin.site.register(User, UserAdmin)
