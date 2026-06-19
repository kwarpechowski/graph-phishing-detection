---
title: "UMGAD: Unsupervised Multiplex Graph Anomaly Detection"
date: 2025-01-01
authors: "Xiang Li, Jianpeng Qi, Zhongying Zhao, Guanjie Zheng, Lei Cao, Junyu Dong, Yanwei Yu"
status: read
doi: "arXiv:2411.12556"
category: "Machine Learning"
tags:
  - multiplex-graph
  - anomaly-detection
  - unsupervised-learning
  - graph-masked-autoencoder
  - contrastive-learning
  - fraud-detection
  - project/graph-phishing-detection
---

# UMGAD: Unsupervised Multiplex Graph Anomaly Detection

## Metadane
- **Autorzy**: Xiang Li, Jianpeng Qi, Zhongying Zhao, Guanjie Zheng, Lei Cao, Junyu Dong, Yanwei Yu (Ocean University of China i in.)
- **Rok**: 2025
- **Źródło**: arXiv preprint (cs.LG), wersja v4
- **DOI/Link**: https://arxiv.org/abs/2411.12556 (`#multiplex`, `#GMAE`, `#contrastive`)
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca dotyczy detekcji anomalii na grafach (GAD) — identyfikacji węzłów znacząco odbiegających od większości, z zastosowaniami m.in. w detekcji oszustw i analizie sieci społecznych. Autorzy wskazują dwa wyzwania istniejących metod: (1) większość ogranicza się do grafów z jednym typem interakcji i nie radzi sobie z wieloma typami w multipleksowych grafach heterogenicznych (np. relacje viewing/carting/buying w e-commerce); (2) w scenariuszach nienadzorowanych dobór progu anomalii (anomaly score threshold) jest trudny, gdy liczba anomalii jest nieznana.

Proponowana metoda UMGAD (Unsupervised Multiplex Graph Anomaly Detection) najpierw uczy się wielorelacyjnych korelacji między węzłami w multipleksowych grafach heterogenicznych i przechwytuje informację o anomaliach podczas rekonstrukcji atrybutów i struktury węzłów za pomocą grafowego maskowanego autoenkodera (GMAE). Następnie generuje grafy w widoku rozszerzonym (augmented-view) na poziomie atrybutów oraz na poziomie podgrafów i wykonuje rekonstrukcję atrybutów i struktury. Na koniec optymalizuje cechy poprzez uczenie kontrastywne między widokiem oryginalnym a rozszerzonym, poprawiając zdolność wykrywania anomalii. Zaproponowano też nową strategię doboru progu, niezależną od informacji ground-truth.

Eksperymenty na sześciu zbiorach (z anomaliami wstrzykniętymi i rzeczywistymi) pokazują, że UMGAD znacząco przewyższa metody SOTA, z średnią poprawą 12.25% AUC i 11.29% Macro-F1.

## Kluczowe Wnioski
- UMGAD osiąga średnio +12.25% AUC i +11.29% Macro-F1 względem SOTA na sześciu zbiorach.
- Multipleksowe grafy heterogeniczne (wiele typów relacji) wymagają dedykowanego modelowania korelacji wielorelacyjnych.
- GMAE z wieloma mechanizmami maskowania rekonstruuje atrybuty, strukturę i podgrafy.
- Nowa strategia doboru progu działa bez ground-truth — istotna w realnym scenariuszu nienadzorowanym.

## Metodologia
Rdzeń: grafowy maskowany autoenkoder (GMAE) z wieloma maskami, rekonstruujący atrybuty i strukturę w widoku oryginalnym oraz w widokach rozszerzonych (poziom atrybutów i poziom podgrafów). Uczenie kontrastywne między widokiem oryginalnym a rozszerzonym wzmacnia detekcję anomalii. Strategia doboru progu oparta na ekstrakcji informacji o anomaliach z obu widoków, bez ground-truth. Ewaluacja: AUC, Macro-F1 na 6 zbiorach (anomalie wstrzyknięte i rzeczywiste).

## Główne Koncepcje
- **Multipleksowy graf heterogeniczny** — wiele typów relacji/interakcji
- **Graph-Masked Autoencoder (GMAE)** — rekonstrukcja atrybutów i struktury
- **Uczenie kontrastywne** widok oryginalny vs rozszerzony
- **Bezprogowy/adaptacyjny dobór progu anomalii** bez ground-truth

## Relevancja dla graph-phishing-detection
UMGAD jest bezpośrednio relevantny dla niezmiennika projektu dotyczącego multipleksowych/wielowarstwowych grafów — pokazuje, jak detekować anomalie przy wielu typach relacji jednocześnie, co odpowiada grafowi wiedzy domenowej łączącemu komunikację, domeny i transakcje. Nienadzorowane podejście (GMAE + kontrastywne) oraz strategia doboru progu bez ground-truth są kluczowe dla scenariusza phishingu z niedoborem etykiet i nieznaną liczbą anomalii. Stanowi nowoczesny (2025) baseline metod multipleksowych do porównania w projekcie.
