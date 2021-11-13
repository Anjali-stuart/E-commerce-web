from django import forms
from django.forms import ModelForm
from .models import StudentForm
# from django.contrib.auth import get_user_model
# class StuForm(forms.Form):
#     First_name = forms.CharField(label = "your name", max_length=30)
#     last_name = forms.CharField(label = "your name", max_length=30)
#     email_id = forms.EmailField()

class StuForm(ModelForm):
    class meta :
        model = StudentForm
        fields = '__all__'