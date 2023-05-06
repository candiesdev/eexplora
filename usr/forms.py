from django import forms
from django.contrib.auth import authenticate

class SessionLogin(forms.Form):
    userId = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"placeholder": "Username", "autofocus": False}))

class SessionAuthenticate(forms.Form):

    def __init__(self, userIdData = ""):
        super().__init__()

        self.fields['userId'] = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"value": userIdData, "readonly": True}))
        self.fields['userPass'] = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Contraseña", "autofocus": True}))

        userId = forms.CharField()
        userPass = forms.CharField()