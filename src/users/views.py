from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import RegisterForm, SellPlan, HireArchitect

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for { username }')
			form.save()
			return redirect('login')

			

	else:
		form = RegisterForm()

	return render(request, "users/register.html", {"form":form})

def sellplan(request):
	if request.method == 'POST':
		form = SellPlan(request.POST, request.FILES)
		if form.is_valid():
			PlanName = form.cleaned_data.get('PlanName')
			messages.success(request, f'Submission for { PlanName } successfull')
			form.save()
			return redirect('store')


	else:
		form = SellPlan()

	return render(request, "users/sellplan.html", {"form":form})

def Hire(request):
	if request.method == 'POST':
		form = HireArchitect(request.POST, request.FILES)
		if form.is_valid():
			PlanName = form.cleaned_data.get('PlanName')
			messages.success(request, f'Submission for { PlanName } successfull. Wait for our response')
			form.save()
			return redirect('store')


	else:
		form = HireArchitect()

	return render(request, "users/hire.html", {"form":form})



