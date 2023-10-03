from django import forms
from .models import Document
from django.core.validators import FileExtensionValidator
from django.contrib.auth.forms import SetPasswordForm
from django.core.exceptions import ValidationError

def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')
class MaxSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        if value.size > self.max_size:
            raise ValidationError(f"File size must be no more than {self.max_size / (1024 * 1024)} MB.")


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
    file = forms.FileField(
        help_text='Upload a PDF,PPTX or DOCX file. Max size is 1 MB',
        
    )
    def clean_file(self):
        file = self.cleaned_data.get('file')

        # Check file size (max size: 1MB)
        max_size = 1 * 1024 * 1024  # 1 MB

        if file and file.size > max_size:
            raise ValidationError('File size must be no more than 1 MB.')

        return file