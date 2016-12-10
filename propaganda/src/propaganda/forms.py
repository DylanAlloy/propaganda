from django import forms

from .models import AddReddit

class AddRedditForm(forms.Form):
	user_name = forms.CharField(required=True)
	password = forms.CharField(widget=forms.PasswordInput,required=True)
	key = forms.CharField(required=True)
	secret = forms.CharField(required=True)
	tag = forms.CharField()