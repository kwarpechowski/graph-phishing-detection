---
title: "The Multilayer Structure of Corporate Networks"
date: 2019-01-01
authors: "Javier Garcia-Bernardo, Jordi van Lidth de Jeude, Tomaso Aste, Guido Caldarelli"
status: read
doi: "10.1088/1367-2630/ab022d"
category: "Data Science"
tags:
  - multilayer-networks
  - corporate-networks
  - network-science
  - ownership-graph
  - financial-networks
  - project/graph-phishing-detection
---

# The Multilayer Structure of Corporate Networks

## Metadane
- **Autorzy**: Javier Garcia-Bernardo, Jordi van Lidth de Jeude, Tomaso Aste, Guido Caldarelli
- **Rok**: 2019
- **Źródło**: New Journal of Physics, vol. 21, 025002 (Open Access)
- **DOI/Link**: https://doi.org/10.1088/1367-2630/ab022d
- **Status**: read
- **Kategoria główna**: Data Science

## Streszczenie
Artykuł analizuje sieci korporacyjne jako układy wielowarstwowe (multilayer networks), w których te same podmioty (firmy, osoby) powiązane są różnymi typami relacji — przede wszystkim relacjami własnościowymi (ownership) oraz powiązaniami zarządczymi/dyrektorskimi (board interlocks). Autorzy pokazują, że potraktowanie tych relacji jako oddzielnych warstw jednej struktury multipleksowej ujawnia organizację gospodarki korporacyjnej lepiej niż analiza pojedynczej, spłaszczonej sieci.

Na dużych zbiorach danych o własności i powiązaniach firm autorzy badają korelacje między warstwami, rolę pośredniczących jednostek (np. spółek-wydmuszek i jurysdykcji offshore) oraz struktury kontroli. Wykazują, że warstwy niosą komplementarną informację, a niektóre podmioty pełnią kluczową rolę łączącą warstwy. Praca jest przykładem zastosowania nauki o sieciach wielowarstwowych do ekonomii i wykrywania nieprzejrzystych struktur korporacyjnych.

## Kluczowe Wnioski
- Sieci korporacyjne są z natury wielowarstwowe (własność + zarząd).
- Spłaszczanie warstw gubi informację o kontroli i pośrednictwie.
- Podmioty pośredniczące (offshore, wydmuszki) pełnią rolę łączników między warstwami.
- Analiza multipleksowa pomaga identyfikować nieprzejrzyste struktury własnościowe.

## Metodologia
Konstrukcja grafu multipleksowego z warstwami relacji własnościowych i dyrektorskich na podstawie dużych baz danych korporacyjnych. Analiza metrykami sieci wielowarstwowych (korelacje między warstwami, centralność, wykrywanie społeczności), z naciskiem na rolę jednostek pośredniczących i jurysdykcji.

## Główne Koncepcje
- **Sieć wielowarstwowa / multipleks** — wiele typów relacji nad tym samym zbiorem węzłów.
- **Ownership network** — graf powiązań właścicielskich.
- **Board interlock** — powiązania przez wspólnych członków zarządu.
- **Pośrednicy strukturalni** — węzły łączące warstwy (offshore).

## Relevancja dla graph-phishing-detection
Praca dostarcza domenowego uzasadnienia dla multipleksowego modelowania relacji finansowo-korporacyjnych, co jest bezpośrednio istotne dla detekcji phishingu wymierzonego w marki finansowe i ataków BEC (Business Email Compromise). Struktury własności/kontroli i pośredniczące jednostki to dokładnie ten kontekst, który napastnicy podszywający się pod kontrahentów próbują naśladować. Wzorzec „te same podmioty, wiele warstw relacji" wspiera projektowany graf wiedzy domenowej, w którym warstwy komunikacji, domen i transakcji nakładają się na ten sam zbiór encji — fundament multipleks-temporalnego podejścia GNN.
