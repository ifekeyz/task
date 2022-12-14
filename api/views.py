from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from .models import Deposite,Withdraw,Balance


class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


def deposite(request):
    user = User.objects.get(id=request.user.id)
    depot = Deposite()
    if request.method == "POST":
        amount = request.POST['amount']

        depot.amount = amount
        depot.save()


    return
    

def withdraw(request):
    user = Withdraw.objects.get(id=request.user.id)
    user.subtract()
    
    return user


def balance(request):
    user = User.objects.get(id=request.user.id)


    return