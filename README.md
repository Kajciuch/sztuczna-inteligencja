# 🚀 Optymalizacja załadunku misji kosmicznych
**Optymalizacja Logistyki Orbitalnej przy użyciu problemu wielu "plecaków"**

## 🛰️ O projekcie
Projekt przedstawia rozwiązanie problemu logistycznego polegającego na optymalnym rozmieszczeniu zasobów w rakietach transportowych lecących na Międzynarodową Stację Kosmiczną. 
**Multiple Knapsack Problem (MKP)** – musimy zarządzać flotą wielu "plecaków" (rakiet) o różnych pojemnościach jednocześnie.


## 🛠️ Scenariusz
Mamy rok 2026. Jako główny logista misji, musisz rozdysponować listę zasobów (tlen, woda, eksperymenty, części zamienne) pomiędzy trzy różne rakiety:
1. **SpaceX ANS** (Udźwig: 6000 kg)
2. **Kaya** (Udźwig: 4000 kg)
3. **AI Dragon** (Udźwig: 2500 kg)

Każdy przedmiot ma swoją **wagę** oraz **wartość priorytetową** dla powodzenia misji.

## 🧠 Algorytm i Logika
Aplikacja wykorzystuje **algorytm zachłanny** opartą na gęstości wartości:
1. Obliczany jest stosunek wartości do wagi ($V/W$) dla każdego przedmiotu.
2. Przedmioty są sortowane malejąco według tego współczynnika.
3. Algorytm próbuje umieścić najcenniejsze przedmioty w rakiecie, która posiada największą dostępną rezerwę udźwigu w danym momencie.

### Model matematyczny:
$Maximize \sum_{j=1}^{m} \sum_{i=1}^{n} v_i x_{ij}$

Przy zachowaniu ograniczeń:
$\sum_{i=1}^{n} w_i x_{ij} \le W_j \quad (dla \ każdej \ rakiety \ j)$

