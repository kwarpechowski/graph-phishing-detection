---
title: "Link Prediction Based on Graph Neural Networks"
date: 2018-01-01
authors: "Muhan Zhang, Yixin Chen"
status: read
doi: "arXiv:1802.09691"
category: "Machine Learning"
tags:
  - link-prediction
  - graph-neural-networks
  - seal
  - enclosing-subgraph
  - heuristics
  - node-labeling
  - project/graph-phishing-detection
---

# Link Prediction Based on Graph Neural Networks

## Metadane
- **Autorzy**: Muhan Zhang, Yixin Chen (Washington University in St. Louis)
- **Rok**: 2018
- **Źródło**: NeurIPS 2018
- **DOI/Link**: arXiv:1802.09691
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca wprowadza SEAL (learning from Subgraphs, Embeddings and Attributes for Link prediction) — ramę predykcji linków opartą na GNN, która zamiast uczyć ustalonej heurystyki, uczy się jej automatycznie z lokalnych podgrafów otaczających parę węzłów. Autorzy formułują teorię γ-decaying heuristic, dowodząc, że szeroka klasa heurystyk wyższego rzędu (Katz, PageRank, SimRank) może być dobrze aproksymowana z lokalnego, h-przeskokowego enklawującego podgrafu (enclosing subgraph), co uzasadnia podejście oparte na małych podgrafach.

Dla każdej kandydującej krawędzi SEAL wycina enklawujący podgraf wokół obu węzłów, znakuje węzły schematem Double-Radius Node Labeling (DRNL) kodującym ich rolę i odległość względem celu, a następnie podaje podgraf (wraz z osadzeniami i atrybutami) do GNN klasyfikującego istnienie krawędzi. Dzięki temu model jednocześnie uczy się heurystyk strukturalnych i wykorzystuje cechy węzłów.

Eksperymenty na wielu sieciach (cytowania, biologiczne, społeczne) pokazują, że SEAL przewyższa zarówno klasyczne heurystyki, jak i metody osadzeniowe (node2vec) oraz wcześniejsze podejścia GNN, ustanawiając silny, uniwersalny baseline predykcji linków.

## Kluczowe Wnioski
- Heurystyki linków można uczyć automatycznie z lokalnych podgrafów (SEAL).
- Teoria γ-decaying: heurystyki wysokiego rzędu aproksymowalne lokalnie.
- DRNL — etykietowanie węzłów po podwójnym promieniu — jest kluczowe.
- SEAL przewyższa heurystyki, node2vec i wcześniejsze GNN.

## Metodologia
Ekstrakcja h-przeskokowego enklawującego podgrafu dla każdej pary węzłów, znakowanie DRNL, opcjonalne osadzenia/atrybuty, klasyfikacja grafu przez DGCNN. Trening na próbkach krawędzi dodatnich i ujemnych. Ewaluacja AUC/AP na zróżnicowanych sieciach.

## Główne Koncepcje
- **Enclosing subgraph** — lokalny podgraf wokół pary węzłów.
- **Double-Radius Node Labeling (DRNL)** — etykietowanie ról węzłów.
- **γ-decaying heuristic theory** — lokalna aproksymacja heurystyk.
- **Subgraph classification** dla predykcji krawędzi.

## Relevancja dla graph-phishing-detection
SEAL to kanoniczny baseline predykcji linków oparty na podgrafach, bezpośrednio użyteczny w projekcie do oceny, czy krawędź (np. domena–nadawca, konto–konto, użytkownik–URL) jest "naturalna" czy anomalna. Podejście subgraph-based jest atrakcyjne dla phishingu, bo lokalna struktura wokół konta atakującego (np. gwiazda jednorazowych transakcji) jest silnie dyskryminacyjna. Łączy się z yan2024topological (które wyjaśnia, kiedy LP zawodzi — niskie TC węzłów-ataków) oraz z domenowymi metodami na Ethereum (zhang2021mcgc, yu2023streaming). W projekcie stanowi punkt odniesienia dla metod opartych na grafie multipleksowym i temporalnym.
