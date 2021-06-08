from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('accounts/register/',views.register,name='register'),
    path('read/analatics/',views.analatics,name='analatics'),
    ]