from sre_constants import SUCCESS
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from signup . models import Saveuser

# Create your views here.


def saveuser(request):
    if request . method == 'POST':
        studentname = request . POST['studentname']
        city = request . POST['city']
        mno = request . POST['mno']
        cls = request . POST['cls']
        collegename = request . POST['collegename']
      
    
        v=Saveuser(studentname=studentname,city=city,mno=mno,cls=cls,collegename=collegename)
        v.save()
        return render (request,'index.html')
    return render (request,'signup.html')

def show(request):
    data=Saveuser.objects.all()
    print(data)
    return render (request,'index.html',{'data':data})














