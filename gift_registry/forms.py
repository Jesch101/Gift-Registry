from django import forms
from .models import Group, Gift, Gifter
from datetime import datetime
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['event_name','event_date','join_code']
        widgets = {
            'event_date': forms.DateInput(attrs={'type':'date', 'min': datetime.now().date(), 'placeholder':'__/__/___' })
        }

class FindGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['event_name', 'join_code']

class AddGiftForm(forms.ModelForm):
    only_one = forms.BooleanField(widget=forms.CheckboxInput)
    url = forms.URLField(required=False)
    reciever = forms.CharField(required=True)
    class Meta:
        model = Gift
        fields = ['title', 'desc', 'reciever','url', 'only_one']

class GifterForm(forms.ModelForm):
    class Meta:
        model = Gifter
        fields = ['name']
        