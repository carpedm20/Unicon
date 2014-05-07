from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags

from .models import Account

class AccountCreateForm(UserCreationForm):
    error_messages = {
        'duplicate_email': "A user with that e-mail already exists.",
        'email_mismatch': "The two e-mail fields didn't match.",
    }

    username = forms.EmailField(label="E-mail")
    #username1 = forms.EmailField(label="E-mail", widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    #username2 = forms.EmailField(label="Confirm E-mail", widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))
 
    def is_valid(self):
        form = super(AccountCreateForm, self).is_valid()
        #for f, error in self.errors.iteritems():
        #    if f != '__all_':
        #        self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form
 
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(AccountCreateForm, self).save(commit=False)
        user.save()
        user_profile = Account(user=user)

        if commit:
            user_profile.save()

        return user_profile

class AccountAuthForm(AuthenticationForm):
    username = forms.EmailField(label="E-mail")
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
 
    def is_valid(self):
        form = super(AccountAuthForm, self).is_valid()
        #print self.cleaned_data["username"]
        return form
