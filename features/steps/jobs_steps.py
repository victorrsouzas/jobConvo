# myapp/features/steps/myapp_steps.py

from behave import *
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from jobs.models import Job, Candidate

use_step_matcher("re")

@given('I am a logged-in user')
def step_impl(context):
    context.client = Client()
    context.user = User.objects.create_user(username='testuser', password='testpassword')
    context.client.login(username='testuser', password='testpassword')

@when('I access the job list page')
def step_impl(context):
    url = reverse('job_list')
    context.response = context.client.get(url)

@then('I should see "(?P<content>.+)" in the list')
def step_impl(context, content):
    assert content in context.response.content.decode()

@given('a job exists with title "(?P<job_title>.+)"')
def step_impl(context, job_title):
    context.job = Job.objects.create(title=job_title, salary_range='De 1.000 a 2.000', education_required='Ensino médio', company=context.user)

@when('I access the job detail page for "(?P<job_title>.+)"')
def step_impl(context, job_title):
    url = reverse('job_detail', args=[context.job.pk])
    context.response = context.client.get(url)

@then('I should see "(?P<job_title>.+)" in the details')
def step_impl(context, job_title):
    assert job_title in context.response.content.decode()

@when('I apply for "(?P<job_title>.+)" with salary expectation "(?P<salary_expectation>.+)", experience "(?P<experience>.+)", and last education "(?P<last_education>.+)"')
def step_impl(context, job_title, salary_expectation, experience, last_education):
    url = reverse('job_apply', args=[context.job.pk])
    data = {
        'salary_expectation': salary_expectation,
        'experience': experience,
        'last_education': last_education,
    }
    context.response = context.client.post(url, data)

@then('I should be redirected to the job list page')
def step_impl(context):
    assert context.response.status_code == 302
    assert context.response.url == reverse('job_list')

@then('I should see "(?P<job_title>.+)" in the applied jobs')
def step_impl(context, job_title):
    url = reverse('job_list')
    response = context.client.get(url)
    assert job_title in response.content.decode()

@when('I edit "(?P<job_title>.+)" with title "(?P<updated_job_title>.+)", salary range "(?P<salary_range>.+)", and education required "(?P<education_required>.+)"')
def step_impl(context, job_title, updated_job_title, salary_range, education_required):
    url = reverse('job_edit', args=[context.job.pk])
    data = {
        'title': updated_job_title,
        'salary_range': salary_range,
        'education_required': education_required,
    }
    context.response = context.client.post(url, data)

@then('I should be redirected to the job detail page for "(?P<job_title>.+)"')
def step_impl(context, job_title):
    assert context.response.status_code == 302
    assert context.response.url == reverse('job_detail', args=[context.job.pk])

@then('I should see "(?P<job_title>.+)" in the details')
def step_impl(context, job_title):
    url = reverse('job_detail', args=[context.job.pk])
    response = context.client.get(url)
    assert job_title in response.content.decode()

@when('I delete "(?P<job_title>.+)"')
def step_impl(context, job_title):
    url = reverse('job_delete', args=[context.job.pk])
    context.response = context.client.post(url)

@then('I should not see "(?P<job_title>.+)" in the list')
def step_impl(context, job_title):
    url = reverse('job_list')
    response = context.client.get(url)
    assert job_title not in response.content.decode()

@given('a candidate named "(?P<candidate_name>.+)" with salary expectation "(?P<salary_expectation>.+)", experience "(?P<experience>.+)", and last education "(?P<last_education>.+)"')
def step_impl(context, candidate_name, salary_expectation, experience, last_education):
    context.candidate = Candidate.objects.create(
        user=context.user,
        name=candidate_name,
        salary_expectation=salary_expectation,
        experience=experience,
        last_education=last_education
    )

@when('I calculate the candidate score for "(?P<candidate_name>.+)" and "(?P<job_title>.+)"')
def step_impl(context, candidate_name, job_title):
    candidate = Candidate.objects.get(name=candidate_name)
    job = Job.objects.get(title=job_title)
    context.score = candidate.calculate_candidate_score(job)

@then('the candidate score should be (?P<expected_score>\d+)')
def step_impl(context, expected_score):
    assert context.score == int(expected_score)
