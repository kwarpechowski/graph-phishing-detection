---
title: "Characterizing the Networks Sending Enterprise Phishing Emails"
date: 2024-01-01
authors: "Elisa Luo, Liane Young, Grant Ho, M. H. Afifi, Marco Schweighauser, Ethan Katz-Bassett, Asaf Cidon"
status: read
doi: "10.48550/arXiv.2412.12403"
category: "Security"
tags:
  - phishing-detection
  - enterprise-security
  - email-security
  - network-analysis
  - email-infrastructure
  - blocklists
  - cloud-hosting
  - random-forest
  - temporal-analysis
  - project/spear-phishing-context
  - project/phishing-detection
---

# Characterizing the Networks Sending Enterprise Phishing Emails

## Metadane
- **Autorzy**: Elisa Luo, Liane Young, Grant Ho, M. H. Afifi, Marco Schweighauser, Ethan Katz-Bassett, Asaf Cidon
- **Rok**: 2024
- **Źródło**: arXiv:2412.12403 (Columbia University / Barracuda Networks / UC San Diego / University of Chicago)
- **DOI/Link**: arXiv:2412.12403
- **Status**: read
- **Kategoria główna**: Security
- **Tagi**: `#phishing-detection` `#enterprise-security` `#email-security` `#network-analysis` `#email-infrastructure` `#blocklists` `#cloud-hosting` `#random-forest` `#temporal-analysis`

## Streszczenie

Artykuł prezentuje pierwszą dużą skalę analizę infrastruktury sieciowej odpowiedzialnej za dostarczanie emaili phishingowych do przedsiębiorstw. Autorzy (Columbia University + Barracuda Networks) analizują nagłówki SMTP z datasetu 800,000+ dostarczonych emaili phishingowych i 4 miliardów czystych emaili, zebranych w trzech miesięcznych okrętach (styczeń 2020, październik 2020, styczeń 2021) ze skrzynek odbiorczych tysięcy organizacji korzystających z Microsoft Office 365.

Zaskakujące odkrycie: ponad 1/3 emaili phishingowych pochodzi z wysoce reputowanych sieci — Amazon AWS i Microsoft Azure — pomimo że stanowią one ułamek ich całkowitego ruchu emailowego. Sieci te są stabilne w czasie, co czyni je niemożliwymi do zablokowania przez statyczne blocklisy. Jednocześnie ok. 40% phishingu pochodzi z sieci o wysokiej koncentracji phishingu (≥2% emaili), które jednak są w większości tymczasowe — pojawiają się i znikają w ciągu dni lub tygodni, atakując z krótkich burstów.

Na podstawie analizy autorzy wdrożyli w środowisku produkcyjnym Barracuda dynamiczny klasyfikator oparty na cechach sieciowych aktualizowanych codziennie (IP phishing probability + volume). Przez 4.5 miesiąca klasyfikator wykrywał dodatkowo 3-5% wcześniej niewidocznych ataków phishingowych bez fałszywie pozytywnych wyników.

## Kluczowe Wnioski

- **1/3 phishingu pochodzi z Amazon/Microsoft**: Amazon (AS 14618, AS 16509) i Microsoft (AS 8075) odpowiadają za 31% phishingu — ale phishing stanowi <0.01% ich całkowitego ruchu; blocklisy IP ich nie blokują
- **Trzy typy sieci**: low concentration (<0.1% phishing, stabilne), medium (0.1-2%), high (≥2%, 39.7% phishingu, głównie tymczasowe)
- **Infrastruktura phishingowa jest niestabilna**: większość high-concentration AS jest aktywna tylko przez 1 miesiąc; zaledwie 9 AS (6.8%) utrzymuje wysoką koncentrację przez wszystkie 3 okresy
- **80% phishingu pochodzi z 100 AS** — ale te same AS generują 70% czystego ruchu; nie da się ich zblokować
- **Statyczne blocklisy zawodzą**: nie aktualizują się dość szybko wobec burstowych ataków; atakujący zmieniają infrastrukturę po detekcji
- **Autentykacja (SPF/DKIM/DMARC) jest słabym sygnałem**: 10.4% phishingu przechodzi DMARC, <50% czystych emaili też go przechodzi
- **Dynamiczne cechy sieciowe działają**: +3-5% detekcji w produkcji bez FP — przez aktualizację codzienną IP phishing probability

## Metodologia

