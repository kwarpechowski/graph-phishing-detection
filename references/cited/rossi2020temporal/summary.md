---
title: "Temporal Graph Networks for Deep Learning on Dynamic Graphs"
date: 2020-01-01
authors: "Emanuele Rossi, Ben Chamberlain, Fabrizio Frasca, Davide Eynard, Federico Monti, Michael Bronstein"
status: read
doi: "arXiv:2006.10637"
category: "Machine Learning"
tags:
  - temporal-graph-networks
  - dynamic-graphs
  - gnn
  - memory-modules
  - link-prediction
  - representation-learning
  - project/graph-phishing-detection
---

# Temporal Graph Networks for Deep Learning on Dynamic Graphs

## Metadane
- **Autorzy**: Emanuele Rossi, Ben Chamberlain, Fabrizio Frasca, Davide Eynard, Federico Monti, Michael Bronstein
- **Rok**: 2020
- **Źródło**: arXiv preprint (zaprezentowane na ICML 2020 Workshop on Graph Representation Learning)
- **DOI/Link**: arXiv:2006.10637 — https://arxiv.org/abs/2006.10637
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca wprowadza Temporal Graph Networks (TGN) — ogólną i wydajną obliczeniowo architekturę do głębokiego uczenia na grafach dynamicznych reprezentowanych jako sekwencje zdarzeń z metką czasową (timed events). Autorzy wskazują, że pomimo bogactwa modeli GNN dla grafów statycznych, niewiele podejść radzi sobie z grafami, w których cechy węzłów lub topologia połączeń ewoluują w czasie. TGN łączy moduły pamięci (memory modules) przypisane do każdego węzła z operatorami opartymi na grafie (graph attention) w celu agregacji informacji z sąsiedztwa czasowego.

Kluczowym elementem jest pamięć węzła aktualizowana przez moduł GRU/RNN przy każdym dotyczącym go zdarzeniu, co pozwala modelowi przechowywać skompresowaną historię interakcji. Moduł embeddingu rozwiązuje problem „nieświeżości" pamięci (staleness), wyliczając aktualną reprezentację węzła na podstawie pamięci jego sąsiadów. Autorzy pokazują, że kilka wcześniejszych modeli dla grafów dynamicznych (TGAT, Jodie, DyRep) stanowi szczególne przypadki ich frameworka.

W szczegółowym badaniu ablacyjnym TGN osiąga stan wiedzy (state-of-the-art) na zadaniach predykcji krawędzi i klasyfikacji węzłów w trybie transduktywnym i indukcyjnym, przewyższając wcześniejsze metody przy mniejszym koszcie obliczeniowym dzięki przetwarzaniu wsadowemu zdarzeń.

## Kluczowe Wnioski
- Moduły pamięci na poziomie węzła pozwalają efektywnie kondensować długą historię interakcji.
- Rozdzielenie pamięci od modułu embeddingu rozwiązuje problem nieaktualnej pamięci (memory staleness).
- TGN uogólnia wcześniejsze modele dynamiczne (TGAT, Jodie, DyRep) jako swoje przypadki szczególne.
- Architektura jest wydajna obliczeniowo dzięki przetwarzaniu zdarzeń w batchach.
- Skuteczna zarówno w predykcji indukcyjnej (nowe węzły), jak i transduktywnej.

## Metodologia
Graf dynamiczny modelowany jako ciągły strumień zdarzeń (continuous-time dynamic graph). Każde zdarzenie aktualizuje wektory pamięci zaangażowanych węzłów (moduł message + agregacja + RNN). Moduł embeddingu (graph attention nad sąsiedztwem czasowym) generuje aktualne reprezentacje. Trening na predykcji krawędzi metodą self-supervised; ablacje porównują warianty pamięci, agregacji i embeddingu na zbiorach Wikipedia, Reddit, Twitter.

## Główne Koncepcje
- **Memory module**: stan węzła kondensujący historię.
- **Memory staleness**: problem nieaktualności pamięci między zdarzeniami.
- **Temporal graph attention**: agregacja po sąsiadach z metką czasu.
- **Tryb indukcyjny vs transduktywny**: predykcja dla nowych vs znanych węzłów.

## Relevancja dla graph-phishing-detection
TGN dostarcza kanoniczny, wydajny szkielet temporalnego GNN, na którym można zbudować niezmiennik dynamiki kaskady phishingowej — kampanie BEC/phishing rozwijają się jako strumień zdarzeń (wysłanie maila, klik, logowanie, transakcja). Moduły pamięci pozwalają śledzić ewoluujący profil ryzyka węzła (nadawcy, domeny, konta) bez przebudowy całego grafu, co odpowiada wymaganiu detekcji w czasie zbliżonym do rzeczywistego. Tryb indukcyjny jest kluczowy dla phishingu, gdzie nieustannie pojawiają się nowe domeny i konta (cold-start) — TGN potrafi generować reprezentacje dla węzłów niewidzianych w treningu. W połączeniu z DySAT (sankar2020dysat) wyznacza dwie rodziny modeli temporalnych (memory-based vs self-attention nad migawkami) do porównania jako baseline dla niezmiennika dynamiki kaskady w projekcie.
