from django import forms
from .models import WikiEntry, Row, Column

class CreateForm(forms.Form):
    row = forms.IntegerField()
    column = forms.IntegerField()
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=2000, widget=forms.Textarea())
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    position = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super(CreateForm, self).clean()
        f_row = cleaned_data.get('row')
        f_column = cleaned_data.get('column')
        f_title = cleaned_data.get('title')
        f_text = cleaned_data.get('text')
        f_name = cleaned_data.get('name')
        f_email = cleaned_data.get('email')
        if f_title and f_name and f_email:
            f_position = WikiEntry.objects.filter(row=f_row, column=f_column).count() + 1
            i_row = Row.objects.get(pk=f_row)
            i_column = Column.objects.get(pk=f_column)
            new = WikiEntry(
                row = i_row,
                column = i_column,
                title = f_title,
                text = f_text,
                contributor_name = f_name,
                contributor_email = f_email,
                position = f_position
            )
            new.save()

        else:
            raise forms.ValidationError('You have to fill all fields!')
