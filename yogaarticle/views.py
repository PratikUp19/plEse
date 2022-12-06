import django
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth  import authenticate,  login, logout

from.models import *
# Create your views here.

def home(request):
    q=article.objects.all()
    return render(request,'index.html',{'all':q})

def register(request):
    return render(request,'register.html')

def contact(request):
    return render(request,'contact.html')


def log(request):
    return render(request,'login.html')


def handleSign(request):
    print(request)
    if request.method=="POST":
        
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password=request.POST['password']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            # messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

    
def art(request):
    if request.method=="POST":
        t=request.POST['a_title']
        d=request.POST['a_description']
        ae=article(a_title=t,a_description=d)
        ae.save()
    return redirect('../')
def k(request,slug):
    q=article.objects.get(a_id=slug)
    a="article object("+slug+")"
    c=BlogComment.objects.filter(artic=a)
    print(c)
    return render(request,'template.html',{'q':q,'c':c})


def postComment(request):
    if request.method == "POST":
        comment=request.POST['comment']
        user=request.user
        postSno =request.POST['id']
        post= article.objects.get(a_id=postSno)
        comment=BlogComment(comment= comment, user=user, artic=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect("/")