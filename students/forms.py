from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Jane Doe',
                'autocomplete': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'name@college.edu',
                'autocomplete': 'email',
            }),
            'age': forms.NumberInput(attrs={
                'min': '1',
                'placeholder': 'Age',
            }),
            'photo': forms.FileInput(attrs={
                'accept': 'image/*',
            }),
        }

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

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo and self.instance and self.instance.pk and self.instance.photo:
            return self.instance.photo
        return photo
