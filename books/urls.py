from django.urls import path
from .views import issue,home,Signin,dashboard


urlpatterns = [

    path('issue',issue,name="issue"),
    path("",home,name = 'home'),
    path("login",Signin,name = 'login'),
    path("dashboard",dashboard,name = 'dashboard'),

]