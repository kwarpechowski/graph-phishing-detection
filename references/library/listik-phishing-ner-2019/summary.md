---
title: "Phishing Email Detection based on Named Entity Recognition"
date: 2019-01-01
authors: "Vit Listik, Simon Let, Jan Sedivy, Vaclav Hlavac"
status: read
doi: "10.5220/0007314202520256"
category: "Security"
tags:
  - phishing-detection
  - named-entity-recognition
  - nlp
  - email-security
  - impersonation-detection
  - random-forest
  - lda
  - domain-link-profile
  - dkim
  - project/personalized-phishing-defense
---

# Phishing Email Detection based on Named Entity Recognition

## Metadane
- **Autorzy**: Vit Listik, Simon Let, Jan Sedivy, Vaclav Hlavac (Czech Technical University in Prague)
- **Rok**: 2019
- **Zrodlo**: Proceedings of the 5th International Conference on Information Systems Security and Privacy (ICISSP 2019), str. 252-256, SCITEPRESS
- **DOI**: 10.5220/0007314202520256
- **Status**: `#read`
- **Kategoria**: Security
- **Tagi**: `#phishing-detection` `#named-entity-recognition` `#nlp` `#email-security` `#impersonation-detection` `#random-forest` `#lda` `#domain-link-profile` `#dkim`

## Streszczenie

Praca ewaluuje dwa algorytmy detekcji phishingu oparte na rozpoznawaniu jednostek nazwanych (Named Entity Recognition, NER), na zywym ruchu Email.cz - najwiekszego darmowego dostawcy poczty w Czechach (~50 mln wiadomosci dziennie, 75% po czesku, 15% po angielsku). Pierwszy algorytm (baseline, wg Ramanathan & Wechsler 2013) uzywa NER oraz latent Dirichlet allocation (LDA) jako ekstraktorow cech dla klasyfikatora random forest. Drugi - nowy wklad pracy - to detekcja impersonacji: NER wykrywa firmy/organizacje wspomniane w tresci emaila, a nastepnie porownuje domeny linkow w emailu z "profilem linkow" danej firmy zbudowanym z legalnej historycznej komunikacji.

Kluczowa zaleta proponowanego rozwiazania jest to, ze NIE wymaga zbioru danych phishingowych, ktory jest trudny do zdobycia - szczegolnie dla jezykow innych niz angielski (dla czeskiego nie istnieje publiczny zbior phishingowy). Zamiast wykrywac phishing leksykalnie z oznaczonych przykladow, system wykorzystuje wiedze strukturalna: phishing podszywa sie pod zaufana jednostke, wiec rozbieznosc miedzy wykryta przez NER firma a faktycznymi domenami linkow jest sygnalem ataku.

System impersonacyjny sklada sie z trzech krokow: (1) Entity Detector - NER (Nametag, tag IF) wykrywa firmy w tresci emaila; (2) Target Detector - mapuje nazwy firm na kanoniczne domeny (z krajowego rejestru firm + 50 recznych firm miedzynarodowych); (3) Domain Link Profile - dla ~20 czesto atakowanych domen buduje profil legalnych linkow z emaili podpisanych DKIM (tydzien ruchu), filtruje long-tail, i flaguje emaile zawierajace nieoczekiwane domeny jako phishing. Na zywym ruchu (132,000 wiadomosci, 2 dni, 7 atakow / 4 unikalne) rozwiazanie autorow przewyzsza baseline, a kombinacja obu osiaga 100% F-measure. Zadnego z wykrytych atakow nie wychwycil system aktualnie uzywany w Email.cz.

## Kluczowe Wnioski
- Cechy strukturalne oparte na NER (wykryta organizacja vs faktyczne domeny linkow) uzupelniaja sygnal leksykalny i pozwalaja wykrywac phishing bez zbioru treningowego phishingu
- Detekcja impersonacji nie wymaga przykladow phishingowych - kluczowe dla jezykow ubogich w dane (czeski, inne niz angielski)
- Profil linkow firmy budowany z legalnej komunikacji podpisanej DKIM stanowi "baseline normalnosci" dla nadawcy - email z domenami spoza profilu jest podejrzany
- Na zywym ruchu: random forest (baseline) ma bardzo niska precyzje (0.0002), po filtrowaniu tylko czesto atakowanych domen 0.33; link profile osiaga precyzje 0.88; kombinacja obu metod 1.00 precyzji i recall (100% F-measure)
- Wlasny model NER trenowany na danych Email.cz (78.91% F-score) drastycznie przewyzsza model Cnec 2.0 (11.05% F-score) - jezyk emaili (mowa nieformalna) rozni sie od korpusow newsowych
- Reimplementacja baseline Ramanathan & Wechsler osiagnela 94% F-measure (vs 100% w oryginale) na danych Nazario - wciaz wystarczajaco dla testu produkcyjnego
- DKIM stanowi pierwszy filtr: dopasowanie podpisu DKIM do wykrytej domeny => email uznany za legalny

## Metodologia

**Baseline (random forest, Sec. 3.1):** NER (Nametag, tagi g/i/p) + LDA (200 tematow, 1000 cech po usunieciu stop-slow, perplexity 421) tworza wektor cech (200 prawdopodobienstw tematow + 40 cech NER) dla random forest (200 slabych uczacych, max depth 5). Trenowany na zbiorze Nazario.

