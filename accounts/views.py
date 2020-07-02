from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import PasswordChangeView as BasePasswordChangeView
from django.http import JsonResponse
from django.contrib import messages

from .forms import SignUpForm, LoginForm
from .models import User

class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        try:
            url = reverse('accounts:login') + '?next=' + self.request.GET['next']
        except:
            url = reverse('accounts:login')
        return url

    def form_valid(self, form):
        form.save()
        messages.success(self.request,
        f'Your account has been created successfully! You are now able to log in with your new account.')
        return super().form_valid(form)

class PasswordChangeView(BasePasswordChangeView):
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request,
        'Your password has been updated successfully!')
        return super().form_valid(form)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        context = {}
        if form.is_valid():
            try:
                email = User.objects.get(username=form.cleaned_data['cred1']).email
            except:
                email = ''
            user = authenticate(request, email=email,
                                password=form.cleaned_data['password'])
            if user is None:
                user = authenticate(request, email=form.cleaned_data['cred1'],
                                    password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                context['redirect_user'] = 'true'
            else:
                context['alert_type'] = 'danger'
                context['alert_msg'] = 'Username or Password is Incorrect.'
        return JsonResponse(context, safe=False)
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})