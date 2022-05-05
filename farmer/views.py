from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from . models import MediaFiles
from django.views.generic.edit import UpdateView
from account.models import User

# Create your views here.
def account(request):
    files=get_object_or_404(MediaFiles,pk=1)
    context={
        'file':files
    }
    return render(request,'farmer/account.html',context)



def dashboard(request):
    return render(request,'farmer/dashboard.html')


class AuthorUpdateView(UpdateView):
    model=User
    fields = ['first_name','last_name','email','phone','client_status']
    success_url = '/'
    template_name = 'farmer/profile.html'


def shippingaddress(request):
    return render(request,'farmer/shippingaddress.html')


def storelocation(request):
    return render(request,'farmer/storelocation.html')


def myproducts(request):
    return render(request,'farmer/myproducts.html')

def purchasedproducts(request):
    return render(request,'farmer/purchasedproduct.html')

