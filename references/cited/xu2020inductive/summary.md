---
title: "Inductive Representation Learning on Temporal Graphs"
date: 2020-01-01
authors: "Da Xu, Chuanwei Ruan, Evren Korpeoglu, Sushant Kumar, Kannan Achan"
status: read
doi: "arXiv:2002.07962"
category: "Machine Learning"
tags:
  - temporal-graphs
  - inductive-learning
  - graph-neural-networks
  - tgat
  - functional-time-encoding
  - representation-learning
  - project/graph-phishing-detection
---

# Inductive Representation Learning on Temporal Graphs

## Metadane
- **Autorzy**: Da Xu, Chuanwei Ruan, Evren Korpeoglu, Sushant Kumar, Kannan Achan (Walmart Labs)
- **Rok**: 2020
- **Źródło**: ICLR 2020
- **DOI/Link**: arXiv:2002.07962 — https://arxiv.org/abs/2002.07962
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca wprowadza TGAT (Temporal Graph Attention) — model uczenia reprezentacji węzłów na grafach temporalnych, działający w trybie indukcyjnym, tzn. zdolny do generowania osadzeń dla węzłów niewidzianych podczas treningu oraz dla nowych krawędzi pojawiających się w czasie. Kluczowym wkładem jest funkcyjne kodowanie czasu (functional time encoding) oparte na klasycznym twierdzeniu Bochnera, które pozwala reprezentować ciągły upływ czasu jako wektor cech kompatybilny z mechanizmem self-attention.

Zamiast traktować graf jako sekwencję statycznych migawek (snapshotów), TGAT modeluje interakcje na poziomie pojedynczych zdarzeń z dokładnym znacznikiem czasowym. Warstwa temporalnej uwagi agreguje sąsiedztwo węzła ważąc sąsiadów zarówno cechami, jak i różnicą czasów interakcji, co tworzy analogię do GraphSAGE rozszerzonego o wymiar czasowy. Architektura jest składalna w wiele warstw, dziedzicząc indukcyjność po GraphSAGE/GAT.

Eksperymenty na zbiorach Reddit, Wikipedia oraz Industrial obejmują predykcję krawędzi temporalnych (transduktywną i indukcyjną) oraz klasyfikację dynamiczną węzłów; TGAT przewyższa baseline'y statyczne i snapshotowe, zwłaszcza w scenariuszu indukcyjnym z nowymi węzłami.

## Kluczowe Wnioski
- Funkcyjne kodowanie czasu (Bochner) umożliwia włączenie ciągłego czasu do self-attention.
- TGAT generuje osadzenia indukcyjnie dla nowych węzłów/krawędzi bez retreningu.
- Modelowanie zdarzeń (event-level) przewyższa podejścia snapshotowe.
- Wagi uwagi są interpretowalne — pokazują wpływ czasu i cech sąsiadów.

## Metodologia
Warstwa temporalnej uwagi: dla węzła zbiera próbkę sąsiadów wraz ze znacznikami czasu, koduje czas funkcją Φ(t), dokleja do cech węzłów, stosuje wieloglowicową self-attention, agreguje. Trening przez maksymalizację prawdopodobieństwa istnienia krawędzi (negative sampling). Ewaluacja: predykcja linków i klasyfikacja węzłów, transduktywnie i indukcyjnie.

## Główne Koncepcje
- **Functional time encoding** — wektorowa reprezentacja czasu ciągłego.
- **Temporal attention** — uwaga ważona różnicą czasów interakcji.
- **Inductive learning** — generalizacja do niewidzianych węzłów.
- **Continuous-time dynamic graph (CTDG)** — graf jako strumień zdarzeń.

## Relevancja dla graph-phishing-detection
TGAT to fundament temporalnych GNN istotny dla modelowania dynamiki kaskady phishingowej: ataki BEC/spear-phishing rozwijają się w czasie jako strumień zdarzeń (e-maile, transakcje, połączenia domena–nadawca), a nie jako statyczne migawki. Funkcyjne kodowanie czasu pozwala uchwycić "świeżość" krawędzi (np. nagły wzrost komunikacji z nowej domeny), co jest sygnałem ataku. Indukcyjność jest kluczowa operacyjnie — nowe domeny/adresy nadawców pojawiają się stale, a model musi je oceniać bez retreningu. Stanowi alternatywę/uzupełnienie dla ROLAND (you2022roland) i EvolveGCN; w projekcie służy jako baseline temporalny przy detekcji ewoluujących wzorców phishingu na grafie multipleksowym.
