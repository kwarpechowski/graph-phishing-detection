---
title: "Business Email Compromise Phishing Detection Based on Machine Learning: A Systematic Literature Review"
date: 2023-01-01
authors: "Hany F. Atlam, Olayonu Oluwatimilehin"
status: read
doi: "10.3390/electronics12010042"
category: "Security"
tags:
  - business-email-compromise
  - phishing-detection
  - systematic-literature-review
  - email-security
  - spear-phishing
  - machine-learning
  - project/graph-phishing-detection
---

# Business Email Compromise Phishing Detection Based on Machine Learning: A Systematic Literature Review

## Metadane
- **Autorzy**: Hany F. Atlam, Olayonu Oluwatimilehin
- **Rok**: 2023
- **Źródło**: Electronics (MDPI), 12(1), 42
- **DOI/Link**: https://doi.org/10.3390/electronics12010042
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca jest systematycznym przeglądem literatury (SLR) dotyczącym detekcji ataków typu Business Email Compromise (BEC) z wykorzystaniem uczenia maszynowego. BEC to wyrafinowana forma spear phishingu wymierzona w organizacje (np. CEO fraud, vendor email compromise), która — w odróżnieniu od klasycznego phishingu — często nie zawiera złośliwego ładunku ani linków, co czyni ją niewykrywalną dla typowych filtrów antyspamowych. Straty z BEC oszacowano na ponad 26 mld USD w latach 2016–2019 (FBI).

Z 950 wstępnie zebranych artykułów (2012–2022) wyselekcjonowano 38 do szczegółowej analizy. Autorzy odpowiadają na cztery pytania badawcze: najnowsza literatura BEC (RQ1), najczęstsze algorytmy ML (RQ2), używane datasety (RQ3) oraz cechy detekcji (RQ4). Praca opisuje cykl życia ataku BEC (10 kroków: research, identyfikacja celu, budowa persony, spoofing, izolacja ofiary, transfer środków), pięć typów BEC oraz techniki (spoofing nagłówków, podobieństwo domen, podszywanie pod kadrę zarządzającą).

Wyniki: najczęściej używane algorytmy to Decision Tree, SVM, ANN, Naive Bayes i Logistic Regression (każdy w ≥10 z 38 prac); dominuje uczenie nadzorowane (nienadzorowane daje niską precyzję przy rzadkiej klasie BEC). Cechy pochodzą z nagłówka (23 prace), treści (28 prac) i URL. Datasety: ponad połowa prac używa własnych, niestandardowych zbiorów; popularne są Nazario, Enron, Kaggle, SpamAssassin. Kierunki przyszłe: dynamiczna selekcja cech, datasety odzwierciedlające realne scenariusze, integracja NLP z deep learning, XAI i detekcja w czasie rzeczywistym.

## Kluczowe Wnioski
- BEC jest trudny do wykrycia, bo zwykle brak ładunku/linków — wymaga analizy treści, nagłówka i kontekstu.
- DT, SVM, ANN, NB, LR to najczęstsze algorytmy; uczenie nadzorowane przeważa nad nienadzorowanym.
- Brak realistycznych, publicznych datasetów BEC to główne ograniczenie pola.
- Cechy treści i nagłówka dominują; URL rzadziej (BEC często nie zawiera linków).

## Metodologia
Systematyczny przegląd literatury (PRISMA-podobny, 5 etapów): formułowanie RQ, kryteria włączenia/wykluczenia, przeszukanie 6 baz (Google Scholar, IEEE, ACM, Springer, ScienceDirect, PubMed), analiza i raport. 950 → 63 → 38 prac po trzech fazach filtrowania.

## Główne Koncepcje
- **BEC (CEO fraud)**: ukierunkowany spear phishing wymierzony w finanse organizacji, bez złośliwego ładunku.
- **Cechy nagłówka/treści/URL**: trzy główne źródła sygnału detekcji.
- **Dynamiczna selekcja cech**: adaptacyjny dobór cech do zmieniających się taktyk atakującego.

## Relevancja dla graph-phishing-detection
Praca bezpośrednio wspiera motywację projektu w obszarze detekcji BEC i lateral/spear phishingu — kluczowych celów planowanej publikacji P3 (realne etykiety BEC). Wskazuje lukę: większość metod to płaska klasyfikacja treści/nagłówka pojedynczych e-maili, ignorująca strukturę komunikacji. To uzasadnia podejście grafowe projektu, gdzie graf komunikacji (kto-do-kogo, relacje organizacyjne) i graf domenowy mogą ujawnić anomalie BEC niewidoczne dla klasyfikatorów treści. Przegląd dostarcza też mapy baselineów (DT/SVM/ANN) oraz datasetów (Enron, Nazario, Avocado), które mogą posłużyć do leak-aware ewaluacji modeli GNN, a podkreślony brak realistycznych zbiorów BEC potwierdza wartość budowy własnego korpusu grafowego.
