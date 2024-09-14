# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, JournalEntry

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'entry-text-title', 'placeholder': 'Name of entry ✏️', 'id': 'entry-title'}),
            'content': forms.Textarea(attrs={'class': 'entry-text-box', 'placeholder': "What's on your mind today? 💭", 'id': 'entry'}),
        }

        labels = {
            'title': 'Entry Title',
            'content': "Today's Entry",
        }

    '''def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        instance.author = user  # Set the author field to the logged-in user
        if commit:
            instance.save()
        return instance
    '''
    