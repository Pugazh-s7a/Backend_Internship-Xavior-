from .models import *

from rest_framework import generics, permissions, status 
from rest_framework.response import Response

class users_api(generics.GenericAPIView):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    def get(self, request):
        request = self.request
        username = request.GET.get('username',None)
        email = request.GET.get('email',None)
        print(request,"request")
        success = False
        if username and email:
            if not User.objects.filter(email = email).exists():
                User.objects.create(first_name = username,email = email)
                success = True
                return Response({'success': success})
            # if User.objects.filter(email=email).exists():
            #     data = User.objects.get(email=email)
            #     additional_user.objects.create(role = 'backend',user_id= data)
            data =  User.objects.filter().values()
            
            data = data[4]['id']
            return Response({'success': success,"data":data})
        return Response({'success': success})

