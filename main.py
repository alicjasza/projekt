import folium
import webbrowser
from geopy.geocoders import Nominatim

# Przykładowe dane
muzea = [
    {"nazwa": "muzeum łyżek", "adres": "al. Jerozolimskie 3, Warszawa", "współrzędne": "52.23199, 21.01859"},
    {"nazwa": "Muzeum misek", "adres": "Grzybowska 79, Warszawa", "współrzędne": "52.2332, 20.9794"}
]

magazyny = {
    "muzeum łyżek": [
        {"nazwa": "magazyn 1", "adres": "ul. Marszałkowska 10, Warszawa", "współrzędne": "52.2297, 21.0117"},
        {"nazwa": "magazyn 2", "adres": "ul. Puławska 15, Warszawa", "współrzędne": "52.2043, 21.0219"}
    ],
    "muzeum misek": [
        {"nazwa": "magazyn 3", "adres": "ul. Prosta 20, Warszawa", "współrzędne": "52.2329, 20.9824"}
    ]
}

pracownicy = {
    "muzeum łyżek": ["Michał Lewandowski", "Zofia Kaczmarek"],
    "muzeum misek": ["Katarzyna Zielińska"]
}

geolocator = Nominatim(user_agent="muzeum_locator")


# Logowanie
def login():
    print("Witaj w systemie zarządzania muzeami.")
    nazwa_uzytkownika = input("Podaj nazwę użytkownika: ")
    haslo = input("Podaj hasło dostępu: ")
    print(f"Próba logowania jako: {nazwa_uzytkownika}, hasło: {haslo}")
    if nazwa_uzytkownika == "ala" and haslo == "programowanie":
        print("Zalogowano pomyślnie.")
        return True
    else:
        print("Niepoprawna nazwa użytkownika lub hasło.")
        return False


# Funkcja read
def read_muzea():
    print("Lista muzeów:")
    for muzeum in muzea:
        print(f"{muzeum['nazwa']}, adres: {muzeum['adres']}, współrzędne: {muzeum.get('współrzędne', 'Brak')}")


def read_magazyny(muzeum):
    if muzeum in magazyny:
        print(f"Magazyny {muzeum}:")
        for magazyn in magazyny[muzeum]:
            print(f"{magazyn['nazwa']}, adres: {magazyn['adres']}, współrzędne: {magazyn.get('współrzędne', 'Brak')}")
    else:
        print("Nie znaleziono muzeum o podanej nazwie.")


def read_pracownicy(muzeum):
    if muzeum in pracownicy:
        print(f"Pracownicy {muzeum}:")
        for pracownik in pracownicy[muzeum]:
            print(f"- {pracownik}")
    else:
        print("Nie znaleziono muzeum o podanej nazwie.")


# Funkcja create
def create_muzea(nazwa, adres):
    location = geolocator.geocode(adres)
    if location:
        wspolrzedne = f"{location.latitude}, {location.longitude}"
        muzea.append({'nazwa': nazwa, 'adres': adres, 'współrzędne': wspolrzedne})
        print(f"Dodano muzeum: {nazwa}, adres: {adres}, współrzędne: {wspolrzedne}")
    else:
        print(f"Nie udało się pobrać współrzędnych dla adresu: {adres}")


def create_magazyny(muzeum, nazwa_magazynu, adres_magazynu):
    location = geolocator.geocode(adres_magazynu)
    if location:
        wspolrzedne = f"{location.latitude}, {location.longitude}"
        magazyn = {
            'nazwa': nazwa_magazynu,
            'adres': adres_magazynu,
            'współrzędne': wspolrzedne
        }
        if muzeum in magazyny:
            magazyny[muzeum].append(magazyn)
        else:
            magazyny[muzeum] = [magazyn]
        print(f"Dodano magazyn {nazwa_magazynu} do muzeum {muzeum}")
    else:
        print(f"Nie udało się pobrać współrzędnych dla adresu: {adres_magazynu}")


def create_pracownicy(muzeum, pracownik):
    if muzeum in pracownicy:
        pracownicy[muzeum].append(pracownik)
    else:
        pracownicy[muzeum] = [pracownik]
    print(f"Dodano pracownika {pracownik} do muzeum {muzeum}")


# Funkcja update
def update_muzea(nazwa, nowa_nazwa, nowy_adres, nowa_miejscowosc):
    location = geolocator.geocode(f"{nowy_adres}, {nowa_miejscowosc}")
    if location:
        nowe_wspolrzedne = f"{location.latitude}, {location.longitude}"
        for muzeum in muzea:
            if muzeum['nazwa'] == nazwa:
                muzeum['nazwa'] = nowa_nazwa
                muzeum['adres'] = f"{nowy_adres}, {nowa_miejscowosc}"
                muzeum['współrzędne'] = nowe_wspolrzedne
                print(f"Zaktualizowano muzeum {nazwa} na {nowa_nazwa}, adres: {nowy_adres}, miejscowość: {nowa_miejscowosc}, współrzędne: {nowe_wspolrzedne}")
                return
        print("Nie znaleziono muzeum o podanej nazwie.")
    else:
        print(f"Nie udało się pobrać współrzędnych dla adresu: {nowy_adres}, miejscowość: {nowa_miejscowosc}")


