import pandas as pd
import random
from datetime import datetime
import io

data = """id,nazwa,kategoria,waga_kg,priorytet_wartosc
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

df = pd.read_csv(io.StringIO(data))

# Konfiguracja floty
RAKIETY = {
    "SpaceX ANS": 6000,
    "Kaya": 4000,
    "AI Dragon": 2500
}

def losuj_ladunek(df, flota):
    start_time = datetime.now()
    
    # Inicjalizacja wyników
    przydzial = {nazwa: [] for nazwa in flota}
    pozostalo_kg = flota.copy()
    earth_storage = []
    
    # Kopiujemy listę przedmiotów i mieszamy ją (losowość)
    przedmioty = df.to_dict('records')
    random.shuffle(przedmioty)
    
    for item in przedmioty:
        waga = item['waga_kg']
        dodano = False
        
        # Próbujemy wrzucić do losowo wybranej dostępnej rakiety
        dostepne_rakiety = list(flota.keys())
        random.shuffle(dostepne_rakiety)
        
        for r in dostepne_rakiety:
            if pozostalo_kg[r] >= waga:
                przydzial[r].append(item['nazwa'])
                pozostalo_kg[r] -= waga
                dodano = True
                break
        
        if not dodano:
            earth_storage.append(item['nazwa'])
            
    end_time = datetime.now()
    hms = end_time.strftime("%H:%M:%S")
    
    return przydzial, earth_storage, hms

# Uruchomienie i prezentacja
wynik, magazyn, czas = losuj_ladunek(df, RAKIETY)

print(f"--- RAPORT MISJI (Wygenerowano o: {czas}) ---")
for rakieta, ladunek in wynik.items():
    print(f"🚀 {rakieta}: {', '.join(ladunek) if ladunek else 'PUSTA'}")

print(f"❌ Earth Storage: {', '.join(magazyn)}")