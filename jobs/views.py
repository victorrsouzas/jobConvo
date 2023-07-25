from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Job, Candidate
from django.db.models import Count
from django.contrib.auth.views import LoginView
from django.views import View
from django.db import models


def job_login(request):
    return LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True
    )(request)


def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    candidates = job.candidates.all()
    return render(request, 'jobs/job_detail.html', {'job': job, 'candidates': candidates})


@login_required
def job_apply(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if request.method == 'POST':
        salary_expectation = request.POST.get('salary_expectation')
        experience = request.POST.get('experience')
        last_education = request.POST.get('last_education')

        # Cria ou obtém o candidato associado ao usuário logado (user=request.user)
        candidate, _ = Candidate.objects.get_or_create(user=request.user)

        # Define os dados do candidato e salva no banco de dados
        candidate.salary_expectation = salary_expectation
        candidate.experience = experience
        candidate.last_education = last_education
        candidate.save()

        # Adiciona o candidato à vaga
        job.candidates.add(candidate)

        return redirect('job_list')

    return render(request, 'jobs/job_apply.html', {'job': job})


@login_required
def job_edit(request, pk):
    job = Job.objects.get(pk=pk)
    if request.user == job.company:
        if request.method == 'POST':
            job.title = request.POST['title']
            job.salary_range = request.POST['salary_range']
            job.education_required = request.POST['education_required']
            job.save()
            return redirect('job_list')
        return render(request, 'jobs/job_edit.html', {'job': job})
    return redirect('job_list')


@login_required
def job_delete(request, pk):
    job = Job.objects.get(pk=pk)
    if request.user == job.company:
        if request.method == 'POST':
            job.delete()
            return redirect('job_list')
        return render(request, 'jobs/job_delete.html', {'job': job})
    return redirect('job_list')


class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(num_candidates=Count('candidates'))


class JobDetailView(View):
    template_name = 'jobs/job_detail.html'

    def get(self, request, pk):
        job = Job.objects.get(pk=pk)
        candidates = job.candidates.all()

        # Cálculo da pontuação dos candidatos em relação à vaga
        candidate_scores = {}
        for candidate in candidates:
            score = candidate.calculate_candidate_score(job)
            candidate_scores[candidate] = score

        return render(request, self.template_name, {'job': job, 'candidates': candidates, 'candidate_scores': candidate_scores})


class VagasPorMesView(View):
    template_name = 'jobs/vagas_por_mes.html'

    def get(self, request):
        # Contagem de vagas criadas por mês
        vagas_por_mes = Job.objects.annotate(mes=models.functions.TruncMonth(
            'created_date')).values('mes').annotate(total=Count('id'))

        return render(request, self.template_name, {'vagas_por_mes': vagas_por_mes})


class CandidatosPorMesView(View):
    template_name = 'jobs/candidatos_por_mes.html'

    def get(self, request):
        # Contagem de candidatos recebidos por mês
        candidatos_por_mes = Candidate.objects.annotate(mes=models.functions.TruncMonth(
            'job_applications__created_date')).values('mes').annotate(total=Count('id'))

        return render(request, self.template_name, {'candidatos_por_mes': candidatos_por_mes})
