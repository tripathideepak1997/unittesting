from django.shortcuts import render
from django.http import HttpResponse


def wishing_user(request, num_input):
    if num_input in range(5, 13):
        return HttpResponse('Good Morning')
    elif num_input in range(12, 18):
        return HttpResponse('Good Evening')
    elif num_input in range(18, 24):
        return HttpResponse('Good Night')
    else:
        return HttpResponse('Go To Bed')
