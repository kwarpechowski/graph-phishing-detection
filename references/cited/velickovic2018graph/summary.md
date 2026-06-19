---
title: "Graph Attention Networks"
date: 2018-01-01
authors: "Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Liò, Yoshua Bengio"
status: read
doi: "arXiv:1710.10903"
category: "Machine Learning"
tags:
  - graph-neural-networks
  - attention
  - node-classification
  - inductive-learning
  - representation-learning
  - project/graph-phishing-detection
---

# Graph Attention Networks

## Metadane
- **Autorzy**: Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Liò, Yoshua Bengio
- **Rok**: 2018 (ICLR)
- **Źródło**: International Conference on Learning Representations (ICLR) 2018; arXiv:1710.10903
- **DOI/Link**: arXiv:1710.10903
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Artykuł wprowadza Graph Attention Networks (GAT) — architekturę sieci neuronowych operującą na danych grafowych za pomocą maskowanych warstw samo-uwagi (self-attention). W odróżnieniu od wcześniejszych metod opartych na splotach spektralnych, GAT pozwala każdemu wierzchołkowi przypisywać różne wagi swoim sąsiadom, ucząc implicytnie znaczenia poszczególnych relacji. Operacja nie wymaga kosztownych działań macierzowych (np. odwracania) ani znajomości całej struktury grafu z góry.

Dzięki temu GAT rozwiązuje kilka kluczowych ograniczeń podejść spektralnych jednocześnie i jest stosowalny zarówno w trybie transdukcyjnym, jak i indukcyjnym (uogólnianie na całkowicie nowe grafy nieobecne podczas treningu). Operacja uwagi jest równoległa po parach wierzchołek-sąsiad i radzi sobie z wierzchołkami o różnym stopniu. Modele GAT osiągnęły lub dorównały wynikom state-of-the-art na czterech benchmarkach: sieciach cytowań Cora, Citeseer i Pubmed (transdukcja) oraz na zbiorze interakcji białko-białko (indukcja).

## Kluczowe Wnioski
- Mechanizm uwagi pozwala uczyć zróżnicowane wagi sąsiadów bez znajomości pełnej struktury grafu.
- GAT działa indukcyjnie — uogólnia na nowe, niewidziane grafy.
- Operacja jest wydajna i zrównoleglona, niezależna od kosztownych operacji spektralnych.
- Osiąga wyniki SOTA na Cora, Citeseer, Pubmed oraz PPI.

## Metodologia
Warstwa GAT oblicza ukryte reprezentacje wierzchołka przez uwagę nad jego sąsiadami: współczynniki uwagi wyznaczane są przez wspólny mechanizm (przekształcenie liniowe + LeakyReLU + softmax), z możliwością użycia wielogłowicowej uwagi (multi-head attention) dla stabilizacji. Ewaluacja na zadaniach klasyfikacji wierzchołków w trybie transdukcyjnym i indukcyjnym.

## Główne Koncepcje
- **Self-attention na grafie**: ważenie wkładu sąsiadów wierzchołka.
- **Multi-head attention**: wiele równoległych mechanizmów uwagi.
- **Uczenie indukcyjne vs transdukcyjne**: uogólnianie na nowe grafy.
- **Niezależność od struktury spektralnej**: brak zależności od bazy własnej Laplasjanu.

## Relevancja dla graph-phishing-detection
GAT to fundamentalna architektura, na której opierają się rozszerzenia heterogeniczne (HAN, HeCo) wykorzystywane w projekcie. Mechanizm uwagi dla wierzchołków jest bezpośrednio użyteczny w grafach komunikacyjnych i domenowych do detekcji phishingu: pozwala modelowi automatycznie wagować, które połączenia (np. nadawca-odbiorca, domena-adres) są istotne dla wykrycia oszustwa. Indukcyjność GAT jest kluczowa dla detekcji w warunkach ciągłego napływu nowych węzłów (nowe domeny, konta), co jest typowe dla scenariuszy phishingowych i grafu wiedzy domenowej.
