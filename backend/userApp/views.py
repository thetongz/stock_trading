# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth.models import User
from rest_framework import status
from userApp.responses import ResponseObject

from userApp.models import UserDetail
from userApp.serializers import UserDetailSerializer
# Create your views here.
@api_view(['POST'])
@permission_classes((AllowAny, ))
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        if data['username'] is not None and data['password'] is not None:
            try:
                userSerializer = UserDetailSerializer(data = {
                    "username": data['username'],
                    "cash": 10000,
                    "stepCount": 0
                })

                if userSerializer.is_valid():
                    user = User.objects.create_user(username = data['username'])
                    Token.objects.get_or_create(user = user)
                    user.set_password(data['password'])
                    userSerializer.save()
                    user.save()
                    response = ResponseObject.createSuccessCreateUserResponse()

                    return JsonResponse(response, status = status.HTTP_201_CREATED)
            except:
                response = ResponseObject.createFailedCreateUserResponse()

                return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)
                
@api_view(['POST'])
@permission_classes((AllowAny, ))
def logIn(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        
        if data['username'] is not None and data['password'] is not None:
            try:
                user = authenticate(username = data['username'], 
                                    password = data['password'])
                if user is not None:
                    token, _ = Token.objects.get_or_create(user=user)

                    response = ResponseObject.createSuccessLoginResponse(user.username, token.key)

                    return JsonResponse(response, status = status.HTTP_200_OK)

            except:
                response = ResponseObject.createFailedLoginResponse()

                return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def logOut(request):
    if request.method == 'GET':

        response = ResponseObject.createSuccessLogoutResponse()

        return JsonResponse(response, status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getUserDetail(request):
    if request.method == 'GET':

        user = UserDetail.objects.get(pk = request.user)
        userSerializer = UserDetailSerializer(user)
        response = ResponseObject.createSuccessGetUserDetailResponse(userSerializer.data)

        return JsonResponse(response, status = status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def nextStep(request):
    if request.method == 'PUT':

        user = UserDetail.objects.get(pk = request.user)
        userSerializer = UserDetailSerializer(user, data = request.data)

        if userSerializer.is_valid():
            userSerializer.save()
            response = ResponseObject.createSuccessNextStepResponse()

            return JsonResponse(response, status = status.HTTP_200_OK)