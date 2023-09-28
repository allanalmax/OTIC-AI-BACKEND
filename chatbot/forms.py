from django import forms
from .models import Document
from django.contrib.auth.forms import SetPasswordForm

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file',)
    error_css_class = 'errorlist'
