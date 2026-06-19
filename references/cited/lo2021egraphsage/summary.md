---
title: "E-GraphSAGE: A Graph Neural Network based Intrusion Detection System for IoT"
date: 2021-01-01
authors: "Wai Weng Lo, Siamak Layeghy, Mohanad Sarhan, Marcus Gallagher, Marius Portmann"
status: read
doi: "arXiv:2103.16329"
category: "Security"
tags:
  - intrusion-detection
  - iot
  - edge-features
  - graphsage
  - graph-neural-networks
  - netflow
  - project/graph-phishing-detection
---

# E-GraphSAGE: A Graph Neural Network based Intrusion Detection System for IoT

## Metadane
- **Autorzy**: Wai Weng Lo, Siamak Layeghy, Mohanad Sarhan, Marcus Gallagher, Marius Portmann (The University of Queensland)
- **Rok**: 2021 (publikacja IEEE/IFIP NOMS 2022)
- **Źródło**: arXiv preprint (cs.NI); IEEE/IFIP Network Operations and Management Symposium
- **DOI/Link**: https://arxiv.org/abs/2103.16329 (`#IDS`, `#IoT`, `#edge-classification`)
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca przedstawia nowy system wykrywania włamań sieciowych (NIDS) oparty na grafowych sieciach neuronowych (GNN), ukierunkowany na sieci IoT. Dane treningowe i ewaluacyjne dla NIDS są zwykle reprezentowane jako rekordy przepływów (flow records, np. NetFlow), identyfikowane przez punkty końcowe komunikacji (adres IP, port L4, protokół) i opatrzone polami przepływu (liczba pakietów, bajtów, czas trwania). Takie dane naturalnie reprezentują się jako graf: punkty końcowe to węzły, a przepływy ruchu to krawędzie. Autorzy argumentują, że dotychczasowe metody ML traktują rekordy przepływów niezależnie, ignorując ich wzajemne relacje i globalny wzorzec ruchu, przez co słabo wykrywają wyrafinowane ataki rozproszone (botnety, distributed port scans, DNS Amplification).

Proponowany E-GraphSAGE jest rozszerzeniem algorytmu GraphSAGE, które — w odróżnieniu od oryginału — pozwala uchwycić zarówno cechy krawędzi grafu, jak i informację topologiczną, umożliwiając klasyfikację krawędzi (a nie tylko węzłów). To kluczowe, ponieważ w detekcji włamań informacja diagnostyczna znajduje się na krawędziach (przepływach), a nie na węzłach (hostach). Mechanizm propagacji wiadomości agreguje cechy krawędzi sąsiednich, by sklasyfikować dany przepływ jako benign lub złośliwy.

Rozległa ewaluacja na czterech aktualnych zbiorach benchmarkowych NIDS pokazuje, że E-GraphSAGE przewyższa stan techniki w kluczowych metrykach klasyfikacji. Według autorów to pierwsze udane, praktyczne i szeroko ewaluowane zastosowanie GNN do detekcji włamań w IoT na danych przepływowych.

## Kluczowe Wnioski
- Cechy krawędzi (przepływów) są kluczowe dla detekcji włamań — standardowy GraphSAGE ich nie wykorzystuje.
- E-GraphSAGE umożliwia klasyfikację krawędzi przez włączenie cech krawędzi do agregacji.
- Globalny widok topologii pozwala wykrywać ataki rozproszone (botnety, skany portów).
- Przewyższa SOTA na czterech benchmarkach NIDS dla IoT.

## Metodologia
Reprezentacja ruchu sieciowego jako graf: punkty końcowe = węzły, przepływy NetFlow = krawędzie z cechami. Modyfikacja GraphSAGE: funkcje agregacji uwzględniają cechy krawędzi sąsiednich przy propagacji wiadomości, a embeddingi krawędzi powstają z konkatenacji embeddingów węzłów końcowych. Klasyfikacja krawędzi (edge classification) na benign/atak. Ewaluacja na 4 zbiorach NIDS (klasyfikacja binarna i wieloklasowa).

## Główne Koncepcje
- **Edge classification** w GNN (klasyfikacja przepływów)
- **Edge features** włączone do agregacji sąsiedztwa
- **GraphSAGE** i indukcyjna propagacja wiadomości
- **NetFlow** jako graf komunikacji

## Relevancja dla graph-phishing-detection
E-GraphSAGE jest metodologicznie istotny dla projektu, ponieważ pokazuje, jak włączyć bogate cechy krawędzi do GNN i wykonać klasyfikację na poziomie krawędzi — bezpośrednio użyteczne dla grafu wiedzy domenowej, gdzie krawędzie (komunikacja, transakcje) niosą atrybuty. Indukcyjny charakter GraphSAGE wspiera niezmiennik projektu dotyczący generalizacji na nowe węzły. Globalny widok ruchu jako sposób wykrywania ataków rozproszonych jest analogiczny do wykrywania skoordynowanych kampanii phishingowych w grafie komunikacji.
