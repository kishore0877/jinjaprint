from django.shortcuts import render

def jinjaprint(request):
    d={'name':'yuva'}
    return render(request,'jinjaprint.html',d)
