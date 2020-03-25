from django import forms
from .models import WikiEntry, Row, Column

class CreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=2000, widget=forms.Textarea(), help_text="Max. length for the text is 2000 characters.")
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

    def clean(self):
        cleaned_data = super(CreateForm, self).clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        if not title and not text and not name and not email:
            raise forms.ValidationError('You have to fill all fields!')
