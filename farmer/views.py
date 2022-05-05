
from django.shortcuts import get_object_or_404, render

from goods.models import ShippingAddress
from . models import MediaFiles
from django.views.generic.edit import UpdateView,CreateView
from django.views.generic import ListView
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


class UserUpdateView(UpdateView):
    model=User
    fields = ['first_name','last_name','email','phone','client_status','Active_Shipping_Address']
    success_url = '/'
    template_name = 'farmer/profile.html'


# LISTVIEW
class ShippingAddressUpdateView(UpdateView):
    model=ShippingAddress
    fields = '__all__'
    success_url = '/'
    template_name = 'farmer/shippingaddress.html'

class ShippingAddressCreateView(CreateView):
    model=ShippingAddress
    fields = '__all__'
    success_url = '/'
    template_name = 'farmer/createnew.html'

class ShippingAddressListView(ListView):
    model=ShippingAddress
    # fields = '__all__'
    success_url = '/'
    template_name = 'farmer/listshippingaddress.html'
    context_object_name='object'

    
# FARMERONLY
def storelocation(request):
    return render(request,'farmer/storelocation.html')

# LIST VIEW OF EXITING THEN (CREATEVIEW)
def myproducts(request):
    return render(request,'farmer/myproducts.html')

# LISTVIEW TABLE
def purchasedproducts(request):
    return render(request,'farmer/purchasedproduct.html')

def new(request):
    return  render(request,'farmer/createnew.html')