from .models import Qna
from django import forms

class QnaForm(forms.ModelForm):
    class Meta:
        model = Qna
        fields = '__all__'