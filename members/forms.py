from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms


# creating a form
class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=15)
    email=forms.EmailField()
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@gmail.com" in data:  
            raise forms.ValidationError("Must Not be a gmail address")
        return data
    
    class Meta:
        model=User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )
