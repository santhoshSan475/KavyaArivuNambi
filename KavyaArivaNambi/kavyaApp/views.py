from django.shortcuts import render

# Create your views here.

def kavyaFunction(request):
    return render(request,"message.html")
