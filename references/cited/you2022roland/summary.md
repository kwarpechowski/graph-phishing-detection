---
title: "ROLAND: Graph Learning Framework for Dynamic Graphs"
date: 2022-01-01
authors: "Jiaxuan You, Tianyu Du, Jure Leskovec"
status: read
doi: "10.1145/3534678.3539300"
category: "Machine Learning"
tags:
  - dynamic-graphs
  - graph-neural-networks
  - temporal-learning
  - live-update
  - hierarchical-state
  - incremental-training
  - project/graph-phishing-detection
---

# ROLAND: Graph Learning Framework for Dynamic Graphs

## Metadane
- **Autorzy**: Jiaxuan You, Tianyu Du, Jure Leskovec (Stanford University)
- **Rok**: 2022
- **Źródło**: KDD 2022
- **DOI/Link**: https://doi.org/10.1145/3534678.3539300
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
ROLAND to ogólny framework, który pozwala ponownie użyć dowolnej statycznej architektury GNN do uczenia na grafach dynamicznych przy minimalnych zmianach. Kluczowa idea: osadzenia węzłów na każdej warstwie GNN traktuje się jako stany hierarchiczne (hierarchical node states), które są aktualizowane w czasie wraz z napływem nowych migawek grafu, zamiast przeliczać model od zera.

Drugi wkład to schemat ewaluacji "live-update": model jest oceniany w sposób przyrostowy, dla każdej kolejnej migawki przewiduje przyszłe krawędzie, a następnie aktualizuje swoje stany — co realistycznie oddaje wdrożenie produkcyjne na strumieniu grafu. Trzeci wkład to skalowalna procedura treningu inkrementalnego (meta-learning / kroczące okno), która utrzymuje wydajność pamięciową przy długich strumieniach.

Eksperymenty na dużych dynamicznych grafach transakcyjnych i społecznych pokazują, że ROLAND z prostymi backbone'ami GCN/GraphSAGE przewyższa dedykowane modele dynamiczne (EvolveGCN, TGCN) w predykcji przyszłych krawędzi, oferując przy tym prostotę i skalowalność.

## Kluczowe Wnioski
- Dowolny statyczny GNN można rozszerzyć do dynamicznego przez stany hierarchiczne.
- Ewaluacja "live-update" lepiej oddaje realistyczne wdrożenie strumieniowe.
- Trening inkrementalny utrzymuje skalowalność na długich strumieniach.
- ROLAND przewyższa dedykowane modele dynamiczne mimo prostoty.

## Metodologia
Każda warstwa GNN ma moduł aktualizacji stanu (np. GRU/moving average) łączący osadzenie z poprzedniej migawki z nowo obliczonym. Predykcja przyszłych krawędzi po każdej migawce; trening kroczącym oknem z fine-tuningiem inkrementalnym. Backbone'y: GCN, GraphSAGE, GIN. Ewaluacja MRR na predykcji linków przyszłych.

## Główne Koncepcje
- **Hierarchical node states** — stany osadzeń na każdej warstwie.
- **Live-update evaluation** — przyrostowa ocena strumienia.
- **Incremental training** — kroczące okno, oszczędność pamięci.
- **Snapshot-based dynamic graph (DTDG)** — graf jako sekwencja migawek.

## Relevancja dla graph-phishing-detection
ROLAND jest centralnym wzorcem architektonicznym dla projektu: pozwala przekształcić statyczny GNN na grafie multipleksowym phishingu w model dynamiczny bez budowy nowej architektury. Paradygmat "live-update" odpowiada dokładnie scenariuszowi operacyjnemu detekcji — strumień zdarzeń (nowe e-maile, transakcje, rejestracje domen) ocenianych na bieżąco, z aktualizacją stanu zamiast retreningu. Razem z TGAT (xu2020inductive) i EvolveGCN tworzy zestaw baseline'ów temporalnych dla modelowania ewolucji kampanii phishingowych; jego inkrementalność jest kluczowa wobec dryfu konceptu (nowe taktyki ataków) opisanego w planie P3 rozprawy.
