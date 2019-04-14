from django.shortcuts import HttpResponse
import json
import re
import os
# Create your views here.

from django.views.decorators.csrf import csrf_exempt

pattern = '[\w,-]+\.[A-Za-z]{3}$'
compiled_pattern = re.compile(pattern)


def read_file(request,file_name):
    if request.method == 'GET':
        if re.match(compiled_pattern,file_name):
            with open(os.getcwd() +'/newapp/'+file_name,'r+') as file:
                lines = file.read()
                return HttpResponse("The contents of file "+file_name+"are "+lines)
        else:
            return HttpResponse("Please provide the correct file name that exist")
    else:
        return HttpResponse("You are posting request which is not to be done")


@csrf_exempt
def write_file(request):
    if request.method == 'POST':
        loaded_data = json.loads(request.body)
        file_name = loaded_data['file_name']
        if re.match(compiled_pattern,file_name):
            with open(os.getcwd() + '/newapp/'+file_name,'w+') as file:
                file.write(loaded_data['contents'])
                return HttpResponse("Successfully file created with the provided content")
        else:
            return HttpResponse("Please provide the correct file name that exist")
    else:
        return HttpResponse("You are getting request")


@csrf_exempt
def update_file(request):
    if request.method == 'POST':
        loaded_data = json.loads(request.body)
        file_name = loaded_data['file_name']
        if re.match(compiled_pattern,file_name):
            if file_name in os.listdir(os.getcwd()+'/newapp/'):
                with open(os.getcwd() + '/newapp/'+file_name,'a+') as file:
                    file.write(loaded_data['contents'])
                    return HttpResponse("Successfully file updated with the provided content")
            else:
                return HttpResponse("File Name Provided Doesn't Exist Firstly create new one")
        else:
            return HttpResponse("Please provide the correct file name that exist")
    else:
        return HttpResponse("Updated Request should be given")


@csrf_exempt
def delete_file(request,file_name):
    if request.method == 'DELETE':
        if re.match(compiled_pattern, file_name):
            if file_name in os.listdir(os.getcwd() + '/newapp/'):
                os.remove(os.getcwd() + '/newapp/'+file_name)
                return HttpResponse("File Deleted Successfully")
            else:
                return HttpResponse("Enter the correct file name ")

        else:
            return HttpResponse("File Name is not in correct format")
    else:
        return HttpResponse("Deleted request should be given")
