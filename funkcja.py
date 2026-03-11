import csv
import random
from datetime import datetime
import io

# Dane w formie tekstowej 
csv_data = """id,nazwa,kategoria,waga_kg,priorytet_wartosc
1,Generator Tlenu Moduł A,Podtrzymywanie życia,1200,95
2,Zbiorniki Wody Pitnej,Podtrzymywanie życia,2500,90
3,Zestaw Medyczny Alpha,Bezpieczeństwo,450,85
4,Eksperyment Hodowla Roślin,Nauka,300,70
5,Części Zamienne Panel Solar,Techniczne,800,80
6,Baterie Litowo-Siarkowe,Zasilanie,1500,88
7,Skafander EVA v4,Sprzęt,250,75
8,Laboratorium Mikrograwitacji,Nauka,2200,92
9,System Recyklingu Moczu,Podtrzymywanie życia,900,82
10,Zapasowa Antena High-Gain,Komunikacja,600,65
11,Prowiant na 6 m-cy,Zapasy,1800,78
12,Komputer Pokładowy Backup,IT,150,98
13,Eksperyment Fizyka Cząstek,Nauka,1100,60
14,Zestaw Naprawczy Poszycia,Techniczne,550,88
15,Paliwo Korekcyjne (RCS),Manewrowanie,1300,85
16,Sonda Badawcza Nano,Nauka,100,40
17,Moduł Rozrywkowy Crew,Psychologia,400,30
18,Kriostat do Próbek,Nauka,700,55
19,Odzież i Środki Higieny,Zapasy,650,50
20,Klucze Momentowe Kosmiczne,Narzędzia,50,45"""

RAKIETY = {"SpaceX ANS": 6000, "Kaya": 4000, "AI Dragon": 2500}

def losuj_rozwiazanie():
    # Odczyt danych 
    f = io.StringIO(csv_data)
    reader = csv.DictReader(f)
    przedmioty = list(reader)
    
    # Losowa kolejność przedmiotów
    random.shuffle(przedmioty)
    
    ladunek = {r: [] for r in RAKIETY}
    wolne_miejsce = RAKIETY.copy()
    earth_storage = []
    
    for p in przedmioty:
        waga = int(p['waga_kg'])
        nazwa = p['nazwa']
        
        # Szukamy rakiety, która pomieści przedmiot
        pasujace_rakiety = [r for r in RAKIETY if wolne_miejsce[r] >= waga]
        
        if pasujace_rakiety:
            wybrana = random.choice(pasujace_rakiety)
            ladunek[wybrana].append(nazwa)
            wolne_miejsce[wybrana] -= waga
        else:
            earth_storage.append(nazwa)
            
    # Pobranie czasu HMS
    hms = datetime.now().strftime("%H:%M:%S")
    return ladunek, earth_storage, hms

# Wywołanie
wynik, magazyn, czas = losuj_rozwiazanie()

print(f"--- RAPORT MISJI [{czas}] ---")
for rakieta, rzeczy in wynik.items():
    print(f"🚀 {rakieta}: {', '.join(rzeczy)}")
print(f"❌ Earth Storage: {', '.join(magazyn)}")