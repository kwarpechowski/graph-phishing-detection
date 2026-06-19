---
title: "Adversarial Attacks on Graph Neural Networks via Meta Learning"
date: 2019-01-01
authors: "Daniel Zügner, Stephan Günnemann"
status: to-read
tags: []
---
# Adversarial Attacks on Graph Neural Networks via Meta Learning

## Metadane
- **Autorzy**: Daniel Zügner, Stephan Günnemann
- **Rok**: 2019
- **Źródło**: ICLR 2019
- **Status**: to-read
- **Pochodzenie**: Wyekstrahowane z xu-edog-adversarial-2023
- **Tagi**: #to-read #reference #meta-attack #global-attack #meta-learning

## Streszczenie

Meta attack - globalne ataki na GNN które nie targetują pojedynczego węzła, ale całego grafu. Cel: zmaksymalizować błędy klasyfikacji na całym zbiorze węzłów V_atk. Pozwala na dodanie do 5% liczby krawędzi. Aproksymuje gradient adjacency matrix aby umożliwić gradient-based optimization.

Różni się od Nettack tym że nie jest local attack - nie ma single target node, tylko zbiór węzłów do zaatakowania.

## Kluczowe Wnioski

- Global attack vs local (single-node) attacks
- Meta-learning approach do adversarial attacks
- Gradient approximation dla discrete adjacency matrix
- 5% perturbation budget - najwięcej spośród rozważanych ataków
- Może zawierać mix różnych typów malicious edges

## Notatki

*Publikacja dodana automatycznie z bibliografii. Definiuje meta attack - czwarty typ ataku wykrywany przez EDoG.*

**Relevancja dla xu-edog-adversarial-2023**:
- Najtrudniejszy attack do wykrycia - EDoG osiąga 0.728 AUC (średnio)
- Mix różnych typów edges wymaga ensemble approach (pełny EDoG pipeline)
- Implementation dostępna: https://github.com/danielzuegner/gnn-meta-attack
