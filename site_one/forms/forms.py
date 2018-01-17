from django import forms

class RegisterForm(forms.Form):
	firstname = forms.CharField(max_length=45)
	lastname = forms.CharField(max_length=45)
	email = forms.CharField(max_length=45)
	password = forms.CharField(widget=forms.PasswordInput)