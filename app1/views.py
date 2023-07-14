from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from urllib.request import Request
from django.http import JsonResponse
from django.contrib import messages
from .models import *


def signup(request):
    return render(request, 'text/signup.html')

def loginpage(request):
    return render(request, 'text/login.html')

def usercreate(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpass=request.POST['cpassword']
        email=request.POST['email']
        image=request.FILES['file']

        if password==cpass:
            if userlogin.objects.filter(username=username).exists():
                messages.info(request, 'This Username Is Already Exists!!!!!')
                return redirect('signup')
            else:
                user=userlogin.objects.create(
                    first_name=fname,
                    last_name=lname,
                    username=username,
                    password=password,
                    email=email,
                    image=image,                    
                )
                user.save()
        else:
            messages.info(request, 'Password doesnot match!!!!!')
            return redirect('signup')
        return redirect('loginpage')
    else:
        return render(request, 'text/signup.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if userlogin.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():

            member = userlogin.objects.get(username=request.POST['username'],password=request.POST['password'])
            messages.info(request, f'Welcome {member.username}')
            request.session['userid'] = member.id
            
            return redirect('index')

        else:
            messages.error(request, 'Invalid username or password')
            return redirect('loginpage')


    else:
        return redirect('loginpage')


 #login  session method
def adminlogout(request):
    if 'userid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 
    return redirect('loginpage')


def index(request):
    ids=request.session['userid']
    filt=userlogin.objects.get(id=ids)
    feed=post.objects.all().order_by('-id')
   
    context={
        "filt":filt,
        "feed":feed,

    }
    return render(request,"text/index.html",context)


def create_post(request):
    filt=userlogin.objects.all()
    context={
        "filt":filt
    }
    return render(request,'text/create_post.html',context)


def create_posts(request):
    ids=request.session['userid']
    idr=userlogin.objects.get(id=ids)
    posts=post()
    posts.description=request.POST.get('des', None)
    posts.tag=request.POST.get('tag', None)
    posts.user=idr
    posts.head=request.POST.get('head', None)
    posts.save()
    return redirect('index')

def profile(request):
    ids=request.session['userid']
    dats=userlogin.objects.filter(id=ids)
    file="/static/image/icon.png"
    filt=userlogin.objects.get(id=ids)
    return render(request, 'text/profile.html',{"dats":dats,"file":file,"filt":filt})

def editpro(request,pk):
    if request.method=='POST':
       
            stf = userlogin.objects.get(id=pk)
            fname=request.POST['first_name']
            lname=request.POST['last_name']
            username=request.POST['username']
            password=request.POST['password']
            cpass=request.POST['cpassword']
            email=request.POST['email']
            if password==cpass:
                if password=="":
                    created = userlogin.objects.filter(id=request.session['userid']).update(first_name=fname,last_name=lname,username=username,email=email)
                    return redirect('profile')
                else: 
                    created = userlogin.objects.filter(id=request.session['userid']).update(first_name=fname,last_name=lname,username=username,email=email,password=password)
                    return redirect('profile')

            else:
                messages.info(request,f"Check Entered Password And Confirm Password")
    return redirect('profile')

def chg_pro(request,pk):
    
    if request.method=='POST':
        stf = userlogin.objects.get(id=pk)
        img=request.FILES['file']
        stf.image=img
        stf.save()
    return redirect('profile')

def edit_post(request,pk):
    ids=request.session['userid']
    filt=userlogin.objects.get(id=ids)
    feed=post.objects.get(id=pk)

    context={
        "feed":feed
    }
    return render(request,'text/edit_post.html',context)

def delete_post(request,pk):
    ids=request.session['userid']
    filt=userlogin.objects.all()
    feed=post.objects.get(id=pk)
    feed.delete()
    context={
        "filt":filt
    }

    return redirect('index')



def save_edit(request,pk):
    ids=request.session['userid']
    idr=userlogin.objects.get(id=ids)
    posts=post.objects.get(id=pk)
    posts.description=request.POST.get('des', None)
    posts.tag=request.POST.get('tag', None)
    posts.head=request.POST.get('head', None)
    posts.save()
  
    return redirect('index')
