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
        success = False
        if username and email:
            if not User.objects.filter(email = email).exists():
                User.objects.create(first_name = username,email = email)
                success = True
            return Response({'success': success})
        return Response({'success': False})

