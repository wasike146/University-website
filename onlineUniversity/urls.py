from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name='home'),
    path('coursePage/',views.coursePage,name='courses'),
    path('login/',views.userLogin,name='login'),
    path('register/',views.userRegistration,name='register'),
    path('logedin/',views.userLogedin,name='login_process')
]