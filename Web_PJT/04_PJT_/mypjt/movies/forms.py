from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    genre = forms.CharField(max_length=30, widget = forms.Select(choices={('comedy','comedy'),('horror','horror'),('romance','romance')}))
    score = forms.FloatField(required=True, max_value=5, min_value=0, widget=forms.NumberInput(attrs={'step':'0.5'})) 
    release_data = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}))
    class Meta:
        model = Movie
        fields = '__all__'