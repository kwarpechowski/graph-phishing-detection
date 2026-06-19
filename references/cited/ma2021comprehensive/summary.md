---
title: "A Comprehensive Survey on Graph Anomaly Detection with Deep Learning"
date: 2021-01-01
authors: "Xiaoxiao Ma, Jia Wu, Shan Xue, Jian Yang, Chuan Zhou, Quan Z. Sheng, Hui Xiong, Leman Akoglu"
status: read
doi: "10.1109/TKDE.2021.3118815"
category: "Machine Learning"
tags:
  - survey
  - graph-anomaly-detection
  - deep-learning
  - fraud-detection
  - graph-neural-networks
  - taxonomy
  - project/graph-phishing-detection
---

# A Comprehensive Survey on Graph Anomaly Detection with Deep Learning

## Metadane
- **Autorzy**: Xiaoxiao Ma, Jia Wu, Shan Xue, Jian Yang, Chuan Zhou, Quan Z. Sheng, Hui Xiong, Leman Akoglu (Macquarie University, CMU i in.)
- **Rok**: 2021
- **Źródło**: IEEE Transactions on Knowledge and Data Engineering (TKDE)
- **DOI/Link**: https://doi.org/10.1109/TKDE.2021.3118815 (`#survey`, `#GAD`, `#deep-learning`)
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
To obszerny przegląd (survey) współczesnych technik głębokiego uczenia do detekcji anomalii na grafach (Graph Anomaly Detection, GAD). Autorzy motywują problem ogromnymi stratami powodowanymi przez anomalie: oszustwa finansowe, włamania sieciowe, spam społecznościowy, fałszywe newsy (globalny koszt fake newsów ok. 78 mld USD rocznie). Klasyczna detekcja anomalii reprezentuje obiekty jako wektory cech i wyszukuje punkty odstające w przestrzeni cech, ignorując relacyjną/strukturalną informację rzeczywistych danych. Grafy ujmują te relacje, co prowadzi do problemu GAD — identyfikacji anomalnych obiektów grafowych (węzłów, krawędzi, podgrafów) w pojedynczym grafie lub anomalnych grafów w zbiorze grafów.

Klasyczne techniki nie radzą sobie z GAD ze względu na złożoność danych grafowych (nieregularna struktura, zależności relacyjne, typy/atrybuty/kierunki/multipleksowość/wagi węzłów i krawędzi, ogromna skala). Głębokie uczenie przełamuje te ograniczenia. Przegląd proponuje taksonomię opartą na strategii zorientowanej na zadanie (task-driven), kategoryzując prace według typu wykrywanego obiektu anomalnego: anomalne węzły, krawędzie, podgrafy oraz całe grafy. Dla każdej kategorii omawiane są kluczowe intuicje, szczegóły techniczne oraz mocne i słabe strony metod.

Autorzy wskazują 12 przyszłych kierunków badawczych obejmujących nierozwiązane i wyłaniające się problemy. Kompilują również zasoby: implementacje open-source, publiczne zbiory danych oraz powszechnie stosowane metryki ewaluacji, tworząc "one-stop-shop" dla badaczy GAD.

## Kluczowe Wnioski
- GAD wymaga uwzględnienia informacji relacyjnej, której klasyczna detekcja anomalii nie wykorzystuje.
- Taksonomia zorientowana na zadanie: anomalie węzłów, krawędzi, podgrafów i grafów.
- Złożoność grafów (multipleksowość, atrybuty, skala) jest głównym wyzwaniem.
- Wskazano 12 otwartych kierunków badawczych + zestaw zasobów (kod, zbiory, metryki).

## Metodologia
Praca przeglądowa (nie eksperymentalna). Systematyczny przegląd literatury z taksonomią task-driven według typu anomalnego obiektu grafowego (node/edge/subgraph/graph). Dla każdej grupy: analiza intuicji, technik i ograniczeń. Kompilacja zasobów open-source, zbiorów benchmarkowych i metryk ewaluacji.

## Główne Koncepcje
- **Graph Anomaly Detection (GAD)** — anomalie węzłów/krawędzi/podgrafów/grafów
- **Taksonomia task-driven** detekcji anomalii grafowych
- **Złożoność grafów**: multipleksowość, atrybuty, kierunkowość, skala
- **Zasoby**: implementacje, zbiory, metryki ewaluacji

## Relevancja dla graph-phishing-detection
Ten przegląd jest centralnym punktem odniesienia dla projektu — dostarcza taksonomię i mapę całego pola GAD, w które wpisuje się detekcja phishingu na grafie. Pomaga umiejscowić wkład projektu (graf wiedzy domenowej, podejścia multipleksowe) względem istniejących kategorii i 12 otwartych problemów. Podkreślenie multipleksowości i skali grafów wspiera oba niezmienniki projektu, a skompilowane zbiory i metryki stanowią praktyczne wsparcie przy projektowaniu ewaluacji (np. Recall@FPR1%).
