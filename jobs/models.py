# models.py
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
    description = models.TextField()
    salary_range = models.CharField(max_length=50, choices=JOB_SALARY_CHOICES)
    education_required = models.CharField(
        max_length=50, choices=JOB_EDUCATION_CHOICES)
    company = models.ForeignKey(
        User, related_name='jobs', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

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

    name = models.CharField(max_length=100)
    salary_expectation = models.CharField(
        max_length=50, choices=SALARY_CHOICES)
    experience = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES)
    last_education = models.CharField(max_length=50, choices=EDUCATION_CHOICES)
    job_applications = models.ManyToManyField(Job, related_name='candidates')
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, related_name='candidates', on_delete=models.CASCADE)

    def calculate_candidate_score(self, job):
        score = 0

        if self.salary_expectation:
            if job.salary_range == 'Até 1.000' and int(self.salary_expectation) <= 1000:
                score += 1
            elif job.salary_range == 'De 1.000 a 2.000' and 1000 < int(self.salary_expectation) <= 2000:
                score += 1
            elif job.salary_range == 'De 2.000 a 3.000' and 2000 < int(self.salary_expectation) <= 3000:
                score += 1
            elif job.salary_range == 'Acima de 3.000' and int(self.salary_expectation) > 3000:
                score += 1

        education_values = {
            'Ensino fundamental': 1,
            'Ensino médio': 2,
            'Tecnólogo': 3,
            'Ensino Superior': 4,
            'Pós / MBA / Mestrado': 5,
            'Doutorado': 6
        }

        # Verificar se o valor existe no dicionário antes de acessá-lo
        if job.education_required in education_values and self.last_education in education_values:
            job_education_value = education_values[job.education_required]
            candidate_education_value = education_values[self.last_education]

            if candidate_education_value >= job_education_value:
                score += 1

        return score

    def __str__(self):
        return self.name
