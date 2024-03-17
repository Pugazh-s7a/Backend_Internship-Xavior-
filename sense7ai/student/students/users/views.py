from django.shortcuts import render,HttpResponse
from . models import Users,Mark

# Create your views here.
def index(request):
    # Retrieve data from your models
    users_data = Users.objects.all()
    mark_data = Mark.objects.all()
    # Create context dictionary
    context = {'users_data': users_data,
                'mark_data': mark_data,}
    return render(request,"users/index.html",context)

def userreg(request):
    return render(request,"users/userreg.html",{})

def insertuser(request):
    if request.method=='POST':
        vurollno= request.POST['tuid'];
        vuname = request.POST['tuname'];
        vuemail = request.POST['tuemail'];
        vucontact= request.POST['tucontact'];
        us=Users(urollno=vurollno, uname=vuname, uemail=vuemail, ucontact=vucontact);
        us.save();
        return HttpResponse("User Sucessfully Added!!")
    else:
        return HttpResponse("Error")
    return render(request, 'users/userreg.html',{})