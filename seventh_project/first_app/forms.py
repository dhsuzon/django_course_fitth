from django import forms
from first_app.models import StudentModel

class StudentFrom(forms.ModelForm):
    class Meta:
        model = StudentModel 
        fields = '__all__'
        labels = {
            'Name':'Student Name',
            'Roll' :'Student Roll'
        }
        widgets ={
            'Name': forms.TextInput(),
            
        }
        help_texts ={
            'Name': 'type your name here'
        }