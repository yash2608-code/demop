from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def ShowPage(request):
    user = User.objects.all()
    print(user)
    # user = [object(1),object(1),object(1),object(1)]
    # for i in user:
    #       print(i)
    # i.email
    # object(1)
    # object(1)
    # object(1)
    # object(1)
    return render(request, "app/show.html", {'users': user})


def InsertPage(request):
    return render(request, "app/insert.html")


def UpdatePage(request, pk):
    print(f"Primary Key:{pk}")
    user = User.objects.get(id=pk)
    print(user)
    return render(request, "app/update.html", {'user': user})


def InsertData(request):
    uname = request.POST['uname']
    passwd = request.POST['passwd']
    email = request.POST['email']
    print(f"{uname}\n{passwd}\n{email}")
    user = User.objects.create(uname=uname, password=passwd, email=email)
    print("DATA INSERTED SUCCESSFULLY")
    return redirect("/")


def UpdateData(request, pk):
    user = User.objects.get(id=pk)
    print(f"Got data for update:{user}")
    user.uname = request.POST['uname'] if request.POST['uname'] else user.uname
    user.email = request.POST['email'] if request.POST['email'] else user.email
    user.password = request.POST['passwd'] if request.POST['passwd'] else user.password
    user.save()
    print("DATA UPDATED SUCCESSFULLY")
    return redirect("/")


def DeleteData(request, pk):
    user = User.objects.get(id=pk)
    print(f"Got data for delete:{user}")
    user.delete()
    print("DATA DELETED SUCCESSFULLY")
    return redirect("/")
