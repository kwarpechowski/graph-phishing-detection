---
title: "User Identity Linkage across Online Social Networks: A Review"
date: 2017-01-01
authors: "Kai Shu, Suhang Wang, Jiliang Tang, Reza Zafarani, Huan Liu"
status: read
doi: "10.1145/3068777.3068781"
category: "Data Science"
tags:
  - identity-linkage
  - social-networks
  - survey
  - entity-resolution
  - link-prediction
  - feature-extraction
  - project/graph-phishing-detection
---

# User Identity Linkage across Online Social Networks: A Review

## Metadane
- **Autorzy**: Kai Shu, Suhang Wang, Jiliang Tang, Reza Zafarani, Huan Liu (Arizona State University; Michigan State University; Syracuse University)
- **Rok**: 2017
- **Źródło**: ACM SIGKDD Explorations Newsletter
- **DOI/Link**: 10.1145/3068777.3068781
- **Status**: read
- **Kategoria główna**: Data Science

## Streszczenie
Przeglądowa praca poświęcona zagadnieniu łączenia tożsamości użytkowników (user identity linkage, UIL) w różnych serwisach społecznościowych. Rosnąca popularność i różnorodność platform sprawia, że użytkownicy posiadają wiele tożsamości (profil, treści, sieć powiązań) na różnych portalach, co rodzi fundamentalne pytanie: czy można powiązać te tożsamości jako należące do tej samej osoby.

Autorzy systematyzują dotychczasowe podejścia, wskazując, że zwykle składają się z dwóch etapów: (1) ekstrakcji cech oraz (2) konstrukcji modeli predykcyjnych z wielu perspektyw. Cechy dzielą się na pochodzące z profilu (nazwa, lokalizacja), treści (styl pisania, czas aktywności) oraz struktury sieci (sąsiedztwo, znajomi). Modele obejmują podejścia nadzorowane, częściowo nadzorowane i nienadzorowane.

W pracy omówiono najważniejsze algorytmy, metryki ewaluacji oraz reprezentatywne zbiory danych. Wskazano też wyzwania wynikające z unikatowej natury danych społecznościowych (szum, heterogeniczność, brak danych) oraz powiązane obszary badawcze, otwarte problemy i kierunki przyszłych prac. Praca ma charakter porządkujący i służy jako mapa pola UIL.

## Kluczowe Wnioski
- UIL zwykle realizuje się dwuetapowo: ekstrakcja cech + model predykcyjny.
- Sygnały dzielą się na profilowe, treściowe i sieciowe (strukturalne).
- Dane społecznościowe są zaszumione i heterogeniczne, co utrudnia linkage.
- UIL wspiera zadania pochodne: rekomendacje, predykcję powiązań, deanonimizację.

## Metodologia
Praca przeglądowa (survey): taksonomia metod według typu cech (profil/treść/sieć) i paradygmatu uczenia (supervised/semi/unsupervised), porównanie metryk (precision, recall, F1) oraz katalog zbiorów danych. Brak własnych eksperymentów — synteza i klasyfikacja istniejącego dorobku.

## Główne Koncepcje
- **User Identity Linkage (UIL)**: powiązanie kont tej samej osoby między platformami.
- **Cechy profilowe/treściowe/sieciowe**: trzy źródła sygnału do linkage.
- **Entity resolution / record linkage**: pokrewne pojęcia łączenia rekordów.
- **Network alignment**: dopasowanie struktur sieci między platformami.

## Relevancja dla graph-phishing-detection
Łączenie tożsamości jest kluczowe przy budowie spójnego grafu phishingowego: ten sam atakujący operuje wieloma adresami, domenami i kontami, a powiązanie ich w jeden węzeł-aktora drastycznie wzmacnia sygnał detekcji (więcej krawędzi, widoczna kampania). Taksonomia cech (profil/treść/sieć) z tej pracy mapuje się na atrybuty węzłów w grafie projektu i podpowiada, jakie sygnały (styl pisania, czas aktywności, sąsiedztwo) wykorzystać do scalania aliasów. Techniki network alignment są przenośne na deduplikację domen/kont w grafie proweniencji. Dla niezmiennika proweniencji UIL dostarcza teoretycznego uzasadnienia, że atrybuty współdzielone między tożsamościami zdradzają wspólne pochodzenie kampanii.
