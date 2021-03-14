from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.http import HttpResponse

from .models import Employee
from .forms import EmployeeCreate

def index(request):
    return render(request,'index.html')

# create employee steps
def create_employee(request):
    upload = EmployeeCreate()
    # when the post coming, it creates new employee
    if request.method == 'POST':
        upload = EmployeeCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('create_employee')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'pages/upload_form.html', {'upload_form':upload})

# delete employee steps
def delete_employee(request, id):
    # delete the relevant employee according to the selected id
    id = int(id)
    try:
        employee_sel = Employee.objects.get(id = id)
    except Employee.DoesNotExist:
        return redirect('index')
    employee_sel.delete()
    return redirect('employee_list')

# update employee steps
def update_employee(request, id):
    id = int(id)
    try:
        employee_sel = Employee.objects.get(id = id)
    except Employee.DoesNotExist:
        return redirect('index')
    employee_form = EmployeeCreate(request.POST or None, instance = employee_sel)
    if employee_form.is_valid():
       employee_form.save()
       return redirect('employee_list')
    return render(request, 'pages/upload_form.html', {'upload_form':employee_form})

# shows all employees in the employee list
def employee_list(request):
    employee_list = Employee.objects.order_by('-id')[:5]
    context = {'employee_list': employee_list}
    return render(request, 'pages/employee_list.html', context)

