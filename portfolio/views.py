from django.shortcuts import render,redirect
from.models import Contact,Blogs
from django.http import JsonResponse

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def personal(request):
    return render(request,'portfolio/index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        message=request.POST.get('message')
        Contact.objects.create(name=name, email=email,mobile=mobile,message=message)
        messages.success(request,"Your message has been submitted sucessfully")
        return redirect('contact')
    messages.error(request, 'Invalid form submission.')
     

    return render(request,'portfolio/contacts.html')


def articles(request):
    recent_article=Blogs.objects.all().order_by('-uploaddate').first()
    articles=Blogs.objects.all()
    return render(request,'portfolio/articles.html',{'articles':articles,'recent_article':recent_article})

def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(username=username,email=email,password=password)
        if user is not None:
            if user.is_superuser:
             login(request,user)
             return JsonResponse({"success":True, "message":"Login successfull"})
            else:
                return JsonResponse({"success":False,"message":"login denied! Only admin can acess "})

        else:
            return JsonResponse({"success": False, "message": "Invalid credentials"}, status=400)
        
    return render(request,'portfolio/loginpage.html')

def admindashboard(request):
    recent_articles=Blogs.objects.all().order_by('-uploaddate').first()
    articles=Blogs.objects.all()
    return render(request,'portfolio/admindashboard.html',{'recent_articles':recent_articles,'articles':articles})

def adminupload(request):
    username=request.user.username
    if request.method=="POST":
     articlewrite=request.POST.get('articlewrite')
     articleimage=request.FILES.get('articleimage')
     title=request.POST.get('title')
     Blogs.objects.create(title=title,description=articlewrite,photos=articleimage)
     messages.success(request,"you have successfully posted article")
     return redirect('adminupload')


    return render(request,'portfolio/articleupload.html',{'username':username})