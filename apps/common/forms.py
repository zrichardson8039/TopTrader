from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegistrationForm(ModelForm):
    first_name = forms.CharField(label=(u'First Name'))
    last_name = forms.CharField(label=(u'Last Name'))
    username = forms.CharField(label=(u'Username'))
    email = forms.EmailField(label=(u'Email'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name

    def clean_lase_name(self):
        last_name = self.cleaned_data.get('last_name')
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Username is taken. Please enter another.")

    def clean(self):
        password = self.cleaned_data.get('password1')
        password1 = self.cleaned_data.get('password2')
        if password1 and password:
            if password != password1:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return password1

class LoginForm(forms.Form):
    username = forms.CharField(label=(u'Username'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))