Dataset: Barracuda Networks — SMTP nagłówki emaili z organizacji Office 365 (3 okresy: Jan 2020, Oct 2020, Jan 2021). Oznaczenia phishingu przez komeryjne detektory Barracuda (precision >99%). Mapowanie IP→AS przez Cymru API, geolokalizacja przez MaxMind GeoLite2. 

Kategoryzacja sieci: low/medium/high concentration per AS (próg: <0.1%, 0.1-2%, ≥2% phishingu + min. 150 emaili/miesiąc). Analiza stabilności przez porównanie trzech snapshot'ów. Produkcyjny klasyfikator: Random Forest z 12 cechami (IP phishing probability, IP phishing volume, AS phishing probability, mail path length, AS phishing volume, # countries in path, SPF/DKIM/DMARC); wdrożono tylko 2 najważniejsze cechy z aktualizacją dzienną przez sliding window n-dniowe.

## Główne Koncepcje

- **AS (Autonomous System)**: autonomiczny system sieciowy; używany jako jednostka analizy reputacji sieci emailowej
- **Phishing concentration**: frakcja emaili z danego AS, które są phishingiem; low (<0.1%), medium (0.1-2%), high (≥2%)
- **Originating IP address**: pierwszy publiczny adres IP w ścieżce RECEIVED headers — rzeczywisty punkt wysyłki
- **Low concentration networks**: Amazon AWS i Microsoft Azure — duże wolumeny phishingu, ale znikomy odsetek ogólnego ruchu; trudne do zablokowania
- **High concentration networks**: hosting companies z ≥2% phishingu; wysoka rotacja, burst sending (30 min – kilka dni), często tymczasowe
- **Phishing campaign**: emaile o tym samym FROM address i znormalizowanej linii tematycznej
- **IaaS abuse**: nadużycie Infrastructure-as-a-Service (AWS EC2, Azure Cloud) do uruchamiania serwerów phishingowych
- **SMTP RECEIVED header**: nagłówek zapisujący adres IP każdego relay serwera w ścieżce dostarczania emaila

## Wyniki

| Kategoria sieci | # AS (Jan 2020) | % phishingu | Stabilność |
|----------------|-----------------|-------------|------------|
| Low concentration | 608 | 26.6% | Wysoka (Amazon/Microsoft) |
| Medium concentration | 1031 | 25.4% | Średnia |
| High concentration | 62 | 42.5% | Niska (80%+ tymczasowe) |

Najważniejsze cechy (Random Forest, Gini importance): IP phishing probability (0.40) > IP phishing volume (0.30) > AS phishing probability (0.10) > mail path length (0.07). SPF/DKIM/DMARC — niemal nieistotne.

Produkcja: +3-5% detekcji/dzień przez 4.5 miesiąca, 0 fałszywie pozytywnych na ręczną inspekcję.

## Przydatne Cytaty

> "Surprisingly, we find that over one-third of the phishing email in our dataset originates from highly reputable networks, including Amazon and Microsoft." (Abstract)

> "In a production environment over a period of 4.5 months, our new detector was able to identify 3-5% more enterprise email attacks that were previously undetected by the company's existing classifiers." (Abstract)

> "Network phishing behavior over time is an important consideration for detection: Our results showed that some networks have highly variable amounts and/or proportions of phishing emails that they send over time. This phenomenon provides a possible explanation for why static lists of suspicious sender IP addresses or ASes, such as those used by many organizations in our dataset, prove insufficient at defending against enterprise phishing attacks." (str. 24)

> "The rise of Infrastructure-as-a-Service (IaaS) has provided an easy path for attackers to acquire infrastructure, with servers on prominent and reputable cloud hosting providers, such as Amazon AWS and Microsoft Azure, being responsible for nearly one-third of all phishing emails in our dataset." (str. 24)

## Datasety

- Barracuda Networks enterprise email dataset (proprietary): 800k+ phishing + 4B clean emaili, 3 miesiące (niedostępny publicznie)

## Powiązane Tematy

- Sieciowa infrastruktura phishingu vs. treść emaila: komplementarne sygnały detekcji
- IaaS abuse: AWS EC2 i Azure Cloud jako platformy do budowania serwerów phishingowych
- Dynamiczne vs. statyczne cechy reputacji: dlaczego statyczne blocklisy nie wystarczają
- Account takeover jako wektor phishingu: powiązanie z Ho et al. 2019 (lateral phishing)
- SPF/DKIM/DMARC — niewystarczające jako sygnały detekcji phishingu (10.4% phishingu przechodzi DMARC)
- Temporal features w detekcji: sliding window reputacji IP jako skuteczne uzupełnienie content-based detekcji

## Notatki

