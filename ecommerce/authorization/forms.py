from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from .models import Order
from django.contrib.auth.models import User

# class OrderForm(ModelForm):
#     model = Order
#     fields = '__all__'

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
