---
title: "Multilayer Networks"
date: 2014-01-01
authors: "Mikko Kivelä, Alex Arenas, Marc Barthelemy, James P. Gleeson, Yamir Moreno, Mason A. Porter"
status: read
doi: "10.1093/comnet/cnu016"
category: "Theory"
tags:
  - multilayer-networks
  - network-science
  - multiplex
  - temporal-networks
  - survey
  - project/graph-phishing-detection
---

# Multilayer Networks

## Metadane
- **Autorzy**: Mikko Kivelä, Alex Arenas, Marc Barthelemy, James P. Gleeson, Yamir Moreno, Mason A. Porter
- **Rok**: 2014
- **Źródło**: Journal of Complex Networks, vol. 2, no. 3 (przegląd / survey)
- **DOI/Link**: https://doi.org/10.1093/comnet/cnu016
- **Status**: read
- **Kategoria główna**: Theory

## Streszczenie
To fundamentalny i szeroko cytowany przegląd (review) wprowadzający spójny formalizm matematyczny dla sieci wielowarstwowych (multilayer networks). Autorzy zauważają, że wiele wariantów rozszerzeń klasycznych grafów — sieci multipleksowe (multiplex), sieci wzajemnie połączone (interconnected), sieci czasowe (temporal), sieci sieci (networks of networks), grafy z wieloma typami krawędzi — było rozwijanych niezależnie i z niespójną terminologią. Praca proponuje uogólnioną definicję sieci wielowarstwowej obejmującą te przypadki jako szczególne instancje.

Przegląd systematyzuje pojęcia (warstwy, aspekty, węzły-stany, krawędzie wewnątrz- i międzywarstwowe), omawia uogólnienia metryk sieciowych (centralność, klastrowanie, struktura społeczności) na przypadek wielowarstwowy oraz konsekwencje dla procesów dynamicznych (rozprzestrzenianie, perkolacja, synchronizacja). Stanowi wspólny język i mapę pojęciową dla całej dziedziny analizy sieci złożonych.

## Kluczowe Wnioski
- Wiele wariantów sieci (multiplex, temporal, interdependent) to przypadki jednego ogólnego formalizmu.
- Ujednolicona notacja (aspekty, warstwy, węzły-stany) porządkuje rozproszoną literaturę.
- Metryki i procesy dynamiczne wymagają uogólnienia na strukturę wielowarstwową.
- Spłaszczanie warstw do jednej sieci traci istotną informację strukturalną.

## Metodologia
Praca przeglądowo-teoretyczna: konsolidacja definicji, formalizacja ogólnej struktury wielowarstwowej, klasyfikacja podtypów, przegląd uogólnionych miar i modeli dynamiki oraz mapowanie wcześniejszych prac na wspólny framework.

## Główne Koncepcje
- **Sieć wielowarstwowa** — uogólnienie grafu na wiele warstw i aspektów.
- **Multiplex** — te same węzły, różne typy krawędzi w warstwach.
- **Sieci temporalne** — warstwy jako kolejne chwile czasowe.
- **Krawędzie międzywarstwowe** — powiązania kopii węzła w różnych warstwach.

## Relevancja dla graph-phishing-detection
Jest to teoretyczna podstawa całego multipleks-temporalnego podejścia projektu. Graf wiedzy domenowej w detekcji phishingu — gdzie te same encje (nadawcy, domeny, konta) występują jednocześnie w warstwie komunikacji, domenowej i transakcyjnej, a czas dodaje wymiar temporalny — jest dokładnie siecią wielowarstwową w sensie tej pracy. Formalizm Kiveli et al. dostarcza precyzyjną notację do opisu modelu danych (warstwy, krawędzie międzywarstwowe) oraz uzasadnia, dlaczego nie należy spłaszczać warstw przed podaniem do GNN. Kluczowa referencja metodologiczna dla P1 (multipleks) i kolejnych publikacji.
