from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']
        widget = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Todo ..',
                'required': True
            })
        }
        
        def clean_title(self):
            title = self.cleaned_data('title')            

            if len(title) < 3:
                raise forms.ValidationError(
                    "Todo must be at least 3 characters long."
            )
        
            # Check for duplicates
            if Todo.objects.filter(title=title, completed=False).exists():
                raise forms.ValidationError(
                    "This todo already exists!"
                )
        
            return title   
    