# payments/admin.py

from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'rank', 'last_4_digits', 'stripe_id', )
    ordering = ('-created_at', )
    fieldsets = (
        ('User Info', {'fields': ('name', 'email', 'rank', )}),
        ('Billing', {'fields': ('stripe_id', )}),
        ('Badges', {'fields': ('badges', )}),
    )
