from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('jobs/<int:pk>/apply/', views.job_apply, name='job_apply'),
    path('jobs/<int:pk>/edit/', views.job_edit, name='job_edit'),
    path('jobs/<int:pk>/delete/', views.job_delete, name='job_delete'),
    path('accounts/login/', views.job_login, name='job_login'),
    path('vagas-por-mes/', views.VagasPorMesView.as_view(), name='vagas_por_mes'),
    path('candidatos-por-mes/', views.CandidatosPorMesView.as_view(), name='candidatos_por_mes'),
    # Outras URLs aqui, como candidaturas, edição/deleção de vagas, etc.
]
