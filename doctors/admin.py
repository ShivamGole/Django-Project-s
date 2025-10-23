from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Doctor model.
    This class customizes how doctors are displayed and managed in the Django admin interface.
    """
    list_display = ('name', 'specialization', 'location', 'experience', 'contact')
    # Display these fields in the list view for quick overview

    list_filter = ('specialization', 'location', 'experience')
    # Add filters to easily find doctors by specialization, location, or experience

    search_fields = ('name', 'specialization', 'location')
    # Enable search functionality for name, specialization, and location

    ordering = ('name',)
    # Order doctors alphabetically by name in the admin list

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'specialization', 'location')
        }),
        ('Professional Details', {
            'fields': ('experience', 'contact')
        }),
    )
    # Organize fields into logical groups for better form layout
