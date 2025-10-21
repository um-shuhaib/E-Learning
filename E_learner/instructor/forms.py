from django import forms
from instructor.models import User


# refer widget-tweaks for styling model form

class InstructorCreateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","username","password","email"]

        widgets={
            'first_name':forms.TextInput(attrs={"class":"form-control"}),
            'username':forms.TextInput(attrs={"class":"form-control"}),
            'password':forms.PasswordInput(attrs={"class":"form-control"}),
            'email':forms.EmailInput(attrs={"class":"form-control"}),
        }