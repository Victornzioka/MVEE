from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import HousePlan, HireArchitect, PhoneNumber

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

class SellPlan(forms.ModelForm):
	class Meta:
		model = HousePlan
		fields = '__all__'

class HireArchitect(forms.ModelForm):
	class Meta:
		model = HireArchitect
		fields = '__all__'

class phoneNumber(forms.ModelForm):
	class Meta:
		model = PhoneNumber
		fields = ['phone_number']
