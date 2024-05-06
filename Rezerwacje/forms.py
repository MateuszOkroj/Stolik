#TWORZENIE FORMULARZY
from django import forms
from Rezerwacje.models import Stolik

RESTAURACJA_FORM_CHOICES = [("", "-------")] + Stolik.RESTAURACJA_CHOICES
LOKALIZACJA_FORM_CHOICES = [("", "-------")] + Stolik.LOKALIZACJA_CHOICES
DZIEN_FORM_CHOICES = [("", "-------")] + Stolik.DZIEN_CHOICES
GODZINA_FORM_CHOICES = [("", "-------")] + Stolik.GODZINA_CHOICES


class StolikForm(forms.ModelForm):
    restauracja = forms.ChoiceField(choices=RESTAURACJA_FORM_CHOICES, required=False)
    ilosc = forms.IntegerField(min_value=1, required=False)
    lokalizacja = forms.ChoiceField(choices=LOKALIZACJA_FORM_CHOICES, required=False)
    dzien = forms.ChoiceField(choices=DZIEN_FORM_CHOICES, required=False)
    godzina = forms.ChoiceField(choices=GODZINA_FORM_CHOICES, required=False)

    class Meta:
        model = Stolik
        fields = ["restauracja", "dzien","godzina", "ilosc", "lokalizacja"]




