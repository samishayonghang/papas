from django.urls import path

from.views import personal,contact,articles,loginpage,admindashboard

urlpatterns = [
    path('', personal , name="personal"),
    path('contact/',contact,name="contact"),
    path('articles/',articles,name="articles"),
    path('loginpage/',loginpage, name="loginpage"),
    path('admindashboard/',admindashboard,name="admindashboard")
]
