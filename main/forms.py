from django import forms

from .models import Product

class RatingForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['rating']
        
    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating > 10:
            raise forms.ValidationError("The rating must be between 1 and 10.")
        return rating