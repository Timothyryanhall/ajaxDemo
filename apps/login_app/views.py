from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core import serializers
from models import *
import bcrypt, datetime

from django.db.models.functions import Lower
def index(request):
    return render(request, 'login_app/index.html')

# Create your views here.

def success(request):
    data = {"user": User.objects.get(id=request.session['user_id'])}
    return render(request, 'login_app/success.html', data)

def register(request):
    # errors = User.objects.register_validator(request.POST)
    # if len(errors):
    #     for tag, error in errors.iteritems():
    #         messages.error(request, error, extra_tags=tag)
    #     return redirect('/')
    # else:
    user = User.objects.create(
    first_name=request.POST['first'],
    last_name=request.POST['last'],
    email=request.POST['email'].lower(),
    age = request.POST['age']
    )
    request.session["user_id"] = user.id
    return redirect('/success')

def login(request):
    user = User.objects.login_validator(request.POST)
    if user["is_valid"]:
        request.session["user_id"] = user["user"].id
        return redirect('/success')
    else:
        for error in user["errors"]:
            messages.add_message(request, messages.ERROR, error)
    return redirect('/success')

def clear(request):
    request.session.clear()
    return redirect('/')

def all_json(request):
    users = User.objects.all()
    users_json = serializers.serialize("json", users)
    return HttpResponse(users_json, content_type='application/json')
    
def all_html(request):
    users = User.objects.all()
    return render(request, "login_app/all.html", {"users": users})

def find(request):
    users = User.objects.filter(first_name__startswith=request.POST['first_name_starts_with'])
    return render(request, "login_app/all.html", {"users": users})

def create(request):
    users = User.objects.order_by("-id")
    user = User.objects.create(
    first_name=request.POST['first'],
    last_name=request.POST['last'],
    email=request.POST['email'].lower(),
    age = request.POST['age']
    )
    return render(request, "login_app/all.html", {"users": users})

def findLastName(request):
    users = User.objects.filter(last_name__startswith=request.POST['last_name_starts_with'])
    return render(request, "login_app/all.html", {"users": users})

def monthFilter(request):
    users = User.objects.filter(created_at__month=request.POST['monthFilter'])
    return render(request, "login_app/all.html", {"users": users})

def lastNameOrder(request):
    users = User.objects.order_by(Lower("last_name"))
    return render(request, "login_app/all.html", {"users": users})

def firstToRegister(request):
    users = User.objects.order_by("created_at")
    return render(request, "login_app/all.html", {"users": users})

def dateRange(request):
    users = User.objects.filter(created_at__lt=request.POST['end']).filter(created_at__gt=request.POST['beginning'])
    return render(request, "login_app/all.html", {"users": users})
