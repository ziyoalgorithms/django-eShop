from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)

from user.models import UserAcc, UserAccProfile
from user.models import GENDER_CHOICES, COUNTRY_CHOICES


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(
        max_length=100,
        error_messages={
            'required': 'Emailingizni kiritishingiz kerak!'
        },
        widget=forms.EmailInput
    )
    name = forms.CharField(
        max_length=30,
        error_messages={
            'required': 'Username kiritishingiz kerak!'
        },
        widget=forms.TextInput
    )
    phone = forms.CharField(
        max_length=13,
        error_messages={
            'required': 'Telefon raqamingizni kiritishingiz kerak!'
        },
        widget=forms.TextInput
    )

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserAcc
        fields = ['email', 'name', 'phone', 'password', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserAcc.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Boshqa email kiriting, Bu email band!')
        return email

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        u = UserAcc.objects.filter(name=name)
        if u.count():
            raise forms.ValidationError('Foydalanuvchi nomi band!')
        return name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        u = UserAcc.objects.filter(phone=phone)
        if u.count():
            raise forms.ValidationError('Telefon raqami band!')
        return phone

    def clena_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Parollar bir biriga mos emas!")
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'col-lg-12 col-md-6', 'placeholder': 'Email'}
        )
        self.fields['name'].widget.attrs.update(
            {'class': 'col-lg-12 col-md-6', 'placeholder': 'Username'}
        )
        self.fields['phone'].widget.attrs.update(
            {'class': 'col-lg-12 col-md-6', 'placeholder': 'Phone'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'col-lg-12 col-md-6', 'placeholder': 'Password'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'col-lg-12 col-md-6', 'placeholder': 'Repeat password'}
        )

        for field, _ in self.fields.items():
            _.label = ""


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserAcc
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Emailingizni kiriting'
        })
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Parolni kiriting'}
        )
        for field, _ in self.fields.items():
            _.label = ''


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserAcc
        fields = ['email', 'name', 'phone']

    email = forms.EmailField(
        label="Elektron pochta manzili (o'zgartirib bo'lmaydi)")
    name = forms.CharField(label='Username')
    phone = forms.CharField(label='Telefon raqam')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email', 'readonly': 'readonly'}
        )
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Username'
        })
        self.fields['phone'].widget.attrs.update({
            'placeholder': 'Telefon raqam'
        })
        for field, _ in self.fields.items():
            _.widget.attrs['class'] = 'col-lg-12 col-md-6'


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserAccProfile
        fields = ['first_name', 'last_name',
                  'gender', 'country', 'address_line']

    first_name = forms.CharField(label='Ism')
    last_name = forms.CharField(label='Familiya')
    gender = forms.ChoiceField(label='Jins', choices=GENDER_CHOICES)
    country = forms.ChoiceField(label='Viloyat', choices=COUNTRY_CHOICES)
    address_line = forms.CharField(label="Manzil")

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Isminizni kiriting'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Familiyangizni kiriting'
        })
        self.fields['address_line'].widget.attrs.update({
            'placeholder': "To'liq manzilni kiriting"
        })
        for field, _ in self.fields.items():
            _.widget.attrs['class'] = 'col-lg-12 col-md-6'


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(
        max_length=63, label='', widget=forms.TextInput(
            attrs={'class': 'col-lg-12 col-md-6', 'placeholder': 'Email'}
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserAcc.objects.filter(email=email)
        if not u:
            raise forms.ValidationError('Afsuski biz bu emailni topa olmadik!')

        return email


class PwdResetConfirmForm(SetPasswordForm):

    new_password1 = forms.CharField(
        label='', min_length=8, max_length=31, widget=forms.PasswordInput(
            attrs={'class': 'col-lg-12 col-md-6',
                   'placeholder': 'Yangi parolni kiriting'}
        )
    )

    new_password2 = forms.CharField(
        label='', min_length=8, max_length=31, widget=forms.PasswordInput(
            attrs={'class': 'col-lg-12 col-md-6',
                   'placeholder': 'Parolni tasdiqlang'}
        )
    )
