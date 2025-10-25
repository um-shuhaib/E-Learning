from django import forms
from instructor.models import User


# refer widget-tweaks for styling model form

class InstructorCreateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","username","password","email"]

        widgets={
            'first_name':forms.TextInput(attrs={"class":"w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent", "placeholder":"John Doe"}),
            'username':forms.TextInput(attrs={"class":"w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent", "placeholder":"@johndoe"}),
            'password':forms.PasswordInput(attrs={"class":"w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent", "placeholder":"********"}),
            'email':forms.EmailInput(attrs={"class":"w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent", "placeholder":"your@email.com"}),
        }