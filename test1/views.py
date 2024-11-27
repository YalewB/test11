from django.shortcuts import render, HttpResponse

def content(request):
    return HttpResponse('Wellcome to content writing')
