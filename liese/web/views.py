from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from .forms import OpportunityRequestForm
from .models import OpportunityRequest, Article, Event
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime
from calendar import monthcalendar
from collections import defaultdict
from dateutil.relativedelta import relativedelta


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


def articles_view(request):
    articles = Article.objects.filter(published=True).order_by('-publication_date')
    print(articles)
    return render(request, 'web/articulos.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'web/article_detail.html', {'article': article})




def opportunities_view(request):
    return render(request, 'web/oportunidades.html')


def verify_email(request, token):
    opportunity_request = get_object_or_404(OpportunityRequest, verification_token=token)

    # Check if the token has expired
    if opportunity_request.verification_token_expires < timezone.now():
        return redirect('error_email_verification')
    
    # Check if the request has already been verified
    if opportunity_request.verified:
        return redirect('error_email_verification')

    # Mark the request as verified
    opportunity_request.verified = True
    opportunity_request.verification_token = None
    opportunity_request.verification_token_expires = None
    opportunity_request.save()

    return redirect('success_email_verification')


def success_email_verification(request):
    return render(request, 'web/verification_success.html')

def error_email_verification(request):
    return render(request, 'web/verification_error.html')

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




def events_view(request):
    # Obtener parámetros de mes/año
    month = request.GET.get('month')
    year = request.GET.get('year')
    
    try:
        month = int(month)
        year = int(year)
    except:
        current_date = timezone.now()
        month = current_date.month
        year = current_date.year
    
    # Calcular meses anterior y siguiente
    prev_month = month - 1 if month > 1 else 12
    next_month = month + 1 if month < 12 else 1
    
    
    
    # Obtener eventos del mes seleccionado
    selected_month_events = Event.objects.filter(
        published=True,
        start_date__month=month,
        start_date__year=year
    ).order_by('start_date')

    # Organizar eventos por día
    events_by_day = defaultdict(list)
    for event in selected_month_events:
        day = event.start_date.day
        events_by_day[day].append(event)

    # Generar semanas con eventos
    cal = monthcalendar(year, month)
    weeks = []
    for week in cal:
        week_data = []
        for day in week:
            week_data.append({
                'day': day if day != 0 else "",
                'events': events_by_day.get(day, []) if day != 0 else []
            })
        weeks.append(week_data)

    datetime_object = datetime(year, month, 1)

    context = {
        'weeks': weeks,
        'current_month': datetime_object.strftime('%B'),
        'current_month_name': datetime_object.strftime('%B'),
        'week_days': ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
        'all_events': selected_month_events,
        'prev_month': prev_month,
        'next_month': next_month,
        'prev_month_name': datetime(year, prev_month, 1).strftime("%B"),
        'current_year': year,
        'next_month_name': datetime(year, next_month, 1).strftime("%B"),
        'prev_year': year,
        'next_year': year,
        }
    return render(request, 'web/events.html', context)
