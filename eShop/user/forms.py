from django import forms


from user.models import UserAcc


class RegistrationForm(forms.ModelForm):

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


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserAcc
        fields = ['email', 'password']

    email = forms.CharField(label="", widget=forms.TextInput(attrs={
        'class': 'col-lg-12 col-md-6', 'placeholder': 'Emailingizni kiriting'
    }))

    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'col-lg-12 col-md-6', 'placeholder': 'Parolni kiriting'
    }))
