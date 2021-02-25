from django import forms


class PostAddForm(forms.Form):
    title = forms.CharField('TITLE', max_length=100)
    url = forms.URLField('URL', unique=True)
