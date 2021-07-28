from django.shortcuts import render
from . import forms
from testapp import forms

def thankyouview(request):
    return render(request,'testapp/thankyou.html')

def feedbackview(request):
    if request.method=='GET':
        form=forms.FeedBackForm()


    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)

        if form.is_valid():
            print("form validating successfull")
            print('name',form.cleaned_data['name'])
            print('rollno',form.cleaned_data['rollno'])
            print('email',form.cleaned_data['email'])
            print('feedback',form.cleaned_data['feedback'])
            #return thankyouview(request)
    return render(request,'testapp/feedback.html',{'form':form})
