from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegistrationForm(ModelForm):
    first_name = forms.CharField(label=(u'First Name'))
    last_name = forms.CharField(label=(u'Last Name'))
    username = forms.CharField(label=(u'Username'))
    email = forms.EmailField(label=(u'Email'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    verify_password = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean_first_name(self):
        first_name = self.cleaned_date['first_name']
        return first_name

    def clean_lase_name(self):
        last_name = self.cleaned_date['last_name']
        return last_name

    def clean_username(self):
        username = self.cleaned_date['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Username is taken. Please enter another.")

    def clean_password(self):
        password = self.cleaned_date['password']
        verify_password = self.cleaned_data['verify_password']
        if password != verify_password:
            raise forms.ValidationError("The passwords do not match. Please try again.")
        return password



