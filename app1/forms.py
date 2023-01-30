from django import forms
from . models import Signup,Image

class SignupForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Signup
        fields='__all__'

class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Signup
        fields=('Email','Password')

class UpdateForm(forms.ModelForm):
    class Meta():
        model=Signup
        fields=('Name','Age','Place','Email')

class ChangePasswordForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmNewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)

class ImageUploadForm(forms.ModelForm):
    class Meta():
        model=Image
        fields='__all__'