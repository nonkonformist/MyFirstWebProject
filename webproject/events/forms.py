from .models import Events
from django.forms import ModelForm, TextInput, DateInput,Textarea

class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields=['title', 'full_text', 'date']

        widgets ={
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Событие"
            }),

            'full_text': Textarea(attrs={
                'class': "form-control",
                'placeholder': "Описание"
            }),

            'date': DateInput(attrs={
                'class': "form-control",
                'placeholder': "Дата события"
            })

        }
