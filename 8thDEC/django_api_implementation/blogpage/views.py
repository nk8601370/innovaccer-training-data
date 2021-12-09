from django.http import response
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegistrationForm 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponseRedirect 
from .serializers import playerSerializer 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from .models import players 
# Create your views here.

def helloWorld(request):
    return HttpResponse("Hello World!")

def index(request):
    val="Nikhil"
    return render(request, "index.html",{"name":val})

# def userregister(request):
#     if request.method == 'POST':
#         f=UserCreationForm(request.POST)
#         if f.is_valid():
#             f.save()
#     else:
#         f=UserCreationForm()
#     return render(request,'register.html',{'form':f})
    
def userregister(request):
    if request.method == 'POST':
        f=CustomRegistrationForm(request.POST)
        if f.is_valid():
            f.save()
    else:
        f=CustomRegistrationForm()
    return render(request,'register.html',{'form':f})

def signin(request):
     if request.method == "POST":
          f = AuthenticationForm(request=request, data=request.POST) 
          if f.is_valid():
               un = f.cleaned_data['username']
               pd = f.cleaned_data['password']
               user = authenticate(username = un, password = pd) 
               if user is not None:
                    login(request,user) 
                    return HttpResponseRedirect('/profile')
                    #return render(request, 'profile.html') 
     else: 
        f = AuthenticationForm() 
     return render(request, 'login.html', {'form': f}) 
    
def userProfile(request):
     return render(request, 'profile.html', {'name': request.user})

def userLogout(request): 
    logout(request) 
    return HttpResponseRedirect('/login')


class playerView(APIView): 
    def get(self, request): 
        player1 = players.objects.all() 
        serialize = playerSerializer(player1, many=True) 
        return Response(serialize.data) 
    
    def post(self,request): 
        serialize = playerSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)
    
    
        
class playerRequest(APIView):
    def put(self,request):
        player1 = players.objects.all()
        serialize = playerSerializer(player1,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)
