---
title: "Self-supervised Incremental Deep Graph Learning for Ethereum Phishing Scam Detection"
date: 2021-01-01
authors: "Shucheng Li, Fengyuan Xu, Runchuan Wang, Sheng Zhong"
status: read
doi: "arXiv:2106.10176"
category: "Security"
tags:
  - ethereum
  - phishing-detection
  - self-supervised-learning
  - graph-neural-networks
  - incremental-learning
  - anomaly-detection
  - project/graph-phishing-detection
---

# Self-supervised Incremental Deep Graph Learning for Ethereum Phishing Scam Detection

## Metadane
- **Autorzy**: Shucheng Li, Fengyuan Xu, Runchuan Wang, Sheng Zhong (National Key Lab for Novel Software Technology, Nanjing University)
- **Rok**: 2021
- **Źródło**: arXiv preprint (cs.LG)
- **DOI/Link**: https://arxiv.org/abs/2106.10176 (`#ethereum`, `#self-supervised`, `#incremental`)
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca podejmuje problem detekcji oszustw phishingowych na Ethereum, drugiej co do wielkości platformie blockchain, gdzie phishing stał się typem przestępstwa angażującym największe kwoty. Autorzy wskazują dwa kluczowe wyzwania przy stosowaniu grafowych sieci neuronowych (GNN) do danych transakcyjnych Ethereum: skalowalność danych (graf transakcji liczy ponad miliard krawędzi i stale rośnie) oraz niedobór etykiet (mało próbek pozytywnych, czasowa nierównowaga etykietowania).

Proponowany model SIEGE (Self-supervised IncrEmental deep Graph lEarning) rozwiązuje oba problemy. Zamiast uczyć się na całym grafie naraz, dzieli graf transakcyjny na bloki o odpowiednim rozmiarze i konsumuje je przyrostowo w porządku czasowym, przekazując pośrednie wyniki uczenia do kolejnego bloku. Aby poradzić sobie z niedoborem etykiet, stosuje uczenie samonadzorowane (SSL) z dwoma zadaniami pretekstowymi: przestrzennym i czasowym, które pozwalają wydobyć informatywne reprezentacje węzłów z ogromnej ilości nieetykietowanych danych.

Autorzy zebrali dane transakcyjne z około pół roku z Ethereum (ponad 70 milionów transakcji). Rozległe eksperymenty pokazują, że SIEGE konsekwentnie przewyższa silne baseline'y zarówno w ustawieniu transdukcyjnym, jak i indukcyjnym, z poprawą F1 rzędu 4%-16%.

## Kluczowe Wnioski
- Phishing na Ethereum jest najkosztowniejszym typem oszustwa; konieczna analiza na poziomie aktywności transakcyjnej.
- Próbkowanie grafu (typowe w istniejących pracach) prowadzi do zniekształcenia rozkładu danych i nie radzi sobie z indukcyjnymi scenariuszami.
- Uczenie samonadzorowane wykorzystuje sygnały nadzoru bezpośrednio z danych, łagodząc niedobór etykiet.
- Paradygmat przyrostowy utrzymuje rozmiar grafu w pamięci pod kontrolą i adaptuje się do zmieniającego rozkładu danych.

## Metodologia
Graf transakcji Ethereum modelowany jako konta (węzły) i transakcje (krawędzie). Graf dzielony na czasowe bloki transakcji konsumowane przyrostowo. Wewnątrz bloku stosowane SSL z dwoma zadaniami pretekstowymi (przestrzennym i czasowym) generującymi embeddingi węzłów bez etykiet. Reprezentacje przekazywane między blokami umożliwiają obliczenia inkrementalne. Metoda jest indukcyjna; ewaluacja w ustawieniach transdukcyjnym i indukcyjnym za pomocą F1.

## Główne Koncepcje
- **Self-supervised learning (SSL) na grafach** — zadania pretekstowe zamiast etykiet
- **Uczenie inkrementalne** — przetwarzanie ewoluującego grafu blok po bloku
- **Indukcyjność** — generalizacja na nowe węzły/transakcje
- **Czasowo-przestrzenne zadania pretekstowe**

## Relevancja dla graph-phishing-detection
SIEGE to jedna z fundamentalnych prac łączących phishing, blockchain i GNN — bezpośrednio relevantna jako reprezentant nurtu detekcji phishingu na grafie transakcji Ethereum. Idea uczenia samonadzorowanego i inkrementalnego na ewoluującym grafie wspiera niezmiennik projektu dotyczący obsługi dynamiki/dryfu danych. Czasowo-przestrzenne zadania pretekstowe stanowią punkt odniesienia dla budowy reprezentacji w grafie wiedzy domenowej oraz dla scenariusza indukcyjnego (generalizacja na nowe konta), istotnego przy ocenie Recall@FPR1%.
