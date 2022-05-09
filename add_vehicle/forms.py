from django.forms import ModelForm, widgets
from django import forms
from home.models import VehicleDetail

class VeihcleForm(ModelForm):
    class Meta:
        model = VehicleDetail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VeihcleForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control-line', 'class':'form-control'})