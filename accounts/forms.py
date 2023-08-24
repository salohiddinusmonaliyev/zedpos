from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username','phone_number', 'shop_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
