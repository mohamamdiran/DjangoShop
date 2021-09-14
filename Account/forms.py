from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    error_css_class = "info"
    class Meta:
        model = User
        fields = ('username','password1','password2', 'email')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'signup-form-input'

        self.fields['email'].widget.attrs['placeholder'] = "email"
        self.fields['username'].widget.attrs['placeholder'] = "username"
        self.fields['password1'].widget.attrs['placeholder'] = "password"
        self.fields['password2'].widget.attrs['placeholder'] = "confirm password"

        

