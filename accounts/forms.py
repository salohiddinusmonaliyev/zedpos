from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import CustomUser


class RegisterForm(UserCreationForm):
    status = forms.CharField(initial='Unpaid', widget=forms.HiddenInput())
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'shop_name', 'password1', 'password2', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['status'].initial = 'Unpaid'
        # Add placeholders for each field
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username',
            'class': 'form-control',  # Add your custom class here
        })
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Enter your First Name',
            'class': 'form-control',  # Add your custom class here
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Enter your Last Name',
            'class': 'form-control',  # Add your custom class here
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter your password',
            'class': 'form-control',  # Add your custom class here
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm password',
            'class': 'form-control',  # Add your custom class here
        })
        self.fields['phone_number'].widget.attrs.update({
            'placeholder': 'Phone number',
            'class': 'form-control',  # Add your custom class here
        })
        self.fields['shop_name'].widget.attrs.update({
            'placeholder': 'Enter your Shop Name',
            'class': 'form-control',  # Add your custom class here
        })
