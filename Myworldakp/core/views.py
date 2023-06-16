from django.http import HttpResponse
def displayMessage(request):
    return HttpResponse("welcome to  my new projectss")

from django.shortcuts import render
def Home(request):
    return render(request,"myworldakpHOME.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def history(request):
    return render(request,"history.html")

