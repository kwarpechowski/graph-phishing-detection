---
title: "Blockchain Phishing Scam Detection via Multi-channel Graph Classification"
date: 2021-01-01
authors: "Dunjie Zhang, Jinyin Chen"
status: read
doi: "arXiv:2108.08456"
category: "Security"
tags:
  - phishing-detection
  - ethereum
  - blockchain
  - graph-classification
  - multi-channel
  - graph-neural-networks
  - project/graph-phishing-detection
---

# Blockchain Phishing Scam Detection via Multi-channel Graph Classification

## Metadane
- **Autorzy**: Dunjie Zhang, Jinyin Chen (Zhejiang University of Technology)
- **Rok**: 2021
- **Źródło**: preprint arXiv (detekcja phishingu na blockchainie)
- **DOI/Link**: arXiv:2108.08456 — https://arxiv.org/abs/2108.08456
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca proponuje MCGC (Multi-Channel Graph Classification) — metodę detekcji kont phishingowych na blockchainie (Ethereum), która formułuje problem jako klasyfikację grafów: dla każdego konta-celu buduje lokalny podgraf transakcji (transaction subgraph) i klasyfikuje cały podgraf jako phishing lub legalny. Motywacją jest to, że wzorce phishingu ujawniają się w strukturze i atrybutach lokalnego otoczenia transakcyjnego konta.

Kluczowy wkład to architektura wielokanałowa (multi-channel): zamiast pojedynczej ścieżki propagacji, model przetwarza podgraf wieloma równoległymi kanałami GNN, każdy uchwytujący inny aspekt/skalę informacji (różne mechanizmy agregacji lub widoki cech), a następnie łączy reprezentacje przez pooling grafowy do końcowej klasyfikacji. Pozwala to wzbogacić reprezentację konta i poprawić rozróżnialność.

Ewaluacja na rzeczywistych danych Ethereum z oznaczonymi kontami phishingowymi pokazuje, że podejście multi-channel graph classification przewyższa metody jednokanałowe i klasyczne osadzenia, poprawiając metryki detekcji (precyzja/recall/F1) na silnie niezbalansowanym zbiorze.

## Kluczowe Wnioski
- Detekcja phishingu jako klasyfikacja lokalnych podgrafów transakcyjnych.
- Architektura wielokanałowa wzbogaca reprezentację konta vs jeden kanał.
- Pooling grafowy agreguje sygnały z wielu kanałów do decyzji.
- Skuteczność potwierdzona na rzeczywistych, niezbalansowanych danych Ethereum.

## Metodologia
Dla konta-celu budowa podgrafu transakcji; równoległe kanały GNN przetwarzają podgraf, ich wyjścia łączone przez graph pooling i klasyfikowane (phishing/benign). Trening nadzorowany na oznaczonym zbiorze Ethereum; metryki precyzja/recall/F1 z uwzględnieniem niezbalansowania klas.

## Główne Koncepcje
- **Multi-channel graph classification** — wiele równoległych kanałów GNN.
- **Transaction subgraph** — lokalny podgraf wokół konta.
- **Graph pooling** — agregacja reprezentacji podgrafu.
- **Phishing account detection** na blockchainie.

## Relevancja dla graph-phishing-detection
Bezpośrednia referencja domenowa łącząca graf transakcji, phishing i GNN, komplementarna do yu2023streaming (ujęcie strumieniowe). Pokazuje skuteczność podejścia subgraph-classification dla kont phishingowych — wzorzec użyteczny w projekcie obok SEAL (zhang2018link). Idea wielokanałowa rezonuje z multipleksowym ujęciem grafu (zhang2018scalable): różne kanały/warstwy uchwytujące różne aspekty relacji. Praca dostarcza dziedzinowego baseline'u i etykietowanego zbioru Ethereum do porównań; razem z yu2023streaming i wątkiem niezbalansowania (zhao2021graphsmote) wyznacza praktyczny krajobraz detekcji phishingu na grafach transakcyjnych.
