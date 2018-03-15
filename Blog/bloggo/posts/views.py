# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Post

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    posts = Post.objects.order_by("-pub_date")
    return render(request, "posts/index.html", {"posts": posts})

def about(request):
    #################################
    # Question 1
    # REPLACE THE LINE WITH YOUR CODE
    return render(request, "posts/about.html")

def post_details(request, pk):
    #################################
    # Question 2
    # You should create a new file in the templates directory.
    # REPLACE THE LINE WITH YOUR CODE
    post = Post.objects.get(pk=pk)
    return render(request, "posts/details.html", {"post": post})


def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(request, username=uname, password=pwd)

        if user is not None:
            auth_login(request, user)
            return index(request)
        else:
            return render(request, "posts/login.html")
    else:
        return render(request, "posts/login.html")


def logout(request):
    auth_logout(request)
    return render(request, "posts/logout.html")


def createprofile(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = User.objects.create_user(username=uname, password=pwd)
        user.save()
        return HttpResponse("Created user")
    else:
        return render(request, 'posts/createprofile.html', {})