def update_magazyny(muzeum, stara_nazwa_magazynu, nowa_nazwa_magazynu, nowy_adres_magazynu):
    if muzeum in magazyny:
        for magazyn in magazyny[muzeum]:
            if magazyn['nazwa'] == stara_nazwa_magazynu:
                location = geolocator.geocode(nowy_adres_magazynu)
                if location:
                    nowe_wspolrzedne = f"{location.latitude}, {location.longitude}"
                    magazyn['nazwa'] = nowa_nazwa_magazynu
                    magazyn['adres'] = nowy_adres_magazynu
                    magazyn['współrzędne'] = nowe_wspolrzedne
                    print(f"Zaktualizowano magazyn {stara_nazwa_magazynu} na {nowa_nazwa_magazynu}, adres: {nowy_adres_magazynu}, współrzędne: {nowe_wspolrzedne}")
                    return
                else:
                    print(f"Nie udało się pobrać współrzędnych dla adresu: {nowy_adres_magazynu}")
                    return
        print(f"Nie znaleziono magazynu {stara_nazwa_magazynu} w muzeum {muzeum}")
    else:
        print(f"Nie znaleziono muzeum {muzeum}")


def update_pracownicy(muzeum, stary_pracownik, nowy_pracownik):
    if muzeum in pracownicy:
        if stary_pracownik in pracownicy[muzeum]:
            pracownicy[muzeum][pracownicy[muzeum].index(stary_pracownik)] = nowy_pracownik
            print(f"Zaktualizowano pracownika {stary_pracownik} na {nowy_pracownik} w muzeum {muzeum}")
        else:
            print(f"Nie znaleziono pracownika {stary_pracownik} w muzeum {muzeum}")
    else:
        print(f"Nie znaleziono muzeum {muzeum}")


# Funkcja remove
def remove_muzea(nazwa):
    global muzea
    muzea = [muzeum for muzeum in muzea if muzeum['nazwa'] != nazwa]
    if nazwa in magazyny:
        del magazyny[nazwa]
    if nazwa in pracownicy:
        del pracownicy[nazwa]
    print(f"Usunięto muzeum {nazwa}")


def remove_magazyny(muzeum, nazwa_magazynu):
    if muzeum in magazyny:
        magazyny[muzeum] = [magazyn for magazyn in magazyny[muzeum] if magazyn['nazwa'] != nazwa_magazynu]
        print(f"Usunięto magazyn {nazwa_magazynu} z muzeum {muzeum}")
    else:
        print(f"Nie znaleziono muzeum {muzeum}")


def remove_pracownicy(muzeum, pracownik):
    if muzeum in pracownicy:
        pracownicy[muzeum] = [p for p in pracownicy[muzeum] if p != pracownik]
        print(f"Usunięto pracownika {pracownik} z muzeum {muzeum}")
    else:
        print(f"Nie znaleziono muzeum {muzeum}")


# Funkcje generujące mapy
def generate_map_muzea():
    mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=12)
    for muzeum in muzea:
        folium.Marker(
            location=[float(coord) for coord in muzeum['współrzędne'].split(", ")],
            popup=muzeum['nazwa'],
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(mapa)
    return mapa


def generate_map_magazyny():
    mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=12)
    for muzeum in magazyny:
        for magazyn in magazyny[muzeum]:
            folium.Marker(
                location=[float(coord) for coord in magazyn['współrzędne'].split(", ")],
                popup=f"{magazyn['nazwa']} ({muzeum})",
                icon=folium.Icon(color='green', icon='info-sign')
            ).add_to(mapa)
    return mapa


