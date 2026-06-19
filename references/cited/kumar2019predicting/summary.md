---
title: "Predicting Dynamic Embedding Trajectory in Temporal Interaction Networks"
date: 2019-01-01
authors: "Srijan Kumar, Xikun Zhang, Jure Leskovec"
status: read
doi: "10.1145/3292500.3330895"
category: "Machine Learning"
tags:
  - temporal-networks
  - dynamic-embeddings
  - interaction-networks
  - recurrent-networks
  - representation-learning
  - project/graph-phishing-detection
---

# Predicting Dynamic Embedding Trajectory in Temporal Interaction Networks

## Metadane
- **Autorzy**: Srijan Kumar, Xikun Zhang, Jure Leskovec
- **Rok**: 2019
- **Źródło**: KDD 2019 (Proceedings of the 25th ACM SIGKDD)
- **DOI/Link**: https://doi.org/10.1145/3292500.3330895
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca wprowadza JODIE — model do uczenia dynamicznych reprezentacji (embeddingów) użytkowników i obiektów w temporalnych sieciach interakcji (np. zakupy w e-commerce, edycje, aktywność w mediach społecznościowych). Każda interakcja użytkownik-obiekt aktualizuje reprezentacje obu stron za pomocą sprzężonych sieci rekurencyjnych (coupled RNN): osobnej dla użytkowników i osobnej dla obiektów, wzajemnie zależnych. Dzięki temu reprezentacje ewoluują w czasie, odzwierciedlając zmieniające się zainteresowania i właściwości.

Kluczową innowacją jest projekcyjny operator (projection operator), który przewiduje przyszłą trajektorię embeddingu użytkownika w czasie ciągłym — czyli jak reprezentacja zmieni się do momentu kolejnej interakcji — bez czekania na zdarzenie. Pozwala to przewidywać, z którym obiektem użytkownik wejdzie w interakcję. Dodatkowo wprowadzono technikę t-Batch umożliwiającą wydajne, zrównoleglone uczenie. JODIE przewyższa wcześniejsze metody w predykcji przyszłych interakcji i zmian stanu użytkownika.

## Kluczowe Wnioski
- Sprzężone RNN aktualizują reprezentacje użytkownika i obiektu przy każdej interakcji.
- Operator projekcji przewiduje embedding w dowolnym przyszłym momencie (czas ciągły).
- Technika t-Batch znacząco przyspiesza trening na sekwencjach interakcji.
- Model lepiej przewiduje przyszłe interakcje i zmiany stanu niż wcześniejsze metody.

## Metodologia
Dwie współzależne sieci RNN aktualizują embeddingi statyczne i dynamiczne na podstawie cech interakcji i upływu czasu. Operator projekcji ekstrapoluje embedding użytkownika względem czasu. Trening minimalizuje błąd przewidywanej reprezentacji obiektu. Ewaluacja na zbiorach Reddit, Wikipedia, LastFM, MOOC w zadaniach predykcji interakcji i zmiany stanu.

## Główne Koncepcje
- **Temporalna sieć interakcji** — strumień datowanych zdarzeń użytkownik-obiekt.
- **Dynamiczny embedding** — reprezentacja ewoluująca w czasie.
- **Projection operator** — predykcja trajektorii embeddingu w czasie ciągłym.
- **Coupled RNN / t-Batch** — sprzężona aktualizacja i wydajny trening.

## Relevancja dla graph-phishing-detection
Detekcja phishingu na grafach komunikacji to w istocie problem na temporalnej sieci interakcji: e-maile to datowane zdarzenia nadawca-odbiorca. JODIE dostarcza wzorzec uczenia dynamicznych reprezentacji w czasie ciągłym — kluczowy dla wykrywania nagłych zmian zachowania (przejęcie konta, nietypowy partner komunikacji) charakterystycznych dla BEC i spear phishingu. Operator projekcji umożliwia detekcję anomalii w czasie rzeczywistym (czy bieżąca interakcja odbiega od przewidzianej trajektorii), a podejście temporalne uzupełnia multipleksowy model grafu projektu. Jest też metodologicznym fundamentem dla uczonego, indukcyjnego GNN temporalnego (P2/P3).
