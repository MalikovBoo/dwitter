from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Dweet


class ProfileInLine(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'password', 'email']
    inlines = [ProfileInLine]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Dweet)
# admin.site.register(Profile)
