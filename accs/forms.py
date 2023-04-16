from django import forms

from django.contrib.auth import get_user_model

class CustomUserChangeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name')