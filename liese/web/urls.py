from django.urls import path
from .views import index, leaders_view, opportunities_view, opportunity_request, verify_email, articles_view, success_email_verification, error_email_verification, article_detail

urlpatterns = [
    path('', index, name='index'),
    path('lideresDeProyecto.html', leaders_view, name='leaders_view'),
    path('oportunidades.html', opportunities_view, name='opportunities_view'),
    path('articles/', articles_view, name='articles_page'),
    path('opportunity_request/', opportunity_request, name='opportunity_request'),
    path('verify-email/<str:token>/', verify_email, name='verify_email'),
    path('success_email_verification/', success_email_verification, name='success_email_verification'),
    path('error_email_verification/', error_email_verification, name='error_email_verification'),
    path('articles/', articles_view, name='articles_view'),
    path('articles/<int:article_id>/', article_detail, name='article_detail'),
]
