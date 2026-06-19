---
title: "Insight-LLM: LLM-enhanced Multi-view Fusion in Insider Threat Detection"
date: 2025-01-01
authors: "Chengyu Song, Jianming Zheng"
status: read
doi: "arXiv:2509.01509"
category: "Security"
tags:
  - insider-threat
  - large-language-models
  - multi-view-fusion
  - anomaly-detection
  - cybersecurity
  - class-imbalance
  - project/graph-phishing-detection
---

# Insight-LLM: LLM-enhanced Multi-view Fusion in Insider Threat Detection

## Metadane
- **Autorzy**: Chengyu Song, Jianming Zheng (klucz cytowania: song2025insight)
- **Rok**: 2025
- **Źródło**: arXiv preprint
- **DOI/Link**: arXiv:2509.01509 — https://arxiv.org/abs/2509.01509
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Insight-LLM to modularny framework fuzji wielowidokowej (multi-view fusion) wspomaganej dużymi modelami językowymi (LLM), zaprojektowany specjalnie pod detekcję zagrożeń wewnętrznych (insider threat detection, ITD). Autorzy wskazują, że ITD wymaga analizy rzadkich, heterogenicznych danych o zachowaniu użytkowników, a dotychczasowe metody opierają się głównie na modelowaniu jednowidokowym, co skutkuje ograniczonym pokryciem i przeoczeniami anomalii.

Bezpośrednie przeniesienie uczenia wielowidokowego do ITD napotyka jednak trudności: wąskie gardła skalowalności (niezależnie trenowane podmodele), niezgodność semantyczną między różnymi przestrzeniami cech oraz nierównowagę widoków (silne modalności przytłaczają słabsze). Insight-LLM rozwiązuje to, używając zamrożonych, wstępnie wytrenowanych enkoderów do wydobycia wysokiej jakości osadzeń dla każdego widoku behawioralnego, co ogranicza przeuczenie i koszt treningu.

Następnie dedykowane Q-formery wyrównują każde osadzenie do semantycznej przestrzeni LLM (deep cross-modal fusion), a warstwa uwagi międzywidokowej (cross-view attention) ponownie waży osadzenia, wzmacniając słabe sygnały zagrożeń i tłumiąc szum. Końcowo zsumowane osadzenia są dostrajane przez fuzję wielowidokową dla odporności przy silnej nierównowadze klas. Eksperymenty na dwóch rzeczywistych zbiorach pokazują przewagę nad baseline'ami, SOTA przy niskiej latencji i niewielkim narzucie parametrów.

## Kluczowe Wnioski
- Modelowanie jednowidokowe gubi anomalie; potrzebna jest fuzja wielu widoków behawioralnych.
- Zamrożone enkodery + Q-formery wyrównują heterogeniczne cechy do przestrzeni LLM.
- Cross-view attention wzmacnia słabe sygnały zagrożeń i tłumi szum.
- Framework radzi sobie z silną nierównowagą klas przy niskiej latencji i narzucie parametrów.

## Metodologia
Każdy widok behawioralny kodowany zamrożonym, pretrenowanym enkoderem; Q-former wyrównuje osadzenia do manifoldu LLM; warstwa cross-view attention re-waży modalności; fuzja wielowidokowa z dostrajaniem pod ITD. Ewaluacja na dwóch rzeczywistych zbiorach (m.in. typu CERT insider threat) z metrykami detekcji przy nierównowadze klas oraz pomiarem latencji i liczby parametrów.

## Główne Koncepcje
- **Multi-view fusion**: łączenie wielu modalności zachowania użytkownika.
- **Q-former**: moduł wyrównujący osadzenia do przestrzeni semantycznej LLM.
- **Cross-view attention**: ważenie widoków, wzmacnianie słabych sygnałów.
- **Frozen encoders**: pretrenowane enkodery bez dostrajania (oszczędność, anty-overfitting).

## Relevancja dla graph-phishing-detection
Insider threat i phishing/BEC dzielą rdzeniowe wyzwania: rzadkie, heterogeniczne sygnały i ekstremalna nierównowaga klas. Wzorzec fuzji wielowidokowej z Insight-LLM jest bezpośrednio inspirujący dla projektu, gdzie graf phishingowy łączy wiele widoków (komunikacja, domena, transakcje, treść) — cross-view attention to gotowy mechanizm ważenia tych widoków i wzmacniania słabego sygnału atakującego ukrytego w szumie. Użycie zamrożonych enkoderów + LLM do wyrównania semantycznego sugeruje praktyczny sposób wstrzyknięcia cech treściowych (np. semantyka maila) do reprezentacji węzłów GNN bez kosztownego współtreningu. Praca wzmacnia też argumentację, że pojedynczy widok (sama treść lub sama struktura) jest niewystarczający — co jest tezą leżącą u podstaw wielowidokowego/multipleksowego grafu w projekcie.
