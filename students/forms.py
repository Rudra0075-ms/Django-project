from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'email', 'age']

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name) < 3:
            raise forms.ValidationError(
                "Name must contain at least 3 characters."
            )

        return name

    def clean_age(self):
        age = self.cleaned_data['age']

        if age < 1:
            raise forms.ValidationError(
                "Age must be greater than 0."
            )

        return age