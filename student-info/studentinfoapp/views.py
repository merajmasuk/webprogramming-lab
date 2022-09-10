from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')
