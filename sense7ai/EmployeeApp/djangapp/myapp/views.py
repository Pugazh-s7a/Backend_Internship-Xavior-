

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from myapp.models import Employees,Department
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status





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

@api_view(['GET','POST'])
def employees_list(request):
    if request.method =='GET':
        #get all the employees,serialize them,return them in json
        employee=Employees.objects.all()
        serializer=EmployeeSerializer(employee,many=True)
        return JsonResponse({'Employees Details':serializer.data})
    
    if request.method =='POST':
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def employees_detail(request,eid):
    try:
        employee=Employees.objects.get(pk=eid)
    except Employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        
    elif request.method=='DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


