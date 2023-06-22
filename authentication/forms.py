from django import forms
from django.contrib.auth.models import  User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-input'
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password':  forms.PasswordInput()
        }