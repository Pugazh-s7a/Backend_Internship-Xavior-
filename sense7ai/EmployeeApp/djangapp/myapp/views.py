

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from myapp.models import Employees,Department



def empreg(request):
    return render(request,"form.html",{})

'''def update(request):
    if request.method=='POST':
        vid=request.POST['tid']
        vname=request.POST['tname']
        vmail=request.POST['tmail']
        vcont=request.POST['tcont']
        employee=Employees(eid=vid,ename=vname,email=vmail,econtact=vcont)
        employee.save()
    else:
        return HttpResponse("Failed")
    return render(request,"employee.html",{})'''


def update(request):
  
    if request.method=='POST':
        vid=request.POST['tid']
        vname=request.POST['tname']
        vmail=request.POST['tmail']
        vcont=request.POST['tcont']
        department_id = request.POST['department_id']
        try:
            department=Department.objects.get(department_id=department_id)

            employee=Employees(eid=vid,ename=vname,email=vmail,econtact=vcont,department=department)
            employee.save()
            return HttpResponse("Employee added succesfully")
        except Department.DoesNotExist:
            return HttpResponse("Department doest not exist")
    else:
        return HttpResponse("Failed")




    

def index(request):
    # return render(request,'data.html')
    emplist=Employees.objects.all().values()
    template=loader.get_template('show.html')
    context={
        'emplist' : emplist,
    }
    return  HttpResponse(template.render(context,request))
