from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date',)

    #name = forms.Charfield(widget=forms.TextInput(attrs={'class': 'input'}))
        