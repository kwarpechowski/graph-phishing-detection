---
title: "DySAT: Deep Neural Representation Learning on Dynamic Graphs via Self-Attention Networks"
date: 2020-01-01
authors: "Aravind Sankar, Yanhong Wu, Liang Gou, Wei Zhang, Hao Yang"
status: read
doi: "10.1145/3336191.3371845"
category: "Machine Learning"
tags:
  - dynamic-graphs
  - self-attention
  - graph-representation-learning
  - temporal-gnn
  - link-prediction
  - node-embedding
  - project/graph-phishing-detection
---

# DySAT: Deep Neural Representation Learning on Dynamic Graphs via Self-Attention Networks

## Metadane
- **Autorzy**: Aravind Sankar, Yanhong Wu, Liang Gou, Wei Zhang, Hao Yang
- **Rok**: 2020
- **Źródło**: WSDM 2020 (ACM International Conference on Web Search and Data Mining); wcześniej ICLR 2019 RLGM Workshop
- **DOI/Link**: 10.1145/3336191.3371845
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
DySAT (Dynamic Self-Attention Network) to architektura sieci neuronowej do uczenia reprezentacji węzłów w grafach dynamicznych, która jednocześnie modeluje właściwości strukturalne i czasowe wzorce ewolucji. W przeciwieństwie do wcześniejszych metod skupionych na grafach statycznych, DySAT przetwarza graf dynamiczny reprezentowany jako sekwencja migawek (snapshots) w dyskretnych krokach czasowych.

Kluczowa idea polega na zastosowaniu mechanizmu samo-uwagi (self-attention) wzdłuż dwóch wymiarów. Pierwszy to uwaga strukturalna (structural attention) — agreguje cechy sąsiadów w obrębie pojedynczej migawki, ucząc, którzy sąsiedzi są istotni. Drugi to uwaga czasowa (temporal attention) — agreguje reprezentacje tego samego węzła w kolejnych migawkach, wychwytując dynamikę i trendy ewolucyjne. Złożenie obu warstw daje końcowe osadzenie węzła kodujące zarówno topologię, jak i historię.

Autorzy przeprowadzili eksperymenty z predykcją krawędzi na dwóch klasach grafów: sieciach komunikacyjnych i dwudzielnych sieciach ocen (bipartite rating). DySAT uzyskuje istotną poprawę nad konkurencyjnymi metodami osadzania grafów (m.in. node2vec, GraphSAGE, DynGEM, DynamicTriad).

## Kluczowe Wnioski
- Self-attention w dwóch wymiarach (strukturalnym i czasowym) skutecznie łączy topologię z dynamiką.
- Reprezentacja dyskretnych migawek czasowych dobrze sprawdza się w predykcji ewolucji grafu.
- Uwaga czasowa pozwala ważyć starsze i nowsze stany węzła zamiast prostego uśredniania.
- Przewaga nad statycznymi i wcześniejszymi dynamicznymi baseline'ami w predykcji krawędzi.

## Metodologia
Graf dynamiczny dzielony na T migawek. Dla każdej migawki warstwy structural self-attention generują osadzenia uwzględniające sąsiedztwo (z wielogłowicową uwagą). Następnie warstwy temporal self-attention (z kodowaniem pozycyjnym) agregują sekwencję osadzeń węzła w czasie. Trening self-supervised na predykcji krawędzi z próbkowaniem negatywnym; ewaluacja na zbiorach komunikacyjnych (Enron, UCI) i ocenowych (ML-10M, Yelp).

## Główne Koncepcje
- **Structural self-attention**: ważona agregacja sąsiadów w migawce.
- **Temporal self-attention**: agregacja stanów węzła w kolejnych migawkach.
- **Snapshot-based dynamic graph**: dyskretna reprezentacja czasowa.
- **Multi-head attention**: wiele równoległych głowic uwagi.

## Relevancja dla graph-phishing-detection
DySAT reprezentuje migawkowe (discrete-time) podejście do temporalnych GNN — komplementarne wobec strumieniowego TGN (rossi2020temporal). W projekcie obie metody stanowią naturalne baseline'y dla niezmiennika dynamiki kaskady: graf phishingowy (komunikacja nadawca-odbiorca, domena, transakcje) można obserwować jako serię migawek dziennych/godzinowych, a temporal attention pozwala wykryć nagłe zmiany topologii sygnalizujące rozkręcanie kampanii. Mechanizm structural attention odpowiada za rozróżnianie istotnych sąsiadów (np. konto-pułapka vs zaufany kontakt), co jest cenne przy heterofilii połączeń fraudowych. DySAT dostarcza też interpretowalności (wagi uwagi czasowej), użytecznej do wskazania momentu eskalacji ataku w analizie kaskady.
