from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget, AdminFileWidget
from django.utils.html import format_html
from django.urls import reverse

from .forms import VisaAdminForm
from .models import Visa


@admin.register(Visa)
class VisaAdmin(admin.ModelAdmin):
    form = VisaAdminForm
    list_display = (
        'visa_number',
        'first_name',
        'surname',
        'passport_number',
        'visa_type',
        'visa_status',
        'visa_valid_from',
        'pdf_download_link',
    )
    search_fields = ('visa_number', 'passport_number', 'surname', 'first_name')
    list_filter = ('visa_status', 'visa_type', 'citizenship')
    readonly_fields = ('photo_preview', 'pdf_status', 'pdf_download_link', 'created_at', 'updated_at')
    fieldsets = (
        ('Visa Details', {
            'fields': (
                'visa_number',
                'passport_number',
                'surname',
                'first_name',
                'fathers_name',
                'reference_number',
                'date_of_birth',
                'citizenship',
                'passport_issue_date',
                'passport_expiry_date',
                'visa_status',
                'visa_valid_from',
                'visa_validity',
                'number_of_entries',
                'duration_of_stay',
                'visa_type',
                'visit_purpose',
                'issue_date',
                'approval_date',
                'invitation_letter_text',
                'photo_upload',
                'photo_preview',
            )
        }),
        ('Document', {
            'fields': ('pdf_status', 'pdf_file', 'pdf_download_link'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

    def photo_preview(self, obj):
        """Display a preview of the uploaded photo with null safety."""
        try:
            if obj and hasattr(obj, 'photo_upload') and obj.photo_upload:
                return format_html(
                    '<img src="{}" style="max-height: 200px; max-width: 200px; object-fit: contain;" />',
                    obj.photo_upload.url,
                )
        except Exception:
            pass
        return 'No photo available.'

    photo_preview.short_description = 'Photo Preview'

    def pdf_status(self, obj):
        """Display PDF generation status with null safety."""
        try:
            if not obj or not obj.pk:
                return format_html('<span style="color: gray;">Not yet saved</span>')
            
            if hasattr(obj, 'pdf_file') and obj.pdf_file:
                return format_html(
                    '<span style="color: green; font-weight: bold;">✓ PDF Generated</span>'
                )
        except Exception:
            pass
        return format_html(
            '<span style="color: orange; font-weight: bold;">⟳ Generating PDF...</span>'
        )

    pdf_status.short_description = 'PDF Status'

    def pdf_download_link(self, obj):
        """Display a download link for the PDF with null safety."""
        try:
            if not obj or not obj.pk:
                return format_html('<span style="color: gray;">Pending...</span>')
            
            if hasattr(obj, 'pdf_file') and obj.pdf_file:
                try:
                    url = reverse('download_visa_pdf', args=[obj.pk])
                    return format_html(
                        '<a class="button" href="{url}">Download PDF</a>',
                        url=url
                    )
                except Exception:
                    pass
        except Exception:
            pass
        return format_html('<span style="color: orange;">Pending...</span>')

    pdf_download_link.short_description = 'Download'

    def save_model(self, request, obj, form, change):
        """Override save to ensure PDF is generated."""
        super().save_model(request, obj, form, change)
        if obj and not obj.pdf_file:
            obj.generate_pdf()


# Customize admin site
admin.site.site_header = 'eVisa Govmd'
admin.site.site_title = 'eVisa Govmd'
admin.site.index_title = 'eVisa Govmd'
