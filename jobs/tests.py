from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Job, Candidate

class JobPortalTests(TestCase):
    def setUp(self):
        self.user_counter = 1
        self.user = self.create_user(username=f'testuser_{self.user_counter}', password='testpassword')
        self.job = Job.objects.create(title='Test Job', salary_range='De 1.000 a 2.000', education_required='Ensino médio', company=self.user)

    def create_user(self, username, password):
        user = User.objects.create_user(username=username, password=password)
        self.user_counter += 1
        return user

    def test_job_list_view(self):
        url = reverse('job_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Job')
        self.assertNotContains(response, 'No job available')

    def test_job_detail_view(self):
        url = reverse('job_detail', args=[self.job.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Job')

    def test_job_apply_view(self):
        self.client.login(username=self.user.username, password='testpassword')
        url = reverse('job_apply', args=[self.job.pk])
        response = self.client.post(url, {'salary_expectation': '1500', 'experience': 'no_experience', 'last_education': 'Ensino médio'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.job.candidates.count(), 1)

    def test_job_edit_view(self):
        self.client.login(username=self.user.username, password='testpassword')
        url = reverse('job_edit', args=[self.job.pk])
        response = self.client.post(url, {'title': 'Updated Job', 'salary_range': 'Acima de 3.000', 'education_required': 'Ensino Superior'})
        self.assertEqual(response.status_code, 302)
        updated_job = Job.objects.get(pk=self.job.pk)
        self.assertEqual(updated_job.title, 'Updated Job')

    def test_job_delete_view(self):
        self.client.login(username=self.user.username, password='testpassword')
        url = reverse('job_delete', args=[self.job.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Job.objects.filter(pk=self.job.pk).exists())

    def test_candidate_score(self):
        user = self.create_user(username=f'testuser_{self.user_counter}', password='testpassword')
        candidate = Candidate.objects.create(
            user=user,
            name='Test Candidate',
            salary_expectation='2000',
            experience='no_experience',
            last_education='Ensino médio'
        )
        score = candidate.calculate_candidate_score(self.job)
        self.assertEqual(score, 2)

    def test_vagas_por_mes_view(self):
        url = reverse('vagas_por_mes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_candidatos_por_mes_view(self):
        url = reverse('candidatos_por_mes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
