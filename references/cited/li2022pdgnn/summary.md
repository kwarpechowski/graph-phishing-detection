---
title: "Phishing Fraud Detection on Ethereum using Graph Neural Network (PDGNN)"
date: 2022-01-01
authors: "Panpan Li, Yunyi Xie, Xinyao Xu, Jiajun Zhou, Qi Xuan"
status: read
doi: "arXiv:2204.08194"
category: "Security"
tags:
  - ethereum
  - phishing-detection
  - graph-classification
  - chebyshev-gcn
  - subgraph-sampling
  - blockchain
  - project/graph-phishing-detection
---

# Phishing Fraud Detection on Ethereum using Graph Neural Network (PDGNN)

## Metadane
- **Autorzy**: Panpan Li, Yunyi Xie, Xinyao Xu, Jiajun Zhou, Qi Xuan (Institute of Cyberspace Security, Zhejiang University of Technology)
- **Rok**: 2022
- **Źródło**: arXiv preprint (cs.SI)
- **DOI/Link**: https://arxiv.org/abs/2204.08194 (`#ethereum`, `#graph-classification`, `#chebyshev-gcn`)
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca podejmuje problem detekcji phishingu na blockchainie Ethereum, traktując go jako zadanie klasyfikacji grafów. Autorzy zwracają uwagę, że dotychczasowe metody oparte na uczeniu reprezentacji grafu (np. trans2vec, GCN+autoenkoder, TSGN) generują wektory cech kont, a następnie używają osobnych klasyfikatorów ML — nie są więc architekturami end-to-end i słabo skalują się w dużych sieciach transakcyjnych Ethereum.

Proponowany framework PDGNN (Phishing Detection Graph Neural Network) jest rozwiązaniem end-to-end. Najpierw konstruowana jest lekka (lightweight) sieć transakcyjna Ethereum poprzez strategię odchudzania (rescaling) zbiorów danych. Następnie formułowana jest reguła próbkowania umożliwiająca ekstrakcję podgrafów o zbliżonej skali, co pozwala na trening mini-batch kolejnych modeli. Rdzeniem jest sieć splotowa grafowa oparta na wielomianach Czebyszewa (Chebyshev-GCN), która automatycznie wydobywa cechy zachowań transakcyjnych kont i rozróżnia konta normalne od phishingowych.

Rozległe eksperymenty na pięciu zbiorach danych Ethereum pokazują, że PDGNN znacząco przewyższa ogólne metody detekcji phishingu i dobrze skaluje się w dużych sieciach transakcyjnych. Architektura obejmuje warstwy splotowe Chebyshev-GCN, warstwę poolingu oraz warstwę w pełni połączoną.

## Kluczowe Wnioski
- Detekcja phishingu sformułowana jako klasyfikacja podgrafów (a nie tylko klasyfikacja węzłów).
- Architektura end-to-end uczy cech związanych bezpośrednio z zadaniem, w odróżnieniu od pipeline'ów dwuetapowych.
- Strategia odchudzania sieci i próbkowania podgrafów zapewnia skalowalność do dużych grafów.
- Chebyshev-GCN skutecznie modeluje wzorce zachowań transakcyjnych kont.

## Metodologia
Dane transakcyjne Ethereum modelowane jako graf G=(V,E,X): konta jako węzły, transakcje (z timestampem i wartością) jako krawędzie. Krok 1: lekka konstrukcja sieci (rescaling). Krok 2: próbkowanie podgrafów wokół kont phishingowych o podobnej skali umożliwiające mini-batch. Krok 3: model klasyfikacji podgrafów oparty na Chebyshev-GCN (warstwy splotowe + pooling + FC). Ewaluacja na pięciu zbiorach Ethereum względem metod ogólnych.

## Główne Koncepcje
- **Klasyfikacja grafów/podgrafów** dla detekcji phishingu
- **Chebyshev-GCN** — spektralna konwolucja grafowa
- **Lightweight network construction** i próbkowanie podgrafów
- **Architektura end-to-end** vs. embeddingi + osobny klasyfikator

## Relevancja dla graph-phishing-detection
PDGNN to bezpośredni baseline dla projektu — reprezentuje podejście klasyfikacji podgrafów na grafie transakcji Ethereum z uczonym GNN. Wspiera niezmiennik projektu dotyczący wyuczonej reprezentacji (zamiast cech ręcznie projektowanych) oraz problem skalowalności (próbkowanie podgrafów). Stanowi punkt odniesienia w porównaniu z grafem wiedzy domenowej i metodami opartymi na proweniencji; technika próbkowania podgrafów o jednolitej skali jest istotna dla porównywalnej, indukcyjnej ewaluacji.
