from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.login, name='login'),
    path('myaccount/password_change/', views.PasswordChangeView.as_view(), name='password_change'),
]