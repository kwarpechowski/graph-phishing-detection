---
title: "Combinatorial Analysis of Multiple Networks"
date: 2013-01-01
authors: "Matteo Magnani, Barbora Micenkova, Luca Rossi"
status: read
doi: "arXiv:1303.4986"
category: "Data Science"
tags:
  - multi-layer-networks
  - multiplex-networks
  - social-network-analysis
  - centrality
  - graph-theory
  - project/graph-phishing-detection
---

# Combinatorial Analysis of Multiple Networks

## Metadane
- **Autorzy**: Matteo Magnani, Barbora Micenkova, Luca Rossi (Aarhus University, ISTI-CNR Pisa, University of Urbino)
- **Rok**: 2013
- **Źródło**: arXiv preprint (cs.SI)
- **DOI/Link**: arXiv:1303.4986
- **Status**: read
- **Kategoria główna**: Data Science (analiza sieci społecznych)
- **Tagi**: `#multi-layer-networks` `#multiplex-networks` `#social-network-analysis` `#centrality` `#graph-theory`

## Streszczenie
Praca argumentuje, że klasyczne, „płaskie" modele grafowe nie oddają wiernie rzeczywistości społecznej, którą lepiej opisują **sieci wielowarstwowe** (multi-layer / multiplex). Autorzy wprowadzają rzeczywisty zbiór danych łączący różne rodzaje relacji online i offline oraz proponują metodologiczne przesunięcie w analizie takich sieci. Kluczowym pojęciem jest **power-sociomatrix** — macierz powstała ze zbioru potęgowego (power-set) super-sociomatrycy, czyli wszystkich możliwych kombinacji warstw relacyjnych.

Centralna konjektura mówi, że analiza jedynie pojedynczych warstw osobno i/lub kompletnej sieci scalającej wszystkie połączenia prowadzi do utraty informacji — istotne wzorce ukrywają się dopiero w kombinacjach warstw. Autorzy sugerują istnienie „ukrytych motywów" przechodzących między warstwami reprezentacji i wprowadzają pojęcie **betweenness centrality dla sieci wielowarstwowych**. Przedstawiają wstępne dowody empiryczne, lecz zaznaczają, że hipotezy pozostają w dużej mierze niezweryfikowane i wzywają do tworzenia nowych metod analizy oraz referencyjnych danych wielowarstwowych.

## Kluczowe Wnioski
- Płaski graf gubi semantykę wielu współistniejących relacji — potrzebne modele wielowarstwowe.
- Analiza warstw osobno lub ich pełnego scalenia może powodować utratę informacji.
- Power-sociomatrix (zbiór potęgowy warstw) ujawnia wzorce w kombinacjach warstw.
- Zaproponowano uogólnienie betweenness centrality na sieci wielowarstwowe.
- Hipotezy są wstępne i wymagają nowych danych referencyjnych oraz narzędzi.

## Metodologia
Sformułowanie modelu super-sociomatrycy i jej zbioru potęgowego (power-sociomatrix); definicja miar centralności dla wielu warstw; analiza kombinatoryczna na zebranym rzeczywistym zbiorze relacji online/offline; charakter eksploracyjny z wstępną weryfikacją trzech hipotez badawczych.

## Główne Koncepcje
- **Sieć wielowarstwowa / multipleksowa**: wiele typów relacji między tymi samymi węzłami.
- **Super-sociomatrix**: kolekcja sociomatryc, po jednej na typ relacji.
- **Power-sociomatrix**: zbiór potęgowy kombinacji warstw.
- **Betweenness centrality wielowarstwowa**: uogólnienie pośrednictwa na wiele warstw.

## Relevancja dla graph-phishing-detection
To wczesna, koncepcyjna podstawa dla **multipleksowego modelu grafu** w P1 projektu. Teza o utracie informacji przy analizie pojedynczych warstw lub ich naiwnym scaleniu wprost motywuje łączne modelowanie warstw phishingu (komunikacja, domena, transakcje) zamiast rozpatrywania ich osobno. Idea power-sociomatrycy i „ukrytych motywów przechodzących między warstwami" rezonuje z projektowym poszukiwaniem niezmienników strukturalnych kampanii oraz z analizą motywów temporalnych — wzorce phishingu mogą ujawniać się dopiero w kombinacji warstw. Uogólniona centralność jest kandydatem na cechę węzła w grafie wiedzy domenowej.
