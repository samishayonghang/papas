from django.urls import path

from.views import personal,contact,articles,loginpage,admindashboard,adminupload

urlpatterns = [
    path('', personal , name="personal"),
    path('contact/',contact,name="contact"),
    path('articles/',articles,name="articles"),
    path('loginpage/',loginpage, name="loginpage"),
    path('admindashboard/',admindashboard,name="admindashboard"),
    path('adminupload/',adminupload,name="adminupload")
]
