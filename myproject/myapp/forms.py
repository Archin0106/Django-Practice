from django import forms
from myapp.models import Student, Employee


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
