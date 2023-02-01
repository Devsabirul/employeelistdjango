from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    if request.user.is_authenticated:
        employee = Employee.objects.order_by("-id")
        for i in employee:
            print(i.picture.url)
        context = {
            'employees': employee
        }
        return render(request, "home/index.html", context)
    else:
        return redirect("login")


def add_employee(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            salary = request.POST.get('salary')
            status = request.POST.get('status')
            join_date = request.POST.get('date')
            picture = request.FILES.get('picture')
            if status == "on":
                Employee(name=name, salary=salary,
                         status=True, join_date=join_date, picture=picture).save()
            else:
                Employee(name=name, salary=salary,
                         status=False, join_date=join_date, picture=picture).save()
        return render(request, "home/add_employee.html")
    else:
        return redirect("login")


def update_employee(request, pk):
    if request.user.is_authenticated:
        id = pk
        employee = Employee.objects.get(id=id)
        fm = Employeeform(instance=employee)
        if request.method == "POST":
            fm = Employeeform(request.POST, request.FILES)
            if fm.is_valid():
                name = fm.cleaned_data.get('name')
                salary = fm.cleaned_data.get('salary')
                join_date = fm.cleaned_data.get('join_date')
                status = fm.cleaned_data.get('status')
                picture = fm.cleaned_data.get('picture')
                if picture == None:
                    Employee(
                        id=id, name=name, salary=salary, join_date=join_date, status=status, picture=employee.picture).save()
                    return redirect('/')
                else:
                    Employee(
                        id=id, name=name, salary=salary, join_date=join_date, status=status, picture=picture).save()
                    return redirect('/')
        context = {
            "form": fm
        }
        return render(request, "home/update_employee.html", context)
    else:
        return redirect("login")


def delete(request, pk):
    id = pk
    obj = Employee.objects.get(id=id)
    obj.delete()
    return redirect("/")
