from django.shortcuts import render, get_object_or_404
from .models import Vaga, Candidato
from django.db.models import Count
from django.db import models

def listar_vagas(request):
    vagas = Vaga.objects.all()
    return render(request, 'jobs/listar_vagas.html', {'vagas': vagas})

def detalhar_vaga(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id)
    candidatos = Candidato.objects.filter(vaga=vaga)
    return render(request, 'jobs/detalhar_vaga.html', {'vaga': vaga, 'candidatos': candidatos})

def candidatar_vaga(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id)
    candidato, created = Candidato.objects.get_or_create(usuario=request.user, vaga=vaga)
    return render(request, 'jobs/candidatar_vaga.html', {'vaga': vaga, 'candidato': candidato})

def relatorio_charts(request):
    vagas_por_mes = Vaga.objects.annotate(mes=models.functions.TruncMonth('data_criacao')).values('mes').annotate(total=Count('id')).order_by()
    candidatos_por_mes = Candidato.objects.annotate(mes=models.functions.TruncMonth('vaga__data_criacao')).values('mes').annotate(total=Count('id')).order_by()
    return render(request, 'jobs/relatorio_charts.html', {'vagas_por_mes': vagas_por_mes, 'candidatos_por_mes': candidatos_por_mes})
