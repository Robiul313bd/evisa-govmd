from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import FileResponse, Http404, JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Visa


def index(request):
    """
    Render the index/home page with visa information.
    """
    return render(request, 'index.html')


def check_visa(request):
    """
    Render the check visa page for visa status lookup.
    """
    visa_number = request.GET.get('visaNumber', '')
    visa = None
    visa_error = None
    visa_is_valid = False

    if 'visaNumber' in request.GET:
        visa_number = visa_number.strip()

        if visa_number == '':
            visa_error = 'Please enter visa number'
        else:
            visa = Visa.objects.filter(visa_number__iexact=visa_number).first()
            if visa:
                visa_is_valid = True
            else:
                visa_error = 'Visa number not found'

        if request.GET.get('ajax') == '1':
            if visa:
                return JsonResponse({
                    'found': True,
                    'visa': {
                        'surname': visa.surname,
                        'first_name': visa.first_name,
                        'date_of_birth': visa.date_of_birth.strftime('%d/%m/%Y'),
                        'citizenship': visa.citizenship,
                        'passport_number': visa.passport_number,
                        'visa_status': visa.get_visa_status_display(),
                        'visa_validity': visa.get_visa_validity_display(),
                        'visa_type': visa.get_visa_type_display(),
                        'visit_purpose': visa.get_visit_purpose_display(),
                        'photo_url': visa.photo_upload.url if visa.photo_upload else None,
                    },
                })
            return JsonResponse({'found': False, 'error': visa_error})

    return render(request, 'check-visa.html', {
        'visa_number': visa_number,
        'visa_error': visa_error,
        'visa_is_valid': visa_is_valid,
        'visa': visa,
    })


def is_admin(user):
    """
    Check if user is staff/admin.
    """
    return user.is_staff and user.is_superuser


@login_required(login_url='/admin/login/')
@user_passes_test(is_admin, login_url='/admin/login/')
@require_http_methods(['GET'])
def download_visa_pdf(request, visa_id):
    """
    Secure PDF download for admin users only.
    Downloads the generated visa PDF.
    """
    visa = get_object_or_404(Visa, pk=visa_id)

    if not visa.pdf_file:
        raise Http404('PDF document not found for this visa.')

    try:
        response = FileResponse(visa.pdf_file.open('rb'), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="visa_{visa.visa_number}.pdf"'
        return response
    except Exception:
        raise Http404('Unable to download PDF document.')


def error_404(request, exception=None):
    """
    Custom 404 error handler.
    """
    return render(request, '404.html', status=404)


def error_500(request):
    """
    Custom 500 error handler.
    """
    return render(request, '500.html', status=500)
