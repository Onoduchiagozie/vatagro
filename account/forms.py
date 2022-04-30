from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms



class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            # 'first_name', 
            # 'last_name', 
            # 'username', 
            'email', 
            # 'password1', 
            ]

    # def __init__(self,*args,**kwargs):
    #     super(SignUpForm,self).__init__(*args,**kwargs)
    #     # self.fields['first_name'].widget.attrs['placeholder']='Enter First Name'
    #     # self.fields['last_name'].widget.attrs['placeholder']='Enter Last Name'
    #     # self.fields['username'].widget.attrs['placeholder']='User Name'
    #     # self.fields['email'].widget.attrs['placeholder']='Enter Email'
    #     # self.fields['password1'].widget.attrs['placeholder']='Repeat Password'

