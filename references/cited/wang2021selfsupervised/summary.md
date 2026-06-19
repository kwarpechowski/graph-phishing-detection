---
title: "Self-supervised Heterogeneous Graph Neural Network with Co-contrastive Learning"
date: 2021-01-01
authors: "Xiao Wang, Nian Liu, Hui Han, Chuan Shi"
status: read
doi: "10.1145/3447548.3467415"
category: "Machine Learning"
tags:
  - heterogeneous-graph
  - self-supervised-learning
  - contrastive-learning
  - graph-neural-networks
  - node-embedding
  - project/graph-phishing-detection
---

# Self-supervised Heterogeneous Graph Neural Network with Co-contrastive Learning

## Metadane
- **Autorzy**: Xiao Wang, Nian Liu, Hui Han, Chuan Shi
- **Rok**: 2021 (KDD 2021)
- **Źródło**: ACM SIGKDD 2021; arXiv:2105.09111
- **DOI/Link**: 10.1145/3447548.3467415
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca podejmuje problem braku etykiet w heterogenicznych sieciach neuronowych (HGNN). Większość HGNN działa w trybie pół-nadzorowanym, co ogranicza ich stosowalność, ponieważ etykiety są w praktyce kosztowne i rzadkie. Autorzy proponują HeCo — samonadzorowany model HGNN oparty na nowym mechanizmie współ-kontrastywnego uczenia (co-contrastive learning).

HeCo wykorzystuje dwa komplementarne widoki tej samej sieci heterogenicznej: widok schematu sieci (network schema) oraz widok ścieżek meta (meta-path). Pierwszy ujmuje lokalną strukturę i bezpośrednich sąsiadów różnych typów, drugi — struktury wyższego rzędu. Mechanizm uczenia kontrastywnego między widokami (cross-view), wraz z mechanizmem maskowania widoku (view mask), pozwala obu widokom wzajemnie się nadzorować i uczyć wysokopoziomowych osadzeń wierzchołków bez etykiet. Zaproponowano też dwa rozszerzenia generujące trudniejsze (high-quality) próbki negatywne, co dodatkowo poprawia wyniki. Eksperymenty na rzeczywistych sieciach pokazują przewagę HeCo nad metodami SOTA.

## Kluczowe Wnioski
- Samonadzorowane uczenie kontrastywne umożliwia trening HGNN bez kosztownych etykiet.
- Dwa widoki (schemat sieci + ścieżki meta) ujmują struktury lokalne i wyższego rzędu jednocześnie.
- Współ-kontrastywny mechanizm cross-view pozwala widokom wzajemnie się nadzorować.
- Generowanie trudniejszych próbek negatywnych dodatkowo zwiększa jakość osadzeń.

## Metodologia
Dwa enkodery widoków (schemat sieci i ścieżki meta) generują osadzenia tego samego wierzchołka; strata kontrastywna cross-view zbliża pozytywne pary i oddala negatywne; mechanizm maskowania widoku wymusza komplementarność; rozszerzenia do doboru trudnych negatywów. Ewaluacja na klasyfikacji i klastrowaniu wierzchołków.

## Główne Koncepcje
- **Co-contrastive learning**: wzajemne nadzorowanie dwóch widoków grafu.
- **Widok schematu sieci vs widok ścieżek meta**: lokalna vs wysokorzędowa struktura.
- **View mask**: maskowanie wymuszające różnorodność widoków.
- **Trudne próbki negatywne**: poprawa jakości kontrastu.

## Relevancja dla graph-phishing-detection
HeCo jest kluczowy dla projektu, ponieważ rzeczywiste dane phishingowe cierpią na niedobór etykiet (oznaczanie BEC/phishingu jest kosztowne i opóźnione). Samonadzorowane uczenie reprezentacji na grafie heterogenicznym (domeny, adresy, konta, transakcje) pozwala uczyć użyteczne osadzenia z dużych nieoznakowanych grafów, a następnie dostrajać mały klasyfikator na nielicznych etykietach. Podejście cross-view i ścieżki meta wpisują się wprost w graf wiedzy domenowej projektu i mogą poprawiać metryki przy ekstremalnej rzadkości etykiet (np. Recall@FPR).
