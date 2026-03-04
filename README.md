# 🚀 Optymalizacja załadunku misji kosmicznych
**Optymalizacja Logistyki Orbitalnej przy użyciu problemu wielu "plecaków"**

## O projekcie
Projekt przedstawia rozwiązanie problemu logistycznego polegającego na optymalnym rozmieszczeniu zasobów w rakietach transportowych lecących na Międzynarodową Stację Kosmiczną. 
**Multiple Knapsack Problem (MKP)** – musimy zarządzać flotą wielu "plecaków" (rakiet) o różnych pojemnościach jednocześnie.


## Scenariusz
Mamy rok 2026. Jako główny logista misji, musisz rozdysponować listę zasobów (tlen, woda, eksperymenty, części zamienne) pomiędzy trzy różne rakiety:
1. **SpaceX ANS** (Udźwig: 6000 kg)
2. **Kaya** (Udźwig: 4000 kg)
3. **AI Dragon** (Udźwig: 2500 kg)

Każdy przedmiot ma swoją **wagę** oraz **wartość priorytetową** dla powodzenia misji.

## Główne założenia
- Dane wejściowe: listę zasobów + jednostki, rakiety i ich udźwig
- Ograniczenia i optymalizacja: Każdy zasób jest niepodzielny i może zostać przypisany do maksymalnie jednej rakiety (model 0/1). Algorytm dąży do maksymalizacji całkowitej wartości ładunku wyniesionego na orbitę
- Zarządzanie flotą (Multi-Knapsack): Algorytm nie skupia się na jednej rakiecie, lecz optymalizuje załadunek całej floty jednocześnie, dbając o to, by suma wag w żadnym kontenerze nie przekroczyła limitu technicznego
- Priorytetyzacja (Heurystyka): Decyzje o załadunku podejmowane są w oparciu o gęstość wartości, co pozwala na efektywne wykorzystanie każdego kilograma udźwigu i zabezpieczenie najbardziej krytycznych zasobów w pierwszej kolejności.
- Struktura wyniku: Program generuje kompletny manifest startowy dla całej misji, dzieląc wynik na:

🚀 SpaceX ANS – lista przypisanych modułów i towarów.

🚀 Kaya – lista przypisanych modułów i towarów.

🚀 AI Dragon – lista przypisanych modułów i towarów.

❌ Earth Storage – lista zasobów, które nie zmieściły się i muszą czekać na kolejną misję.

