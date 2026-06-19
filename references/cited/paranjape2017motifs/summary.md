---
title: "Motifs in Temporal Networks"
date: 2017-01-01
authors: "Ashwin Paranjape, Austin R. Benson, Jure Leskovec"
status: read
doi: "10.1145/3018661.3018731"
category: "Data Science"
tags:
  - temporal-networks
  - network-motifs
  - graph-mining
  - dynamic-graphs
  - algorithms
  - project/graph-phishing-detection
---

# Motifs in Temporal Networks

## Metadane
- **Autorzy**: Ashwin Paranjape, Austin R. Benson, Jure Leskovec (Stanford University)
- **Rok**: 2017
- **Źródło**: WSDM '17 (10th ACM Int. Conf. on Web Search and Data Mining)
- **DOI/Link**: 10.1145/3018661.3018731 / arXiv:1612.09259
- **Status**: read
- **Kategoria główna**: Data Science (analiza sieci / graph mining)
- **Tagi**: `#temporal-networks` `#network-motifs` `#graph-mining` `#dynamic-graphs` `#algorithms`

## Streszczenie
Praca wprowadza pojęcie **motywu temporalnego** (δ-temporal motif) jako elementarnej jednostki sieci temporalnych — sieci złożonych z wielu znakowanych czasowo krawędzi między węzłami. Klasyczne motywy sieciowe (małe indukowane podgrafy) opisują strukturę grafów statycznych, jednak nie ujmują dynamiki: kolejności i odstępów czasowych pomiędzy zdarzeniami. Autorzy definiują motyw temporalny jako indukowany podgraf na sekwencji krawędzi temporalnych, w której wszystkie krawędzie muszą wystąpić w oknie czasowym o szerokości δ oraz w określonym porządku.

Głównym wkładem są szybkie algorytmy zliczania takich motywów wraz z dowodami ich złożoności obliczeniowej; osiągają one przyspieszenie do 56,5x względem metody bazowej. Autorzy stosują algorytmy do sieci z różnych domen (komunikacja e-mail/IM, połączenia telefoniczne, transakcje, sieci biologiczne) i pokazują, że liczności motywów różnią się istotnie między domenami, natomiast są podobne w obrębie jednej domeny. Wykazują również, że różne motywy występują w różnych skalach czasowych, co daje wgląd w strukturę i funkcję sieci dynamicznych.

## Kluczowe Wnioski
- Motywy temporalne (δ-temporal motifs) jednocześnie kodują kolejność krawędzi i ograniczenie czasowe (okno δ).
- Liczności motywów są charakterystyczne dla domeny — mogą służyć jako „odcisk palca" typu sieci.
- Różne wzorce (np. recyprokacja, łańcuchy A→B→C) zachodzą w różnych skalach czasowych.
- Efektywne algorytmy zliczania są niezbędne, bo liczba krawędzi temporalnych bywa ogromna mimo umiarkowanej liczby węzłów.

## Metodologia
Formalizacja δ-temporalnych motywów jako uporządkowanych sekwencji k krawędzi w oknie δ; projekt algorytmów zliczania (m.in. 2- i 3-węzłowych motywów dwu- i trój-krawędziowych) z analizą złożoności; ewaluacja empiryczna na zbiorach z wielu domen pod kątem profili motywów i skal czasowych.

## Główne Koncepcje
- **Motyw temporalny / δ-temporal motif**: indukowany podgraf na uporządkowanej sekwencji krawędzi temporalnych w oknie δ.
- **Sieć temporalna**: zbiór węzłów i kolekcja skierowanych krawędzi ze znacznikami czasu.
- **Skala czasowa wzorca**: charakterystyczny czas, w którym dany motyw się manifestuje.

## Relevancja dla graph-phishing-detection
Praca jest fundamentem dla traktowania grafów phishingu (komunikacja, kampanie BEC, transakcje) jako sieci temporalnych, a nie zagregowanych snapshotów. Pojęcie δ-temporalnego motywu bezpośrednio wspiera projektowy **niezmiennik dynamiki kaskady**: kampania phishingowa to uporządkowana w czasie sekwencja zdarzeń (rozesłanie, otwarcia, kliknięcia, dalsza propagacja), której wzorzec powinien być stabilny niezależnie od konkretnych tożsamości węzłów. Profile motywów temporalnych mogą stanowić cechę odróżniającą ruch złośliwy od benign oraz wykrywać skoordynowane „rings". Ostrzeżenie autorów przed agregacją czasu do snapshotów współgra z metodologią **leak-aware**: zliczanie motywów musi respektować porządek czasowy (tylko zdarzenia z przeszłości), by uniknąć wycieku przyszłej informacji do cech.
