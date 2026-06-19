---
title: "Deep Learning for Insider Threat Detection: Review, Challenges and Opportunities"
date: 2020-01-01
authors: "Shuhan Yuan, Xintao Wu"
status: read
doi: "arxiv:2005.12433"
category: "Security"
tags:
  - insider-threat
  - deep-learning
  - survey
  - anomaly-detection
  - ueba
  - lstm
  - autoencoder
  - project/behavioral-security-ueba
---

# Deep Learning for Insider Threat Detection: Review, Challenges and Opportunities

## Metadane
- **Autorzy**: Shuhan Yuan, Xintao Wu
- **Rok**: 2020
- **Źródło**: arXiv:2005.12433
- **DOI**: arxiv:2005.12433
- **Status**: `#read`
- **Kategoria**: Security / Deep Learning
- **Tagi**: `#insider-threat` `#deep-learning` `#survey` `#anomaly-detection` `#ueba` `#lstm`

## Streszczenie

Kompleksowy survey metod deep learning dla detekcji insider threats. Autorzy systematycznie przeglądają techniki DL stosowane w tym obszarze, identyfikują kluczowe wyzwania i otwarte problemy badawcze.

Survey obejmuje metody sekwencyjne (LSTM, RNN), autoenkoderowe (dla anomaly detection), grafowe (graph neural networks) oraz hybrydowe. Omawia specyficzne wyzwania insider threat detection: brak labeled data, imbalanced classes, adaptive attackers, prywatność danych.

Kluczowe rozróżnienie: insider threats vs. external attacks — insiderzy mają legitymowany dostęp, więc ich zachowanie trudniej odróżnić od normalnego. DL radzi sobie lepiej niż tradycyjny ML dzięki zdolności do uczenia się reprezentacji z surowych danych.

## Kluczowe Wnioski
- DL przewyższa tradycyjny ML dla insider threat gdy dostępne są wystarczające dane
- Główne wyzwania: (1) niewystarczająca liczba labeled examples, (2) adaptive attackers, (3) prywatność danych, (4) interpretability
- CERT Insider Threat Dataset jest dominującym benchmarkiem (ale ma znane ograniczenia — mały, syntetyczny)
- Sekwencyjne modele (LSTM) skuteczniejsze dla temporalnych wzorców zachowania
- Federated learning jako kierunek dla prywatność-preserving UEBA

## Metodologia
Survey/review — systematyczny przegląd literatury kategoryzujący metody DL według architektury i zastosowania.

## Główne Koncepcje
- **Insider threat**: zagrożenie ze strony aktora z legitymowanym dostępem (pracownik, kontrahent)
- **Behavioral anomaly**: odchylenie od baseline zachowania jako sygnał zagrożenia
- **Adaptive attacker**: atakujący świadomy systemu detekcji, celowo naśladujący normalne zachowanie
- **Federated learning for UEBA**: lokalne modele bez centralnego agregowania danych

## Wyniki
Nie prezentuje własnych wyników empirycznych — survey paper. Synteza wyników z literatury.

## Przydatne Cytaty
- "Deep learning outperforms traditional ML for insider threat when sufficient data is available"
- "The challenges include insufficient labeled data and adaptive attacks"

## Datasety
- [CERT Insider Threat Dataset](../../datasets/cert-insider-threat.md) — wspomniany jako dominujący benchmark w literaturze

## Powiązane Tematy
- BPP baseline vs. deep learning (#BSU-1)
- Adaptive attackers i MMC (#BSU-2)
- FL+DP dla UEBA (#BSU-3)

## Notatki
Essential related work. Ważne: autorzy sami wskazują federated learning jako obiecujący kierunek — to uzasadnienie dla BSU-3.
