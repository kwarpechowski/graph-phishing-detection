---
title: "Panning for Gold: Automatically Analysing Online Social Engineering Attack Surfaces"
date: 2017-01-01
authors: "Matthew Edwards, Robert Larson, Benjamin Green, Awais Rashid, Alistair Baron"
status: to-read
doi: "10.1016/j.cose.2016.09.010"
category: "Security"
tags:
  - social-engineering
  - osint
  - attack-surface
  - phishing
  - information-disclosure
  - human-factors
  - project/graph-phishing-detection
---

# Panning for Gold: Automatically Analysing Online Social Engineering Attack Surfaces

## Metadane
- **Autorzy**: Matthew Edwards, Robert Larson, Benjamin Green, Awais Rashid, Alistair Baron
- **Rok**: 2017
- **Źródło**: Computers & Security (Elsevier)
- **DOI/Link**: 10.1016/j.cose.2016.09.010
- **Status**: to-read
- **Kategoria główna**: Security

## Streszczenie
(Uwaga: brak dołączonego PDF — notatka oparta na metadanych i ogólnej wiedzy o tej znanej pracy; wymaga weryfikacji przy lekturze pełnego tekstu.) Praca podejmuje problem automatycznej analizy "powierzchni ataku" inżynierii społecznej (social engineering attack surface) wynikającej z informacji dostępnych publicznie online. Autorzy argumentują, że dane ujawniane przez użytkowników i organizacje (profile, media społecznościowe, ślad cyfrowy) tworzą bogaty zasób (stąd metafora "panning for gold"), który atakujący wykorzystują do przygotowania ataków ukierunkowanych, takich jak spear phishing.

Wkładem pracy jest zautomatyzowane podejście (framework/narzędzie) do zbierania i analizowania publicznie dostępnych informacji w celu oceny, jakie dane mogą zostać użyte w atakach socjotechnicznych oraz jak duża jest indywidualna/organizacyjna powierzchnia ataku. Praca łączy perspektywę OSINT (open-source intelligence) z modelowaniem zagrożeń socjotechnicznych i czynnikiem ludzkim, wskazując ryzyka prywatności i implikacje obronne.

Praca jest często cytowana w kontekście profilowania ofiar, automatyzacji rekonesansu atakującego oraz oceny podatności na phishing ukierunkowany, dostarczając ram do myślenia o tym, jak dane publiczne przekładają się na konkretne wektory ataku.

## Kluczowe Wnioski
- Publicznie dostępne informacje online tworzą wymierną powierzchnię ataku dla inżynierii społecznej.
- Możliwa jest automatyzacja zbierania/analizy tych danych (OSINT) w celu oceny ryzyka.
- Wyniki mają implikacje zarówno ofensywne (rekonesans), jak i defensywne (ograniczanie ekspozycji).

## Metodologia
(Do potwierdzenia przy lekturze.) Automatyczne pozyskiwanie i analiza danych OSINT, kwantyfikacja powierzchni ataku socjotechnicznego; prawdopodobnie analiza przypadków i/lub ewaluacja na zebranych profilach.

## Główne Koncepcje
- **Powierzchnia ataku socjotechnicznego** — zakres danych wykorzystywalnych przez atakującego.
- **OSINT** — wywiad z otwartych źródeł.
- **Spear phishing / profilowanie ofiary** — personalizacja ataku na bazie zebranych danych.

## Relevancja dla graph-phishing-detection
Praca dostarcza motywacji i kontekstu zagrożeń dla projektu, zwłaszcza dla wątków spear phishing/BEC. Dane OSINT o relacjach (kto z kim się komunikuje, powiązania organizacyjne, profile) naturalnie tworzą strukturę grafową, którą można modelować jako graf komunikacji/relacji w detekcji phishingu ukierunkowanego. Stanowi to uzasadnienie dla budowy grafowej reprezentacji kontekstu ofiary/nadawcy oraz dla podejść context-aware w wykrywaniu spear phishingu i lateral movement w projekcie.

## Przydatne Cytaty
- (Do uzupełnienia po lekturze pełnego tekstu.)

## Datasety
- (Do potwierdzenia — prawdopodobnie zebrane dane OSINT/profile online.)

## Powiązane Tematy
- Spear phishing i BEC.
- Profilowanie ofiar / personalizacja ataku.
- Ochrona prywatności i ograniczanie ekspozycji online.

## Notatki
