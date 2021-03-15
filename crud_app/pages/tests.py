from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views
from .models import Employee

# create the home page simple test 
class HomePageTests(SimpleTestCase):

    # check the home page
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    # check the view url 
    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    # check the using correct template
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # TODO check home page contains correct html
    # def test_home_page_contains_correct_html(self):
    #     response = self.client.get('/')
    #     with open('pages/templates/index.html', 'r') as f:
    #         html_string = f.read()
    #     self.assertContains(response, html_string)

    # check home pages does not contain incorrect html
    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

h_rate = 30
w_percentage = 100

# check Employee object
class EmployeeTests(TestCase):

    # create sample employee
    def setUp(self):
        Employee.objects.create(name='Martin', surname='Mustermann', hourly_rate= h_rate, working_percentage=w_percentage)

    # check employee name
    def test_name_content(self):
        employee = Employee.objects.get(id=1)
        expected_object_name = f'{employee.name}'
        self.assertEquals(expected_object_name, 'Martin')
        
    # check the employee salary
    def test_salary_content(self):
        employee = Employee.objects.get(id=1)
        expected_object_salary = employee.salary
        salary_calculated = h_rate * 160 * w_percentage / 100
        self.assertEquals(expected_object_salary, salary_calculated)

    # check the view employee in the employee_list page 
    def test_employee_list_view(self):
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Martin')
        self.assertTemplateUsed(response, 'pages/employee_list.html')
