from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    name=forms.CharField(label="Name of the studnet")
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea(),validators=[validators.MaxLengthValidator(40)])
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

def clean(self):
    print("BOt validtions")
    cleaned_data=super().clean()
    bot_handler_value=cleaned_data['bot_handler']
    if len(bot_handler_value)>0:
        raise forms.ValidtionError('Thank u BOt')
