# APLIKACJA DO REZERWACJI STOLIKA W RESTAURACJI

````
 KOD ŹRÓDŁOWY STRONY
````
# cd
# git clone https://github.com/MateuszOkroj/Rezerwacja_stolika.git
# cd Rezerwacja_stolika

# sudo apt-get update
# sudo apt-get install libpython3-dev
# sudo apt-get install python3-venv
# python3 -m venv venv
````
#### Aktywacja venv ubuntu
````
# source venv/bin/activate
````
### Instalacja
````
# pip install -r requirements.txt
````

### AKTYWACJA STRONY
````
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py runserver
````
### TWORZENIA KONTA ADMINISTRATORA
````
# python3 manage.py createsuperuser
````
### OBSŁUGA PANELU ADMINISTRATORA
````
# Po otworzeniu strony wpisujemy w przeglądarce:
# http://127.0.0.1:8000/admin/
````
### OBSŁUGA STRONY STOLIK
````
# Po otworzeniu strony wpisujemy w przeglądarce
# http://127.0.0.1:8000/Stolik/
````
### GDYBY STRONA SIĘ ZAWIESIŁA WPISZ W KONSOLE
````
# sudo pkill -9 python
````
* contact:
mateusz.okroj.99@gmail.com