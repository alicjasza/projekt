import folium
import webbrowser
from geopy.geocoders import Nominatim

# Dane początkowe
muzea = [
    ("Muzeum łyżek", "52.2407,21.0202"),
    ("Muzeum Kur", "52.2324,21.0208"),
    ("Muzeum Przypraw", "52.2284,21.0119"),
]

magazyny = [
    ("Magazyn nr 1", "52.2413,21.0155", 0),
    ("Magazyn nr 2", "52.2406,21.0202", 0),
    ("Magazyn nr 3", "52.2401,21.0205", 0),
    ("Magazyn nr 4", "52.2323,21.0203", 1),
    ("Magazyn nr 5", "52.2326,21.0207", 1),
    ("Magazyn nr 6", "52.2325,21.0202", 1),
    ("Magazyn nr 7", "52.2280,21.0121", 2),
    ("Magazyn nr 8", "52.2284,21.0114", 2),
    ("Magazyn nr 9", "52.2288,21.0117", 2),
]

pracownicy = [
    ("Karol Karolczak", "52.2401,21.0206", 0),
    ("Hanna Ana", "52.2409,21.0203", 0),
    ("Józef Król", "52.2412,21.0157", 0),
    ("Nikola Grzegrzółka", "52.2323,21.0204", 1),
    ("Magda Gejzer", "52.2326,21.0203", 1),
    ("Dariusz Brzęczyszczykiewicz", "52.2325,21.0209", 1),
    ("Grzegorz Maczuga", "52.2280,21.0120", 2),
    ("Genowefa Jeżykowska", "52.2284,21.0117", 2),
    ("Piotr Glukoza", "52.2289,21.0117", 2),
]

# Geolocator
geolocator = Nominatim(user_agent="geoapiExercises")


# Funkcje
def pobierz_wspolrzedne(miejscowosc):
    location = geolocator.geocode(miejscowosc)
    if location:
        return location.latitude, location.longitude
    else:
        print(f"Nie znaleziono lokalizacji dla {miejscowosc}!")
        return None


def dodaj_do_listy(lista, item, miejscowosc, museum_id=None):
    wspolrzedne = pobierz_wspolrzedne(miejscowosc)
    if wspolrzedne:
        lista.append((item, f"{wspolrzedne[0]},{wspolrzedne[1]}", museum_id))
        print(f"Dodano element {item} do listy!")
    else:
        print("Nie można dodać elementu do listy bez współrzędnych!")


def wyswietl_liste(lista):
    if not lista:
        print("Lista jest pusta!")
    else:
        for i, (item, coords, *_) in enumerate(lista, start=1):
            print(f"{i}. {item} - {coords}")


def usun_element(lista):
    wyswietl_liste(lista)
    item = int(input("Podaj numer elementu do usunięcia: ")) - 1
    if 0 <= item < len(lista):
        del lista[item]
        print("Usunięto element z listy!")
    else:
        print("Element nie znaleziony!")


def aktualizuj_element(lista, czy_muzea=False):
    wyswietl_liste(lista)
    item = int(input("Podaj numer elementu do aktualizacji: ")) - 1
    if 0 <= item < len(lista):
        new_item = input("Podaj nową wartość: ")
        miejscowosc = input("Podaj nową miejscowość: ")
        wspolrzedne = pobierz_wspolrzedne(miejscowosc)
        if wspolrzedne:
            if czy_muzea:
                lista[item] = (new_item, f"{wspolrzedne[0]},{wspolrzedne[1]}")
            else:
                lista[item] = (new_item, f"{wspolrzedne[0]},{wspolrzedne[1]}", lista[item][2])
            print("Zaktualizowano element!")
        else:
            print("Nie znaleziono lokalizacji!")
    else:
        print("Element nie znaleziony!")


def wyswietl_magazyny_dla_muzeum():
    wyswietl_liste(muzea)
    muzeum = int(input("Podaj numer muzeum: ")) - 1
    if 0 <= muzeum < len(muzea):
        muzeum_nazwa = muzea[muzeum][0]
        print(f"Magazyny dla {muzeum_nazwa}:")
        for magazyn, coords, museum_id in magazyny:
            if museum_id == muzeum:
                print(f"- {magazyn} - {coords}")
    else:
        print("Niepoprawny numer muzeum!")


