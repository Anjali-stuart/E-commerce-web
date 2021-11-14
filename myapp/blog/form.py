from django import  forms
from .models import Student, Employee

class StuForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)
    lastname  = forms.CharField(label="Enter last name", max_length = 100)

class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"