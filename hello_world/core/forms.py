from django import forms
from .utils import check_password

class PasswordCheckForm(forms.Form):
    password = forms.CharField(
        label='Password',
        max_length=128,
    )

    def clean_password(self):
        password = self.cleaned_data.get("password", "")
        ok, error = check_password(password)
        if not ok:
            raise forms.ValidationError(error)
        return password