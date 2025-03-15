from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from .forms import OpportunityRequestForm
from .models import OpportunityRequest
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone


def index(request):
    integrantes = [
        {"nombre": "Rubi Janet Núñez Dorantes", "rol": "Tesista de maestría", "descripcion": "Contribuye al diseño de sistemas de comando y control."},
        {"nombre": "Nombre Apellido", "rol": "Investigador", "descripcion": "Desarrollo de instrumentación para sistemas embebidos."},
    ]
    return render(request, "web/index.html", {"integrantes": integrantes})



def leaders_view(request):
    leaders = [
        {
            'name': 'Rubi Janet Núñez Dorantes',
            'role': 'Tesista de maestría',
            'description': 'Contribuye al diseño de sistemas de comando y control, optimizando la gestión de información y el rendimiento operativo de los satélites.',
            'image': 'Integrantes.png',
            'linkedin': '#',
            'email': '#',
        },
        {
            'name': 'José Luis López Pérez',
            'role': 'Investigador',
            'description': 'Desarrollo de instrumentación para sistemas embebidos, con énfasis en la adquisición de datos y el control de sistemas.',
            'image': 'Integrantes.png',
            'linkedin': '#',
            'email': '#',
        },
        {
            'name': 'Nombre Apellido',
            'role': 'Investigador',
            'description': 'Desarrollo de sistemas de comunicación y control para aplicaciones aeroespaciales.',
            'image': 'Integrantes.png',
            'linkedin': '#',
            'email': '#',
        },
        {
            'name': 'Rubi Janet Núñez Dorantes',
            'role': 'Tesista de maestría',
            'description': 'Contribuye al diseño de sistemas de comando y control, optimizando la gestión de información y el rendimiento operativo de los satélites.',
            'image': 'Integrantes.png',
            'linkedin': '#',
            'email': '#',
        },
        {
            'name': 'José Luis López Pérez',
            'role': 'Investigador',
            'description': 'Desarrollo de instrumentación para sistemas embebidos, con énfasis en la adquisición de datos y el control de sistemas.',
            'image': 'Integrantes.png',
            'linkedin': '#',
            'email': '#',
        },
        {
            'name': 'Nombre Apellido',
            'role': 'Investigador',
            'description': 'Desarrollo de sistemas de comunicación y control para aplicaciones aeroespaciales.',
            'image': 'Integrantes.png',
            'linkedin': '#',
            'email': '#',
        }
        # Add more leaders as needed
    ]
    return render(request, 'web/lideresDeProyecto.html', {'leaders': leaders})



def opportunities_view(request):
    return render(request, 'web/oportunidades.html')



def opportunity_request(request):
    if request.method == 'POST':
        form = OpportunityRequestForm(request.POST)
        if form.is_valid():
            opportunity_request = form.save(commit=False)
            opportunity_request.generate_verification_token()
            opportunity_request.save()

            try:
                # Send verification email
                verification_url = request.build_absolute_uri(
                    reverse('verify_email', args=[opportunity_request.verification_token])
                )
                plain_message = f"Por favor verifica tu correo electrónico para completar tu solicitud:\n\n{verification_url}"
                
                subject = "LIESE - Verifica tu correo electrónico"
                message = render_to_string('web/verification_email.html', {
                    'verification_url': verification_url,
                })

                send_mail(
                    subject,
                    plain_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [opportunity_request.email],
                    html_message=message,
                    fail_silently=False,
                )
            except Exception as e:
                # Log the error or display a message to the user
                print(f"Error sending email: {e}")
                return render(request, 'web/email_error.html')  # Show an error page

            return render(request, 'web/verification_sent.html')  # Show a confirmation page
    else:
        form = OpportunityRequestForm()

    return render(request, 'web/opportunity_request.html', {'form': form})




def verify_email(request, token):
    opportunity_request = get_object_or_404(OpportunityRequest, verification_token=token)

    # Check if the token has expired
    if opportunity_request.verification_token_expires < timezone.now():
        messages.error(request, "The verification link has expired. Please submit your request again.")
        return redirect('home')

    # Mark the request as verified
    opportunity_request.verified = True
    opportunity_request.verification_token = None
    opportunity_request.verification_token_expires = None
    opportunity_request.save()

    messages.success(request, "Your email has been verified. Your request has been submitted.")
    return redirect('home')  # Redirect to a success page or home page