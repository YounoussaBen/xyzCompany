from django import forms
from .models import JobApplication
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a message here', 'style': 'height: 150px'}))

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'portfolio', 'resume', 'cover_letter']
        
    def clean_resume(self):
        resume = self.cleaned_data.get('resume')

        if resume:
            # Get the file extension
            file_extension = resume.name.split('.')[-1].lower()

            # Check if the file extension is not allowed
            if file_extension not in ('pdf', 'docx'):
                raise ValidationError('Only PDF and DOCX files are allowed.')

        return resume