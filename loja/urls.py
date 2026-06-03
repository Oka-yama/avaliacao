from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('contato/', views.contato, name='contato')
]
