---
title: "Representation Learning for Attributed Multiplex Heterogeneous Network"
date: 2019-01-01
authors: "Yukuo Cen, Xu Zou, Jianwei Zhang, Hongxia Yang, Jingren Zhou, Jie Tang"
status: read
doi: "10.1145/3292500.3330964"
category: "Machine Learning"
tags:
  - network-embedding
  - multiplex-heterogeneous-network
  - graph-representation-learning
  - inductive-learning
  - attention-mechanism
  - link-prediction
  - project/graph-phishing-detection
---

# Representation Learning for Attributed Multiplex Heterogeneous Network

## Metadane
- **Autorzy**: Yukuo Cen, Xu Zou, Jianwei Zhang, Hongxia Yang, Jingren Zhou, Jie Tang (Tsinghua / Alibaba DAMO)
- **Rok**: 2019
- **Źródło**: KDD '19 (ACM SIGKDD) / arXiv:1905.01669
- **DOI/Link**: https://doi.org/10.1145/3292500.3330964
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca formalizuje problem uczenia reprezentacji (network embedding) dla atrybutowanych multipleksowych sieci heterogenicznych (AMHEN) — sieci, w których węzły mają wiele typów, krawędzie wiele typów (multipleks), a węzły mają bogate atrybuty. Autorzy klasyfikują sześć typów sieci (HON, AHON, HEN, AHEN, MHEN, AMHEN) i wskazują, że AMHEN — najbliższy realnym aplikacjom (np. e-commerce) — był najsłabiej zbadany. Wyzwania: krawędzie multipleksowe (wiele relacji między tą samą parą), częściowa obserwacja (problem cold-start/long-tail) oraz skalowalność (miliardy węzłów/krawędzi).

Proponowany framework GATNE (General Attributed Multiplex HeTerogeneous Network Embedding) dzieli embedding węzła na: base embedding (współdzielony między typami krawędzi), edge embedding (agregowany z sąsiadów per typ relacji, w stylu GraphSAGE z mean/max-pooling) oraz — w wariancie indukcyjnym — attribute embedding. Wagi łączące embeddingi różnych typów krawędzi liczone są mechanizmem self-attention. Występują dwa warianty: GATNE-T (transdukcyjny, tylko struktura) i GATNE-I (indukcyjny, struktura + atrybuty, radzi sobie z niewidzianymi węzłami). Autorzy dowodzą teoretycznie, że GATNE-T jest ogólniejszą formą modelu MNE. Uczenie: meta-path random walk + heterogeniczny skip-gram z negative samplingiem.

Ewaluacja (predykcja krawędzi) na czterech zbiorach (Amazon, YouTube, Twitter, Alibaba) pokazuje istotne statystycznie poprawy F1 o 5,99–28,23% (p≪0,01) nad SOTA. Model wdrożono w systemie rekomendacyjnym Alibaba (testy offline A/B: +3,26% hit-rate nad MNE, +24,26% nad DeepWalk); skaluje się do >40 mln węzłów i >500 mln krawędzi.

## Kluczowe Wnioski
- AMHEN (multipleks + heterogeniczność + atrybuty) lepiej oddaje realne sieci niż prostsze modele; daje znaczne zyski na predykcji krawędzi.
- GATNE rozdziela embedding na base/edge/attribute i łączy typy relacji przez self-attention.
- GATNE-I (indukcyjny) radzi sobie z niewidzianymi węzłami (cold-start) i przewyższa wariant transdukcyjny na dużych, bogato atrybutowanych zbiorach.
- Skalowalność do miliardów krawędzi i realne wdrożenie produkcyjne (Alibaba).

## Metodologia
Network embedding oparty na meta-path random walk + heterogeniczny skip-gram z heterogenicznym negative samplingiem. Agregacja sąsiadów (mean/max-pooling) per typ krawędzi, self-attention łączące widoki, transformacje atrybutów (MLP/liniowe) w wariancie indukcyjnym. Ewaluacja: ROC-AUC, PR-AUC, F1 na predykcji krawędzi; analiza zbieżności, skalowalności, wrażliwości parametrów; testy A/B.

## Główne Koncepcje
- **AMHEN**: atrybutowana multipleksowa sieć heterogeniczna (wiele typów węzłów/krawędzi + atrybuty).
- **Base/edge/attribute embedding**: dekompozycja reprezentacji węzła; base współdzielony, edge per typ relacji.
- **Self-attention nad typami krawędzi**: ważenie wkładu różnych relacji do embeddingu.
- **Uczenie transdukcyjne vs indukcyjne**: GATNE-T (stałe węzły) vs GATNE-I (uogólnia na nowe węzły z atrybutów).

## Relevancja dla graph-phishing-detection
GATNE to jeden z fundamentalnych modeli embeddingu multipleksowego, bezpośrednio relevantny dla rdzenia projektu (P1 multipleks, P2 uczony GNN + indukcja). Architektura (base+edge embedding, self-attention nad typami relacji, wariant indukcyjny) jest niemal gotowym wzorcem do modelowania grafów phishingowych, gdzie relacje komunikacja/domena/transakcje stanowią warstwy multipleksu, a nowe domeny/konta wymagają indukcji (cold-start). Dla projektu kluczowy jest wątek indukcyjnego uogólniania na niewidziane węzły — istotny wobec ciągłego pojawiania się nowych domen phishingowych — oraz wykorzystanie atrybutów węzłów. GATNE jest naturalnym, silnym baseline'em (obok ANOMULY z behrouz2022anomaly) przy ocenie uczonych modeli grafowych na predykcji krawędzi/detekcji, mierzonej ROC-AUC/PR-AUC, którą projekt rozszerza o leak-aware Recall@FPR1%.
