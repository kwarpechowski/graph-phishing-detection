---
title: "Web Scraping for Research: Legal, Ethical, Institutional, and Scientific Considerations"
date: 2025-01-01
authors: "Megan A. Brown, Andrew Gruen, Gabe Maldoff, Solomon Messing, Zeve Sanderson, Michael Zimmer"
status: read
doi: "10.1177/20539517251381686"
category: "Data Science"
tags:
  - web-scraping
  - data-access
  - research-ethics
  - data-collection
  - sampling-bias
  - gdpr
  - project/graph-phishing-detection
---

# Web Scraping for Research: Legal, Ethical, Institutional, and Scientific Considerations

## Metadane
- **Autorzy**: Megan A. Brown, Andrew Gruen, Gabe Maldoff, Solomon Messing, Zeve Sanderson, Michael Zimmer
- **Rok**: 2025 (arXiv 2024)
- **Źródło**: Big Data & Society / arXiv:2410.23432
- **DOI/Link**: https://doi.org/10.1177/20539517251381686
- **Status**: read
- **Kategoria główna**: Data Science

## Streszczenie
Praca proponuje kompleksowe ramy (framework) dla web scrapingu w badaniach nauk społecznych (kontekst USA), obejmujące cztery wymiary: prawny, etyczny, instytucjonalny i naukowy. Motywacją jest gwałtowne ograniczenie oficjalnego dostępu do danych platform (zamknięcie darmowego API Twittera/X w 2023, wyłączenie CrowdTangle przez Meta w 2024), które zmusza badaczy do częstszego scrapingu — przy niejasnym, mozaikowym otoczeniu regulacyjnym. Autorzy definiują scraping jako zautomatyzowane zbieranie danych renderowanych na stronie/aplikacji i rozróżniają trzy metody: tradycyjny scraping (parsowanie HTML), nieudokumentowane API oraz wtyczki przeglądarkowe (citizen science).

Część prawna omawia ograniczenia umowne (terms of service, browsewrap vs clickwrap), statutowe (CFAA — kluczowe orzeczenia hiQ v. LinkedIn, Sandvig v. Barr: samo naruszenie ToS bez obejścia kontroli technicznych nie tworzy odpowiedzialności karnej) oraz prawo ochrony prywatności (mozaika USA, sektorowe HIPAA/GLBA/FERPA, stanowe CCPA; GDPR z wyjątkami badawczymi — legitimate interest, zwolnienie z notyfikacji). Omówiono też nowe prawa dostępu (DSA Art. 40, propozycje PATA w USA).

Część naukowa — najistotniejsza metodologicznie — wskazuje cztery zagrożenia walidacji danych scrapowanych: (1) słabe ramy próbkowania (brak losowej próby, nieznana reprezentatywność), (2) brakujące dane w sposób nielosowy, (3) niestabilność temporalna (platformy zmieniają algorytmy/interfejsy bez zapowiedzi), (4) walidność konstruktu (np. "impressions" ≠ rzeczywista konsumpcja). Rekomendacje: strategia próbkowania zamiast convenience sampling, ostrożne kwalifikowanie wniosków, jasne definiowanie subpopulacji; dołączono checklistę dla badaczy.

## Kluczowe Wnioski
- Ograniczenie oficjalnych API zmusza badaczy do scrapingu; otoczenie prawne jest niejasne i wymaga analizy case-by-case.
- Scraping danych publicznych (bez logowania) niesie istotnie niższe ryzyko prawne niż dostęp do treści chronionych.
- Główne zagrożenie naukowe to ramy próbkowania — reprezentatywność danych scrapowanych jest trudna do potwierdzenia.
- Niestabilność temporalna platform zagraża replikowalności i walidności czasowej zbiorów.
- Konieczne: minimalizacja danych, zabezpieczenia prywatności (pseudonimizacja), angażowanie IRB/OGC i archiwów.

## Metodologia
Praca przeglądowo-normatywna (framework + analiza prawa): przegląd orzecznictwa i ustaw USA, GDPR/DSA, wytycznych etycznych (Common Rule, AoIR), oraz problemów naukowych. Wynik: zestaw rekomendacji i checklista (cel badania, zbieranie danych, walidność naukowa, proporcjonalność/mitygacja ryzyka, zaangażowanie instytucjonalne).

## Główne Koncepcje
- **Metody dostępu**: oficjalne API vs nieudokumentowane API vs tradycyjny scraping vs wtyczki przeglądarkowe.
- **Logged-in vs logged-out scraping**: kluczowe dla zakresu danych i ryzyka prawnego.
- **Ramy próbkowania (sampling frame)**: brak kontroli nad reprezentatywnością danych scrapowanych.
- **Niestabilność temporalna**: zmiany platform łamią pipeline'y i obniżają walidność czasową.

## Relevancja dla graph-phishing-detection
Praca jest przewodnikiem metodologicznym i etyczno-prawnym dla pozyskiwania danych do projektu — istotna wszędzie tam, gdzie grafy phishingowe budowane są z danych scrapowanych (domeny, profile, struktury komunikacji, OSINT). Bezpośrednio uzupełnia rygor wymagany przez arp2022dos: ostrzeżenia o słabych ramach próbkowania i niestabilności temporalnej przekładają się na ryzyko sampling bias i data snooping temporalnego w datasetach grafowych, wzmacniając argument za leak-aware ewaluacją i ostrożnym kwalifikowaniem wniosków o generalizowalności. Aspekty prawne/etyczne (GDPR, CFAA, minimalizacja danych, pseudonimizacja) są kluczowe przy budowie korpusu BEC/spear-phishing z realnych danych — temat planowanej publikacji P3 — oraz przy ewentualnym scrapingu OSINT spójnym z pipeline'em bethany2024evaluating.
