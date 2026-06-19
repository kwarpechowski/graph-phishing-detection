---
title: "COMPA: Detecting Compromised Accounts on Social Networks"
date: 2013-01-01
authors: "Manuel Egele, Gianluca Stringhini, Christopher Kruegel, Giovanni Vigna"
status: to-read
doi: ""
category: "Security"
tags:
  - compromised-accounts
  - social-networks
  - anomaly-detection
  - behavioral-modeling
  - spam-detection
  - account-security
  - project/graph-phishing-detection
---

# COMPA: Detecting Compromised Accounts on Social Networks

## Metadane
- **Autorzy**: Manuel Egele, Gianluca Stringhini, Christopher Kruegel, Giovanni Vigna
- **Rok**: 2013
- **Źródło**: NDSS 2013 (Network and Distributed System Security Symposium)
- **DOI/Link**: — (brak w metadanych)
- **Status**: to-read
- **Kategoria główna**: Security

## Streszczenie
(Uwaga: brak dołączonego PDF — notatka oparta na metadanych i ogólnej wiedzy o tej znanej pracy; wymaga weryfikacji przy lekturze pełnego tekstu.) COMPA to system do wykrywania przejętych kont (compromised accounts) w sieciach społecznościowych (Twitter, Facebook). Kluczowa idea: zamiast wykrywać konta tworzone od razu jako fałszywe/spamowe, COMPA modeluje normalne zachowanie legalnego użytkownika i wykrywa odchylenia świadczące o przejęciu konta przez atakującego (np. po wykradzeniu poświadczeń lub przez malware).

Dla każdego konta budowane są profile behawioralne na podstawie cech historycznych wiadomości: czas publikacji (godzina dnia), źródło/aplikacja klienta, język, tematy/hashtagi, użyte linki (domeny), oraz interakcje (do kogo kierowane). Nowa wiadomość, która istotnie odbiega od wyuczonego modelu zachowania, jest oznaczana jako anomalia. Aby ograniczyć fałszywe alarmy, COMPA grupuje podobne anomalie (np. wiele kont publikujących nagle ten sam podejrzany link), zakładając, że skompromitowane konta często są nadużywane w skoordynowanych kampaniach.

Praca jest klasycznym odniesieniem w detekcji nadużyć w sieciach społecznościowych i pokazuje skuteczność modelowania behawioralnego oraz korelacji grupowej do wykrywania kont przejętych i kampanii spamowych/phishingowych.

## Kluczowe Wnioski
- Modele zachowania użytkownika pozwalają wykrywać przejęcie konta jako odchylenie od normy.
- Grupowanie podobnych anomalii (kampanie) zwiększa precyzję i redukuje fałszywe alarmy.
- Cechy: czas, klient/źródło, język, temat, linki, odbiorcy interakcji.

## Metodologia
(Do potwierdzenia przy lekturze.) Budowa statystycznych profili behawioralnych per konto; detekcja odchyleń; klastrowanie/korelacja anomalii w kampanie; ewaluacja na dużych zbiorach z Twittera/Facebooka.

## Główne Koncepcje
- **Compromised account** — przejęte legalne konto, w odróżnieniu od konta fałszywego.
- **Behavioral profile** — model normalnego zachowania użytkownika.
- **Korelacja kampanii** — grupowanie skoordynowanych anomalii.

## Relevancja dla graph-phishing-detection
Relewantna dla wątków detekcji anomalii oraz grafów komunikacji w projekcie. Korelowanie skoordynowanych anomalii (wiele kont rozsyłających ten sam link/treść) ma naturalną reprezentację grafową — wspólne URL/domeny/treści łączą konta w klastry kampanii, co bezpośrednio motywuje grafowe wykrywanie kampanii phishingowych i BEC. Modelowanie behawioralne nadawcy (czas, kanał, odbiorcy) wzbogaca cechy węzłów w grafie komunikacji projektu, a idea wykrywania przejętych kont łączy się z detekcją lateral movement i nadużyć zaufanych tożsamości.

## Przydatne Cytaty
- (Do uzupełnienia po lekturze pełnego tekstu.)

## Datasety
- (Do potwierdzenia — duże zbiory wiadomości z Twittera/Facebooka.)

## Powiązane Tematy
- Detekcja spamu i kampanii w sieciach społecznościowych.
- Behawioralne modelowanie użytkownika.
- Grafowe wykrywanie skoordynowanych kampanii.

## Notatki
