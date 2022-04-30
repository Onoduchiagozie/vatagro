from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate
from django.contrib.auth.views  import LoginView
from account.forms import SignUpForm
from django.views.generic import TemplateView,ListView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages


def home(request):
    return render(request,'account/index.html')


class MyLogin(LoginView):
    template_name='account/login.html'
    success_url = reverse_lazy('home')


# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				return redirect("home")
		
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request, "account/login.html",{"form":form})


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'account/register.html'

# def register(request):
#     if request.method == 'POST':
#         form=SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email=form.cleaned_data.get('email')
#             password=form.cleaned_data.get('password')
#             user=authenticate(email=email,password=password)
#             login(request,user)
#             return redirect('login')
#     else:
#         form=SignUpForm()
#     return render(request,'account/register.html',{'form':form})
