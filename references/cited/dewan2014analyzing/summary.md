---
title: "Analyzing Social and Stylometric Features to Identify Spear Phishing Emails"
date: 2014-01-01
authors: "Prateek Dewan, Anand Kashyap, Ponnurangam Kumaraguru"
status: read
doi: "10.48550/arXiv.1406.3692"
category: "Security"
tags:
  - phishing-detection
  - spear-phishing
  - stylometric-features
  - osint
  - linkedin
  - social-features
  - random-forest
  - enterprise-security
  - apt
  - project/spear-phishing-context
---

# Analyzing Social and Stylometric Features to Identify Spear Phishing Emails

## Metadane
- **Autorzy**: Prateek Dewan, Anand Kashyap, Ponnurangam Kumaraguru
- **Rok**: 2014
- **Źródło**: arXiv:1406.3692 (IIIT-Delhi / Symantec Research Labs)
- **DOI/Link**: arXiv:1406.3692
- **Status**: read
- **Kategoria główna**: Security
- **Tagi**: `#phishing-detection` `#spear-phishing` `#stylometric-features` `#osint` `#linkedin` `#social-features` `#random-forest` `#enterprise-security` `#apt`

## Streszczenie

Artykuł bada, czy publicznie dostępne informacje z profili LinkedIn ofiar mogą wspomagać automatyczną detekcję spear phishingu. Autorzy charakteryzują zbiór prawdziwych emaili spear phishingowych z systemu skanowania poczty Symantec (4,742 targetowanych emaili do 2,434 ofiar z 14 międzynarodowych organizacji) oraz zbiór emaili niezargetowanych (9,353 emaili spam/phishing do 5,912 odbiorców), uzupełniając go 6,601 benignowymi emailami z datasetu Enron.

Dla każdego odbiorcy zebrano profil LinkedIn (łącznie ~9,588 profili przez LinkedIn People Search API — proces trwał 4 miesiące ze względu na limity API). Ekstrakcja cech objęła 18 cech stylometrycznych z emaili (cechy tematu, treści, załącznika) i 9 cech socjalnych z LinkedIn (lokalizacja, liczba połączeń, job level/type, bogactwo podsumowania). Testowano 4 klasyfikatory (Random Forest, J48, Naive Bayes, Decision Table) z 10-fold cross-validation na Weka.

Zaskakujący wynik: cechy socjalne z LinkedIn **nie pomagają** w identyfikacji spear phishingu — email features alone osiągają 98.28% accuracy (Random Forest, SPEAR vs SPAM), natomiast połączenie email + social features spada do 96.47%. Najsilniejszą cechą dyskryminującą są cechy załączników (attachment size: information gain 0.631), a nie cechy treści czy profili LinkedIn.

## Kluczowe Wnioski

- **LinkedIn nie pomaga**: w 2 z 3 scenariuszy klasyfikacji cechy socjalne LinkedIn obniżają accuracy — atakujący w zbiorze Symantec najwyraźniej nie wykorzystywali LinkedIn do personalizacji ataków
- **Cechy załączników dominują**: attachment size (IG=0.631) i length of attachment name (IG=0.485) — spear phishing attachments są nazwane bardziej realistycznie i mają mniejszą wariancję rozmiaru niż spam
- **Najlepsza accuracy**: 98.28% (Random Forest, email features only) dla SPEAR vs SPAM; 97.39% dla SPEAR vs BENIGN
- **Cechy tematu słabe**: subject features osiągają max 83.91% — sam temat emaila nie wystarczy do detekcji
- **APT charakterystyka**: spear phishing rósł o 238% vs 35,422% wzrostu spam/phishing — stabilniejsza, celowa aktywność
- **Ograniczenie**: LinkedIn API pozwalało znaleźć profil tylko dla 1 na 10 odbiorców — zbyt mała pokrywalność dla solidnych wniosków

## Metodologia

Dane: Symantec enterprise email scanning service (marzec 2009 – grudzień 2013). Podział: SPEAR (4,742 targetowanych emaili, 2,434 ofiary z 14 organizacji), SPAM (9,353 emaili, 5,912 odbiorców), BENIGN (6,601 emaili Enron, 1,240 pracowników). Trzy scenariusze klasyfikacji: SPEAR vs SPAM, SPEAR vs BENIGN, SPEAR vs SPAM+BENIGN.

