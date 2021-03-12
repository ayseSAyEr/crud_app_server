from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse


from .models import Employee
import pandas as pd

def index(request):
    return render(request,'index.html')

def employee_list(request):
    # latest_question_list = Employee.objects.order_by('-id')
    # names = [] 
    # names.append([q.name for q in latest_question_list])
    # rates = [] 
    # rates.append([q.hourly_rate for q in latest_question_list])
    # return HttpResponse(rates)
    employee_list = Employee.objects.order_by('-id')[:5]
    #template = loader.get_template('pages/employee_list.html')
    context = {'employee_list': employee_list}
    return render(request, 'pages/employee_list.html', context)

def detail(request, id):
    employee = get_object_or_404(Employee, pk=id)
    return render(request, 'pages/detail.html', {'employee': employee})
# Create your views here.
# def detail(request, id):
#     return HttpResponse("You're looking at employee %s." % id)

# def results(request, id):
#     response = "You're looking at the results of employee %s."
#     return HttpResponse(response % id)

# def vote(request, id):
#     return HttpResponse("You're voting on question %s." % id)
