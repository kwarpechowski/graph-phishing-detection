---
title: "Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics"
date: 2019-01-01
authors: "Mark Weber, Giacomo Domeniconi, Jie Chen, Daniel Karl I. Weidele, Claudio Bellei, Tom Robinson, Charles E. Leiserson"
status: read
doi: "arXiv:1908.02591"
category: "Security"
tags:
  - anti-money-laundering
  - bitcoin
  - graph-convolutional-networks
  - financial-forensics
  - elliptic-dataset
  - project/graph-phishing-detection
---

# Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics

## Metadane
- **Autorzy**: Mark Weber, Giacomo Domeniconi, Jie Chen, Daniel Karl I. Weidele, Claudio Bellei, Tom Robinson, Charles E. Leiserson
- **Rok**: 2019 (KDD '19 Workshop on Anomaly Detection in Finance)
- **Źródło**: KDD 2019 Workshop AML in Finance; arXiv:1908.02591
- **DOI/Link**: arXiv:1908.02591
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca dotyczy przeciwdziałania praniu pieniędzy (AML) w Bitcoinie i lokuje problem w szerszym kontekście inkluzji finansowej — regulacje AML chronią system finansowy, ale generują wysokie koszty i wykluczają osoby z marginesu społecznego. Pseudonimowość kryptowalut pozwala przestępcom ukrywać się, lecz otwarte dane dają śledczym nowe możliwości analizy forensycznej.

Głównym wkładem jest udostępnienie zbioru Elliptic Data Set — szeregu czasowego grafu ponad 200 tys. transakcji Bitcoin (wierzchołki), 234 tys. skierowanych przepływów płatności (krawędzie) i 166 cech wierzchołków (w tym opartych na danych niepublicznych); według autorów to największy publicznie dostępny oznakowany zbiór transakcji w kryptowalutach. Autorzy raportują wyniki binarnej klasyfikacji transakcji nielegalnych za pomocą regresji logistycznej (LR), lasów losowych (RF), perceptronów wielowarstwowych (MLP) oraz grafowych sieci splotowych (GCN). Wyniki wskazują na przewagę Random Forest, lecz zachęcają do łączenia mocnych stron RF i metod grafowych. Omawiana jest też wizualizacja i wyjaśnialność, z prototypem do nawigacji po grafie i obserwacji wyników w czasie.

## Kluczowe Wnioski
- Wprowadzono Elliptic Data Set: ~200 tys. wierzchołków, ~234 tys. krawędzi, 166 cech, oznakowany (legalne/nielegalne/nieznane).
- W binarnej klasyfikacji Random Forest osiągał najlepsze wyniki, przewyższając proste GCN.
- Połączenie cech tablicowych (RF) z informacją relacyjną (GCN) to obiecujący kierunek.
- Wizualizacja i wyjaśnialność są trudne przy dużych, dynamicznych grafach transakcyjnych.

## Metodologia
Konstrukcja czasowego grafu transakcji Bitcoin z cechami wierzchołków; binarna klasyfikacja (illicit/licit) za pomocą LR, RF, MLP oraz GCN; analiza w podziale na kroki czasowe; prototyp wizualizacji do eksploracji i oceny modelu na aktywności nielegalnej.

## Główne Koncepcje
- **Elliptic Data Set**: oznakowany czasowy graf transakcji Bitcoin.
- **Financial forensics / AML**: kryminalistyka finansowa i przeciwdziałanie praniu pieniędzy.
- **GCN vs metody klasyczne**: porównanie metod relacyjnych i tablicowych.
- **Inkluzja finansowa**: napięcie między bezpieczeństwem a dostępem do usług.

## Relevancja dla graph-phishing-detection
Praca jest kanonicznym odniesieniem dla detekcji oszustw finansowych na grafach transakcyjnych i źródłem szeroko używanego benchmarku Elliptic. Dla projektu istotne są: (1) modelowanie nielegalnej aktywności jako klasyfikacji wierzchołków/transakcji w czasowym grafie, (2) obserwacja, że silne baseline tablicowe (RF) bywają konkurencyjne wobec GNN — ważne przy porównywaniu z metodami proweniencyjnymi, oraz (3) potrzeba wyjaśnialności. Te wątki bezpośrednio informują projektowanie grafu wiedzy domenowej i ewaluację detektorów phishingu/oszustw przy rzadkich etykietach i dryfie czasowym.
