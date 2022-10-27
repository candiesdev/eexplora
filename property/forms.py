from django import forms

class UserInfoForm(forms.Form):
    userName = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={"placeholder": "Nombre"}))
    userPhone = forms.CharField(label = "", max_length=25, widget=forms.TextInput(attrs={"placeholder": "Teléfono"}))
    userEmail = forms.EmailField(label = "", max_length=100, required=False, widget=forms.TextInput(attrs={"placeholder": "Email (Opcional)"}))