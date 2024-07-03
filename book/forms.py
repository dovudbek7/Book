from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'description',)

class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'description',)
