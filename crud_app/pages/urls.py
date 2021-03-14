from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # show all employees
    path('employee_list', views.employee_list, name='employee_list'),
    # create 
    path('create_employee', views.create_employee, name = 'create_employee'),
    # update 
    path('update_employee/<int:id>', views.update_employee, name = 'update_employee'),
    # delete 
    path('delete_employee/<int:id>', views.delete_employee, name = 'delete_employee'),
    # calculate salary
    path('calculate_salary', views.calculate_salary, name = 'calculate_salary'),
    
    # # ex: /polls/5/
    # path('<int:id>/', views.detail, name='detail'),
   
]
