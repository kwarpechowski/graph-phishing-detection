---
title: "An Overview of End-to-End Entity Resolution for Big Data"
date: 2021-01-01
authors: "Vassilis Christophides, Vasilis Efthymiou, Themis Palpanas, George Papadakis, Kostas Stefanidis"
status: read
doi: "10.1145/3418896"
category: "Data Science"
tags:
  - entity-resolution
  - record-linkage
  - data-integration
  - blocking
  - knowledge-graphs
  - survey
  - project/graph-phishing-detection
---

# An Overview of End-to-End Entity Resolution for Big Data

## Metadane
- **Autorzy**: Vassilis Christophides, Vasilis Efthymiou, Themis Palpanas, George Papadakis, Kostas Stefanidis
- **Rok**: 2021
- **Zrodlo**: ACM Computing Surveys (CSUR)
- **DOI/Link**: https://doi.org/10.1145/3418896
- **Status**: read
- **Kategoria glowna**: Data Science

## Streszczenie
Artykul jest obszernym przegladem (survey) poswieconym rozwiazywaniu tozsamosci encji (Entity Resolution, ER) - zadaniu identyfikacji roznych opisow odnoszacych sie do tej samej rzeczywistej encji, gdy brakuje unikalnych identyfikatorow. Autorzy koncentruja sie na wyzwaniach charakterystycznych dla Big Data, gdzie jednoczesnie wystepuja wolumen (Volume), predkosc (Velocity) i roznorodnosc (Variety) danych. Lacza perspektywy trzech spolecznosci: baz danych, semantycznego Webu oraz uczenia maszynowego.

Praca prezentuje kompletny widok end-to-end procesu ER: od blokow wstepnego dopasowania (blocking) redukujacych liczbe porownan, przez filtrowanie i dopasowanie (matching), az po klasteryzacje encji. Autorzy krytycznie analizuja kompromisy miedzy metodami nadzorowanymi a nienadzorowanymi, technikami opartymi na schematach i bezschematowymi (schema-agnostic) oraz strategiami wykonania (batch vs. inkrementalne, rownolegle na Apache Spark). Ilustruja problem na przykladzie laczenia opisow filmow, rezyserow i miejsc z baz wiedzy DBpedia i Freebase.

## Kluczowe Wnioski
- ER w Big Data wymaga technik bezschematowych i bardzo skalowalnych z powodu luznej struktury i ekstremalnej roznorodnosci opisow.
- Blocking jest kluczowym etapem ograniczajacym kwadratowa zlozonosc porownan par.
- Dopasowanie moze laczyc podobienstwo atrybutowe, kolektywne (wykorzystujace relacje miedzy encjami) oraz metody ML/glebokie.
- Otwarte kierunki: ER inkrementalne/strumieniowe, ER na grafach wiedzy, wyjasnialnosc i ewaluacja bez ground truth.

## Metodologia
Przeglad literatury strukturyzujacy setki prac w ujednolicony schemat workflow ER. Klasyfikuje metody wedlug etapow (blocking, block processing, matching, clustering), modelu danych (relacyjny, RDF/grafowy) i paradygmatu (regulowy, ML, deep learning).

## Glowne Koncepcje
- **Entity Resolution (ER)** - laczenie opisow tej samej encji.
- **Blocking** - grupowanie kandydatow w celu redukcji porownan.
- **Collective ER** - dopasowanie wykorzystujace powiazania relacyjne miedzy encjami.
- **Schema-agnostic matching** - dopasowanie bez znajomosci schematu.

## Relevancja dla graph-phishing-detection
ER jest fundamentem budowy grafu wiedzy domenowej w detekcji phishingu: te same byty (domeny, adresy IP, nadawcy e-mail, hosty, certyfikaty) pojawiaja sie w wielu zrodlach w roznych formach i musza zostac scalone w spojne wezly grafu przed propagacja sygnalow. Techniki collective ER sa bezposrednio analogiczne do wykorzystania struktury grafu do rozwiazywania tozsamosci wezlow. Dla architektury multipleksowej/temporalnej GNN poprawna rozdzielczosc encji warunkuje jakosc warstw grafu i krawedzi miedzy nimi. Survey jest tez ostrzezeniem dot. ewaluacji leak-aware - niepoprawne scalanie encji moze powodowac wyciek informacji miedzy zbiorem treningowym a testowym, gdy ten sam aktor wystepuje pod roznymi opisami.
