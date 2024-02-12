from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from applications.forms import Sign_Up_Form,Login_Form,Create_Task
from django.contrib.auth.decorators import login_required
from applications.models import Task

def index(req):
    return render(req,"index.html")
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from .forms import Login_Form  # Make sure to import your Login_Form


def login(req):
    form = Login_Form()  # Create an instance of the form
    if req.method == "POST":
        form = Login_Form(req, data=req.POST)
        if form.is_valid():
            u = req.POST.get('username')  # Use square brackets instead of parentheses
            p = req.POST.get('password')
            user = authenticate(req, username=u, password=p)
            if user is not None:
                auth.login(req, user)
                return redirect("dashboard")
    return render(req, "login.html", {"form": form})

#SignUp
def signup(req):
    form=Sign_Up_Form()
    if req.method=="POST":
        form=Sign_Up_Form(req.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    return render(req,"signup.html",{"take":form})

#Logout
def logout(req):
    auth.logout(req)
    return redirect("")

#Login
@login_required(login_url="login")
def dashboard(req):
    return render(req,"profile/dashboard.html")

#Create Task
@login_required(login_url="login")
def create_task(req):
    task=Create_Task()
    if req.method=="POST":
        task=Create_Task(req.POST)
        if task.is_valid():
            u_task=task.save(commit=False)
            u_task.user=req.user
            u_task.save()
            return redirect("view_task")
    data={"keys":task}
    return render(req,"profile/create_task.html",context=data)

#View Task
@login_required(login_url="login")
def view_task(req):
    current_user=req.user.id
    task=Task.objects.all().filter(user=current_user)
    data={"show":task}
    return render(req,"profile/view_tasks.html",context=data)

#Update Task
@login_required(login_url="login")
def update_task(req,pk):
    task=Task.objects.get(id=pk)
    form=Create_Task(instance=task)
    if req.method=="POST":
        form=Create_Task(req.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("view_task")
    data={"key":form}
    return render(req,"profile/update_tasks.html",context=data)

#Delete Task
@login_required(login_url="login")
def delete_task(req,pk):
    task=Task.objects.get(id=pk)
    if req.method=="POST":
        task.delete()
        return redirect("view_task")
    return render(req,"profile/delete_tasks.html")













    