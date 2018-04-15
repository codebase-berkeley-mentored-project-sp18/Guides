# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Post

# Create your views here.

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
    return render(request ,"posts/post-deets.html", {"post": post})


def add(request):
    if request.method == "POST":

        title = request.POST['title']
        body = request.POST['body']

        post = Post(title=title, body=body)
        post.save()

        return JsonResponse({"title": post.title, "body": post.body, "pub_date": post.pub_date, "success": True})

    return HttpResponse("yeeha")
