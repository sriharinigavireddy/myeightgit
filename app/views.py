from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':13,'b':45,'c':98}
    return render(request,'operations.html',d)