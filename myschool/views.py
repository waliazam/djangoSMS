from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render , redirect
from .forms import usersForm

def homePage(request):
    return render(request, "index.html")

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