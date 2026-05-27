import os
from datetime import datetime
from django.conf import settings
from django.db import models
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors


class Visa(models.Model):
    VISA_STATUS_VALID = 'valid'
    VISA_STATUS_INVALID = 'invalid'
    VISA_STATUS_PENDING = 'pending'
    VISA_STATUS_CHOICES = [
        (VISA_STATUS_VALID, 'Valid'),
        (VISA_STATUS_INVALID, 'Invalid'),
        (VISA_STATUS_PENDING, 'Pending'),
    ]

    ENTRY_SINGLE = 'single_entry'
    ENTRY_DOUBLE = 'double_entry'
    ENTRY_MULTIPLE = 'multiple_entry'
    ENTRY_CHOICES = [
        (ENTRY_SINGLE, 'Single Entry'),
        (ENTRY_DOUBLE, 'Double Entry'),
        (ENTRY_MULTIPLE, 'Multiple Entry'),
    ]

    VISA_TYPE_A = 'A'
    VISA_TYPE_B = 'B'
    VISA_TYPE_C = 'C'
    VISA_TYPE_D = 'D'
    VISA_TYPE_CHOICES = [
        (VISA_TYPE_A, 'Type A'),
        (VISA_TYPE_B, 'Type B'),
        (VISA_TYPE_C, 'Type C'),
        (VISA_TYPE_D, 'Type D'),
    ]

    PURPOSE_TOURISM = 'tourism'
    PURPOSE_BUSINESS = 'business'
    PURPOSE_STUDY = 'study'
    PURPOSE_MEDICAL = 'medical'
    PURPOSE_OTHER = 'other'
    VISIT_PURPOSE_CHOICES = [
        (PURPOSE_TOURISM, 'Tourism'),
        (PURPOSE_BUSINESS, 'Business'),
        (PURPOSE_STUDY, 'Study'),
        (PURPOSE_MEDICAL, 'Medical'),
        (PURPOSE_OTHER, 'Other'),
    ]

    visa_number = models.CharField('Visa Number', max_length=64, blank=False, null=False)
    passport_number = models.CharField('Passport Number', max_length=64, blank=False, null=False)
    surname = models.CharField('Surname', max_length=128, blank=False, null=False)
    first_name = models.CharField('First Name', max_length=128, blank=False, null=False)
    fathers_name = models.CharField('Father\'s Name', max_length=128, blank=True, null=True)
    reference_number = models.CharField('Reference Number', max_length=128, blank=True, null=True)
    date_of_birth = models.DateField('Date of Birth', blank=False, null=False)
    citizenship = models.CharField('Citizenship', max_length=100, blank=False, null=False)
    passport_issue_date = models.DateField('Passport Issue Date', blank=False, null=False)
    passport_expiry_date = models.DateField('Passport Expiry Date', blank=False, null=False)
    visa_status = models.CharField('Visa Status', max_length=10, choices=VISA_STATUS_CHOICES, default=VISA_STATUS_VALID, blank=False, null=False)
    visa_valid_from = models.DateField('Visa Valid From', blank=False, null=False)
    visa_validity = models.DateField('Visa Validity', blank=False, null=False)
    number_of_entries = models.CharField('Number of Entries', max_length=20, choices=ENTRY_CHOICES, blank=False, null=False)
    duration_of_stay = models.IntegerField('Duration of Stay (days)', default=30, blank=False, null=False)
    visa_type = models.CharField('Visa Type', max_length=2, choices=VISA_TYPE_CHOICES, blank=False, null=False)
    visit_purpose = models.CharField('Visit Purpose', max_length=20, choices=VISIT_PURPOSE_CHOICES, blank=False, null=False)
    issue_date = models.DateField('Issue Date', blank=False, null=False)
    approval_date = models.DateField('Approval Date', blank=False, null=False)
    invitation_letter_text = models.TextField('Remarks / Invitation Details', blank=False, null=False)
    photo_upload = models.ImageField('Photo Upload', upload_to='visa_photos/', blank=False, null=False)
    pdf_file = models.FileField('PDF Document', upload_to='visa_pdfs/', blank=True, null=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Visa'
        verbose_name_plural = 'Visas'

    def __str__(self):
        return f"{self.visa_number} - {self.first_name}"

    @property
    def country_header(self):
        """Return the selected citizenship name in uppercase for PDF headers."""
        return self.citizenship.strip().upper() if self.citizenship else 'REPUBLIC OF MOLDOVA'

    @property
    def pdf_filename(self):
        return f"visa_{self.pk}.pdf"

    @property
    def pdf_file_path(self):
        return os.path.join(settings.MEDIA_ROOT, 'pdf', self.pdf_filename)

    @property
    def pdf_url(self):
        return f"/visa/download-pdf/{self.pk}/"

    def save(self, *args, **kwargs):
        # Save the object first so it has a primary key.
        created = self.pk is None
        super().save(*args, **kwargs)

        # Generate PDF after first save if no PDF exists yet.
        if self.pk and (created or not self.pdf_file):
            self.generate_pdf()
            if self.pdf_file:
                super().save(update_fields=['pdf_file'])

    def generate_pdf(self):
        """Generate a professional eVisa PDF document."""
        if not self.pk:
            return

        try:
            # Create PDF directory if it doesn't exist
            pdf_dir = os.path.join(settings.MEDIA_ROOT, 'visa_pdfs')
            os.makedirs(pdf_dir, exist_ok=True)

            # Generate filename based on visa number
            pdf_filename = f"visa_{self.visa_number.replace(' ', '_')}.pdf"
            pdf_path = os.path.join(pdf_dir, pdf_filename)

            # Create canvas
            c = canvas.Canvas(pdf_path, pagesize=A4)
            width, height = A4
            margin_left = 20 * mm
            margin_right = 20 * mm
            margin_top = 20 * mm
            page_width = width - margin_left - margin_right

            # Header section with red bar
            c.setFillColor(HexColor('#C8102E'))  # Red color for Moldova theme
            c.rect(0, height - 30 * mm, width, 30 * mm, fill=1, stroke=0)

            # Title in header, based on selected citizenship
            c.setFont('Helvetica-Bold', 24)
            c.setFillColor(HexColor('#FFFFFF'))  # White text
            c.drawString(margin_left, height - 15 * mm, self.country_header)

            c.setFont('Helvetica', 14)
            c.drawString(margin_left, height - 22 * mm, 'Electronic Visa (eVisa)')

            # Reset for body
            c.setFillColor(HexColor('#000000'))
            y_position = height - 35 * mm

            # Applicant photo on the right
            photo_x = width - margin_right - 50 * mm
            photo_y = y_position - 60 * mm
            if self.photo_upload and os.path.exists(self.photo_upload.path):
                try:
                    img = ImageReader(self.photo_upload.path)
                    c.drawImage(img, photo_x, photo_y, width=50 * mm, height=60 * mm, preserveAspectRatio=True)
                except Exception:
                    pass

            # Left section - Applicant info
            info_x = margin_left
            info_width = photo_x - margin_left - 5 * mm

            # Section title
            c.setFont('Helvetica-Bold', 12)
            c.drawString(info_x, y_position, 'APPLICANT INFORMATION')
            c.line(info_x, y_position - 2 * mm, info_x + info_width, y_position - 2 * mm)

            y_position -= 6 * mm
            c.setFont('Helvetica', 10)
            
            # Applicant details
            details = [
                ('Visa Number:', self.visa_number),
                ('Passport Number:', self.passport_number),
                ('Surname:', self.surname),
                ('First Name:', self.first_name),
                ('Father\'s Name:', self.fathers_name or 'N/A'),
                ('Date of Birth:', str(self.date_of_birth)),
                ('Citizenship:', self.citizenship),
            ]

            for label, value in details:
                c.setFont('Helvetica-Bold', 9)
                c.drawString(info_x, y_position, label)
                c.setFont('Helvetica', 9)
                c.drawString(info_x + 50 * mm, y_position, str(value))
                y_position -= 5 * mm

            # Visa details section
            y_position -= 3 * mm
            c.setFont('Helvetica-Bold', 12)
            c.drawString(info_x, y_position, 'VISA INFORMATION')
            c.line(info_x, y_position - 2 * mm, info_x + info_width, y_position - 2 * mm)

            y_position -= 6 * mm
            
            visa_details = [
                ('Visa Type:', self.get_visa_type_display()),
                ('Visa Status:', self.get_visa_status_display()),
                ('Visa Valid From:', str(self.visa_valid_from)),
                ('Visa Validity:', self.visa_validity.strftime('%d/%m/%Y')),
                ('Number of Entries:', self.get_number_of_entries_display()),
                ('Duration of Stay:', f"{self.duration_of_stay} days"),
                ('Visit Purpose:', self.get_visit_purpose_display()),
                ('Issue Date:', str(self.issue_date)),
                ('Approval Date:', str(self.approval_date)),
            ]

            for label, value in visa_details:
                c.setFont('Helvetica-Bold', 9)
                c.drawString(info_x, y_position, label)
                c.setFont('Helvetica', 9)
                c.drawString(info_x + 50 * mm, y_position, str(value))
                y_position -= 5 * mm

            # Passport details section
            y_position -= 3 * mm
            c.setFont('Helvetica-Bold', 12)
            c.drawString(info_x, y_position, 'PASSPORT DETAILS')
            c.line(info_x, y_position - 2 * mm, info_x + info_width, y_position - 2 * mm)

            y_position -= 6 * mm
            
            passport_details = [
                ('Passport Issue Date:', str(self.passport_issue_date)),
                ('Passport Expiry Date:', str(self.passport_expiry_date)),
                ('Reference Number:', self.reference_number or 'N/A'),
            ]

            for label, value in passport_details:
                c.setFont('Helvetica-Bold', 9)
                c.drawString(info_x, y_position, label)
                c.setFont('Helvetica', 9)
                c.drawString(info_x + 50 * mm, y_position, str(value))
                y_position -= 5 * mm

            # Remarks section
            y_position -= 3 * mm
            c.setFont('Helvetica-Bold', 12)
            c.drawString(info_x, y_position, 'REMARKS / INVITATION DETAILS')
            c.line(info_x, y_position - 2 * mm, width - margin_right, y_position - 2 * mm)

            y_position -= 5 * mm
            c.setFont('Helvetica', 9)
            remarks_text = self.invitation_letter_text[:500]  # Limit to 500 chars
            for line in remarks_text.split('\n')[:5]:  # Max 5 lines
                c.drawString(info_x + 5 * mm, y_position, line[:70])
                y_position -= 4 * mm

            # Footer with timestamp
            c.setFont('Helvetica', 8)
            c.setFillColor(HexColor('#666666'))
            c.drawString(margin_left, 15 * mm, f'Generated: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
            c.drawString(margin_left, 10 * mm, 'This is an official eVisa document issued by the Ministry of Foreign Affairs.')

            # Save PDF
            c.save()

            # Store PDF path in database (relative path for FileField)
            relative_path = os.path.join('visa_pdfs', pdf_filename)
            self.pdf_file.name = relative_path
            # Save without triggering PDF generation again
            models.Model.save(self)

        except Exception as e:
            # Silently fail PDF generation if there's an error
            pass
