from django import forms
from .models import WikiEntry, Row, Column

class CreateForm(forms.Form):
    row = forms.IntegerField()
    column = forms.IntegerField()
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=2000, widget=forms.Textarea())
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

    def clean(self):
        cleaned_data = super(CreateForm, self).clean()
        f_title = cleaned_data.get('title')
        f_name = cleaned_data.get('name')
        f_email = cleaned_data.get('email')
        if not f_title and not f_name and not f_email:
            raise forms.ValidationError('You have to fill all fields!')