Feature engineering: 18 stylometrycznych cech z emaila (subject: 7, attachment: 2, body: 9) + 9 socjalnych z LinkedIn (Location, numConnections, 5× summary features, jobLevel, jobType). Klasyfikacja: Random Forest, J48 Decision Tree, Naive Bayesian, Decision Table (Weka, 10-fold CV). Feature importance przez InfoGainAttributeEval.

## Główne Koncepcje

- **APT (Advanced Persistent Threat)**: długoterminowe, ukierunkowane ataki cybernetyczne infekujące infrastrukturę organizacji; spear phishing jest głównym wektorem wejścia
- **Stylometric features**: cechy bazujące na strukturze i stylu pisania emaila — liczba słów, znaków, wyjątkowość słów, bogactwo (richness = words/chars)
- **Social features (LinkedIn)**: lokalizacja, liczba połączeń, job level (0-7: Support→Executive), job type (0-9: Engineering→Sales), bogactwo podsumowania
- **Information gain**: miara dyskryminatywności cechy (0-1); attachment size IG=0.631 — najwyższy w zbiorze
- **Richness**: stosunek liczby słów do liczby znaków — miara gęstości informacyjnej tekstu
- **SPEAR/SPAM/BENIGN**: trzy klasy emaili używane do ewaluacji (spear phishing, niezargetowane ataki, benignowe emaile Enron)

## Wyniki

| Scenariusz | Feature set | Random Forest accuracy |
|-----------|-------------|----------------------|
| SPEAR vs SPAM | Email only (9) | **98.28%** |
| SPEAR vs SPAM | Email + Social (18) | 96.47% |
| SPEAR vs SPAM | Social only (9) | 81.73% |
| SPEAR vs BENIGN | Email only (16) | **97.39%** |
| SPEAR vs BENIGN | Email + Social (25) | 97.04% |
| SPEAR vs SPAM+BENIGN | Email + Social (16) | 89.86% |

Najważniejsze cechy (SPEAR vs SPAM): attachment size (IG=0.631), attachment name length (IG=0.485), subject richness (IG=0.279). Cechy LinkedIn (poza Location i numConnections) nie weszły do top 10 najbardziej informacyjnych.

## Przydatne Cytaty

> "Our analysis revealed that social features extracted from LinkedIn do not help in identifying spear phishing emails." (Abstract)

> "We achieved an overall maximum accuracy of 98.28% without the social features." (Abstract)

> "It is likely that in a real-world scenario, an attacker may be able to gain much more information about a victim prior to the attack. This could include looking for the victim's profile on other social networks like Facebook, Twitter etc., looking for the victim's presence on the Internet in general, using search engines (Google, Bing etc.), and profiling websites like Pipl, Yasni etc." (str. 12)

> "We believe that it is safe to conclude that publicly available content on an employee's LinkedIn profile was not used to send her targeted spear phishing emails in our dataset. However, we cannot rule out the possibility of such an attack outside our dataset, or in future." (str. 12)

## Datasety

- Symantec enterprise email dataset (proprietary): 4,742 SPEAR + 9,353 SPAM emaili z 14 org. (niedostępny publicznie)
- [Enron Email Dataset](../../datasets/enron-corpus.md) — 6,601 benignowych emaili jako klasa bazowa

## Powiązane Tematy

- Stylometria vs OSINT jako cechy detekcji spear phishingu: wniosek, że email content jest silniejszym sygnałem niż profil ofiary
- LinkedIn API limitations: tylko 1/10 odbiorców znalezionych — problem pokrywalności OSINT
- APT kill chain: spear phishing jako wektor wejścia dla APT
- Context-aware phishing (Jagatic et al. 2007): 4.5× wyższy sukces z kontekstem społecznym — napięcie z wynikami tej pracy
- Facebook/Twitter jako alternatywne źródła OSINT (niezbadane w tej pracy)
- Generalizacja: czy wyniki z 2014 są nadal aktualne w erze LLM-generated spear phishing?

## Notatki

