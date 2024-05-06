from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Rezerwacje.models import Stolik, Rezerwacja
from django.db import transaction
from Rezerwacje.forms import StolikForm


# Create your views here.
class StolikListView(ListView):
    model = Stolik
    template_name = "index.html"
    queryset = Stolik.objects.all()
    context_object_name = "object_list"
    def get_queryset(self):
        return self.queryset.filter(rezerwacja=None)

    def get_context_data(self, **kwargs):
        context = super(StolikListView, self).get_context_data(**kwargs)
        context["form"] = StolikForm(self.request.POST or None)
        return context

    """ FILTROWANIE DANYCH TAK, ABY ZOSTAŁY TYLKE TE, KTÓRE ZAZNACZYLIŚMY """

    def post(self, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        form = context["form"]
        if form.is_valid():
            ilosc = self.request.POST["ilosc"]
            restauracja = self.request.POST["restauracja"]
            dzien = self.request.POST["dzien"]
            godzina = self.request.POST["godzina"]
            lokalizacja = self.request.POST["lokalizacja"]

            if ilosc != "":
                self.object_list = self.object_list.filter(ilosc=ilosc)
            if restauracja != "":
                self.object_list = self.object_list.filter(restauracja=restauracja)
            if dzien != "":
                self.object_list = self.object_list.filter(dzien=dzien)
            if lokalizacja != "":
                self.object_list = self.object_list.filter(lokalizacja=lokalizacja)
            if godzina != "":
                self.object_list = self.object_list.filter(godzina=godzina)

            context[self.context_object_name] = self.object_list
        return render(self.request, self.template_name, context)


class StolikDetailView(DetailView):
    model = Stolik
    template_name = "detail.html"

class RezerwacjaListView(ListView):
    model = Rezerwacja
    template_name = "rezerwacje.html"

@transaction.atomic
def reserve(request, stolik_id):
    stolik = Stolik.objects.get(id=stolik_id)
    if request.user.is_authenticated:
        if not stolik.is_reserved:
            rez = Rezerwacja(user=request.user, stolik=stolik)
            rez.save()
        return redirect("index")
    else:
        return redirect("login")

@transaction.atomic
def unreserve(request, rezerwacja_id):
    if request.user.is_authenticated:
        try:
            rez = Rezerwacja.objects.get(user=request.user, id=rezerwacja_id)
        except Rezerwacja.DoesNotExist:
            pass
        else:
            rez.delete()
    return redirect("rezerwacje")



# @transaction.atomic
# Zapewnia atomowość operacji bazodanowych, co oznacza, że w przypadku wystąpienia błędu wewnątrz funkcji, żadne zmiany nie zostaną zapisane w bazie danych.

# queryset
# Inicjalizuje zapytanie, które pobiera wszystkie obiekty z modelu Stolik.

# context_object_name
# Określa nazwę, pod jaką lista obiektów będzie dostępna w kontekście szablonu.

# get_context_data
# Jest to metoda, która zwraca kontekst danych, który zostanie przekazany do szablonu.

# Post
# Jest to metoda obsługująca żądania typu POST. Tutaj następuje filtrowanie danych w oparciu o dane przekazane przez formularz.

# class StolikListView(ListView)
# Zadaniem poniższej klasy jest wyświetlenie listy obiektów klasy Stolik.

# class StolikDetailView(DetailView)
# Służy do wyświetlania szczegółowych informacji na temat pojedynczego obiektu modelu Stolik.

# class RezerwacjaListView(ListView)
# Służy do wyświetlania listy obiektów modelu Rezerwacja.

# Reserve
# Obsługuje operacje związane z rezerwacją zamówienia.

# Unreserve
# Obsługuje operacje związane z odrezerwowaniem zamówienia.
