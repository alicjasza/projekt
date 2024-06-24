import folium
import webbrowser

# Dane z zróżnicowanymi współrzędnymi
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
    ("Jan Kowalski", "52.2401,21.0206", 0),
    ("Anna Nowak", "52.2409,21.0203", 0),
    ("Piotr Wiśniewski", "52.2412,21.0157", 0),
    ("Marek Zalewski", "52.2323,21.0204", 1),
    ("Magda Kowalczyk", "52.2326,21.0203", 1),
    ("Jacek Wójcik", "52.2325,21.0209", 1),
    ("Paweł Zieliński", "52.2280,21.0120", 2),
    ("Katarzyna Kwiatkowska", "52.2284,21.0117", 2),
    ("Krzysztof Zając", "52.2289,21.0117", 2),
]

# Funkcje

def dodaj_do_listy(lista, item, coords, museum_id=None):
    lista.append((item, coords, museum_id))
    print("Dodano element do listy!")

def wyswietl_liste(lista):
    if not lista:
        print("Lista jest pusta!")
    else:
        for i, (item, coords, *_) in enumerate(lista, start=1):
            print(f"{i}. {item} - {coords}")

def wyswietl_magazyny_dla_muzeum():
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
    muzeum = int(input("Podaj numer muzeum: ")) - 1
    if 0 <= muzeum < len(muzea):
        muzeum_nazwa = muzea[muzeum][0]
        print(f"Pracownicy dla {muzeum_nazwa}:")
        for pracownik, coords, museum_id in pracownicy:
            if museum_id == muzeum:
                print(f"- {pracownik} - {coords}")
    else:
        print("Niepoprawny numer muzeum!")

def usun_element(lista):
    item = int(input("Podaj numer elementu do usunięcia: ")) - 1
    if 0 <= item < len(lista):
        del lista[item]
        print("Usunięto element z listy!")
    else:
        print("Element nie znaleziony!")

def aktualizuj_element(lista, czy_muzea=False):
    item = int(input("Podaj numer elementu do aktualizacji: ")) - 1
    if 0 <= item < len(lista):
        new_item = input("Podaj nową nazwę: ")
        new_coords = input("Podaj nowe współrzędne: ")
        if czy_muzea:
            lista[item] = (new_item, new_coords)
        else:
            lista[item] = (new_item, new_coords, lista[item][2])
        print("Zaktualizowano element!")
    else:
        print("Element nie znaleziony!")

def generuj_mape():
    mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=12)

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
    if user == "admin" and password == "password":
        print("Zalogowano pomyślnie!")
        otworz_panel_glowny()
    else:
        print("Niepoprawne dane logowania!")

# Panel główny
def otworz_panel_glowny():
    while True:
        print("\n--- Panel Główny ---")
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
            nazwa_muzeum = input("Podaj nazwę muzeum: ")
            wspolrzedne_muzeum = input("Podaj współrzędne muzeum (np. 52.2410,21.0205): ")
            muzea.append((nazwa_muzeum, wspolrzedne_muzeum))
            print("Dodano muzeum!")

            # Przypisanie przykładowych magazynów i pracowników do nowo dodanego muzeum
            id_muzeum = len(muzea) - 1
            for i in range(3):
                magazyny.append((f"Magazyn_{i+1} dla {nazwa_muzeum}", "52.2410,21.0205", id_muzeum))
                pracownicy.append((f"Pracownik_{i+1} dla {nazwa_muzeum}", "52.2410,21.0205", id_muzeum))
        elif choice == "2":
            wyswietl_liste(muzea)
        elif choice == "3":
            usun_element(muzea)
        elif choice == "4":
            aktualizuj_element(muzea, czy_muzea=True)
        elif choice == "5":
            nazwa_magazynu = input("Podaj nazwę magazynu: ")
            wspolrzedne_magazynu = input("Podaj współrzędne magazynu (np. 52.2410,21.0205): ")
            print("Wybierz muzeum z listy:")
            wyswietl_liste(muzea)
            id_muzeum = int(input("Podaj numer muzeum: ")) - 1
            if 0 <= id_muzeum < len(muzea):
                magazyny.append((nazwa_magazynu, wspolrzedne_magazynu, id_muzeum))
                print("Dodano magazyn!")
            else:
                print("Niepoprawny numer muzeum!")
        elif choice == "6":
            wyswietl_magazyny_dla_muzeum()
        elif choice == "7":
            usun_element(magazyny)
        elif choice == "8":
            aktualizuj_element(magazyny)
        elif choice == "9":
            nazwa_pracownika = input("Podaj nazwę pracownika: ")
            wspolrzedne_pracownika = input("Podaj współrzędne pracownika (np. 52.2410,21.0205): ")
            print("Wybierz muzeum z listy:")
            wyswietl_liste(muzea)
            id_muzeum = int(input("Podaj numer muzeum: ")) - 1
            if 0 <= id_muzeum < len(muzea):
                pracownicy.append((nazwa_pracownika, wspolrzedne_pracownika, id_muzeum))
                print("Dodano pracownika!")
            else:
                print("Niepoprawny numer muzeum!")
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