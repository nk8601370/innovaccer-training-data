from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.helloWorld, name='helloWorld'),
    path('page', views.index, name='index'),
    path('register', views.userregister, name='register'),
    path('signin',views.signin,name='signin'),
    path('profile', views.userProfile,name='userprofile'),
    path('logout',views.userLogout,name='userlogout'),
    path('api/', views.playerView.as_view()),
    path('api/<int:id>', views.playerRequest.as_view(), name="playerRequest") 
]