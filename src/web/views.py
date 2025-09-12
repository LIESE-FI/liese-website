from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from .forms import OpportunityRequestForm
from .models import OpportunityRequest, Article, Event, News, Project, Member
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
    """
    Vista que muestra los miembros del laboratorio marcados como líderes
    y sus artículos publicados
    """
    # Obtener miembros que son líderes y están activos
    leaders = Member.objects.filter(is_leader=True, active=True).order_by('date_joined')
    
    # Si no hay líderes en la BD, usar datos de ejemplo
    if not leaders.exists():
        # Datos de respaldo por si no hay miembros en la BD
        example_leaders = [
            {
                'full_name': 'Rubi Janet Núñez Dorantes',
                'position': 'Tesista de maestría',
                'description': 'Contribuye al diseño de sistemas de comando y control, optimizando la gestión de información y el rendimiento operativo de los satélites.',
                'image_url': '/static/web/images/default-avatar.png',
                'linkedin_url': '#',
                'email': 'rubi@liese.unam.mx',
                'articles': []  # Sin artículos de ejemplo
            },
            {
                'full_name': 'José Luis López Pérez',
                'position': 'Investigador',
                'description': 'Desarrollo de instrumentación para sistemas embebidos, con énfasis en la adquisición de datos y el control de sistemas.',
                'image_url': '/static/web/images/default-avatar.png',
                'linkedin_url': '#',
                'email': 'jose@liese.unam.mx',
                'articles': []
            },
            {
                'full_name': 'Dr. Saúl de la Rosa Nieves',
                'position': 'Director del Laboratorio',
                'description': 'Líder del LIESE, especialista en sistemas espaciales y desarrollo de microsatélites.',
                'image_url': '/static/web/images/default-avatar.png',
                'linkedin_url': '#',
                'email': 'director@liese.unam.mx',
                'articles': []
            }
        ]
        return render(request, 'web/lideresDeProyecto.html', {'leaders': example_leaders, 'from_database': False})
    
    # Convertir QuerySet a lista de diccionarios para el template
    leaders_data = []
    for leader in leaders:
        # Obtener artículos publicados del líder
        leader_articles = Article.objects.filter(
            author=leader, 
            published=True
        ).order_by('-publication_date')
        
        # Obtener solo los primeros 3 para mostrar
        displayed_articles = leader_articles[:3]
        has_more = leader_articles.count() > 3
        
        # Convertir artículos a formato para template
        articles_data = []
        for article in displayed_articles:
            articles_data.append({
                'title': article.title,
                'content': article.content[:100] + '...' if len(article.content) > 100 else article.content,
                'created_at': article.publication_date,  # Usar created_at para que coincida con el template
                'image_url': article.image_url,
                'url': f'/articles/{article.id}/',
            })
        
        leaders_data.append({
            'full_name': leader.full_name,
            'position': leader.position or 'Miembro del Laboratorio',
            'description': leader.description or 'Contribuye al desarrollo de sistemas espaciales en LIESE.',
            'image_url': leader.image_url,
            'linkedin_url': leader.linkedin_url or '#',
            'email': leader.email,
            'articles': articles_data,  # Agregar artículos del líder
            'has_more_articles': has_more,  # Flag para mostrar "ver más"
            'id': leader.id,  # ID para el enlace "ver más artículos"
        })
    
    return render(request, 'web/lideresDeProyecto.html', {'leaders': leaders_data, 'from_database': True})


def articles_view(request):
    articles = Article.objects.filter(published=True).order_by('-publication_date')
    return render(request, 'web/articulos.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'web/article_detail.html', {'article': article})


def projects_view(request):
    """Vista que muestra los proyectos activos"""
    projects = Project.objects.filter(active=True).order_by('-start_date')
    return render(request, 'web/projects.html', {'projects': projects})


def project_detail(request, project_id):
    """Vista que muestra el detalle de un proyecto específico"""
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'web/project_detail.html', {'project': project})


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
                    'opportunity_request': opportunity_request
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
    if month > 1:
        prev_month = month - 1
        prev_year = year
    else:
        prev_month = 12
        prev_year = year - 1
    
    if month < 12:
        next_month = month + 1
        next_year = year
    else:
        next_month = 1
        next_year = year + 1
    
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
        'current_month_name': datetime_object.strftime('%B'),
        'week_days': ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
        'all_events': selected_month_events,
        'prev_month': prev_month,
        'next_month': next_month,
        'prev_month_name': datetime(prev_year, prev_month, 1).strftime("%B"),
        'current_year': year,
        'next_month_name': datetime(next_year, next_month, 1).strftime("%B"),
        'prev_year': prev_year,
        'next_year': next_year,
        }
    return render(request, 'web/events.html', context)

