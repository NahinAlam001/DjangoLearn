from cgitb import handler
from urllib import request, response
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action
def say_hello(request):
# pull data from database
# transform data 
# send email
    return render(request,'hello.html'),#{'name':'BOKACHODA'})