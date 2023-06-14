from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from .models import CustomUser


class RegistrationForm(BaseUserCreationForm):
    username = forms.CharField(label="Логин", min_length=5, max_length=30)
    email = forms.EmailField(label='Почта', required=False)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        new = CustomUser.objects.filter(username=username)
        if new.count():
            raise ValidationError("Пользователь уже существует")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        new = CustomUser.objects.filter(email=email)
        if new.count():
            raise ValidationError("Почта уже существует")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if len(password1) < 3:
            raise ValidationError("Пароль слишком короткий")
        if len(password1) > 30:
            raise ValidationError("Пароль слишком длинный")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password1

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        return user

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "avatar", "realname")
