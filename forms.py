from django import forms
from .models import Entry

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['mood','paragraphs', ]
