---
title: "Building a Business Email Compromise Research Dataset with Large Language Models"
date: 2024-01-01
authors: "Rohit Dube"
status: read
doi: "10.1007/s11416-024-00544-y"
category: "Security"
tags:
  - business-email-compromise
  - bec
  - dataset-generation
  - large-language-models
  - email-security
  - spear-phishing
  - project/graph-phishing-detection
---

# Building a Business Email Compromise Research Dataset with Large Language Models

## Metadane
- **Autorzy**: Rohit Dube (Cisco Systems)
- **Rok**: 2024 (opublikowane 2025)
- **Zrodlo**: Journal of Computer Virology and Hacking Techniques, 21:3
- **DOI/Link**: https://doi.org/10.1007/s11416-024-00544-y
- **Status**: read
- **Kategoria glowna**: Security

## Streszczenie
Praca adresuje brak publicznie dostepnego zbioru danych do badan nad atakami Business Email Compromise (BEC). Autor zauwaza, ze duze modele jezykowe (LLM) zwiekszyly skutecznosc atakow e-mailowych, umozliwiajac napastnikom pokonanie bariery jezykowej i tworzenie wiarygodnych wiadomosci - a jednoczesnie te same LLM moga posluzyc do generowania danych badawczych.

Zaproponowany system zlozony z LLM tworzy dwa zbiory BEC. Pierwszy (BEC-1) to maly, 20-emailowy zbior proof-of-concept, ktory potwierdza, ze ludzki analityk uznaje generowane wiadomosci za wiarygodne. Drugi (BEC-2) to wiekszy zbior 279 e-maili - pierwszy publiczny zbior BEC dostepny dla spolecznosci badaczy bezpieczenstwa e-mail. Autor wprowadza tez metryke "agreement score" do oceny jakosci zbiorow; BEC-1 i BEC-2 osiagaja wysokie wartosci (odpowiednio 90 i 93), co potwierdza skutecznosc systemu LLM.

## Kluczowe Wnioski
- Brak publicznego zbioru BEC jest powaznym hamulcem badan; LLM moga go wypelnic.
- BEC-2 (279 e-maili) to pierwszy publiczny zbior BEC.
- Metryka "agreement score" mierzy jakosc/wiarygodnosc generowanego zbioru.
- LLM jednoczesnie zwiekszaja potencjal atakow i umozliwiaja generacje danych obronnych.

## Metodologia
System wieloetapowy oparty na LLM generujacy realistyczne watki BEC; walidacja wiarygodnosci przez analityka (BEC-1) i pomiar jakosci metryka agreement score; skalowanie do wiekszego zbioru (BEC-2, 279 e-maili). BEC modelowany jako podkategoria spear phishingu polegajaca na podszywaniu sie pod zaufanego partnera i wyludzeniu przelewu.

## Glowne Koncepcje
- **BEC** - oszustwo e-mailowe polegajace na podszywaniu sie pod zaufanego partnera.
- **LLM-based data generation** - synteza realistycznych e-maili atakujacych.
- **Agreement score** - metryka oceny jakosci wygenerowanego zbioru.
- **Spear phishing** - ukierunkowany phishing, nadkategoria BEC.

## Relevancja dla graph-phishing-detection
Praca jest bezposrednio uzyteczna dla projektu jako zrodlo danych: brak realnych etykiet BEC to glowny problem trzeciej publikacji rozprawy, a syntetyczne zbiory BEC-1/BEC-2 moga sluzyc do wstepnego trenowania i augmentacji grafowych modeli. Generacja przez LLM jest tez spojna z metodyka projektu personalized-phishing-defense (OSINT->profil->generacja). Jednoczesnie praca uwypukla ryzyko adaptacyjnego napastnika wykorzystujacego LLM - co motywuje ewaluacje odpornosci i leak-aware na grafie komunikacyjnym, gdzie watki BEC tworza krawedzie nadawca-odbiorca do analizy GNN.
