---
title: "GraphSMOTE: Imbalanced Node Classification on Graphs with Graph Neural Networks"
date: 2021-01-01
authors: "Tianxiang Zhao, Xiang Zhang, Suhang Wang"
status: read
doi: "10.1145/3437963.3441720"
category: "Machine Learning"
tags:
  - imbalanced-learning
  - node-classification
  - graph-neural-networks
  - smote
  - oversampling
  - edge-generator
  - project/graph-phishing-detection
---

# GraphSMOTE: Imbalanced Node Classification on Graphs with Graph Neural Networks

## Metadane
- **Autorzy**: Tianxiang Zhao, Xiang Zhang, Suhang Wang (Penn State University)
- **Rok**: 2021
- **Źródło**: WSDM 2021
- **DOI/Link**: https://doi.org/10.1145/3437963.3441720
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
GraphSMOTE adaptuje klasyczną technikę nadpróbkowania SMOTE do klasyfikacji węzłów na grafach w warunkach silnego niezbalansowania klas (mała liczba przykładów klasy mniejszościowej). Naiwne zastosowanie SMOTE w przestrzeni cech surowych zawodzi na grafach, bo nie uwzględnia struktury i nie wiadomo, jak połączyć syntetyczne węzły z resztą grafu.

Rozwiązanie: nadpróbkowanie odbywa się w wyuczonej przestrzeni osadzeń (embedding space) generowanej przez enkoder GNN, gdzie odległości lepiej oddają podobieństwo węzłów. Syntetyczne węzły klasy mniejszościowej tworzone są przez interpolację między sąsiadującymi przykładami w tej przestrzeni. Kluczowy komponent to wytrenowany generator krawędzi (edge generator), który przewiduje połączenia nowo wygenerowanych węzłów z istniejącym grafem, tworząc spójną, rozszerzoną strukturę. Całość (enkoder, generator krawędzi, klasyfikator) jest uczona end-to-end.

Eksperymenty na niezbalansowanych zbiorach (cytowania, sieci) pokazują, że GraphSMOTE poprawia metryki czułe na niezbalansowanie (F1 makro, AUC-ROC) względem strategii re-ważenia, klasycznego SMOTE i innych metod oversamplingu, jednocześnie zachowując dokładność klasy większościowej.

## Kluczowe Wnioski
- SMOTE należy stosować w przestrzeni osadzeń GNN, nie cech surowych.
- Generator krawędzi spójnie wpina syntetyczne węzły w strukturę grafu.
- Trening end-to-end enkodera, generatora i klasyfikatora poprawia wyniki.
- Wzrost F1/AUC dla klasy mniejszościowej bez utraty większościowej.

## Metodologia
Enkoder GNN → osadzenia; oversampling przez interpolację w przestrzeni osadzeń dla klasy mniejszościowej; generator krawędzi przewiduje połączenia nowych węzłów; klasyfikator GNN na rozszerzonym grafie; uczenie end-to-end. Ewaluacja na niezbalansowanych benchmarkach metrykami F1 makro / AUC-ROC.

## Główne Koncepcje
- **Embedding-space SMOTE** — interpolacja w przestrzeni osadzeń.
- **Edge generator** — przewidywanie krawędzi syntetycznych węzłów.
- **Imbalanced node classification** — niezbalansowana klasyfikacja.
- **End-to-end oversampling** zintegrowane z GNN.

## Relevancja dla graph-phishing-detection
Niezbalansowanie klas jest nieodłączną cechą detekcji phishingu — konta/krawędzie phishingowe to znikomy ułamek danych (klasa mniejszościowa), co zniekształca uczenie i metryki. GraphSMOTE dostarcza dokładnie dopasowanego narzędzia: nadpróbkowanie świadome struktury, kluczowe dla zbiorów Ethereum (zhang2021mcgc, yu2023streaming) i grafu multipleksowego phishingu. Wpisuje się też w wątek metryk operacyjnych (Recall@FPR1%), gdzie liczy się czułość na rzadką klasę ataku. W projekcie stanowi referencyjną metodę przeciwdziałania niezbalansowaniu, komplementarną do strategii re-ważenia i selekcji progu decyzyjnego.
