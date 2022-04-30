from django.shortcuts import render

from account.forms import SignUpForm
from django.views.generic import TemplateView,ListView,CreateView
from django.urls import reverse_lazy


def home(request):
    return render(request,'account/index.html')


def login(request):
    form=SignUpForm()
    
    context={}
    return render(request,'account/login.html',context)

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'account/register.html'
    
