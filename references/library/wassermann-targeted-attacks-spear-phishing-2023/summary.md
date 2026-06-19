---
title: "Targeted Attacks: Redefining Spear Phishing and Business Email Compromise"
date: 2023-01-01
authors: "Sarah Wassermann, Maxime Meyer, Sebastien Goutal, Damien Riquet"
status: read
doi: "arxiv:2309.14166"
category: "Security"
tags:
  - targeted-attacks
  - spear-phishing
  - bec
  - social-engineering
  - email-security
  - taxonomy
  - email-security
  - survey
  - project/spear-phishing-context
---

# Targeted Attacks: Redefining Spear Phishing and Business Email Compromise

## Metadane
- **Autorzy**: Sarah Wassermann, Maxime Meyer, Sebastien Goutal, Damien Riquet
- **Rok**: 2023
- **Zrodlo**: arXiv:2309.14166 (Vade researchers)
- **DOI**: arxiv:2309.14166
- **Status**: `#read`
- **Kategoria**: Security
- **Tagi**: `#targeted-attacks` `#spear-phishing` `#bec` `#social-engineering` `#email-security` `#taxonomy` `#survey`

## Streszczenie

Praca proponuje ujednolicona taksonomie atakow "targeted attacks" (ataków ukierunkowanych), zastepujac niejednoznaczne i niespojne definicje spear phishingu (SP) i Business Email Compromise (BEC), ktore sa uzywane zamiennie lub blednie w literaturze. Autorzy (badacze z Vade, firmy email security) systematyzuja dziedzine, definiujac 4 cechy charakterystyczne atakow ukierunkowanych, 4 kategorie celow (GC1-GC4), oraz taksonomie typow atakow tekstowych (CEO fraud, W-2 fraud, gift card scam, payroll fraud, lawyer fraud, establish rapport).

Praca przeglada istniejace metody detekcji: reguly, ML (semi-supervised, graph-based), NLP, anomaly detection oraz LLM-based podejscia. Autorzy argumentuja, ze fragmentacja terminologii utrudnia porownywanie metod i budowanie benchmarkow - co jest kluczowym problemem dziedziny. Statystyki pokazuja skale problemu: FBI raportuje $43B strat z BEC w latach 2016-2021, wskaznik konwersji atakow ukierunkowanych jest 10x wyzszy niz zwyklego phishingu (Cisco), a Abnormal Security odnotowuje 3.81% wskaznik prevalencji wsrod organizacji.

## Kluczowe Wnioski
- Terminologia "spear phishing" i "BEC" jest uzywana niespojnie w literaturze - autorzy proponuja zunifikowany termin "targeted attacks"
- 4 cechy charakterystyczne atakow ukierunkowanych: (1) ukierunkowanie na konkretna ofiare, (2) personalizacja/kontekstualizacja, (3) podszywanie sie pod zaufane zrodlo, (4) social engineering
- 4 kategorie celow atakow (GC1-GC4): kradzez danych uwierzytelniajacych, przelew srodkow finansowych, zdobycie informacji poufnych, instalacja malware/ransomware
- Tekstowa taksonomia atakow: CEO fraud, W-2 fraud, gift card scam, payroll fraud, lawyer fraud, establish rapport (budowanie relacji jako etap wstepny)
- 6 zasad social engineeringu (za Cialdini): authority, social proof, scarcity, commitment/consistency, liking, reciprocity
- FBI raportuje $43B strat z BEC 2016-2021; atakami ukierunkowanymi targetuje sie C-suite i finance dept

## Metodologia

Praca ma charakter przegladowy (survey) i taksonomiczny:
- Analiza definicji SP i BEC z literatury akademickiej i raportow branżowych (FBI IC3, Cisco, Abnormal Security, Verizon DBIR)
- Systematyczne porownanie terminologii z roznych zrodel
- Propozycja nowej, ujednoliconej taksonomii "targeted attacks"
- Przeglad metod detekcji: rule-based, ML, NLP, graph-based, LLM-based
- Nie zawiera eksperymentow empirycznych - jest to praca koncepcyjna i survey

## Glowne Koncepcje

**Targeted Attacks (TA)**: Zunifikowany termin dla SP i BEC. Atak jest "targeted" gdy spelnia 4 cechy: ukierunkowanie, personalizacja, podszywanie sie, social engineering.

**4 Goal Categories (GC1-GC4)**:
- GC1: Credential harvesting - pozyskanie danych do logowania
- GC2: Financial fraud - przelew srodkow, zmiana danych bankowych
- GC3: Information theft - poufne dane firmowe, IP
- GC4: Malware delivery - zlosliwe zalaczniki lub linki

**Tekstowa typologia atakow**:
- CEO Fraud: podszywanie sie pod CEO/CFO w prosbie o pilny przelew
- W-2 Fraud: prosby o dane podatkowe pracownikow
- Gift Card Scam: prosba o zakup kart podarunkowych
- Payroll Fraud: zmiana danych do przelewu wynagrodzenia
- Lawyer Fraud: podszywanie sie pod prawnikow (M&A, legal disputes)
- Establish Rapport: budowanie relacji przed atakiem wlasciwym

**Zasady social engineeringu (Cialdini)**:
- Authority: autorytet (np. CEO, prawnik)
- Social Proof: konformizm spoleczny
- Scarcity: niedobor/pilnosc
- Commitment/Consistency: konsekwencja
- Liking: sympatia
- Reciprocity: wzajemnosc

## Wyniki

Statystyki skali problemu:
- FBI IC3 2021: $43B strat z BEC w latach 2016-2021
- Cisco: atakami ukierunkowanymi conversion rate 10x wyzszy niz zwykly phishing
- Abnormal Security: 3.81% organizacji dotknietych targeted attacks
- Vade: 4.1M kampanii phishingowych/miesiac w Q1 2023

Przeglad metod detekcji (brak unified benchmark):
- Rule-based: wysoka precyzja, niska coverage, podatnosc na evasion
- Semi-supervised ML: dobry balans precision/recall przy malej ilosci etykietowanych danych (Han & Shen 2020)
- Graph-based: EmailProfiler (Duman et al.) - graph komunikacji email; skuteczny dla anomalii
- LLM-based: wczesne wyniki obiecujace, ale brak standardowych benchmarkow

## Przydatne Cytaty

"the terms 'spear phishing' and 'BEC' are not clearly delineated in the literature, and are sometimes used interchangeably" (Introduction)

"We propose the term 'targeted attacks' as an umbrella term encompassing both SP and BEC, defined by four key characteristics: targeting, personalization, impersonation, and social engineering" (Section 2)

"According to the FBI IC3 report, BEC scams resulted in losses of $43 billion between 2016 and 2021" (Section 1)

"targeted attacks have a conversion rate up to 10 times higher than generic phishing attacks" (za Cisco, Section 1)

## Datasety
- Brak publicznie dostepnych datasetow (praca survey/taksonomiczna)
- Vade wewnetrzny dataset emaili (niepubliczny)

## Powiazane Tematy
- Unified taxonomy i benchmarking targeted attacks
- Social engineering persuasion principles (Cialdini framework)
- BEC detection methods: rule-based, ML, graph-based, LLM
- EmailProfiler - graph-based email anomaly detection
- LLM-augmented spear phishing (Hazell 2023, Nahmias 2024)
- FBI IC3 annual reports jako source statystyk

## Notatki

