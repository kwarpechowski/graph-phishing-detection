---
title: "Label Information Enhanced Fraud Detection against Low Homophily in Graphs"
date: 2023-01-01
authors: "Yuchen Wang, Jinghui Zhang, Zhengjie Huang, Weibin Li, Shikun Feng, Ziheng Ma, Yu Sun, Dianhai Yu, Fang Dong, Jiahui Jin, Beilun Wang, Junzhou Luo"
status: read
doi: "10.1145/3543507.3583373"
category: "Security"
tags:
  - fraud-detection
  - low-homophily
  - graph-transformer
  - label-utilization
  - graph-neural-networks
  - project/graph-phishing-detection
---

# Label Information Enhanced Fraud Detection against Low Homophily in Graphs

## Metadane
- **Autorzy**: Yuchen Wang, Jinghui Zhang, Zhengjie Huang, Weibin Li, Shikun Feng, Ziheng Ma, Yu Sun, Dianhai Yu, Fang Dong, Jiahui Jin, Beilun Wang, Junzhou Luo
- **Rok**: 2023 (TheWebConf / WWW 2023)
- **Źródło**: The Web Conference (WWW) 2023
- **DOI/Link**: 10.1145/3543507.3583373
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca dotyczy klasyfikacji wierzchołków w grafowej detekcji oszustw, gdzie typowym problemem jest niska homofilia: węzły oszukańcze celowo łączą się z węzłami legalnymi, by się zamaskować. Większość detektorów GNN nie generalizuje dobrze w warunkach niskiej homofilii, a standardowe metody wykorzystania etykiet (label utilization) są tu mało skuteczne.

Autorzy proponują GAGA (Group AGgregation enhanced TrAnsformer). Kluczowym pomysłem jest agregacja grupowa (group aggregation) — przenośna metoda radzenia sobie z niską homofilią, która jawnie integruje informacje o etykietach, by generować rozróżnialne informacje sąsiedztwa. Wraz z agregacją grupową wprowadzono trenowalne kodowanie grupowe, które wzbogaca oryginalną przestrzeń cech o etykiety klas, a także dwa dodatkowe uczone kodowania rozpoznające kontekst strukturalny i relacyjny. Całość łączona jest w enkoderze typu Transformer ujmującym informacje semantyczne. Wyniki pokazują, że GAGA przewyższa konkurencyjne detektory grafowe nawet o 24,39% na dwóch publicznych zbiorach oraz na rzeczywistym zbiorze przemysłowym z Baidu, a agregacja grupowa bije inne metody wykorzystania etykiet (np. C&S, BoT/UniMP) w ustawieniu niskiej homofilii.

## Kluczowe Wnioski
- Niska homofilia (oszuści łączą się z legalnymi węzłami) degraduje typowe detektory GNN.
- Agregacja grupowa jawnie włącza informacje o etykietach do agregacji sąsiedztwa, poprawiając rozróżnialność.
- Architektura oparta na Transformerze z dodatkowymi kodowaniami strukturalnymi/relacyjnymi ujmuje semantykę wielorelacyjną.
- GAGA poprawia wyniki nawet o 24,39% względem konkurencji na zbiorach publicznych i przemysłowym.

## Metodologia
Group aggregation grupująca sąsiadów wg etykiet klas (z bezpiecznym traktowaniem nieznanych etykiet), trenowalne kodowanie grupowe, kodowania strukturalne i relacyjne, połączone w enkoder Transformer; klasyfikacja wierzchołków oszukańczych. Ewaluacja na dwóch publicznych zbiorach (low-homophily) oraz przemysłowym zbiorze Baidu.

## Główne Koncepcje
- **Niska homofilia (low homophily)**: węzły tej samej klasy rzadko sąsiadują.
- **Group aggregation**: agregacja sąsiadów pogrupowanych wg etykiet.
- **Label utilization**: jawne wykorzystanie etykiet jako cech.
- **Graph Transformer**: enkoder semantyczny dla wielorelacyjnych grafów.

## Relevancja dla graph-phishing-detection
GAGA jest wysoce istotny dla projektu, ponieważ phisherzy i oszuści aktywnie maskują się, łącząc z legalnymi węzłami — dokładnie scenariusz niskiej homofilii w grafie wiedzy domenowej. Mechanizm agregacji grupowej i jawnego wykorzystania etykiet stanowi mocny baseline i inspirację dla detektora projektu, zwłaszcza gdy celem jest pobicie metod proweniencyjnych przy niskim FPR. Wielorelacyjne, oparte na Transformerze ujęcie kontekstu wpisuje się w heterogeniczną naturę grafów phishingowych (domeny, adresy, konta, relacje).
