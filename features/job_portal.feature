# job_portal.feature

Feature: Job Portal

  Background:
    Given I am a logged-in user

  Scenario: View job list
    When I access the job list page
    Then I should see "Test Job" in the list

  Scenario: View job detail
    Given a job exists with title "Test Job"
    When I access the job detail page for "Test Job"
    Then I should see "Test Job" in the details

  Scenario: Apply for a job
    Given a job exists with title "Test Job"
    When I apply for "Test Job" with salary expectation "1500", experience "no_experience", and last education "Ensino médio"
    Then I should be redirected to the job list page
    And I should see "Test Job" in the applied jobs

  Scenario: Edit a job
    Given a job exists with title "Test Job"
    When I edit "Test Job" with title "Updated Job", salary range "Acima de 3.000", and education required "Ensino Superior"
    Then I should be redirected to the job detail page for "Updated Job"
    And I should see "Updated Job" in the details

  Scenario: Delete a job
    Given a job exists with title "Test Job"
    When I delete "Test Job"
    Then I should be redirected to the job list page
    And I should not see "Test Job" in the list

  Scenario: Calculate candidate score
    Given a job exists with title "Test Job"
    And a candidate named "Test Candidate" with salary expectation "2000", experience "no_experience", and last education "Ensino médio"
    When I calculate the candidate score for "Test Candidate" and "Test Job"
    Then the candidate score should be 2

  Scenario: View job applications by month
    When I access the job applications by month page
    Then I should see the job application chart

  Scenario: View candidates by month
    When I access the candidates by month page
    Then I should see the candidates chart
