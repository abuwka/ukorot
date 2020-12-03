from django import forms

class LinksForm(forms.Form):
    link = forms.URLField()
    link.widget.attrs.update({
        'class': 'form-control',
        'placeholder': "Please enter Link"})
