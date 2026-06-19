---
title: "cGraph: Graph Based Extensible Predictive Domain Threat Intelligence Platform"
date: 2022-01-01
authors: "Wathsara Daluwatta, Ravindu De Silva, Sanduni Kariyawasam, Mohamed Nabeel, Charith Elvitigala, Kasun De Zoysa, Chamath Keppitiyagama"
status: read
doi: "arXiv:2202.07883"
category: "Security"
tags:
  - threat-intelligence
  - malicious-domains
  - belief-propagation
  - graph-inference
  - domain-graph
  - predictive-detection
  - project/graph-phishing-detection
---

# cGraph: Graph Based Extensible Predictive Domain Threat Intelligence Platform

## Metadane
- **Autorzy**: Wathsara Daluwatta, Ravindu De Silva, Sanduni Kariyawasam, Mohamed Nabeel, Charith Elvitigala, Kasun De Zoysa, Chamath Keppitiyagama
- **Rok**: 2022
- **Zrodlo**: The Web Conference 2022 (WWW)
- **DOI/Link**: https://arxiv.org/abs/2202.07883
- **Status**: read
- **Kategoria glowna**: Security

## Streszczenie
Praca przedstawia cGraph - rozszerzalna, predykcyjna platforme threat intelligence opartą na grafie. Autorzy zauważają, że większość obecnych systemów threat intelligence (np. Cisco Umbrella Investigate, Anomali) jest reaktywna: identyfikuje zasoby atakujące dopiero po przeprowadzeniu ataku i nie wykorzystuje powiązań między zasobami sieciowymi do wykrywania ukrytych, powiązanych zasobów złośliwych.

cGraph jest zbudowany jako system graph-first, w którym analitycy eksplorują zasoby sieciowe (domeny, IP, hosty) przez grafowe API. Platforma oferuje predykcję w czasie rzeczywistym opartą na algorytmach wnioskowania (belief propagation), przewidując złośliwe domeny z grafu sieciowego na podstawie kilku znanych złośliwych i łagodnych "ziaren" (seeds). System jest rozszerzalny (nowe typy zasobów dodawane transparentnie) i skalowalny (Apache Spark, Kubernetes).

## Kluczowe Wnioski
- Powiazania miedzy zasobami sieciowymi (wspoldzielone IP, hosting, rejestracja) umozliwiaja wykrycie ukrytych zlosliwych domen.
- Belief propagation na grafie pozwala propagowac etykiety z malej liczby ziaren do calej infrastruktury.
- Podejscie predykcyjne (proaktywne) przewyzsza reaktywne blacklisty.
- System graph-first z grafowym API ulatwia eksploracje infrastruktury atakujacych.

## Metodologia
Konstrukcja heterogenicznego grafu zasobow internetowych z wielu zrodel; propagacja przekonan (belief propagation) z ziaren malicious/benign w celu nadania kazdej domenie score zlosliwosci. Implementacja na Apache Spark + Kubernetes dla skalowalnosci i predykcji w czasie rzeczywistym.

## Glowne Koncepcje
- **Belief propagation** - iteracyjna propagacja prawdopodobienstw po grafie.
- **Seeds (malicious/benign)** - znane wezly startowe inicjujace inferencje.
- **Graph-first platform** - architektura, w ktorej graf jest centralnym modelem danych.
- **Predictive threat intelligence** - przewidywanie zlosliwosci zanim atak sie zmaterializuje.

## Relevancja dla graph-phishing-detection
cGraph jest wzorcowym przykladem grafu wiedzy domenowej w bezpieczenstwie - dokladnie tej koncepcji, ktora projekt rozwija. Propagacja z malej liczby ziaren odpowiada reżimowi rzadkich etykiet i jest klasyczna alternatywa (baseline) dla uczonego GNN. Heterogeniczny graf domen/IP/hostow stanowi szkielet dla warstw multipleksowych. Belief propagation to naturalny punkt odniesienia, ktory uczony GNN ma pobic na metryce Recall@FPR1%. Praca dostarcza tez argumentu za podejsciem proaktywnym/predykcyjnym zamiast reaktywnych blacklist.
