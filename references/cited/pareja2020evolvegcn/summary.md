---
title: "EvolveGCN: Evolving Graph Convolutional Networks for Dynamic Graphs"
date: 2020-01-01
authors: "Aldo Pareja, Giacomo Domeniconi, Jie Chen, Tengfei Ma, Toyotaro Suzumura, Hiroki Kanezashi, Tim Kaler, Tao B. Schardl, Charles E. Leiserson"
status: read
doi: "arXiv:1902.10191"
category: "Machine Learning"
tags:
  - dynamic-graphs
  - graph-neural-networks
  - gcn
  - rnn
  - temporal-learning
  - project/graph-phishing-detection
---

# EvolveGCN: Evolving Graph Convolutional Networks for Dynamic Graphs

## Metadane
- **Autorzy**: Aldo Pareja, Giacomo Domeniconi, Jie Chen, Tengfei Ma, Toyotaro Suzumura, Hiroki Kanezashi, Tim Kaler, Tao B. Schardl, Charles E. Leiserson (MIT-IBM Watson AI Lab, IBM Research, MIT CSAIL)
- **Rok**: 2020
- **Źródło**: AAAI 2020
- **DOI/Link**: arXiv:1902.10191
- **Status**: read
- **Kategoria główna**: Machine Learning
- **Tagi**: `#dynamic-graphs` `#graph-neural-networks` `#gcn` `#rnn` `#temporal-learning`

## Streszczenie
Praca proponuje **EvolveGCN** — metodę uczenia reprezentacji na grafach dynamicznie ewoluujących w czasie. W przeciwieństwie do wcześniejszych podejść, które uczą osadzeń węzłów (node embeddings) i regulują je sieciami rekurencyjnymi, EvolveGCN ewoluuje w czasie same **parametry** sieci grafowej (GCN), a nie osadzenia. Dzięki temu metoda nie wymaga znajomości węzła w całym horyzoncie czasowym (treningu i testu) i radzi sobie ze scenariuszami, w których zbiór węzłów często się zmienia, a nawet całkowicie różni między krokami czasowymi.

Dynamizm grafu jest wstrzykiwany przez sieć rekurencyjną (RNN/GRU), która aktualizuje wagi GCN na każdym kroku czasowym, tworząc ewoluującą sekwencję parametrów. Rozważane są dwie architektury ewolucji parametrów (wariant traktujący wagi jako stan ukryty oraz jako wejście/wyjście GRU). Metodę oceniono na zadaniach predykcji krawędzi, klasyfikacji krawędzi i klasyfikacji węzłów, gdzie EvolveGCN generalnie przewyższa pokrewne podejścia. Autorzy wskazują zastosowania m.in. w sieciach finansowych (wykrywanie prania pieniędzy, oszustw kartowych), gdzie wczesne wykrycie zmiany charakteru konta jest kluczowe.

## Kluczowe Wnioski
- Ewolucja parametrów GCN (a nie osadzeń) zapewnia indukcyjność wobec nowych/zmiennych zbiorów węzłów.
- Podejście radzi sobie ze skrajnymi przypadkami, gdy węzły pojawiają się i znikają między krokami czasu.
- RNN reguluje wagi GCN, łącząc strukturę grafu z dynamiką czasową.
- EvolveGCN przewyższa metody bazowe w predykcji/klasyfikacji krawędzi i węzłów.

## Metodologia
Połączenie GCN z RNN, gdzie RNN aktualizuje macierze wag GCN na kolejnych snapshotach grafu; dwa warianty (EvolveGCN-H — wagi jako stan ukryty GRU; EvolveGCN-O — wagi jako wejście/wyjście); ewaluacja na zadaniach link prediction, edge classification i node classification na wielu zbiorach dynamicznych.

## Główne Koncepcje
- **Ewolucja parametrów (vs. osadzeń)**: RNN przewiduje wagi GCN w kolejnych krokach.
- **Indukcyjność**: zdolność do działania na nowych węzłach niewidzianych w treningu.
- **Snapshot grafu**: stan grafu w danym kroku czasowym.

## Relevancja dla graph-phishing-detection
EvolveGCN to kanoniczny model bazowy dla **uczonego GNN na grafach dynamicznych** (publikacja P2 w łuku rozprawy: uczony GNN + spójność + indukcja). Phishingowe grafy komunikacji/domen/transakcji ewoluują, a tożsamości węzłów (adresy, domeny, konta) ciągle się zmieniają — indukcyjny mechanizm ewolucji parametrów odpowiada wprost na ten problem i wspiera projektowy nacisk na uogólnianie do nieznanych węzłów. Architektura naturalnie respektuje porządek snapshotów, co współgra z niezmiennikiem dynamiki kaskady i metodologią leak-aware (parametry kroku t bazują tylko na przeszłości). Stanowi też mocny punkt odniesienia, który projekt zamierza pobić na metryce Recall@FPR1% względem prostszej proweniencji binarnej.
