---
title: "SNAP Datasets: Stanford Large Network Dataset Collection"
date: 2014-01-01
authors: "Jure Leskovec, Andrej Krevl"
status: to-read
doi: "http://snap.stanford.edu/data"
category: "Data Science"
tags:
  - dataset-collection
  - network-datasets
  - benchmark
  - graph-data
  - meta-resource
  - project/graph-phishing-detection
---

# SNAP Datasets: Stanford Large Network Dataset Collection

> **Uwaga (META):** To nie jest klasyczna praca naukowa, lecz kolekcja zbiorów danych (SNAP — Stanford Network Analysis Project). Wpis ma charakter META i odsyła do repozytorium danych. Brak dołączonego PDF; status ustawiony na **to-read** (zasób do przejrzenia/wykorzystania jako źródło danych).

## Metadane
- **Autorzy**: Jure Leskovec, Andrej Krevl (Stanford University)
- **Rok**: 2014
- **Źródło**: Stanford Network Analysis Project (SNAP), zasób online
- **DOI/Link**: http://snap.stanford.edu/data
- **Status**: to-read
- **Kategoria główna**: Data Science

## Streszczenie
SNAP Datasets to obszerna, publicznie dostępna kolekcja dużych zbiorów danych sieciowych utrzymywana przez Stanford Network Analysis Project. Kolekcja gromadzi setki grafów z różnych domen: sieci społecznościowe (np. ego-sieci, sieci znajomości), sieci komunikacji i e-mail, grafy cytowań i współautorstwa, sieci WWW i hiperłączy, grafy zakupów i recenzji, sieci drogowe, sieci autonomicznych systemów internetowych, grafy temporalne i wiele innych. Zbiory są standardowym punktem odniesienia (benchmarkiem) w badaniach nad analizą sieci i grafowymi sieciami neuronowymi.

Kolekcja jest powiązana z biblioteką SNAP (C++/Python) służącą do analizy i manipulacji dużymi grafami. Cytowanie `\citep{leskovec2014snap}` jest standardowym sposobem odwołania się do źródła pochodzenia danych wykorzystanych w eksperymentach.

## Kluczowe Wnioski
- Standaryzowane, powtarzalne źródło dużych grafów do benchmarkingu metod sieciowych i GNN.
- Pokrywa wiele domen, w tym sieci komunikacji/e-mail i grafy temporalne istotne dla cyberbezpieczeństwa.
- Dane często wykorzystywane do ewaluacji skalowalności i jakości metod grafowych.

## Metodologia
Nie dotyczy w sensie pojedynczego badania — jest to repozytorium danych. Zbiory różnią się sposobem pozyskania (logi, scraping, publiczne dumpy), formatem (listy krawędzi, grafy z atrybutami) oraz właściwościami (statyczne vs. temporalne, jedno- vs. heterogeniczne).

## Główne Koncepcje
- **Kolekcja zbiorów danych sieciowych** (benchmark).
- **Grafy temporalne i komunikacyjne** dostępne w repozytorium.
- **Biblioteka SNAP** do analizy dużych grafów.

## Relevancja dla graph-phishing-detection
SNAP dostarcza realne grafy komunikacji i e-mail (np. sieci e-mailowe instytucji, grafy temporalne) oraz duże grafy heterogeniczne, które mogą posłużyć jako tło, dane do pretreningu samonadzorowanego lub jako negatywne/benigne struktury w eksperymentach detekcji phishingu. Standaryzowane benchmarki ze SNAP wspierają porównywalność i rygor ewaluacji (w tym leak-aware), a grafy temporalne wpisują się w multipleks-temporalne podejście projektu. Wpis należy traktować jako źródło danych do dalszego przeglądu i selekcji konkretnych zbiorów.
