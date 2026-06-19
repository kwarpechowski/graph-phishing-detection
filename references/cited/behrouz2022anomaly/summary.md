---
title: "Anomaly Detection in Multiplex Dynamic Networks: from Blockchain Security to Brain Disease Prediction"
date: 2022-01-01
authors: "Ali Behrouz, Margo Seltzer"
status: read
doi: "arXiv:2211.08378"
category: "Machine Learning"
tags:
  - multiplex-networks
  - dynamic-graphs
  - edge-anomaly-detection
  - graph-neural-networks
  - attention-mechanism
  - fraud-detection
  - project/graph-phishing-detection
---

# Anomaly Detection in Multiplex Dynamic Networks: from Blockchain Security to Brain Disease Prediction

## Metadane
- **Autorzy**: Ali Behrouz, Margo Seltzer
- **Rok**: 2022
- **Źródło**: NeurIPS 2022 Temporal Graph Learning Workshop / arXiv
- **DOI/Link**: https://arxiv.org/abs/2211.08378
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca wprowadza ANOMULY — ogólny, nienadzorowany framework do detekcji anomalnych krawędzi w multipleksowych sieciach dynamicznych (wiele typów relacji między tymi samymi węzłami, ewoluujących w czasie). Autorzy wskazują trzy ograniczenia dotychczasowych metod: sztywność struktury/cech (predefiniowane wzorce lub ręcznie tworzone cechy), traktowanie wszystkich warstw (typów relacji) jednakowo oraz brak detekcji anomalii na poziomie krawędzi (wcześniejsze prace skupiały się na węzłach/podgrafach/zdarzeniach). ANOMULY jest pierwszą metodą detekcji anomalnych krawędzi dla sieci multipleksowych.

Architektura opiera się na "Snapshot Encoderze": dla każdego typu relacji GNN agreguje cechy z sąsiedztwa (z hierarchicznymi stanami węzłów po każdej warstwie), komórka GRU aktualizuje embeddingi w czasie, a mechanizm uwagi (attention) integruje informację z różnych warstw z wagami zależnymi od węzła (różne warstwy mają różną ważność dla różnych węzłów). Anomalny wynik krawędzi liczony jest z embeddingów warstwowych, a uczenie odbywa się przez selektywne negative sampling (rozkład Bernoulliego zależny od stopni węzłów) i margin loss — bez etykiet ground-truth.

Eksperymenty na 9 zbiorach (sieci społeczne, współautorstwa, blockchain, co-purchasing) pokazują przewagę ANOMULY: średnio +8,18% AUC nad najlepszym baseline'em na sieciach multipleksowych i +2,46% na jednowarstwowych. Studium przypadku: detekcja zdarzeń w sieci Ethereum (top-4 anomalie pokrywają się z ważnymi wydarzeniami rynkowymi) oraz analiza sieci mózgowych ADHD (74% wykrytych anomalii w grupie ADHD).

## Kluczowe Wnioski
- ANOMULY jako pierwszy wykrywa anomalne krawędzie w multipleksowych sieciach dynamicznych.
- Mechanizm uwagi ważący warstwy per-węzeł i komórki GRU są kluczowe (ablacja potwierdza spadek bez nich).
- Modelowanie sieci jako multipleksowej (zamiast jednowarstwowej) daje bogatszą informację i lepszą detekcję.
- Detekcja oparta na uczeniu pokonuje metody z predefiniowanymi wzorcami nawet na sieciach statycznych.

## Metodologia
Nienadzorowane uczenie end-to-end. GNN (200 wymiarów, sum-aggregation, skip-connections) + GRU + attention. Margin-based pairwise loss z negative samplingiem zależnym od stopni. Metryka: AUC. Anomalie wstrzykiwane (layer-independent i layer-dependent), bo brak ground-truth. Implementacja w GraphGym, GPU V100.

## Główne Koncepcje
- **Sieć multipleksowa dynamiczna**: wspólny zbiór węzłów, wiele typów krawędzi (warstw), ewolucja w czasie (snapshoty).
- **Hierarchiczne stany węzłów**: embeddingi z różnych warstw GNN traktowane jako stany aktualizowane przez GRU.
- **Attention ważący warstwy per-węzeł**: różna istotność typów relacji dla różnych węzłów.
- **Layer-dependent anomaly**: krawędź anomalna względem konkretnej warstwy/relacji.

## Relevancja dla graph-phishing-detection
To jedna z najbliższych prac metodologicznych dla projektu — bezpośrednio uzasadnia rdzeń publikacji P1 (multipleks) i P2 (uczony GNN + spójność + indukcja). Architektura ANOMULY (GNN+GRU+attention na warstwach, snapshoty temporalne, negative sampling, margin loss) jest niemal gotowym szablonem dla detekcji anomalnych krawędzi w wielowarstwowych grafach phishingowych (relacje komunikacja/domena/transakcje jako warstwy multipleksu). Studium fraudu na blockchainie pokazuje przenośność na detekcję anomalii transakcyjnych. Istotny jest też wniosek, że attention ważący warstwy per-węzeł przewyższa równe traktowanie warstw — kluczowy argument przy projektowaniu spójnościowego GNN dla phishingu i przy ewaluacji opartej na AUC/Recall@FPR.
