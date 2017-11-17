# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.timezone import datetime
from django.utils.formats import localize

from django.contrib.auth.models import User
from userApp.definitions import HttpStatus
# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        if data['username'] is not None and data['password'] is not None:
            try:
                user = User.objects.create_user(username = data['username'])
                user.set_password(data['password'])
            
                user.save()

                response = {
                    "message": "Creating user succesful"
                }

                return JsonResponse(response, status = HttpStatus.CREATED)
            except:
                response = {
                    "message": "User's already exist"
                }

                return JsonResponse(response, status = HttpStatus.BAD_REQUEST)
                
@api_view(['POST'])
def authentication(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        
        if data['username'] is not None and data['password'] is not None:
            try:
                user = User.objects.get(username = data['username'])
                
                if user.check_password(data['password']):
                    request.session['username'] = data['username']
                    response = {
                        "message": "Authentication succesful",
                        "username": data['username']
                    }

                    return JsonResponse(response, status = HttpStatus.OK)
                else:
                    response = {
                        "message": "Authentication failed"
                    }

                    return JsonResponse(response, status = HttpStatus.BAD_REQUEST)
                    
            except:
                response = {
                    "message": "Authentication failed"
                }

                return JsonResponse(response, status = HttpStatus.BAD_REQUEST)