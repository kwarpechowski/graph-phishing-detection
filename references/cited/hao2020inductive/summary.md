---
title: "Inductive Link Prediction for Nodes Having Only Attribute Information"
date: 2020-01-01
authors: "Yu Hao, Xin Cao, Yixiang Fang, Xike Xie, Sibo Wang"
status: read
doi: "arXiv:2007.08053"
category: "Machine Learning"
tags:
  - inductive-link-prediction
  - graph-embedding
  - attributed-graph
  - dual-encoder
  - alignment-mechanism
  - cold-start
  - project/graph-phishing-detection
---

# Inductive Link Prediction for Nodes Having Only Attribute Information

## Metadane
- **Autorzy**: Yu Hao, Xin Cao, Yixiang Fang, Xike Xie, Sibo Wang
- **Rok**: 2020
- **Źródło**: IJCAI 2020 (preprint arXiv)
- **DOI/Link**: arXiv:2007.08053
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca dotyczy induktywnej predykcji powiązań (inductive link prediction) dla nowych węzłów, dla których znane są wyłącznie atrybuty, a nieznana jest lokalna struktura grafu (węzeł nie był widziany podczas treningu). Jest to trudniejsze niż predykcja transduktywna (gdzie oba węzły są już w grafie i widoczne w treningu), a typowe metody jak GCN, GAE czy SEAL wymagają informacji strukturalnej. Jedyną wcześniejszą metodą induktywną z samych atrybutów jest G2G, która jednak słabo rozróżnia węzły o podobnych atrybutach, bo nie wykorzystuje dobrze struktury.

Autorzy proponują model DEAL (Dual-Encoder graph embedding with ALignment), złożony z trzech komponentów: (1) kodera zorientowanego na atrybuty (Ha, MLP — celowo bez agregacji GCN, bo agregowanie sąsiedztwa pogarsza reprezentację atrybutów do predykcji powiązań), (2) kodera zorientowanego na strukturę (Hs, model liniowy na one-hot identyfikatorach węzłów), (3) mechanizmu wyrównania (alignment), który łączy osadzenia atrybutowe i strukturalne we wspólnej przestrzeni. Wprowadzono nową, regularyzowaną funkcję straty rankingowej (uogólniona strata logistyczna z marginesami) oraz ważenie negatywnych próbek odległością najkrótszej ścieżki.

DEAL jest wszechstronny — działa zarówno induktywnie (lambda1=0, tylko enkoder atrybutowy dla nowego węzła), jak i transduktywnie. Eksperymenty na siedmiu zbiorach (Cora, CiteSeer, PubMed, CS, PPI, Computers, Photo) pokazują, że DEAL konsekwentnie przewyższa SOTA: w trybie induktywnym poprawa AP o co najmniej 6% (na Computers AUC +6.12%, AP +17.98%), a także przewyższa metody transduktywne.

## Kluczowe Wnioski
- DEAL rozwiązuje induktywną predykcję powiązań z samych atrybutów dzięki wyrównaniu dwóch enkoderów.
- Mechanizm alignment buduje pomost atrybuty<->struktura, poprawiając reprezentacje (loose alignment > tight).
- MLP jako enkoder atrybutowy przewyższa enkodery GCN-podobne dla tego zadania (agregacja sąsiedztwa szkodzi).
- Model działa zarówno induktywnie, jak i transduktywnie; przewyższa G2G, GAE i warianty.

## Metodologia
Graf atrybutowy G=(V,E,X); dwa enkodery + alignment; mini-batch z 40% par połączonych; strata rankingowa z regularyzacją (gamma, b) i ważeniem alpha po najkrótszej ścieżce. Predykcja: ważona suma podobieństw (struktura-struktura, atrybut-atrybut, struktura-atrybut). Metryki: AUC, AP (10 prób). Wymiar osadzenia 64, grid search.

## Główne Koncepcje
- **Predykcja induktywna vs transduktywna** — węzły niewidziane vs widziane w treningu.
- **Dual-encoder** — osobne osadzenia atrybutowe i strukturalne.
- **Alignment** — wyrównanie obu typów osadzeń.
- **Ważenie negatywów** — uwzględnienie odległości w grafie.

## Relevancja dla graph-phishing-detection
Bardzo istotna dla wątku "indukcyjność modeli GNN" i "ewaluacja leak-aware" w projekcie. W realnym phishingu/BEC stale pojawiają się nowe domeny, URL i nadawcy bez historii strukturalnej (cold-start) — predykcja induktywna z samych atrybutów jest dokładnie tym scenariuszem. DEAL pokazuje, jak łączyć cechy treściowe węzła (atrybuty domeny/URL/IP) z informacją strukturalną w sposób generalizujący na niewidziane węzły, co jest projektowym celem pobicia detekcji binarnej proweniencji przy zachowaniu Recall@FPR. Idea, że enkoder atrybutowy nie powinien agregować sąsiedztwa (bo węzeł testowy go nie ma), jest kluczowa dla poprawnej, świadomej-przecieku ewaluacji indukcyjnej w projekcie.

## Przydatne Cytaty
- "many real-world applications need inductive link prediction which requires embeddings to be quickly generated for new nodes with only attribute information" (Wstęp).
- "the loose alignment method slightly outperforms the tight alignment method, especially for the inductive link prediction task" (Sekcja 5.6).

## Datasety
- Cora, CiteSeer, PubMed (sieci cytowań), CS (współautorstwo), PPI (interakcje białek), Computers, Photo (współzakupy).

## Powiązane Tematy
- G2G (Gaussian embedding), GAE/SEAL.
- Strata rankingowa / kontrastywna w grafach.
- Cold-start w systemach rekomendacyjnych i bezpieczeństwie.

## Notatki
