from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField


class AddUserForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginUserForm(forms.Form):
    
    username = forms.CharField(
        widget=forms.TextInput(),
        required=False,
        label='نام کاربری'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        label='رمز عبور'
    )

    captcha = CaptchaField()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('لطفاً نام کاربری را وارد نمایید')
        
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('لطفاً رمز عبور خود را تأیید نمایید')
        
        return password

