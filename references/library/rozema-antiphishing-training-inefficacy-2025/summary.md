---
title: "Anti-Phishing Training (Still) Does Not Work: A Large-Scale Reproduction Study"
date: 2025-01-01
authors: "Andrew T. Rozema, James C. Davis"
status: read
doi: "arxiv:2506.19899"
category: "Security"
tags:
  - phishing-training
  - security-awareness
  - ineffectiveness
  - nist-phish-scale
  - human-factors
  - reproduction-study
  - organizational-security
  - embedded-training
  - project/phishing-simulation-ethics
---

# Anti-Phishing Training (Still) Does Not Work: A Large-Scale Reproduction Study

## Metadane
- **Autorzy**: Andrew T. Rozema, James C. Davis
- **Rok**: 2025
- **Zrodlo**: arXiv:2506.19899 [cs.CR]
- **DOI**: arxiv:2506.19899
- **Status**: `#read`
- **Kategoria**: Security
- **Tagi**: `#phishing-training` `#security-awareness` `#ineffectiveness` `#nist-phish-scale` `#human-factors` `#reproduction-study` `#project/phishing-simulation-ethics`

## Streszczenie

Large-scale reproduction study (N=12,511) w US-based fintech firm potwierdzajace nieefektywnosc szkolen anti-phishing. Dwuczynnikowy eksperyment: (1) modality szkoleniowa - Treatment A (wyklady+quiz, n=6,023), Treatment B (wyklady+cwiczenia interaktywne, n=6,026), kontrola (n=462); (2) trudnosc przesliki phishingowej wg NIST Phish Scale (easy/medium/hard).

Kluczowe wyniki: szkolenia nie wykazaly istotnych efektow na click rates (p=0.450) ani reporting rates (p=0.417), z zaniedbywalnym effect size (eta2<0.01). NIST Phish Scale skutecznie przewidywala zachowanie (click rates: 7.0% easy -> 15.0% hard). Wprowadzono Organizational Inoculation Index (OII): 36-55% kampanii osiagnelo wzorzec "inokulacji" (raporty przed kliknieciami), niezaleznie od efektow szkolen.

Badanie replikuje wyniki Lain et al. i Ho et al. w nowym kontekscie organizacyjnym. Compliance-driven training spelnia wymogi regulacyjne, ale zapewnia minimalna operacyjna ochrone.

## Kluczowe Wnioski

- Training nie wykazal statystycznie istotnego efektu: p=0.450 (klikniecia), p=0.417 (raportowanie), eta2<0.01
- NIST Phish Scale skutecznie przewiduje zachowanie: click rates rosna dwukrotnie (7.0% -> 15.0%) wraz z trudnoscia
- Interactive training nie jest lepszy od lecture-only w metrykach raportowania
- 36-55% kampanii osiagnelo "inokulacje" - odpornosc organizacyjna dziala niezaleznie od indywidualnych szkolen
- Vendorzy moga manipulowac postrzegana skutecznoscia przez selekcje latwich szablonow
- Compliance != Security: szkolenia regulacyjne minimalizuja ryzyko prawne, nie operacyjne

## Metodologia

Eksperyment dwuczynnikowy (N=12,511), losowe przypisanie do grup szkoleniowych, 1-miesiac okno na szkolenie, symulacje phishingowe w ciagu 3 miesiecy po szkoleniu. Kazdy uczestnik otrzymal jeden email phishingowy. Analiza: two-way ANOVA + regresja logistyczna. Nowe metryki temporalne: OII = t_first_click - t_first_report.

## Glowne Koncepcje

- **NIST Phish Scale**: Standaryzowana miara trudnosci przesliki (2 wymiary: Phishing Cues + Premise Alignment)
- **Organizational Inoculation Index (OII)**: OII = t_first_click - t_first_report; mierzy odpornosc organizacji w czasie
- **Reproduction Study**: Testuje generalizowalnosc zjawiska w nowym kontekscie, nie powtarza identycznych procedur

## Wyniki

- H1 (NIST Phish Scale): POTWIERDZONA - F(2,12086)=41.415, p<0.001, eta2=0.007
- H2 (efekt szkolenia): NIEPOTWIERDZONA - F(2,12086)=0.800, p=0.450
- H3 (interactive training): NIEPOTWIERDZONA
- H4 (interakcja training x trudnosc): NIEPOTWIERDZONA (marginalna interakcja dla najtrudniejszych emaili)
- H5 (timeliness raportowania): CZESCIOWO - mediana czasu-do-raportu = 21 minut; 52.9% kampanii inokulowanych

## Przydatne Cytaty

> "After deploying regulation-compliant training programs to over 12,000 employees, we found no statistically significant main effects of training on either click rates (p=0.450) or report rates (p=0.417)." (str. 8)

> "Organizations setting specific performance targets (such as click-through rates around 2%) may achieve these by using low-difficulty lures that fail to represent sophisticated attacks." (str. 8)

## Datasety

- Wewnetrzne dane fintechu + biblioteka szablonow phishingowych dostawcy (zastrzezone)
- NIST Phish Scale: pierwsza walidacja enterprise scale (N=12,511)

## Powiazane Tematy

- Skutecznosc szkolen phishingowych
- Walidacja NIST Phish Scale
- Human factors w cyberbezpieczenstwie
- LLM-generated phishing i ewolucja zagrozen
- Organizational Inoculation Index jako miara bezpieczenstwa

## Notatki

Kluczowy paper dla #PSE-1 i #PSE-4: potwierdza bazowa hipoteze, ze standardowy embedded training nie dziala. Umozliwia benchmark P0 (GoPhish generic). Uwaga: paper ten ma rowniez folder as anti-phishing-training-2025 z pelniejszym summary.
