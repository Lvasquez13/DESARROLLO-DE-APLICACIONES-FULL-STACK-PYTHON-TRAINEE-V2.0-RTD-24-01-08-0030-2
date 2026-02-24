from django.urls import path
from .views import registro
from django.contrib.auth.views import LoginView
from .views import area_reservada
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('area/', area_reservada, name='area_reservada'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]