from django import forms
from .models import Group, Gift

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['event_name','event_date','join_code']

class FindGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['event_name', 'join_code']

class AddGiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['title', 'desc', 'url', 'only_one']