def activities_view(request):
    """
    Vista que combina todas las actividades del laboratorio:
    eventos, artículos, noticias y proyectos en un timeline unificado
    """
    activities = []
    filter_type = request.GET.get('filter', 'all')
    
    # Eventos próximos y recientes
    if filter_type in ['all', 'event']:
        # Cambiamos el filtro para mostrar TODOS los eventos, no solo los futuros
        events = Event.objects.filter(published=True).order_by('-start_date')[:10]
        print(f"=== EVENTS DEBUG ===")
        print(f"Total events found: {events.count()}")
        for event in events:
            print(f"- {event.title} | {event.start_date} | Published: {event.published}")
            # Convertir datetime con timezone a datetime naive para comparación
            event_date = event.start_date
            if hasattr(event_date, 'tzinfo') and event_date.tzinfo is not None:
                event_date = timezone.make_naive(event_date)
            
            activities.append({
                'type': 'event',
                'title': event.title,
                'description': event.description[:150] + '...' if len(event.description) > 150 else event.description,
                'date': event_date,
                'image': event.image,
                'url': f'/events/',
                'category': 'Evento',
                'location': event.location,
                'color_class': 'event-color'
            })
    
    # Artículos recientes
    if filter_type in ['all', 'article']:
        articles = Article.objects.filter(published=True).order_by('-publication_date')[:10]
        for article in articles:
            # Convertir date a datetime para comparación consistente
            article_date = article.publication_date
            if not isinstance(article_date, datetime):
                article_date = datetime.combine(article_date, datetime.min.time())
            
            activities.append({
                'type': 'article',
                'title': article.title,
                'description': article.content[:150] + '...' if len(article.content) > 150 else article.content,
                'date': article_date,
                'image': article.picture,
                'url': f'/articles/{article.id}/',
                'category': 'Artículo',
                'author': article.author.first_name + ' ' + article.author.last_name,
                'color_class': 'article-color'
            })
    
    # Noticias recientes - mostrar TODAS las noticias, no solo publicadas
    if filter_type in ['all', 'news']:
        # Cambiar filtro para mostrar todas las noticias
        news = News.objects.all().order_by('-publication_date')[:10]
        print(f"Debug: Found {news.count()} total news")
        for news_item in news:
            print(f"Debug: News - {news_item.title} | Published: {getattr(news_item, 'published', 'No published field')}")
            # Convertir date a datetime para comparación consistente
            news_date = news_item.publication_date
            if not isinstance(news_date, datetime):
                news_date = datetime.combine(news_date, datetime.min.time())
            
            activities.append({
                'type': 'news',
                'title': news_item.title,
                'description': news_item.content[:150] + '...' if len(news_item.content) > 150 else news_item.content,
                'date': news_date,
                'image': None,  # News model doesn't have image field
                'url': '#',
                'category': 'Noticia',
                'author': news_item.author.first_name + ' ' + news_item.author.last_name,
                'color_class': 'news-color'
            })
    
    # Proyectos
    if filter_type in ['all', 'project']:
        projects = Project.objects.all().order_by('-start_date')[:5]
        print(f"Debug: Found {projects.count()} projects")
        for project in projects:
            print(f"Debug: Project - {project.name}")
            # Convertir date a datetime para comparación consistente
            project_date = project.start_date
            if not isinstance(project_date, datetime):
                project_date = datetime.combine(project_date, datetime.min.time())
            
            activities.append({
                'type': 'project',
                'title': project.name,
                'description': project.description[:150] + '...' if len(project.description) > 150 else project.description,
                'date': project_date,
                'image': project.image,  # Usando el nuevo campo de imagen
                'url': f'/proyectos/{project.id}/',  # URL para enlazar al detalle del proyecto
                'category': 'Proyecto',
                'end_date': project.end_date,
                'color_class': 'project-color'
            })
    
    # Ordenar todas las actividades por fecha (más recientes primero)
    activities.sort(key=lambda x: x['date'], reverse=True)
    
    # Debug: mostrar qué actividades se encontraron
    print(f"Debug: Total activities before limit: {len(activities)}")
    for activity in activities:
        print(f"Debug: {activity['type']} - {activity['title']}")
    
    # Limitar a 20 actividades para mejor performance
    activities = activities[:20]
    
    print(f"Debug: Final filter_type: {filter_type}")
    print(f"Debug: Final activities count: {len(activities)}")
    
    context = {
        'activities': activities,
        'filter_type': filter_type,
        'total_count': len(activities)
    }
    
    return render(request, 'web/activities.html', context)
