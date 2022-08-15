from django.contrib.auth.forms import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Document
from django.db import IntegrityError


#user registration form
class RegForm(UserCreationForm):
    username=forms.CharField(label="Enter username", widget=forms.TextInput(
        attrs={'placeholder':"Enter username", 'class': 'form-control border-primary'}))
    first_name = forms.CharField(label="Enter first name", widget=forms.TextInput(
        attrs={'placeholder': "Enter your First Name", 'class': 'form-control border-primary'}))
    last_name = forms.CharField(label="Enter last name", widget=forms.TextInput(
        attrs={'placeholder': "Enter your Last Name", 'class': 'form-control border-primary'}))
    email = forms.CharField(label="Enter your email", widget=forms.EmailInput(
        attrs={'placeholder': "Enter your email ", 'class': 'form-control border-primary'}))
    password1 = forms.CharField(label="Enter your password", widget=forms.PasswordInput(
        attrs={'placeholder': "Enter your password ", 'class': 'form-control border-primary'}))
    password2 = forms.CharField(label="Enter your confirm password", widget=forms.PasswordInput(
        attrs={'placeholder': "Enter your confirm password ", 'class': 'form-control border-primary'}))
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email']

#user login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Enter username", widget=forms.TextInput(
        attrs={'placeholder': "Enter username", 'class': 'form-control border-primary'}))
    password = forms.CharField(label="Enter your password", widget=forms.PasswordInput(
        attrs={'placeholder': "Enter your password ", 'class': 'form-control border-primary'}))

#change profile form
class ChangeProfileForm(UserChangeForm):
    password = None
    first_name = forms.CharField(label="Your first name", widget=forms.TextInput(
        attrs={'placeholder': "Your First Name", 'class': 'form-control border-primary'}))
    last_name = forms.CharField(label="Your last name", widget=forms.TextInput(
        attrs={'placeholder': "Your Last Name", 'class': 'form-control border-primary'}))
    email = forms.CharField(label="Your email", widget=forms.EmailInput(
        attrs={'placeholder': "Your email ", 'class': 'form-control border-primary'}))
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'email']

#change password form
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Enter your current password", widget=forms.PasswordInput(
        attrs={'placeholder': "Enter your current password ", 'class': 'form-control border-primary'}))
    new_password1 = forms.CharField(label="Enter your new password", widget=forms.PasswordInput(
        attrs={'placeholder': "Enter your new password ", 'class': 'form-control border-primary'}))
    new_password2 = forms.CharField(label="Enter your confirm password", widget=forms.PasswordInput(
        attrs={'placeholder': "Enter your confirm password ", 'class': 'form-control border-primary'}))

#File Uploading pdfs

class GalleryForm(forms.ModelForm):
    about = forms.CharField(label="About", widget=forms.Textarea(
        attrs={'placeholder': "Enter the details", 'class': 'form-control border-primary'}))
    subject = forms.CharField(label="Subject", widget=forms.TextInput(
        attrs={'placeholder': "Enter the subject", 'class': 'form-control border-primary'}))
    file = forms.FileField(label="File",  widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model=Document
        fields=['about', 'subject', 'file']
