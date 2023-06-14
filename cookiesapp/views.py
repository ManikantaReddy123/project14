from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class Input(View):
    def post(self,request):
        x=int(request.POST["t1"])
        y=int(request.POST["t2"])
        z=x+y
        res=HttpResponse("The Data Is Submitted Successfully")
        res.set_cookie('c',str(z),max_age=60)
        return res
class Display(View):
    def get(self,request):
        if 'c' in request.COOKIES:
            p=request.COOKIES['c']
            return HttpResponse("THE SUM TWO VALUES IS::"+p)
        else:
            return render(request,'home.html')




