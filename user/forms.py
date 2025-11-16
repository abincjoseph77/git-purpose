from django import forms
from.models import User

class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname','lname','email','photo']