from django.urls import path
from . import views

#urlpatterns = [
#    path('', views.index,name = "index"),
    # path(route, view, opt(shortcut name))
#]

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # show all employees
    path('employee_list', views.employee_list, name='employee_list'),
    # ex: /polls/5/
    path('<int:id>/', views.detail, name='detail'),
]