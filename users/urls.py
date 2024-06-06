from django.urls import path
from . import views
from django.contrib import admin  # Django admin module
from django.conf import settings   # Application settings

urlpatterns = [
    path("login_user",views.login_user,name="login_user"),
    path("home",views.home,name="home"),
    path("register/",views.register_page,name="regester"),
    path("table/",views.table,name="table"),
    path("courses/",views.courses,name="courses"),
    path("Nutriment/",views.Nutriment,name="nutriment"), 
  
#  path("loginview",views.loginview.as_view(),name="loginview")
] 
# Serve static files using staticfiles_urlpatterns
