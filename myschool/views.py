from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse("Hello this is my test page")

def contact(request):
    return HttpResponse("THis is contact page")

def course(request):
    return HttpResponse("This is the list of cources")

def courseDetails(request, courseId):
    return HttpResponse(courseId)
