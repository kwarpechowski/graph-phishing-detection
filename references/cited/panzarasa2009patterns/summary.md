---
title: "Patterns and Dynamics of Users' Behavior and Interaction: Network Analysis of an Online Community"
date: 2009-01-01
authors: "Pietro Panzarasa, Tore Opsahl, Kathleen M. Carley"
status: to-read
doi: "10.1002/asi.21015"
category: "Data Science"
tags:
  - online-community
  - temporal-networks
  - social-network-analysis
  - interaction-dynamics
  - communication-network
  - project/graph-phishing-detection
---

# Patterns and Dynamics of Users' Behavior and Interaction: Network Analysis of an Online Community

> **Uwaga**: wpis utworzony na podstawie metadanych (reference.md) i wiedzy ogólnej o publikacji — **PDF niedostępny** w repozytorium. Status: **to-read**. Treść poniżej należy zweryfikować po pozyskaniu pełnego tekstu.

## Metadane
- **Autorzy**: Pietro Panzarasa, Tore Opsahl, Kathleen M. Carley
- **Rok**: 2009
- **Źródło**: Journal of the American Society for Information Science and Technology (JASIST), 60(5)
- **DOI/Link**: 10.1002/asi.21015
- **Status**: to-read (META — bez PDF)
- **Kategoria główna**: Data Science (analiza sieci społecznych)
- **Tagi**: `#online-community` `#temporal-networks` `#social-network-analysis` `#interaction-dynamics` `#communication-network`

## Streszczenie
Praca analizuje wzorce zachowań i interakcji użytkowników w internetowej społeczności (znanej sieci wymiany wiadomości studentów — zbiór często określany jako „UC Irvine messages"/Facebook-like forum). Autorzy badają strukturę i dynamikę sieci komunikacyjnej powstającej z czasowo znakowanych wiadomości wymienianych między użytkownikami, traktując ją jako sieć temporalną oraz ważoną. Analiza obejmuje rozkłady aktywności, wzorce recyprokacji oraz ewolucję sieci w czasie.

Badanie pokazuje, jak topologia powiązań społecznych oraz intensywność interakcji kształtują się i zmieniają w trakcie życia społeczności, oraz jak indywidualne zachowania użytkowników agregują się w globalne własności sieci. Zbiór danych użyty w pracy stał się jednym ze standardowych benchmarków dla badań nad sieciami temporalnymi i ważonymi sieciami społecznymi. (Opis przybliżony — do potwierdzenia po lekturze pełnego tekstu.)

## Kluczowe Wnioski
- Sieci komunikacji online mają charakter temporalny i ważony — same agregaty statyczne nie wystarczają.
- Wzorce aktywności i recyprokacji są heterogeniczne między użytkownikami.
- Struktura społeczności ewoluuje w czasie wraz z napływem/odpływem interakcji.
- Zbiór danych stanowi benchmark dla analiz sieci temporalnych.

## Metodologia
Analiza sieci społecznej (SNA) na czasowo znakowanym strumieniu wiadomości; badanie miar topologicznych, wag krawędzi i recyprokacji oraz ich ewolucji w czasie. (Szczegóły do uzupełnienia po lekturze PDF.)

## Główne Koncepcje
- **Online community / sieć komunikacji**: graf wiadomości między użytkownikami.
- **Sieć temporalna i ważona**: krawędzie ze znacznikiem czasu i intensywnością.
- **Recyprokacja**: odwzajemnianie kontaktów między użytkownikami.

## Relevancja dla graph-phishing-detection
Publikacja dostarcza empirycznej podstawy dla traktowania **komunikacji jako sieci temporalnej i ważonej** — bezpośrednio relewantnej dla phishingowej warstwy komunikacji (e-mail/BEC). Wzorce recyprokacji i dynamiki interakcji są kandydatami na cechy/niezmienniki odróżniające naturalną komunikację od skoordynowanych kampanii (niezmiennik dynamiki kaskady). Zbiór danych może posłużyć jako benign baseline ruchu komunikacyjnego przy konstrukcji i ewaluacji grafów oraz testowaniu motywów temporalnych. Analiza ewolucji sieci w czasie wspiera metodologię leak-aware: cechy społeczności muszą być liczone na oknach przeszłych, bez wycieku przyszłej struktury.
