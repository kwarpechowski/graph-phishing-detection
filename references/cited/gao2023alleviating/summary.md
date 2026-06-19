---
title: "Alleviating Structural Distribution Shift in Graph Anomaly Detection"
date: 2023-01-01
authors: "Yuan Gao, Xiang Wang, Xiangnan He, Zhenguang Liu, Huamin Feng, Yongdong Zhang"
status: read
doi: "10.1145/3539597.3570377"
category: "Machine Learning"
tags:
  - graph-anomaly-detection
  - fraud-detection
  - distribution-shift
  - heterophily
  - graph-neural-network
  - out-of-distribution
  - project/graph-phishing-detection
---

# Alleviating Structural Distribution Shift in Graph Anomaly Detection

## Metadane
- **Autorzy**: Yuan Gao, Xiang Wang, Xiangnan He, Zhenguang Liu, Huamin Feng, Yongdong Zhang
- **Rok**: 2023
- **Źródło**: WSDM '23 (Sixteenth ACM International Conference on Web Search and Data Mining), Singapur
- **DOI/Link**: 10.1145/3539597.3570377 (arXiv:2401.14155)
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca podejmuje problem przesunięcia rozkładu strukturalnego (Structural Distribution Shift, SDS) w grafowej detekcji anomalii (Graph Anomaly Detection, GAD). GAD to binarna klasyfikacja na grafie, gdzie anomalie (oszuści) są mniejszością i cechują się wysoką heterofilią (krawędzie do klasy przeciwnej) oraz niską homofilią w porównaniu z węzłami normalnymi. Autorzy zauważają, że stopień heterofilii/homofilii zmienia się między danymi treningowymi i testowymi (SDS), zwłaszcza dla anomalii, co psuje generalizację modeli GNN, które ślepo agregują sąsiedztwo.

Proponowanym rozwiązaniem jest Graph Decomposition Network (GDN). Kluczowa idea: dekompozycja cech węzła na cechę klasową (C) i cechę otoczenia (S). Dla anomalii cecha C jest ograniczana przez wektor prototypu klasy, aby była niezmiennicza względem heterofilii i SDS (redukcja wpływu zaszumionych heterofilnych sąsiadów). Dla węzłów normalnych cecha S podlega ograniczeniu spójności (connectivity constraint), aby korzystać z homofilnego, stabilnego sąsiedztwa. Selektor cech oparty na gradiencie (Grad-CAM) wybiera top-K wymiarów jako C. Backbone to RGCN; prototypy aktualizowane adaptacyjnie w każdej epoce.

Eksperymenty na zbiorach YelpChi i Amazon (oba: atrybutowane grafy multi-relacyjne, recenzje) pokazują, że GDN przewyższa silne metody GAD (CARE-GNN, PC-GNN, FRAUDRE, GraphConsis) we wszystkich metrykach, a różnica jest największa w ustawieniu biased (silny SDS). Moduł separacji cech i regularyzatory można też doczepić do innych GNN (GCN, GraphSAGE), poprawiając ich wyniki.

## Kluczowe Wnioski
- SDS jest wyraźny dla anomalii, a trywialny dla węzłów normalnych — wymaga różnych strategii uczenia per klasa.
- Heterofilia jest przyczyną SDS (im wyższa, tym silniejsze przesunięcie — Amazon > YelpChi).
- Dekompozycja na cechy klasowe (niezmiennicze, ograniczone prototypem) i cechy otoczenia (spójność) alleviuje SDS.
- GDN jest elastyczny (wzmacnia GCN/SAGE) i osiąga SOTA (YelpChi AUC 0.9034, Amazon AUC 0.9709).

## Metodologia
Sformalizowanie SDS przez rozkład beta sąsiedztwa i biased selection (P(O=1) zależne od homofilii). Funkcja straty: cross-entropy + ograniczenia (L_cla z dywergencją KL do prototypów, L_sur ze spójnością sąsiadów, negative sampling). Backbone RGCN, wymiar ukryty 64, split 40/20/40. Metryki: F1-macro, AUC, GMean.

## Główne Koncepcje
- **Heterofilia/homofilia** — krawędzie między klasami różnymi/tymi samymi.
- **SDS** — zmiana rozkładu strukturalnego między train/test.
- **Dekompozycja cech (C/S)** — cecha klasowa niezmiennicza vs cecha otoczenia.
- **Wektor prototypu** — adaptacyjny opis "jak wygląda prototyp klasy".

## Relevancja dla graph-phishing-detection
Bezpośrednio relewantna dla wątków "detekcja fraudu/anomalii na grafach" oraz "ewaluacja leak-aware/dryf" w projekcie. Phishing/BEC na grafie to klasyczny przypadek silnie niezbalansowanej, heterofilnej detekcji anomalii, a SDS modeluje realistyczny dryf rozkładu między zebranymi danymi treningowymi a wdrożeniem (zmiany w czasie, preferencje anotatorów) — co bezpośrednio motywuje ewaluację świadomą przecieku i dryfu w projekcie (cel P3). Pomysł rozdzielenia cechy niezmienniczej (odpornej na heterofilnych sąsiadów) od cechy strukturalnej jest cenny dla budowy uczonego GNN, który ma utrzymać Recall przy niskim FPR mimo zmieniającego się sąsiedztwa. Backbone RGCN i wykorzystanie grafów multi-relacyjnych łączy się z heterogenicznym/multipleksowym grafem domenowym phishingu.

## Przydatne Cytaty
- "the structural distribution shift on anomalies is apparent, while that on normals is trivial" (Sekcja 3.1.3).
- "SDS is exaggerated by heterophily" (Sekcja 4.3).

## Datasety
- YelpChi (recenzje hoteli/restauracji, 3 relacje, cechy 32-wym.).
- Amazon (recenzje instrumentów muzycznych, 3 relacje, cechy 25-wym.).

## Powiązane Tematy
- Uczenie out-of-distribution na grafach (IRM, stable learning).
- Camouflage-resistant GNN (CARE-GNN, PC-GNN).
- Spektralna detekcja anomalii (wysokie częstotliwości).

## Notatki
