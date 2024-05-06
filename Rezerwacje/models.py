from django.db import models
from Account.models import Account


# Create your models here.
class Stolik(models.Model):
    RESTAURACJA_CHOICES = [("BISTRO", "bistro"), ("CHIŃCZYK", "chińczyk"),("MEKSYKAŃSKA","meksykańska"),("PIZZA WŁOSKA","pizza włoska"),("RAMENOWNIA","ramenownia")]
    LOKALIZACJA_CHOICES = [("PRZY OKNIE","przy oknie"),("PRZY BARZE","przy barze"),("NA ŚRODKU","na środku")]
    DZIEN_CHOICES = [("PONIEDZIALEK","poniedzialek"),("WTOREK","wtorek"),("SRODA","sroda"),("CZWARTEK","czwartek"),("PIATEK","piatek"),("SOBOTA","sobota"),("NIEDZIELA","niedziela")]
    GODZINA_CHOICES = [("16:00","16:00"),("17:00","17:00"),("18:00","18:00"),("19:00","19:00"),("20:00","20:00"),("21:00","21:00")]
    ilosc = models.PositiveSmallIntegerField()
    restauracja = models.CharField(max_length=16, choices=RESTAURACJA_CHOICES, default="BISTRO")
    dzien = models.CharField(max_length=16, choices=DZIEN_CHOICES, default="SOBOTA")
    godzina = models.CharField(max_length=16, choices=GODZINA_CHOICES, default="20:00")
    lokalizacja = models.CharField(max_length=16, choices=LOKALIZACJA_CHOICES, default="NA ŚRODKU")

    class Meta:
        verbose_name_plural = "Stoliki"
    @property
    def is_reserved(self):
        try:
            rez = self.rezerwacja
        except Rezerwacja.DoesNotExist:
            return False
        else:
            return True

    def __str__(self):
        #4_zielony_ok
        return f"Restauracja {self.restauracja} dla {self.ilosc} osób z lokalizacją {self.lokalizacja} w {self.dzien} o {self.godzina}"

class Rezerwacja(models.Model):
    stolik = models.OneToOneField(Stolik, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Rezerwacje"





    def __str__(self):
         return f"{self.id}/{self.stolik} {self.user}"