def generate_map_pracownicy():
    mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=12)
    for muzeum in pracownicy:
        location = next((m['współrzędne'] for m in muzea if m['nazwa'] == muzeum), None)
        if location:
            folium.Marker(
                location=[float(coord) for coord in location.split(", ")],
                popup=f"Pracownicy: {', '.join(pracownicy[muzeum])}",
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(mapa)
    return mapa


def generate_map_all():
    mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=12)
    for muzeum in muzea:
        folium.Marker(
            location=[float(coord) for coord in muzeum['współrzędne'].split(", ")],
            popup=muzeum['nazwa'],
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(mapa)
    for muzeum in magazyny:
        for magazyn in magazyny[muzeum]:
            folium.Marker(
                location=[float(coord) for coord in magazyn['współrzędne'].split(", ")],
                popup=f"{magazyn['nazwa']} ({muzeum})",
                icon=folium.Icon(color='green', icon='info-sign')
            ).add_to(mapa)
    for muzeum in pracownicy:
        location = next((m['współrzędne'] for m in muzea if m['nazwa'] == muzeum), None)
        if location:
            folium.Marker(
                location=[float(coord) for coord in location.split(", ")],
                popup=f"Pracownicy: {', '.join(pracownicy[muzeum])}",
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(mapa)
    return mapa


# Główna funkcja programu
def main():
    if login():
        while True:
            print("\nDostępne opcje:")
            print("1. Wyświetl listę muzeów")
            print("2. Wyświetl listę magazynów danego muzeum")
            print("3. Wyświetl listę pracowników danego muzeum")
            print("4. Dodaj muzeum")
            print("5. Dodaj magazyn do muzeum")
            print("6. Dodaj pracownika do muzeum")
            print("7. Zaktualizuj dane muzeum")
            print("8. Zaktualizuj dane magazynu")
            print("9. Zaktualizuj dane pracownika")
            print("10. Usuń muzeum")
            print("11. Usuń magazyn z muzeum")
            print("12. Usuń pracownika z muzeum")
            print("13. Generuj mapę muzeów")
            print("14. Generuj mapę magazynów")
            print("15. Generuj mapę pracowników")
            print("16. Generuj mapę wszystkiego")
            print("0. Wyjdź z programu")

            opcja = input("Wybierz opcję: ")
            if opcja == "1":
                read_muzea()
            elif opcja == "2":
                muzeum = input("Podaj nazwę muzeum: ")
                read_magazyny(muzeum)
            elif opcja == "3":
                muzeum = input("Podaj nazwę muzeum: ")
                read_pracownicy(muzeum)
            elif opcja == "4":
                nazwa = input("Podaj nazwę muzeum: ")
                adres = input("Podaj adres muzeum: ")
                create_muzea(nazwa, adres)
            elif opcja == "5":
                muzeum = input("Podaj nazwę muzeum: ")
                nazwa_magazynu = input("Podaj nazwę magazynu: ")
                adres_magazynu = input("Podaj adres magazynu: ")
                create_magazyny(muzeum, nazwa_magazynu, adres_magazynu)
            elif opcja == "6":
                muzeum = input("Podaj nazwę muzeum: ")
                pracownik = input("Podaj imię i nazwisko pracownika: ")
                create_pracownicy(muzeum, pracownik)
            elif opcja == "7":
                nazwa = input("Podaj nazwę muzeum: ")
                nowa_nazwa = input("Podaj nową nazwę muzeum: ")
                nowy_adres = input("Podaj nowy adres muzeum: ")
                nowa_miejscowosc = input("Podaj nową miejscowość muzeum: ")
                update_muzea(nazwa, nowa_nazwa, nowy_adres, nowa_miejscowosc)
            elif opcja == "8":
                muzeum = input("Podaj nazwę muzeum: ")
                stara_nazwa_magazynu = input("Podaj starą nazwę magazynu: ")
                nowa_nazwa_magazynu = input("Podaj nową nazwę magazynu: ")
                nowy_adres_magazynu = input("Podaj nowy adres magazynu: ")
                update_magazyny(muzeum, stara_nazwa_magazynu, nowa_nazwa_magazynu, nowy_adres_magazynu)
            elif opcja == "9":
                muzeum = input("Podaj nazwę muzeum: ")
                stary_pracownik = input("Podaj imię i nazwisko starego pracownika: ")
                nowy_pracownik = input("Podaj imię i nazwisko nowego pracownika: ")
                update_pracownicy(muzeum, stary_pracownik, nowy_pracownik)
            elif opcja == "10":
                nazwa = input("Podaj nazwę muzeum do usunięcia: ")
                remove_muzea(nazwa)
            elif opcja == "11":
                muzeum = input("Podaj nazwę muzeum: ")
                nazwa_magazynu = input("Podaj nazwę magazynu do usunięcia: ")
                remove_magazyny(muzeum, nazwa_magazynu)
            elif opcja == "12":
                muzeum = input("Podaj nazwę muzeum: ")
                pracownik = input("Podaj imię i nazwisko pracownika do usunięcia: ")
                remove_pracownicy(muzeum, pracownik)
            elif opcja == "13":
                mapa = generate_map_muzea()
                mapa.save("mapa_muzea.html")
                webbrowser.open("mapa_muzea.html")
            elif opcja == "14":
                mapa = generate_map_magazyny()
                mapa.save("mapa_magazyny.html")
                webbrowser.open("mapa_magazyny.html")
            elif opcja == "15":
                mapa = generate_map_pracownicy()
                mapa.save("mapa_pracownicy.html")
                webbrowser.open("mapa_pracownicy.html")
            elif opcja == "16":
                mapa = generate_map_all()
                mapa.save("mapa_wszystkiego.html")
                webbrowser.open("mapa_wszystkiego.html")
            elif opcja == "0":
                print("Wylogowywanie...")
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
