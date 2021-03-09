from django import forms
from .models import Customer
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','address','mobile','other','query','created_at','updated_at']

