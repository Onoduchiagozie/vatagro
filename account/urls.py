
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
        # path('login',views.login_request,name='login'),
        #         path('register',views.register,name='register'),

                     path('login',views.MyLogin.as_view(),name='login'),
                path('register',views.SignUpView.as_view(),name='register')


]