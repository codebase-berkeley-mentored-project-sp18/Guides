# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.shortcuts import redirect
import requests
from requests.auth import HTTPBasicAuth

import urllib
import base64

from .models import Post


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


def fitbit_info(request):
    params = {"client_id": "22CV5W",
              "response_type": "code",
              "scope": "activity",
              "redirect_uri": "http://localhost:8000/posts/getactivitydata/"}
    url = "https://www.fitbit.com/oauth2/authorize?" + urllib.parse.urlencode(params)
    return redirect(url)


def fitbit_callback(request):
    client_id = "22CV5W"
    client_secret = ""

    if request.method == 'GET':
        code = request.GET.get('code')
        get_token_url = "https://api.fitbit.com/oauth2/token"
        r = requests.post(get_token_url,
            auth=HTTPBasicAuth(client_id, client_secret),
            headers= {"content-type": "application/x-www-form-urlencoded"},
            params={"code": code, "grant_type": "authorization_code", "redirect_uri": "http://localhost:8000/posts/getactivitydata/"})
        access_token = r.json()['access_token']
        print(access_token)

        get_activity_url = "https://api.fitbit.com/1/user/-/activities/date/2018-03-21.json"
        r = requests.post(get_activity_url,
                        headers={"Authorization": "Bearer " + access_token})
                  
        return JsonResponse(r.json())

    return HttpResponse("Hello")
