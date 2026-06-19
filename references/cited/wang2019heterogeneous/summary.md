---
title: "Heterogeneous Graph Attention Network"
date: 2019-01-01
authors: "Xiao Wang, Houye Ji, Chuan Shi, Bai Wang, Peng Cui, Philip S. Yu, Yanfang Ye"
status: read
doi: "arXiv:1903.07293"
category: "Machine Learning"
tags:
  - heterogeneous-graph
  - graph-neural-networks
  - attention
  - meta-path
  - node-embedding
  - project/graph-phishing-detection
---

# Heterogeneous Graph Attention Network

## Metadane
- **Autorzy**: Xiao Wang, Houye Ji, Chuan Shi, Bai Wang, Peng Cui, Philip S. Yu, Yanfang Ye
- **Rok**: 2019 (WWW 2019)
- **Źródło**: The Web Conference (WWW) 2019; arXiv:1903.07293
- **DOI/Link**: arXiv:1903.07293
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Artykuł wprowadza Heterogeneous Graph Attention Network (HAN) — sieci neuronowe dla grafów heterogenicznych zawierających różne typy wierzchołków i krawędzi (heterogeneous information network, HIN). Autorzy zauważają, że klasyczny GAT obsługuje jedynie grafy homogeniczne, podczas gdy rzeczywiste dane (sieci społecznościowe, bibliograficzne, filmowe) są heterogeniczne i niosą bogatą semantykę wyrażaną przez ścieżki meta (meta-paths).

HAN wprowadza hierarchiczny mechanizm uwagi złożony z dwóch poziomów: uwaga na poziomie wierzchołka (node-level) uczy ważności między wierzchołkiem a jego sąsiadami zdefiniowanymi przez daną ścieżkę meta, natomiast uwaga na poziomie semantycznym (semantic-level) uczy ważności różnych ścieżek meta. Dzięki temu model agreguje cechy w sposób hierarchiczny, generując osadzenia wierzchołków uwzględniające zarówno znaczenie pojedynczych sąsiadów, jak i całych typów relacji. Eksperymenty na trzech rzeczywistych grafach heterogenicznych pokazały przewagę HAN nad metodami SOTA oraz dobrą interpretowalność dzięki wagom uwagi.

## Kluczowe Wnioski
- Grafy heterogeniczne wymagają modelowania rozlicznych typów wierzchołków i relacji — klasyczny GAT jest niewystarczający.
- Hierarchiczna uwaga (poziom wierzchołka + poziom semantyczny) skutecznie agreguje informacje z różnych ścieżek meta.
- Wagi uwagi zapewniają interpretowalność: pokazują, które ścieżki meta i którzy sąsiedzi są najistotniejsi.
- HAN przewyższa metody bazowe na trzech rzeczywistych zbiorach danych.

## Metodologia
Definicja ścieżek meta łączących wierzchołki przez pośrednie typy; agregacja sąsiadów opartych na ścieżkach meta z uwagą na poziomie wierzchołka; następnie łączenie osadzeń z różnych ścieżek meta z uwagą semantyczną. Trening w trybie pół-nadzorowanym; ewaluacja na klasyfikacji i klastrowaniu wierzchołków.

## Główne Koncepcje
- **Heterogeneous Information Network (HIN)**: graf z wieloma typami wierzchołków/krawędzi.
- **Meta-path (ścieżka meta)**: złożona relacja opisująca semantykę (np. Movie-Actor-Movie).
- **Uwaga node-level i semantic-level**: dwupoziomowa hierarchia uwagi.
- **Osadzenia wierzchołków**: reprezentacje uwzględniające heterogeniczność.

## Relevancja dla graph-phishing-detection
HAN jest bezpośrednim wzorcem architektonicznym dla projektu, który modeluje phishing jako graf heterogeniczny / wiedzy domenowej (węzły: e-maile, domeny, adresy, konta, transakcje; różne typy relacji). Mechanizm ścieżek meta pozwala uchwycić semantyczne wzorce oszustwa (np. domena-rejestrator-domena, adres-transakcja-adres), a uwaga semantyczna automatycznie wagować, które typy powiązań są diagnostyczne dla phishingu. Interpretowalność wag uwagi jest wartościowa dla wyjaśnialnej detekcji oszustw.
