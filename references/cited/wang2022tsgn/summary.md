---
title: "TSGN: Transaction Subgraph Networks Assisting Phishing Detection in Ethereum"
date: 2022-01-01
authors: "Jinhuan Wang, Pengtao Chen, Xinyao Xu, Jiajing Wu, Meng Shen, Qi Xuan, Xiaoniu Yang"
status: read
doi: "arXiv:2208.12938"
category: "Security"
tags:
  - ethereum
  - phishing-detection
  - transaction-subgraph
  - graph-classification
  - blockchain
  - project/graph-phishing-detection
---

# TSGN: Transaction Subgraph Networks Assisting Phishing Detection in Ethereum

## Metadane
- **Autorzy**: Jinhuan Wang, Pengtao Chen, Xinyao Xu, Jiajing Wu, Meng Shen, Qi Xuan, Xiaoniu Yang
- **Rok**: 2022
- **Źródło**: arXiv:2208.12938
- **DOI/Link**: arXiv:2208.12938
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca dotyczy wykrywania kont phishingowych na platformie Ethereum. Istniejące metody opierają się głównie na analizie oryginalnych sieci transakcji, co utrudnia głęboką eksplorację wzorców ukrytych w strukturze interakcji. Autorzy proponują Transaction SubGraph Network (TSGN) — framework identyfikacji kont phishingowych oparty na podgrafach transakcji.

Metoda najpierw ekstrahuje podgrafy transakcji dla docelowych kont, a następnie rozszerza je do odpowiadających TSGN na podstawie różnych mechanizmów mapowania. Aby model uwzględniał więcej istotnych informacji o realnych transakcjach, atrybuty transakcji są kodowane w procesie modelowania TSGN, co daje dwa warianty: Directed-TSGN i Temporal-TSGN, stosowalne do różnych sieci atrybutowanych. Wprowadzenie TSGN do sieci wielokrawędziowych daje model Multiple-TSGN, który zachowuje informacje o czasowym przepływie transakcji i ujmuje istotne wzorce topologiczne phishingu, redukując złożoność obliczeniową modelowania dużych sieci. Eksperymenty pokazują, że modele TSGN dostarczają więcej informacji poprawiających skuteczność detekcji phishingu dzięki uczeniu reprezentacji grafu.

## Kluczowe Wnioski
- Modelowanie na poziomie podgrafów transakcji ujmuje wzorce strukturalne, które giną przy analizie surowej sieci.
- Kodowanie atrybutów transakcji (kierunek, czas, wielokrotne krawędzie) poprawia detekcję.
- Warianty Directed-/Temporal-/Multiple-TSGN dostosowują się do różnych typów sieci atrybutowanych.
- Reprezentacja podgrafowa redukuje złożoność modelowania dużych sieci transakcyjnych.

## Metodologia
Ekstrakcja podgrafów transakcji wokół kont docelowych, mapowanie ich na sieci podgrafów (TSGN) z zakodowanymi atrybutami (kierunek, znaczniki czasu, wielokrotne krawędzie), a następnie klasyfikacja grafów za pomocą uczenia reprezentacji grafowej. Ewaluacja na danych transakcyjnych Ethereum.

## Główne Koncepcje
- **Transaction subgraph network (TSGN)**: transformacja podgrafu transakcji w sieci wyższego rzędu.
- **Directed/Temporal/Multiple-TSGN**: warianty uwzględniające kierunek, czas i wielokrotne krawędzie.
- **Atrybuty transakcji**: kwota, znacznik czasu, kierunek przepływu.
- **Klasyfikacja grafów**: detekcja phishingu jako zadanie klasyfikacji podgrafu.

## Relevancja dla graph-phishing-detection
TSGN to bezpośredni punkt odniesienia dla projektu w domenie phishingu na grafach transakcyjnych. Pomysł ekstrakcji podgrafów wokół węzłów docelowych i wzbogacania ich o atrybuty czasowe i kierunkowe jest przenośny na graf wiedzy domenowej projektu (np. podgrafy wokół podejrzanych domen/kont). Stanowi konkurencyjny baseline dla uczonych modeli GNN oraz inspirację dla reprezentacji uwzględniających czasowy przepływ i topologię, istotnych przy detekcji oszustw i wykrywaniu wzorców proweniencyjnych.
