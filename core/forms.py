from django.forms import ModelForm, widgets,TextInput, Select, Textarea,  DateTimeInput, NumberInput
from .models import ShopEvent
from django import forms

class ShopEventForm(ModelForm):
    class Meta:
        model = ShopEvent
        fields = "__all__"
        widgets = {
            "তারিখ": DateTimeInput(attrs = {'type' : 'dateTime', 'class' : 'form-control'}),
            "পোশাক": TextInput(attrs = {'class' : 'form-control clothfm'}),
            "রেট": TextInput(attrs = {'class' : 'form-control clothfm'}),
            "পরিমান": NumberInput(attrs = {'class' : 'form-control clothfm'}),
            "টাকা": NumberInput(attrs = {'class': 'form-control'}),
            "ধরন": Select(attrs = {'class': 'form-control'})
        }
        
