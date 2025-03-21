from django.urls import path
from .views import index, leaders_view, opportunities_view, opportunity_request, verify_email

urlpatterns = [
    path('', index, name='index'),
    path('lideresDeProyecto.html', leaders_view, name='leaders_view'),
    path('oportunidades.html', opportunities_view, name='opportunities_view'),
    path('opportunity_request/', opportunity_request, name='opportunity_request'),
    path('verify-email/<str:token>/', verify_email, name='verify_email'),
    
]
