---
title: "Heterogeneous Graph Transformer"
date: 2020-01-01
authors: "Ziniu Hu, Yuxiao Dong, Kuansan Wang, Yizhou Sun"
status: read
doi: "10.1145/3366423.3380027"
category: "Machine Learning"
tags:
  - heterogeneous-graphs
  - graph-neural-networks
  - transformer
  - attention
  - temporal-graphs
  - project/graph-phishing-detection
---

# Heterogeneous Graph Transformer

## Metadane
- **Autorzy**: Ziniu Hu, Yuxiao Dong, Kuansan Wang, Yizhou Sun
- **Rok**: 2020
- **Źródło**: The Web Conference (WWW) 2020
- **DOI/Link**: https://doi.org/10.1145/3366423.3380027
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Heterogeneous Graph Transformer (HGT) to architektura sieci neuronowej dla grafów heterogenicznych — takich, w których występuje wiele typów węzłów i wiele typów relacji (np. autor-publikacja-konferencja). HGT modeluje heterogeniczność za pomocą mechanizmu uwagi (attention) zależnego od typu: dla każdej krawędzi parametry transformacji zależą od typu węzła źródłowego, typu węzła docelowego i typu relacji. Pozwala to uczyć osobne wzorce komunikacji dla różnych metarelacji bez ręcznego definiowania metaścieżek (meta-paths).

Dodatkowo HGT wprowadza kodowanie czasu względnego (relative temporal encoding, RTE), które pozwala modelować dynamiczne grafy heterogeniczne, gdzie krawędzie pojawiają się w różnych momentach. Dla skalowalności autorzy proponują algorytm próbkowania podgrafów HGSampling, utrzymujący zbalansowane typy węzłów. HGT osiąga znaczącą poprawę nad wcześniejszymi GNN na dużym akademickim grafie (Open Academic Graph) w zadaniach klasyfikacji i predykcji krawędzi.

## Kluczowe Wnioski
- Uwaga zależna od typu (meta-relacji) lepiej oddaje heterogeniczność niż wspólne wagi.
- Metaścieżki nie są konieczne — model uczy się ich pośrednio.
- Relative Temporal Encoding pozwala obsłużyć dynamiczne grafy heterogeniczne.
- HGSampling umożliwia trening na grafach o skali milionów węzłów.

## Metodologia
Każda warstwa HGT oblicza uwagę heterogeniczną (Heterogeneous Mutual Attention), agregację heterogeniczną i aktualizację specyficzną dla typu docelowego, parametryzując projekcje per typ węzła/relacji. Czas krawędzi kodowany jest jako RTE dodawane do reprezentacji źródła. Ewaluacja na Open Academic Graph z porównaniem do GCN, GAT, RGCN, HAN i innych.

## Główne Koncepcje
- **Graf heterogeniczny** — wiele typów węzłów i relacji.
- **Heterogeneous attention** — parametry uwagi zależne od metarelacji.
- **Relative Temporal Encoding** — modelowanie czasu krawędzi.
- **HGSampling** — skalowalne próbkowanie podgrafów.

## Relevancja dla graph-phishing-detection
Grafy w detekcji phishingu są z natury heterogeniczne: węzły to nadawcy, odbiorcy, domeny, adresy URL, załączniki, transakcje, a relacje mają różne typy (wysłał-do, należy-do-domeny, linkuje-do). HGT dostarcza gotowy szkielet do modelowania takiego grafu wiedzy domenowej bez ręcznych metaścieżek, a RTE bezpośrednio wspiera multipleks-temporalne podejście projektu (krawędzie komunikacji ewoluują w czasie). Uwaga zależna od typu relacji może wzmocnić rozróżnianie legalnych i impersonujących ścieżek, a HGSampling daje ścieżkę skalowania uczonego GNN na realne korporacyjne wolumeny (cel P2/P3).
