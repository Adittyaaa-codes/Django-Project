from django import forms
from .models import InstaPost,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostingInsta(forms.ModelForm):
    class Meta:
        model = InstaPost
        fields = ['post','caption']

class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add a comment...',
            })
        }