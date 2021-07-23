from django import forms


class PetstagramUserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        widget = forms.PasswordInput()
    )