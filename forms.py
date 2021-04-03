from django import forms
from .models import User
#DataFlair
class BookCreate(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'