from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    JOB_SALARY_CHOICES = [
        ('1000', 'Até 1.000'),
        ('1000-2000', 'De 1.000 a 2.000'),
        ('2000-3000', 'De 2.000 a 3.000'),
        ('3000+', 'Acima de 3.000'),
    ]

    JOB_EDUCATION_CHOICES = [
        ('fundamental', 'Ensino fundamental'),
        ('medio', 'Ensino médio'),
        ('tecnologo', 'Tecnólogo'),
        ('superior', 'Ensino Superior'),
        ('pos_mba_mestrado', 'Pós / MBA / Mestrado'),
        ('doutorado', 'Doutorado'),
    ]

    title = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=50, choices=JOB_SALARY_CHOICES)
    education_required = models.CharField(max_length=50, choices=JOB_EDUCATION_CHOICES)
    company = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Candidate(models.Model):
    SALARY_CHOICES = [
        ('1000', 'Até 1.000'),
        ('1000-2000', 'De 1.000 a 2.000'),
        ('2000-3000', 'De 2.000 a 3.000'),
        ('3000+', 'Acima de 3.000'),
    ]

    EXPERIENCE_CHOICES = [
        ('no_experience', 'Sem experiência'),
        ('1-3_years', '1 a 3 anos'),
        ('3-5_years', '3 a 5 anos'),
        ('5+_years', 'Mais de 5 anos'),
    ]

    EDUCATION_CHOICES = [
        ('fundamental', 'Ensino fundamental'),
        ('medio', 'Ensino médio'),
        ('tecnologo', 'Tecnólogo'),
        ('superior', 'Ensino Superior'),
        ('pos_mba_mestrado', 'Pós / MBA / Mestrado'),
        ('doutorado', 'Doutorado'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    salary_expectation = models.CharField(max_length=50, choices=SALARY_CHOICES)
    experience = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES)
    last_education = models.CharField(max_length=50, choices=EDUCATION_CHOICES)
    applied_jobs = models.ManyToManyField(Job, related_name='candidates')

    def calculate_candidate_score(self, job):
        # Implemente a lógica de cálculo da pontuação aqui
        # Você pode acessar as informações da vaga (job) e do candidato (self) para calcular a pontuação
        # Retorne a pontuação calculada como um valor numérico
        # Por exemplo:
        score = 0
        if self.salary_expectation <= job.salary_range:
            score += 1
        if self.last_education in job.education_required:
            score += 1
        return score

    def __str__(self):
        return self.user.email
