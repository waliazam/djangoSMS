from django import forms

class usersForm(forms.Form):
    name = forms.CharField(label="Enter Name", max_length="30", required=True)
    email = forms.EmailField(label="Enter Email", required=False)
    subject = forms.CharField(label="Enter subject", required=False)
    message = forms.CharField(max_length="100")
    
    