from django.db.models import fields
from django.forms import ModelForm
from accounts.models import *


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name')


class StudentForm(ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'
