from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_principal, name='tela_principal'),
    path('confirmar/', views.confirmar_presenca, name='confirmar_presenca'),
    path('admin-convite/', views.login_admin, name='login_admin'),
    path('painel/', views.painel_admin, name='painel_admin'),
    path('confirmar/', views.confirmar_presenca, name='confirmar_presenca'),
    path('admin-convite/', views.login_admin, name='login_admin'),
    path('painel/', views.painel_admin, name='painel_admin'),
    path('logout/', views.logout_admin, name='logout_admin'),
    path('excluir/<int:id>/', views.excluir_confirmacao, name='excluir_confirmacao'),

]
