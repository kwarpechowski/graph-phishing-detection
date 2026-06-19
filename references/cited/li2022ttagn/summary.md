---
title: "TTAGN: Temporal Transaction Aggregation Graph Network for Ethereum Phishing Scams Detection"
date: 2022-01-01
authors: "Sijia Li, Gaopeng Gou, Chang Liu, Chengshang Hou, Zhenzhen Li, Gang Xiong"
status: read
doi: "10.1145/3485447.3512226"
category: "Security"
tags:
  - ethereum
  - phishing-detection
  - temporal-graph
  - edge-representation
  - graph-neural-networks
  - blockchain
  - project/graph-phishing-detection
---

# TTAGN: Temporal Transaction Aggregation Graph Network for Ethereum Phishing Scams Detection

## Metadane
- **Autorzy**: Sijia Li, Gaopeng Gou, Chang Liu, Chengshang Hou, Zhenzhen Li, Gang Xiong (Institute of Information Engineering, Chinese Academy of Sciences)
- **Rok**: 2022
- **Źródło**: Proceedings of the ACM Web Conference 2022 (WWW '22), Lyon
- **DOI/Link**: https://doi.org/10.1145/3485447.3512226 (`#ethereum`, `#temporal`, `#edge2node`)
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca dotyczy detekcji oszustw phishingowych na Ethereum, gdzie phishing stał się najpoważniejszym typem przestępstwa. Autorzy podkreślają, że tradycyjne metody detekcji phishingu (oparte na wykrywaniu sfałszowanych platform: URL, CSS) są nieskuteczne w kontekście Ethereum, ponieważ tu phishing polega na bezpośrednim nakłanianiu do przelewu na adres, bez stałego wzorca platformy. Istniejące metody na Ethereum mają dwa braki: (1) brak informacji czasowej — wykorzystują tylko ostatni rekord transakcji lub całkowicie go pomijają; (2) słabą reprezentację węzła — uwzględniają jedynie cechy statystyczne i strukturalne, ignorując cechy handlowe (trading features).

Proponowany model TTAGN (Temporal Transaction Aggregation Graph Network) rozwiązuje te problemy poprzez efektywne wykorzystanie informacji czasowej transakcji. Buduje wielokrawędziowy skierowany graf transakcji (adres = węzeł, transakcja = skierowana krawędź). Składa się z trzech modułów: modułu reprezentacji krawędzi czasowych (Temporal Edge Representation), który modeluje relacje czasowe historycznych rekordów transakcji; modułu edge2node, który agreguje reprezentacje krawędzi wokół węzła, tworząc cechy handlowe; oraz modułu wzmocnienia strukturalnego (Structural Enhancement). Cechy statystyczne, strukturalne i handlowe są łączone w finalną reprezentację węzła.

Ewaluowany na rzeczywistych zbiorach phishingu Ethereum, TTAGN osiąga 92.8% AUC i 81.6% F1-score, przewyższając metody state-of-the-art. Wykazano skuteczność modułów reprezentacji krawędzi czasowych oraz edge2node.

## Kluczowe Wnioski
- TTAGN osiąga 92.8% AUC i 81.6% F1, przewyższając SOTA.
- Informacja czasowa transakcji (a nie tylko ostatni rekord) istotnie poprawia detekcję.
- Cechy handlowe (trading features) z agregacji krawędzi wzbogacają reprezentację węzła.
- Łączenie cech statystycznych, strukturalnych i handlowych daje najlepszą reprezentację.

## Metodologia
Wielokrawędziowy skierowany graf transakcji Ethereum. Trzy moduły: (1) Temporal Edge Representation modeluje czasowe sekwencje transakcji między parą adresów, generując reprezentacje krawędzi; (2) Edge2node agreguje reprezentacje krawędzi wokół węzła w cechy handlowe; (3) Structural Enhancement wydobywa cechy strukturalne za pomocą GNN. Finalna reprezentacja = statystyczne + strukturalne + handlowe; klasyfikator identyfikuje węzły phishingowe. Ewaluacja: AUC, F1.

## Główne Koncepcje
- **Temporal edge representation** — modelowanie sekwencji czasowych transakcji
- **Edge2node aggregation** — krawędzie → cechy handlowe węzła
- **Trading features** vs. cechy statystyczne/strukturalne
- **Wielokrawędziowy graf skierowany** transakcji

## Relevancja dla graph-phishing-detection
TTAGN to kluczowy baseline dla projektu — pokazuje, jak modelować informację czasową i bogatą reprezentację krawędzi w grafie transakcji phishingowych. Idea edge2node oraz cech handlowych bezpośrednio inspiruje konstrukcję wielowarstwowego/multipleksowego grafu wiedzy domenowej, gdzie krawędzie (komunikacja, transakcje) niosą informacje czasowe. Wynik 92.8% AUC stanowi konkretny punkt odniesienia, a nacisk na temporalność wspiera niezmiennik projektu dotyczący dynamiki grafu i jest istotny przy porównaniu z proweniencją binarną na Recall@FPR1%.
