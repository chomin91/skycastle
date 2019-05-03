from django.contrib.auth import login
from django.contrib.auth.views import LoginView as django_LoginView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import User, CoordinatorInfo
from .forms import SignupForm, CoordiInfoForm, UnivInfoForm
def check_id(request):
	is_exist = User.objects.filter(email=request.POST.get('id', None)).exists()
	return HttpResponse(is_exist)

class LoginView(django_LoginView):
	def __init__(self):
		self.template_name = 'accounts/login.html'

class CoordinatorSignupView(CreateView):
	model = User
	form_class = SignupForm
	template_name = 'accounts/signup_coordi.html'
	
	def form_valid(self, form):
		coordinator = User.objects.create_coordinator(**form.cleaned_data)
		if coordinator is None:
			return redirect('accounts/signup_fail.html')
		else:
			login(self.request, coordinator)
			return redirect('addinfo_coordi')

class AddCoordiInfoView(CreateView):
    model = CoordinatorInfo
    form_class = CoordiInfoForm
    template_name = 'accounts/addinfo_coordi.html'
    
    def form_valid(self, form):
        User.objects.SetCoordinatorInfo(self.request.user, **form.cleaned_data)
        return render(self.request, 'accounts/signup_done.html')

class ParentSignupView(CreateView):
	model = User
	form_class = SignupForm
	template_name = 'accounts/signup_parent.html'

	def form_valid(self, form):
		parent = User.objects.create_parent(**form.cleaned_data)
		if parent is None:
			return redirect('accounts/signup_fail.html')
		return render(self.request, 'accounts/coordinator/add_info')
	
class SignupDoneView():
	template_name = 'accounts/singup_done.html'

class add_certificate(CreateView):
	model = CoordinatorInfo
	form_class = UnivInfoForm
	template_name = 'accounts/add_certificate.html'
