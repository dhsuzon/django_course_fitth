from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name = forms.CharField(label="Full Name :", help_text="total length must be 70 charaters",required= False , widget= forms.Textarea(attrs={'id':'textarea','class':'class1 class','placeholder':'Enter full name'}))
    # file = forms.FileField()
    # email = forms.EmailField(label="user email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget = forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField( widget= forms.DateInput( attrs ={'type':'date'}))
    appointment = forms.CharField( widget= forms.DateInput( attrs ={'type':'datetime-local'}))
    CHOISE = [('S','small'),('M','medium'), ('L','large'),]
    choice = forms.ChoiceField( choices= CHOISE, widget= forms.RadioSelect)
    MEAL = [('P','Pepperroni'),('M','Massroom'),('B','Beef')]
    pizza =  forms.MultipleChoiceField( choices=MEAL,widget= forms.CheckboxSelectMultiple)
    
    
# class  student_data(forms.Form):
#     name = forms.CharField( widget = forms.TextInput)
#     email = forms.CharField( widget = forms.EmailInput)
    
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("enter at name with at least 10 characters")
#     #     else:
#     #         return valname
        
#     # def clean_email(self):
#     #     valemail = self .cleaned_data['email']
#     #     if  '.com' not in valemail:
#     #         raise forms.ValidationError('the  missing .com  in the email address')
#     #     else:
#     #         return valemail
            
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError("enter at name with at least 10 characters") 
#         if  '.com' not in valemail:
#             raise forms.ValidationError('the  missing .com  in the email address')
        
class  student_data(forms.Form):
    name = forms.CharField( validators=[(validators.MaxLengthValidator(10,message="enter at name with at maximum 10 characters" ))])
    email = forms.CharField( widget = forms.EmailInput, validators=[(validators.EmailValidator(message="Enter a valid email address"))])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(30,message="age must be miximum 30"),validators.MinValueValidator(20,message=" age at least 20")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(['jpg'],message="file must be extension jng")])
    
    
class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        con_pass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_pass != con_pass:
           raise forms.ValidationError('Passwords do not match')
        if len(val_name) < 15:
            raise forms.ValidationError('name must be at least 15 characters')