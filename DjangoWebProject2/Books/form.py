
from django import forms
from Books.models import Book

class PostForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','status','sheets','price','publisher']