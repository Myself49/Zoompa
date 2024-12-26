from django import forms
from .models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'
        labels = {
            'name': 'Name',
            'uni_id': 'Enter ID',
            'email': 'Email',
            'phone_num': 'Phone number',
            'address': 'Address',
            'password': 'Password', 
        }
    

    