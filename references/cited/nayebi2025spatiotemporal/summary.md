---
title: "Spatio-Temporal Directed Graph Learning for Account Takeover Fraud Detection"
date: 2025-01-01
authors: "Mohsen Nayebi Kerdabadi, William Andrew Byron, Xin Sun, Amirfarrokh Iranitalab"
status: read
doi: "arXiv:2509.20339"
category: "Security"
tags:
  - account-takeover
  - fraud-detection
  - spatio-temporal-graph
  - graphsage
  - leakage-free
  - project/graph-phishing-detection
---

# Spatio-Temporal Directed Graph Learning for Account Takeover Fraud Detection

## Metadane
- **Autorzy**: Mohsen Nayebi Kerdabadi, William Andrew Byron, Xin Sun, Amirfarrokh Iranitalab (AI Foundations, Capital One)
- **Rok**: 2025
- **Źródło**: Preprint (arXiv, cs.LG)
- **DOI/Link**: arXiv:2509.20339
- **Status**: read
- **Kategoria główna**: Security
- **Tagi**: `#account-takeover` `#fraud-detection` `#spatio-temporal-graph` `#graphsage` `#leakage-free`

## Streszczenie
Praca wprowadza **ATLAS** (Account Takeover Learning Across Spatio-Temporal Directed Graph) — framework przeformułowujący detekcję przejęcia konta (ATO) jako klasyfikację węzłów na **skierowanym, respektującym czas grafie sesji**. Produkcyjne systemy bankowe zwykle opierają się na tabelarycznych modelach typu gradient boosting (np. XGBoost), które scorują każdą sesję niezależnie (założenie i.i.d.), ignorując relacyjną i temporalną strukturę aktywności online charakterystyczną dla skoordynowanych ataków i „fraud rings".

ATLAS łączy encje przez współdzielone identyfikatory (konto, urządzenie, IP) i reguluje łączność ograniczeniami okna czasowego oraz świeżości (recency), umożliwiając **przyczynowe, respektujące czas przekazywanie komunikatów** (message passing) oraz **propagację etykiet świadomą opóźnień**, która wykorzystuje wyłącznie etykiety dostępne w momencie scorowania — nieantycypacyjnie i bez wycieku (leakage-free). Framework operacjonalizowany jest indukcyjnym koderem GraphSAGE trenowanym przez neighbor sampling, w skali grafu o 100M+ węzłach i ~1 mld krawędzi. Na rzeczywistym, wysokoryzykowym produkcie cyfrowym w Capital One ATLAS daje +6,38% AUC i ponad 50% redukcji friction dla klientów, poprawiając wykrywalność oszustw przy niższym tarciu dla legalnych użytkowników.

## Kluczowe Wnioski
- Niezależne scorowanie sesji (i.i.d.) gubi sygnały relacyjne i temporalne typowe dla fraud rings.
- Skierowany graf sesji z porządkiem przeszłość→przyszłość umożliwia przyczynowe message passing.
- Propagacja etykiet musi być nieantycypacyjna (tylko etykiety dostępne w czasie scorowania) — leakage-free.
- Indukcyjny GraphSAGE z neighbor sampling skaluje się do 100M+ węzłów i ~1 mld krawędzi.
- Wynik produkcyjny: +6,38% AUC i >50% redukcji friction.

## Metodologia
Budowa skierowanego, temporalnego DAG sesji ze ścisłym porządkiem przyczynowym; linkowanie encji przez współdzielone identyfikatory (konto/urządzenie/IP) z ograniczeniami okna i świeżości; indukcyjny enkoder GraphSAGE trenowany neighbor samplingiem z zachowaniem spójności serve-time i budżetu latencji (<250 ms); ewaluacja na produkcyjnym zbiorze Capital One.

## Główne Koncepcje
- **Spatio-temporalny graf skierowany**: encje + czasowo uporządkowane krawędzie.
- **Time-respecting message passing**: agregacja tylko z przeszłości względem węzła.
- **Lag-aware / leakage-free label propagation**: etykiety dostępne w czasie scorowania.
- **Indukcyjny GraphSAGE**: uogólnianie do nowych węzłów przez sampling sąsiedztwa.

## Relevancja dla graph-phishing-detection
To jedna z najbliższych prac dla projektu — wprost operacjonalizuje **metodologię leak-aware** i **niezmiennik dynamiki kaskady**. Skierowany, respektujący czas graf sesji oraz nieantycypacyjna propagacja etykiet są dokładnie tym mechanizmem, który projekt forsuje, by uniknąć wycieku przyszłości (zgodnie z TESSERACT). ATO jest często skutkiem phishingu (autorzy wprost wymieniają phishing jako wektor), więc graf sesji łączący konto/urządzenie/IP jest pokrewny phishingowym grafom komunikacji/transakcji i pojęciu fraud rings. Indukcyjny GraphSAGE w skali 100M+ węzłów potwierdza wykonalność uczonego GNN (P2) na realistycznie dużych grafach, a metryki AUC/Recall przy kontroli friction/FPR są zbieżne z projektowym celem Recall@FPR1%.
