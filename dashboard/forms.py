from django import forms
from .models import*

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
class SupplierForm(FormSettings):
    class Meta:
        model = Supplier
        fields = '__all__'
