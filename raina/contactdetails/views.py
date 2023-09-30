from urllib import response
from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from contactdetails.forms import contact_details
# Create your views here.

def contact(request):
    if request.method=='GET':
        form=contact_details()
    else:
        form = contact_details(request.POST,request.FILES)
        # file=request.FILES['Uploadefile']
        if form.is_valid():
            Subject='Contact Details'
            body={
                'firstname':form.cleaned_data['first_name'],
                'lastname':form.cleaned_data['last_name'],
                'jobdescription':form.cleaned_data['Job_description'],
                

            }
            message='\n'.join(body.values())
            email=form.cleaned_data['Email_id']
            mail=send_mail("hello Raina", message, email,['rainaraji66@gmail.com'])
            # mail.attach(file.name,file.read(),file.content_type)
            # mail.send()
            # return HttpResponse('%s'%mail)
            return HttpResponse('Successfully Submitted')    
    return render(request,'login.html',{'form':form})
#if __name__=='__main__':