**Detekcja impersonacji (Sec. 3.2-3.5):**
1. Entity Detector - Nametag (custom model Email.cz) wykrywa firmy (tag IF) w tresci emaila (naglowki moga byc sfalszowane, ale tresc zwykle zawiera podszywana firme)
2. Target Detector - mapowanie nazw firm na kanoniczne domeny (krajowy rejestr firm + 50 recznych firm miedzynarodowych, entity name expansion)
3. Domain Link Profile - dla ~20 czesto atakowanych domen (z PhishTank + wewnetrznej bazy): bierz emaile podpisane DKIM z historycznego ruchu (1 tydzien), wyciagnij domeny z linkow (href), odfiltruj long-tail. Detekcja: jesli DKIM pasuje => valid; w przeciwnym razie sprawdz czy domeny linkow sa w profilu - jesli nie, oznacz jako phishing.

**Dane (Sec. 4):** zbiory phishingu Nazario (4450 emaili 2004-2007) i SpamAssassin (6047 ham/spam); wlasny zbior NER Email.cz (2 mln tekstow, 4 anotatorow, tagi Cnec 2.0 - 39 z 45 uzytych, 54,724 zdania, 125,711 tagow).

**Ewaluacja:** NER na tescie Email.cz; baseline random forest na 20% Nazario; oba systemy na zywym ruchu Email.cz (132,000 wiadomosci, 2 dni, anotacja reczna).

## Glowne Koncepcje

**Detekcja impersonacji przez NER**: phishing z definicji podszywa sie pod zaufana jednostke; NER wykrywa wspomniana organizacje, a niezgodnosc miedzy ta organizacja a domenami linkow zdradza atak. Cechy strukturalne (jednostka vs domena) uzupelniaja sygnal czysto leksykalny.

**Domain Link Profile (profil linkow firmy)**: zbior domen, ktore legalnie pojawiaja sie w komunikacji danej firmy, budowany z emaili zweryfikowanych DKIM. Pelni role baseline normalnosci - odchylenie sygnalizuje phishing; nowe domeny mozna dodawac, co obniza false positives.

**Niezaleznosc od zbioru phishingowego**: kluczowa przewaga - metoda nie potrzebuje oznaczonych przykladow phishingu, wiec jest rozszerzalna na jezyki bez publicznych zbiorow (czeski).

**NER dla jezyka emaili**: model trenowany na korpusie newsowym (Cnec 2.0) zawodzi na emailach (mowa nieformalna); domain-specific model NER (Email.cz) jest niezbedny.

## Wyniki

NER na danych Email.cz (Tab. 1): Cnec 2.0 - 11.05% F-score; Email.cz - 78.91% F-score. Dla samego taga firm IF (Tab. 2): Cnec 2.0 - 23.53%; Email.cz - 75.41%.

Baseline random forest na publicznym Nazario (Tab. 3): avg F-score 0.94 (Phishing: precyzja 0.99, recall 0.75, F 0.85).

Zywy ruch Email.cz (Tab. 4, 132,000 wiadomosci, 77 wsparcie po filtrze):
- Random forest: precyzja 0.0002, recall 1.00, F 0.0004
- Random forest filtered: precyzja 0.33, recall 1.00, F 0.50
- Link profile: precyzja 0.88, recall 1.00, F 0.93
- Combined: precyzja 1.00, recall 1.00, F 1.00

7 atakow phishingowych (4 unikalne) wykrytych; zaden nie byl wychwycony przez aktualny system Email.cz. Odsetek atakow: 0.0053%.

## Przydatne Cytaty

"The advantage of the proposed solution is that it does not need phishing dataset, which is hard to get, especially for languages other than English." (Abstract, str. 252)

"Phishing is based on entity impersonation. ... This method is using the knowledge that phishing is impersonating some trusted entity to make a user click on the malicious link." (str. 254)

"The company link profile is built from historical data and consists of domains which are referred in the legitimate emails sent by the company." (str. 253)

"Combination of the solutions achieves 100 % F-measure on the portion of live traffic." (Abstract, str. 252)

"None of the detected phishing attacks was detected by system currently used at Email.cz." (str. 256)

## Datasety
- Nazario Phishing Corpus - 4450 emaili phishingowych (2004-2007); standardowy zbior pozytywnych probek phishingu
- SpamAssassin Corpus - 6047 wiadomosci ham/spam (2002-2005); negatywne probki
- Email.cz NER Dataset (wewnetrzny) - 2 mln tekstow emaili, 54,724 zdan, 125,711 tagow (Cnec 2.0, 39 tagow); niepubliczny

## Powiazane Tematy
- Detekcja impersonacji marek/firm jako sygnal phishingu (komplementarny do sygnalu leksykalnego)
- Baseline normalnosci nadawcy oparty na historii komunikacji (profil linkow, DKIM) - powiazanie z baseline personalnym (EXP-4)
- NER w emailach (Alkhereyf & Rambow 2017, Mitra & Gilbert 2013)
- Detekcja phishingu niezalezna od jezyka / bez zbioru treningowego (low-resource)
- DKIM i weryfikacja autentycznosci nadawcy
- Random forest + LDA + NER (Ramanathan & Wechsler 2013) jako baseline
- Brak publicznych zbiorow phishingowych dla jezykow innych niz angielski

## Notatki