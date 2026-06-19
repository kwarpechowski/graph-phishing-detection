---
title: "Streaming Phishing Scam Detection Method on Ethereum"
date: 2023-01-01
authors: "Sheng Yu, Wei Xia, Bo Liu, Jiajing Wu"
status: read
doi: "arXiv:2306.16624"
category: "Security"
tags:
  - phishing-detection
  - ethereum
  - blockchain
  - streaming-graph
  - graph-neural-networks
  - transaction-graph
  - project/graph-phishing-detection
---

# Streaming Phishing Scam Detection Method on Ethereum

## Metadane
- **Autorzy**: Sheng Yu, Wei Xia, Bo Liu, Jiajing Wu
- **Rok**: 2023
- **Źródło**: preprint arXiv (kontekst: detekcja phishingu na Ethereum)
- **DOI/Link**: arXiv:2306.16624 — https://arxiv.org/abs/2306.16624
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca proponuje metodę detekcji kont phishingowych na blockchainie Ethereum w ujęciu strumieniowym (streaming), traktującym graf transakcji jako stale rosnący, dynamiczny obiekt, a nie statyczną migawkę. Motywacją jest fakt, że tradycyjne metody oparte na statycznym grafie transakcji wymagają ponownego budowania osadzeń przy każdej nowej transakcji, co jest nieskalowalne i nie nadaje się do detekcji w czasie zbliżonym do rzeczywistego.

Autorzy modelują napływające transakcje jako strumień zdarzeń i aktualizują reprezentacje kont przyrostowo, propagując informacje wzdłuż nowo pojawiających się krawędzi transakcyjnych. Wykorzystują temporalne/strumieniowe osadzenia węzłów zasilane do klasyfikatora odróżniającego konta phishingowe od legalnych. Podejście kładzie nacisk na efektywność aktualizacji oraz na uchwycenie wzorców czasowych zachowania kont (częstotliwość, kierunek i wolumen przelewów).

Ewaluacja na rzeczywistych danych transakcyjnych Ethereum z etykietami kont phishingowych pokazuje, że metoda strumieniowa utrzymuje konkurencyjną skuteczność detekcji przy znacznie niższym koszcie aktualizacji niż przeliczanie pełnego grafu, co czyni ją odpowiednią do monitoringu na żywo.

## Kluczowe Wnioski
- Detekcja phishingu na Ethereum zyskuje na ujęciu strumieniowym vs statyczny graf.
- Przyrostowa aktualizacja osadzeń kont jest znacznie tańsza niż przeliczanie całości.
- Wzorce temporalne transakcji są dyskryminacyjne dla kont phishingowych.
- Metoda nadaje się do monitoringu w czasie zbliżonym do rzeczywistego.

## Metodologia
Graf transakcji Ethereum modelowany jako strumień krawędzi z znacznikami czasu; przyrostowe osadzanie węzłów (temporalny/strumieniowy GNN) aktualizowane przy napływie transakcji; klasyfikacja binarna kont (phishing vs benign) na rzeczywistym zbiorze z etykietami. Metryki: precyzja/recall/F1, koszt aktualizacji.

## Główne Koncepcje
- **Streaming transaction graph** — strumieniowy graf transakcji.
- **Incremental node embedding** — przyrostowe osadzanie kont.
- **Phishing account classification** — klasyfikacja kont.
- **Temporal transaction patterns** — wzorce czasowe przelewów.

## Relevancja dla graph-phishing-detection
To jedna z najbliższych referencji domenowych: bezpośrednio łączy graf transakcji, phishing i ujęcie strumieniowe/temporalne. Potwierdza tezę projektu, że phishing najlepiej modelować jako dynamiczny graf zdarzeń, a nie statyczną migawkę, oraz dostarcza dziedzinowego baseline'u dla detekcji na grafie transakcji (komplementarnie do zhang2021mcgc — multi-channel graph classification na Ethereum). Strumieniowa aktualizacja osadzeń jest spójna z paradygmatem ROLAND (you2022roland) i TGAT (xu2020inductive); w projekcie służy do uzasadnienia metryk operacyjnych (Recall@FPR1%) i jako punkt odniesienia dla detekcji ewoluujących kampanii.
