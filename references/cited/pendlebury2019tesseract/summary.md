---
title: "TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time"
date: 2019-01-01
authors: "Feargus Pendlebury, Fabio Pierazzi, Roberto Jordaney, Johannes Kinder, Lorenzo Cavallaro"
status: read
doi: "arXiv:1807.07838"
category: "Security"
tags:
  - evaluation-bias
  - concept-drift
  - temporal-bias
  - malware-classification
  - methodology
  - project/graph-phishing-detection
---

# TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time

## Metadane
- **Autorzy**: Feargus Pendlebury, Fabio Pierazzi, Roberto Jordaney, Johannes Kinder, Lorenzo Cavallaro (King's College London, Royal Holloway, Bundeswehr University Munich)
- **Rok**: 2019
- **Źródło**: 28th USENIX Security Symposium
- **DOI/Link**: arXiv:1807.07838
- **Status**: read
- **Kategoria główna**: Security
- **Tagi**: `#evaluation-bias` `#concept-drift` `#temporal-bias` `#malware-classification` `#methodology`

## Streszczenie
Autorzy podważają tezę, że klasyfikacja malware (na przykładzie Androida) jest problemem rozwiązanym, mimo publikowanych wyników F1 sięgających 0,99. Wskazują, że tak wysokie metryki są zawyżone przez dwa wszechobecne źródła stronniczości eksperymentalnej: **stronniczość przestrzenną** (spatial bias) — nierealistyczne proporcje goodware do malware w zbiorach treningowych/testowych — oraz **stronniczość czasową** (temporal bias) — niepoprawne podziały czasowe, które pozwalają modelowi „uczyć się na przyszłości" i tworzą niemożliwe w praktyce konfiguracje.

Praca proponuje zbiór ograniczeń przestrzenno-czasowych do projektowania eksperymentów, które eliminują oba źródła błędu, oraz nową metrykę (AUT) podsumowującą oczekiwaną odporność klasyfikatora w realnym wdrożeniu wraz z algorytmem strojenia. Autorzy implementują rozwiązanie w otwartoźródłowym frameworku TESSERACT i ewaluują trzy klasyfikatory z literatury na zbiorze 129 tys. aplikacji obejmującym ponad trzy lata. Potwierdzają, że wcześniejsze wyniki są obciążone błędem, ujawniają nieintuicyjne zachowania wydajności oraz pokazują, że odpowiednie strojenie (np. active learning) może istotnie poprawić odporność na degradację czasową (time decay).

## Kluczowe Wnioski
- Wysokie F1/AUROC potrafią ukrywać brak odporności na realne wdrożenie z powodu spatial i temporal bias.
- Podziały treningowo-testowe muszą respektować czas: trenuj wyłącznie na przeszłości, testuj na przyszłości.
- Proporcje klas w teście muszą odzwierciedlać realne rozkłady danej domeny.
- Wprowadzona metryka AUT podsumowuje odporność na koncept drift w czasie.
- Active learning łagodzi degradację wydajności wynikającą z dryfu.

## Metodologia
Systematyzacja źródeł błędu ewaluacyjnego; sformułowanie ograniczeń (spójność czasowa treningu, czasowa rozłączność okien, realistyczna proporcja klas w teście); definicja metryki AUT (Area Under Time); reimplementacja i porównanie trzech klasyfikatorów Android na 129 tys. aplikacji w oknie ponad 3 lat z użyciem frameworka TESSERACT.

## Główne Koncepcje
- **Spatial bias**: nierealistyczna proporcja goodware/malware zaburzająca metryki.
- **Temporal bias**: wyciek przyszłej wiedzy do treningu przez błędny podział czasowy.
- **AUT (Area Under Time)**: metryka odporności klasyfikatora na dryf w czasie.
- **Time decay / concept drift**: spadek skuteczności w miarę ewolucji zagrożeń.

## Relevancja dla graph-phishing-detection
TESSERACT to bezpośredni fundament **metodologii leak-aware** projektu. Definiuje formalne ograniczenia chroniące przed wyciekiem czasowym — kluczowe przy detekcji phishingu, gdzie kampanie i taktyki szybko ewoluują (silny concept drift). Podział danych grafowych musi być czasowo spójny: krawędzie i etykiety dostępne tylko z przeszłości względem momentu scorowania, dokładnie jak w niezmienniku dynamiki kaskady. Metryka AUT jest naturalnym kandydatem do raportowania odporności modeli GNN na dryf phishingu zamiast pojedynczego, zawyżonego F1. Postulat realistycznych proporcji klas odpowiada skrajnej nierównowadze klas typowej dla phishingu/BEC. Praca uzasadnia także raportowanie Recall@FPR — metryki centralnej dla projektu — zamiast metryk maskujących stronniczość.
