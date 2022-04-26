from django import forms

from .models import Notes
from django.core.exceptions import ValidationError


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ("title", "text")
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control my-5'}),
            "text": forms.Textarea(attrs={"class": "form-control mb-5"})
        }

    '''def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('we only accept notes about Django!')
        return title'''
