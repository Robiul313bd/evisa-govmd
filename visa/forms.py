from django.contrib.admin.widgets import AdminFileWidget
from django import forms

from .models import Visa


class VisaAdminForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = '__all__'
        widgets = {
            'visa_number': forms.TextInput(attrs={'class': 'vTextField form-control'}),
            'passport_number': forms.TextInput(attrs={'class': 'vTextField form-control'}),
            'surname': forms.TextInput(attrs={'class': 'vTextField form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'vTextField form-control'}),
            'fathers_name': forms.TextInput(attrs={'class': 'vTextField form-control'}),
            'reference_number': forms.TextInput(attrs={'class': 'vTextField form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'vDateField form-control'}),
            'citizenship': forms.TextInput(attrs={'class': 'vTextField form-control'}),
            'passport_issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'vDateField form-control'}),
            'passport_expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'vDateField form-control'}),
            'visa_status': forms.Select(attrs={'class': 'vSelect form-control'}),
            'visa_valid_from': forms.DateInput(attrs={'type': 'date', 'class': 'vDateField form-control'}),
            'visa_validity': forms.DateInput(attrs={'type': 'date', 'class': 'vDateField form-control'}),
            'number_of_entries': forms.Select(attrs={'class': 'vSelect form-control'}),
            'duration_of_stay': forms.NumberInput(attrs={'class': 'vIntegerField form-control'}),
            'visa_type': forms.Select(attrs={'class': 'vSelect form-control'}),
            'visit_purpose': forms.Select(attrs={'class': 'vSelect form-control'}),
            'issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'vDateField form-control'}),
            'approval_date': forms.DateInput(attrs={'type': 'date', 'class': 'vDateField form-control'}),
            'invitation_letter_text': forms.Textarea(attrs={'class': 'vLargeTextField form-control', 'rows': 4}),
            'photo_upload': AdminFileWidget(attrs={'class': 'vClearableFileInput form-control-file'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        passport_issue_date = cleaned_data.get('passport_issue_date')
        passport_expiry_date = cleaned_data.get('passport_expiry_date')
        issue_date = cleaned_data.get('issue_date')
        visa_valid_from = cleaned_data.get('visa_valid_from')

        if passport_issue_date and passport_expiry_date:
            if passport_expiry_date <= passport_issue_date:
                self.add_error(
                    'passport_expiry_date',
                    'Passport expiry date must be later than passport issue date.',
                )

        if issue_date and visa_valid_from:
            if visa_valid_from < issue_date:
                self.add_error(
                    'visa_valid_from',
                    'Visa valid from date cannot be earlier than issue date.',
                )

        return cleaned_data


class VisaSearchForm(forms.Form):
    query = forms.CharField(
        label='Visa number or Passport number',
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'class': 'input-field',
                'placeholder': 'Enter Visa number or Passport number',
                'autocomplete': 'off',
            }
        ),
    )
