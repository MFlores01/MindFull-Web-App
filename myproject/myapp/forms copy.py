# forms.py
from django import forms
from .models import JournalEntry

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