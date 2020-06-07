from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from details.models import *
from details.serializers import *
 
class UserViewSet(viewsets.ModelViewSet):  
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AppViewSet(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    queryset = App.objects.all()
