---
title: "Collective Opinion Spam Detection: Bridging Review Networks and Metadata"
date: 2015-01-01
authors: "Shebuti Rayana, Leman Akoglu"
status: to-read
doi: "10.1145/2783258.2783370"
category: "Security"
tags:
  - opinion-spam
  - fraud-detection
  - review-networks
  - metadata
  - collective-classification
  - graph-mining
  - project/graph-phishing-detection
---

# Collective Opinion Spam Detection: Bridging Review Networks and Metadata

> Uwaga: wpis META — wygenerowany z metadanych referencji oraz wiedzy ogólnej, bez dostępu do PDF. Status: to-read. Treść poniżej należy zweryfikować względem oryginału.

## Metadane
- **Autorzy**: Shebuti Rayana, Leman Akoglu (Stony Brook University)
- **Rok**: 2015
- **Źródło**: KDD 2015 (ACM SIGKDD Conference on Knowledge Discovery and Data Mining)
- **DOI/Link**: 10.1145/2783258.2783370 — https://doi.org/10.1145/2783258.2783370
- **Status**: to-read
- **Kategoria główna**: Security

## Streszczenie
Praca (znana jako system SpEagle) proponuje zunifikowane podejście do wykrywania spamu opinii (opinion spam / fałszywych recenzji), które łączy sygnały sieciowe (relacje recenzent-produkt) z metadanymi i treścią recenzji. Autorzy argumentują, że pojedyncze źródło sygnału (sama treść, same metadane lub sama struktura sieci) jest niewystarczające, ponieważ spamerzy adaptują się do detektorów opartych tylko na jednym typie cech.

SpEagle integruje cechy metadanych (ocena, czas, długość recenzji, burstiness) z sygnałami sieciowymi w jednym frameworku klasyfikacji zbiorowej (collective classification). Wykorzystuje sieć recenzji modelowaną jako graf (recenzenci, recenzje, produkty) i propaguje informację za pomocą wnioskowania w grafie (np. Loopy Belief Propagation na sieci typu Markov Random Field), łącząc słabe sygnały priorytetowe z metadanych z propagacją po strukturze.

Metoda działa zarówno w trybie nienadzorowanym, jak i częściowo nadzorowanym (wykorzystując nieliczne etykiety), i była ewaluowana na rzeczywistych danych recenzji (m.in. Yelp). Wyniki wskazują na przewagę zintegrowanego podejścia nad metodami opartymi na pojedynczym źródle sygnału.

## Kluczowe Wnioski
- Skuteczna detekcja spamu opinii wymaga łączenia metadanych, treści i sieci.
- Klasyfikacja zbiorowa (propagacja po grafie) wzmacnia słabe sygnały pojedynczych recenzji.
- Framework działa w trybie nienadzorowanym i częściowo nadzorowanym.
- Integracja sygnałów daje przewagę nad detektorami jednoźródłowymi (odporność na adaptację spamerów).

## Metodologia
Modelowanie sieci recenzji jako grafu (recenzent-recenzja-produkt) z priorytetami pochodzącymi z metadanych i treści; wnioskowanie zbiorowe (Loopy Belief Propagation / Markov Random Field) propaguje prawdopodobieństwa spamerstwa po strukturze. Ewaluacja na rzeczywistych zbiorach recenzji (Yelp) w trybach unsupervised i semi-supervised.

## Główne Koncepcje
- **Opinion spam**: fałszywe recenzje manipulujące reputacją.
- **Collective classification**: wspólne etykietowanie powiązanych obiektów w grafie.
- **Belief propagation**: propagacja prawdopodobieństw po strukturze grafu.
- **Fuzja sygnałów (metadane + sieć + treść)**: integracja heterogenicznych źródeł.

## Relevancja dla graph-phishing-detection
To wczesny, wzorcowy przykład tezy projektu: pojedynczy widok jest niewystarczający, a fuzja sieci + metadanych + treści z propagacją zbiorową istotnie poprawia detekcję adwersarialnego fraudu. Mechanizm collective classification / belief propagation jest bezpośrednio analogiczny do propagacji ryzyka w grafie phishingowym — etykieta „złośliwy" dla jednej domeny/konta powinna propagować się na powiązane węzły. Podejście SpEagle uzasadnia architekturę multipleksowego grafu (komunikacja/domena/transakcje + metadane) i dostarcza klasycznego (nie-GNN) baseline'u opartego na propagacji, względem którego nowoczesne GNN projektu można porównać pod kątem Recall@FPR1% i odporności na kamuflaż atakującego.
