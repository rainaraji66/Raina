from django import forms


class contact_details(forms.Form):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    Email_id=forms.EmailField(max_length=50)
    Job_description=forms.CharField(widget=forms.Textarea,max_length=100)
    # Uploadfile=forms.FileField()
    