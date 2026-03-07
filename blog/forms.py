from django import forms 
from .models import comment

class commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('names','body')
        
        widgets={
            "name": forms.TextInput(attrs={
                "class":"form-control"
            }),
            
            "body":forms.Textarea(attrs={
                "class":"form-control"
            })
            
        }
