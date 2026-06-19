---
title: "A Topological Perspective on Demystifying GNN-Based Link Prediction Performance"
date: 2024-01-01
authors: "Yu Wang, Tong Zhao, Yuying Zhao, Yunchao Liu, Xueqi Cheng, Neil Shah, Tyler Derr"
status: read
doi: "arXiv:2310.04612"
category: "Theory"
tags:
  - link-prediction
  - graph-neural-networks
  - topology
  - degree-bias
  - common-neighbors
  - node-embedding
  - project/graph-phishing-detection
---

# A Topological Perspective on Demystifying GNN-Based Link Prediction Performance

## Metadane
- **Autorzy**: Yu Wang, Yuying Zhao, Yunchao Liu, Xueqi Cheng, Tyler Derr (Vanderbilt University), Tong Zhao, Neil Shah (Snap Inc.)
- **Rok**: 2024
- **Źródło**: ICLR 2024
- **DOI/Link**: arXiv:2310.04612 — https://arxiv.org/abs/2310.04612
- **Status**: read
- **Kategoria główna**: Theory

## Streszczenie
Artykuł analizuje, dlaczego GNN do predykcji linków (LP) osiągają nierównomierną skuteczność dla różnych węzłów, i wyjaśnia to z perspektywy topologicznej. Autorzy pokazują, że globalna metryka skuteczności LP maskuje silne dysproporcje na poziomie pojedynczych węzłów — niektóre węzły mają systematycznie niedoszacowane prawdopodobieństwa krawędzi.

Wprowadzają miarę Topological Concentration (TC) opisującą, jak bardzo lokalna podstruktura wspólnych sąsiadów węzła koncentruje się wokół jego rzeczywistych połączeń. Wykazują, że TC silnie koreluje ze skutecznością LP — lepiej niż stopień węzła — i że istnieje zjawisko podobne do degree bias: węzły o niskiej koncentracji topologicznej są obsługiwane gorzej. Proponują przybliżenie (Approximated TC) redukujące koszt obliczeniowy oraz metodę re-ważenia/wzbogacania uczenia, poprawiającą skuteczność dla węzłów "trudnych" bez degradacji pozostałych.

Eksperymenty na standardowych benchmarkach LP potwierdzają, że TC tłumaczy wariancję skuteczności i że interwencje topologiczne dają wzrost zwłaszcza w "ogonie" rozkładu.

## Kluczowe Wnioski
- Globalna metryka LP ukrywa dużą wariancję skuteczności per węzeł.
- Topological Concentration (TC) wyjaśnia skuteczność lepiej niż stopień.
- Istnieje topologiczny bias analogiczny do degree bias.
- Re-ważenie/wzbogacanie oparte o TC poprawia węzły o niskiej koncentracji.

## Metodologia
Analiza teoretyczno-empiryczna: definicja TC na bazie nakładania się sąsiedztw, korelacja TC vs metryki LP (Hits@K) na poziomie węzła, aproksymacja TC dla skalowalności oraz interwencje treningowe podnoszące skuteczność węzłów o niskim TC. Ewaluacja na grafach cytowań i sieciach społecznych.

## Główne Koncepcje
- **Topological Concentration (TC)** — koncentracja wspólnych sąsiadów.
- **Degree-related / topological bias** w predykcji linków.
- **Per-node performance disparity** — nierówność skuteczności.
- **Common neighbors** jako sygnał strukturalny LP.

## Relevancja dla graph-phishing-detection
Detekcja phishingu na grafie często sprowadza się do oceny anomalnych krawędzi (czy krawędź domena–nadawca lub konto–konto jest legalna). Praca tłumaczy, dla których węzłów predykcja linków będzie zawodna — co jest krytyczne dla phishingu, bo konta atakujące mają zwykle nietypową, rzadką topologię (mało wspólnych sąsiadów z ofiarą), czyli niskie TC. Sugeruje to, że naiwne LP będzie systematycznie gorsze właśnie dla węzłów-ataków. Dla projektu daje to diagnostykę słabości modeli SEAL/link-pred (zhang2018link) na rzadkich węzłach, uzasadnienie metryk per-segment (Recall@FPR1%) zamiast globalnych oraz inspirację do wzbogacania topologii węzłów o niskiej koncentracji.
