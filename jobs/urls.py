from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from jobs import views as jobs_views

urlpatterns = [
    path('jobs-admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', jobs_views.listar_vagas, name='listar_vagas'),
    path('vaga/<int:vaga_id>/', jobs_views.detalhar_vaga, name='detalhar_vaga'),
    path('vaga/<int:vaga_id>/candidatar/', jobs_views.candidatar_vaga, name='candidatar_vaga'),
    path('relatorio/', jobs_views.relatorio_charts, name='relatorio_charts'),
]