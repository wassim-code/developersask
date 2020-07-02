from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordResetForm as BasePasswordResetForm,
    SetPasswordForm,
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Submit, Layout

from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        for field_name, field in self.fields.items():
            self.helper.layout.append(Field(field_name, placeholder=field.label))
        self.helper.layout.append(Submit('submit', 'Sign Up', css_class='btn-block'))
        self.helper.form_show_labels = False

class LoginForm(forms.Form):
    cred1 = forms.CharField(label='Username or Email Address')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        for field_name, field in self.fields.items():
            self.helper.layout.append(Field(field_name, placeholder=field.label))
        self.helper.layout.append(Submit('submit', 'Log in', css_class='btn-block'))
        self.helper.form_tag = False
        self.helper.form_show_labels = False

class PasswordResetForm(BasePasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        for field_name, field in self.fields.items():
            self.helper.layout.append(Field(field_name, placeholder=field.label))
        self.helper.layout.append(Submit('submit', 'Send Password Reset Email', css_class='btn-block'))
        self.helper.form_show_labels = False

class PasswordResetConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        for field_name, field in self.fields.items():
            self.helper.layout.append(Field(field_name, placeholder=field.label))
        self.helper.layout.append(Submit('submit', 'Reset My Password', css_class='btn-success btn-block'))
        self.helper.form_show_labels = False