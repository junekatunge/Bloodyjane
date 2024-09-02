from django import forms
from .models import SymptomLog
class SymptomLogForm(forms.ModelForm):
    class Meta:
        model = SymptomLog
        fields = '__all__' # Include all fields from SymptomLog
