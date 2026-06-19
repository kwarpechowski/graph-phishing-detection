---
title: "Unsupervised Attributed Multiplex Network Embedding"
date: 2020-01-01
authors: "Chanyoung Park, Donghyun Kim, Jiawei Han, Hwanjo Yu"
status: read
doi: "arXiv:1911.06750"
category: "Machine Learning"
tags:
  - multiplex-networks
  - network-embedding
  - unsupervised-learning
  - deep-graph-infomax
  - attention
  - project/graph-phishing-detection
---

# Unsupervised Attributed Multiplex Network Embedding

## Metadane
- **Autorzy**: Chanyoung Park, Donghyun Kim, Jiawei Han, Hwanjo Yu (UIUC, Yahoo! Research, POSTECH)
- **Rok**: 2020
- **Źródło**: AAAI 2020
- **DOI/Link**: arXiv:1911.06750
- **Status**: read
- **Kategoria główna**: Machine Learning
- **Tagi**: `#multiplex-networks` `#network-embedding` `#unsupervised-learning` `#deep-graph-infomax` `#attention`

## Streszczenie
Praca przedstawia **DMGI** (Deep Multiplex Graph Infomax) — prostą, lecz skuteczną nienadzorowaną metodę osadzania atrybutowanych sieci multipleksowych, w których węzły łączą wiele typów relacji (np. wspólny autor, cytowanie, wspólne słowa kluczowe). Większość istniejących metod zakłada pojedynczy typ relacji, a te uwzględniające multipleksowość ignorują atrybuty węzłów, wymagają etykiet do treningu lub nie modelują globalnych własności grafu. DMGI rozszerza Deep Graph Infomax (DGI), który maksymalizuje informację wzajemną między lokalnymi fragmentami grafu a globalną reprezentacją całego grafu.

Autorzy proponują systematyczny sposób łączenia osadzeń z wielu grafów relacyjnych poprzez: (1) ramę **regularyzacji konsensusu** minimalizującą rozbieżności między osadzeniami specyficznymi dla typu relacji oraz (2) **uniwersalny dyskryminator** rozróżniający prawdziwe próbki niezależnie od typu relacji. Mechanizm uwagi (attention) wnioskuje o ważności każdego typu relacji, co pozwala odfiltrować nieistotne warstwy w preprocessingu. Rozległe eksperymenty na zadaniach downstream pokazują, że w pełni nienadzorowany DMGI przewyższa metody stanu sztuki, także te nadzorowane.

## Kluczowe Wnioski
- Sieci są w naturze multipleksowe — wiele typów relacji wzajemnie się uzupełnia.
- Maksymalizacja informacji wzajemnej (DGI) ujmuje globalne własności grafu, nie tylko lokalne.
- Regularyzacja konsensusu spaja osadzenia z różnych warstw relacyjnych.
- Uwaga (attention) szacuje ważność typów relacji i pozwala filtrować zbędne warstwy.
- Metoda jest w pełni nienadzorowana, a mimo to przewyższa podejścia nadzorowane.

## Metodologia
Rozszerzenie Deep Graph Infomax na wiele warstw relacyjnych: per-relacja kodery GCN maksymalizujące MI lokalne-globalne; regularyzacja konsensusu zbiegająca osadzenia warstw; uniwersalny dyskryminator i mechanizm uwagi do ważenia relacji; ewaluacja nienadzorowana na zadaniach klasyfikacji i grupowania węzłów.

## Główne Koncepcje
- **Sieć multipleksowa**: węzły połączone wieloma typami relacji (warstwami).
- **Deep Graph Infomax (DGI)**: maksymalizacja informacji wzajemnej lokalne-globalne.
- **Regularyzacja konsensusu**: spójność osadzeń między warstwami.
- **Uwaga nad relacjami**: ważenie i filtrowanie typów relacji.

## Relevancja dla graph-phishing-detection
DMGI to bezpośrednie zaplecze pierwszej publikacji projektu (P1 — graf **multipleksowy**), w której struktury phishingu modeluje się jednocześnie jako warstwy komunikacji, domeny i transakcji. Nienadzorowane osadzanie multipleksowe odpowiada na deficyt etykiet w phishingu, a mechanizm uwagi pozwala ocenić, które warstwy relacyjne (np. współdzielona infrastruktura domenowa vs. przepływy transakcyjne) niosą najwięcej sygnału do detekcji. Idea konsensusu między warstwami wspiera projektowy nacisk na spójność reprezentacji oraz syntezę warstw w jeden graf wiedzy domenowej. Choć DMGI jest statyczny, stanowi punkt wyjścia, który prace P2/P3 rozszerzają o dynamikę temporalną i ewaluację leak-aware.
