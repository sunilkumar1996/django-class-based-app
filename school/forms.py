from django import forms
from .models import Student, Teacher, Contractor


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'fees']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}),
            'fees': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Fees'}),
        }
        labels = {'name': 'Student Name', 'age': 'Student Age', 'fees': 'Student Fees'}


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'age', 'date', 'salary']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}),
            'date': forms.DateInput(attrs={'class': 'form-control input-group date', 'data-provide': 'datepicker', 'placeholder': 'Select Date'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Enter Salary'}),
        }
        labels = {'name': 'Teacher Name', 'age': 'Select Age', 'date': 'Select Date', 'salary': 'Enter Salary'}

class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['name', 'age', 'date', 'payment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Select Age'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Select Date'}),
            'payment': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Payment'}),
        }   