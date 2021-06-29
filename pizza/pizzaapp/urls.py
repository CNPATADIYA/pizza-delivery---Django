"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from pizzaapp import views

urlpatterns = [
    path('admin/',views.adminloginview,name="adminloginpage"),
    path('admin/authenticateadmin',views.authenticateadmin),
    path('admin/homepage',views.adminhomepageview,name="adminhomepage"),
    path('admin/logoutadmin/',views.logoutadmin),
    path('admin/addpizza',views.addpizza),
    path('admin/delpizza/<int:id>',views.delpizza),
    path('admin/adminorders',views.adminorders),
    path('admin/acceptorder/<int:orderid>',views.acceptorder),
    path('admin/declineorder/<int:orderid>',views.declineorder),
    path('',views.homepage,name="homepage"),
    path('su',views.signupuser),
    path('login',views.userloginview,name='userloginpage'),
    path('me',views.customerwelcome,name="customerpage"),
    path('authenticateuser',views.authenticateuser),
    path('userlogout',views.userlogout),
    path('placeorder',views.placeorder),
    path('userorders',views.userorders),
    path('admin/acceptorder/<int:orderid>',views.acceptorder),
    path('admin/declineorder/<int:orderid>',views.declineorder),
    
]
