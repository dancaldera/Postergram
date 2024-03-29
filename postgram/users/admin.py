"""User admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    """Posts Admin model"""

    list_display = ('pk', 'user', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('photo',)
    list_filter = (
                'created',
                'modified'
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    """Profile Admin."""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('website', 'picture', 'phone_number')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user','picture'),),
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created','modified'),),
        }),
    )

    readonly_fields = ('created', 'modified', 'user')

class ProfileInLine(admin.StackedInline):
    """Profile in-line admin for users"""

    model = Profile
    can_delete = False
    verbose_name_plurals = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)