def wyswietl_pracownikow_dla_muzeum():
    wyswietl_liste(muzea)
    muzeum = int(input("Podaj numer muzeum: ")) - 1
    if 0 <= muzeum < len(muzea):
        muzeum_nazwa = muzea[muzeum][0]
        print(f"Pracownicy dla {muzeum_nazwa}:")
        for pracownik, coords, museum_id in pracownicy:
            if museum_id == muzeum:
                print(f"- {pracownik} - {coords}")
    else:
        print("Niepoprawny numer muzeum!")


def generuj_mape():
    mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=6)

    for muzeum, coords in muzea:
        lat, lon = map(float, coords.split(","))
        folium.Marker([lat, lon], popup=f"Muzeum: {muzeum}", icon=folium.Icon(color='blue')).add_to(mapa)

    for magazyn, coords, _ in magazyny:
        lat, lon = map(float, coords.split(","))
        folium.Marker([lat, lon], popup=f"Magazyn: {magazyn}", icon=folium.Icon(color='green')).add_to(mapa)

    for pracownik, coords, _ in pracownicy:
        lat, lon = map(float, coords.split(","))
        folium.Marker([lat, lon], popup=f"Pracownik: {pracownik}", icon=folium.Icon(color='red')).add_to(mapa)

    mapa.save("mapa.html")
    print("Mapa została wygenerowana i zapisana jako 'mapa.html'.")

    # Otwórz mapę w przeglądarce
    webbrowser.open("mapa.html")


# Logowanie
def zaloguj():
    user = input("Użytkownik: ")
    password = input("Hasło: ")
    if user == "Ala" and password == "programowanie":
        print("Zalogowano pomyślnie!")
        otworz_panel_glowny()
    else:
        print("Niepoprawne dane logowania!")


# Panel główny
def otworz_panel_glowny():
    while True:
        print("--- Panel Główny ---")
        print("1. Dodaj muzeum")
        print("2. Wyświetl muzea")
        print("3. Usuń muzeum")
        print("4. Aktualizuj muzeum")
        print("5. Dodaj magazyn")
        print("6. Wyświetl magazyny")
        print("7. Usuń magazyn")
        print("8. Aktualizuj magazyn")
        print("9. Dodaj pracownika")
        print("10. Wyświetl pracowników")
        print("11. Usuń pracownika")
        print("12. Aktualizuj pracownika")
        print("13. Wyświetl magazyny dla muzeum")
        print("14. Wyświetl pracowników dla muzeum")
        print("15. Generuj mapę")
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            dodaj_do_listy(muzea, input("Podaj nazwę muzeum: "), input("Podaj miejscowość muzeum: "))
        elif choice == "2":
            wyswietl_liste(muzea)
        elif choice == "3":
            usun_element(muzea)
        elif choice == "4":
            aktualizuj_element(muzea, czy_muzea=True)
        elif choice == "5":
            dodaj_do_listy(magazyny, input("Podaj nazwę magazynu: "), input("Podaj miejscowość magazynu: "), int(input("Podaj numer muzeum, do którego przypisać magazyn: ")) - 1)
        elif choice == "6":
            wyswietl_magazyny_dla_muzeum()
        elif choice == "7":
            usun_element(magazyny)
        elif choice == "8":
            aktualizuj_element(magazyny)
        elif choice == "9":
            dodaj_do_listy(pracownicy, input("Podaj imię i nazwisko pracownika: "), input("Podaj miejscowość pracownika: "), int(input("Podaj numer muzeum, do którego przypisać pracownika: ")) - 1)
        elif choice == "10":
            wyswietl_pracownikow_dla_muzeum()
        elif choice == "11":
            usun_element(pracownicy)
        elif choice == "12":
            aktualizuj_element(pracownicy)
        elif choice == "13":
            wyswietl_magazyny_dla_muzeum()
        elif choice == "14":
            wyswietl_pracownikow_dla_muzeum()
        elif choice == "15":
            generuj_mape()
        elif choice == "0":
            break
        else:
            print("Niepoprawna opcja!")


if __name__ == "__main__":
    zaloguj()
