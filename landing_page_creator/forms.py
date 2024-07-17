from django import forms

class CreateAppForm(forms.Form):
    app_name = forms.CharField(max_length=100, help_text="Enter the name for your new Django app")