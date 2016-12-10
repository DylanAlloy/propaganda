from django import forms
from .models import Account
from django.shortcuts import get_object_or_404

class AddRedditForm(forms.ModelForm):
	class Meta:
		password = forms.CharField(widget=forms.PasswordInput)
		model = Account
		fields = ['user_name','password','secret','tag']
		widgets = {
			'password': forms.PasswordInput(),
		}
