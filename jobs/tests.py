from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Job, Candidate

class JobPortalTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.job = Job.objects.create(title='Test Job', salary_range='1000', education_required='fundamental', company=self.user)

    def test_job_list_view(self):
        url = reverse('job_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Job')
        self.assertNotContains(response, 'No job available')  # Verifica que a mensagem "No job available" não está presente

    def test_job_detail_view(self):
        url = reverse('job_detail', args=[self.job.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Job')

    def test_job_apply_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('job_apply', args=[self.job.pk])
        response = self.client.post(url, {'salary_expectation': '1000', 'experience': 'no_experience', 'last_education': 'fundamental'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.job.candidates.count(), 1)

    def test_job_edit_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('job_edit', args=[self.job.pk])
        response = self.client.post(url, {'title': 'Updated Job', 'salary_range': '2000-3000', 'education_required': 'medio'})
        self.assertEqual(response.status_code, 302)
        updated_job = Job.objects.get(pk=self.job.pk)
        self.assertEqual(updated_job.title, 'Updated Job')

    def test_job_delete_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('job_delete', args=[self.job.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Job.objects.filter(pk=self.job.pk).exists())
