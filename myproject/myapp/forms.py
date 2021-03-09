from django import forms
from .models import Car, Application

  
# creating a form 
class CarForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Car 
  
        # specify fields to be used 
        fields = [ 
            "title", 
            "brand",
            "model_no", 
        ] 

class ApplicationForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Application 
  
        # specify fields to be used 
        fields = [ 
            "name", 
            "details",
        ] 
