---
title: "Adversarial Attacks on Neural Networks for Graph Data"
date: 2018-01-01
authors: "Daniel Zügner, Amir Akbarnejad, Stephan Günnemann"
status: to-read
tags: []
---
# Adversarial Attacks on Neural Networks for Graph Data

## Metadane
- **Autorzy**: Daniel Zügner, Amir Akbarnejad, Stephan Günnemann
- **Rok**: 2018
- **Źródło**: SIGKDD 2018
- **Status**: to-read
- **Pochodzenie**: Wyekstrahowane z xu-edog-adversarial-2023
- **Tagi**: #to-read #reference #gnn-attack #nettack #greedy-approximation

## Streszczenie

Propozycja Nettack - greedy approximation attack targeting na pojedyncze węzły w GNN. Definiuje equivalency indicator: całkowita liczba zmienionych krawędzi i node features jest bounded. Rozwija prostą aproksymację modelu GNN na której można analitycznie rozwiązać problem optymalizacji.

Multi-edge direct attack i multi-edge indirect attack pochodzą z tej pracy - liczba adversarial edges ≤ degree(target node).

## Kluczowe Wnioski

- Greedy approximation jako alternatywa dla RL-based attacks
- Wprowadzenie bounded perturbation model
- Rozróżnienie direct vs indirect attacks (czy edges łączą się z target node)
- Analityczne rozwiązanie na simplified GNN surrogate model

## Notatki

*Publikacja dodana automatycznie z bibliografii. Definiuje multi-edge direct i indirect attacks - dwa z czterech typów wykrywanych przez EDoG.*

**Relevancja dla xu-edog-adversarial-2023**:
- Multi-edge direct: EDoG osiąga 0.755 AUC (bez wiedzy o attack), OutlierDetect >0.9 dla high-degree nodes
- Multi-edge indirect: EDoG osiąga 0.829 AUC, GraphGenDetect działa najlepiej
