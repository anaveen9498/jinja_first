from django.shortcuts import render

# Create your views here.
def jinja_first(request):
    d={'name':'Naveen','age':22}
    return render(request,'jinja_first.html',context=d)