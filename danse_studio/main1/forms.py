from django import forms

from .models import *
from django.forms import ModelForm, TextInput, TimeInput, ModelMultipleChoiceField, ModelChoiceField, IntegerField, BooleanField


class UserForm(ModelForm):
    class Meta:
        model =User11
        fields = ['login', 'password', 'privilegies']

        widgets={
            "login":TextInput(attrs={

                'placeholder':'Логин'
            }),
            "password ":TextInput(attrs={
                "type": "password",
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
            "privilegies ": BooleanField(


            )
        }

class StudentForm(ModelForm):
    class Meta:
        model =Student
        fields = ['surname', 'name','middle_name','number','date_of_birth','skill_level','user_id']
        labels = {'surname': 'Фамилия', 'name': 'Имя'}
        surname = forms.CharField(

        )
        name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        middle_name = forms.CharField()
        number = forms.IntegerField()
        user_id=forms.ModelChoiceField(
        queryset=User11.objects.all(),
        widget=forms.CheckboxSelectMultiple
        ),
        date_of_birth = forms.DateField()
        skill_level = forms.ChoiceField()
class SearchForm(forms.Form):
    query = forms.CharField()

class timetableForm(ModelForm):
    class Meta:
        model =Schedule
        fields = ['date', 'time', 'group_id','educator_id']

        date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        time = forms.TimeField()

        group_id = forms.ModelChoiceField(
            queryset=Style.objects.all(),

        ),
        educator_id = forms.ModelChoiceField(
            queryset=Educator.objects.all(),)


class subscriptionForm(ModelForm):
    class Meta:
        model =Subscription
        fields = ['number_of_lessons', 'price', 'student_id', 'group_id','manager_id']

        number_of_lessons = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        price=forms.IntegerField()

        student_id = forms.ModelChoiceField(
            queryset=Student.objects.all(), )
        group_id = forms.ModelChoiceField(
            queryset=Style.objects.all(),)

        manager_id = forms.ModelChoiceField(
            queryset=Manager.objects.all(),)

