from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render , redirect
from .forms import usersForm
from service.models import Service
from news.models import news

def homePage(request):
    newsData = news.objects.all();
    ServiceData = Service.objects.all().order_by('-service_title')[:3]
    
    if request.method == "GET":
        st = request.GET.get('servicesearch')
        if st!=None:
            ServiceData = Service.objects.filter(service_title__icontains=st)
    data ={
        'serviceData': ServiceData,
        'newsData': newsData
    }
    return render(request, "index.html", data)

def newsdetail(request, slug):
    newsdetail = news.objects.get(news_slug=slug)
    
    data = {
        'newsdetail': newsdetail
    }
    return render(request, "newsdetail.html", data)


def topicslisting(requset):
    return render(requset, "topics-listing.html")

def contact(requset):
    myform = usersForm
    data = {'myform' : usersForm}
    try:
        if requset.method == "POST":
            name = requset.POST('name')
            email = requset.POST('email')
            subject = requset.POST('subject')
            message = requset.POST('message')
            data = {
                'name' : name,
                'email' : email,
                'subject' : subject,
                'nesasge' : message,
                'myform' : usersForm
                }
            # return HttpResponseRedirect('/')
    except:
        pass
        # return redirect('/')
    return render(requset, "contact.html",data)


def calculator(request):
    c= ''
    
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('value1'))
            n2 = eval(request.POST.get('value2'))
            opr = request.POST.get('opr')
            
            if opr == "+":
                c= n1 + n2     
            
              
    except:
        c="Involid opr"
        
    print(c)
    return render(request, "calculator.html" , {'c':c})