from django import forms
from .models import InstaPost

class PostingInsta(forms.ModelForm):
    class Meta:
        model = InstaPost
        fields = ['post','caption']