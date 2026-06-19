---
title: "PhishAri: Automatic Realtime Phishing Detection on Twitter"
date: 2013-01-01
authors: "Anupama Aggarwal, Ashwin Rajadesingan, Ponnurangam Kumaraguru"
status: read
doi: "arXiv:1301.6899"
category: "Security"
tags:
  - phishing-detection
  - social-media-security
  - twitter
  - url-features
  - random-forest
  - real-time-detection
  - project/graph-phishing-detection
---

# PhishAri: Automatic Realtime Phishing Detection on Twitter

## Metadane
- **Autorzy**: Anupama Aggarwal, Ashwin Rajadesingan, Ponnurangam Kumaraguru
- **Rok**: 2013
- **Źródło**: COMSNETS / arXiv (IEEE 2012)
- **DOI/Link**: https://arxiv.org/abs/1301.6899
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca przedstawia PhishAri — system detekcji phishingu na Twitterze działający w czasie rzeczywistym. Autorzy argumentują, że phishing w mediach społecznościowych jest trudniejszy do wykrycia niż w e-mailu z powodu szybkiego rozprzestrzeniania się linków, ograniczenia 140 znaków oraz powszechnego stosowania skróconych URL maskujących cel. PhishAri łączy cztery grupy cech: cechy URL (długość, liczba kropek, subdomeny, przekierowania, warunkowe przekierowania bot/przeglądarka), cechy WHOIS (rejestrator, wiek domeny), cechy tweeta (#hashtagi, @wzmianki, trendujące tagi, retweety) oraz cechy sieciowe/użytkownika (liczba followerów/followee, wiek konta, liczba tweetów).

Zbiór danych zbudowano z 309 321 tweetów zawierających URL (luty–kwiecień 2012), etykietowanych przez blacklisty PhishTank i Google Safebrowsing (po 3-dniowym opóźnieniu), uzyskując 1589 tweetów phishingowych. Spośród trzech klasyfikatorów (Naive Bayes, drzewa decyzyjne, Random Forest) najlepszy okazał się Random Forest z dokładnością 92,52%, recall dla klasy phishing 92,21%. Dodanie cech twitterowych do samych cech URL podniosło dokładność z 82,22% do 92,52%.

System zaimplementowano jako RESTful API (Python, mod_wsgi) oraz rozszerzenie Chrome wyświetlające czerwony/zielony wskaźnik przy tweetach; średni czas klasyfikacji 0,425 s. PhishAri wykrywał 80,6% tweetów phishingowych w "godzinie zerowej", zanim trafiły na blacklisty, oraz przewyższał własny mechanizm Twittera o 84,6%.

## Kluczowe Wnioski
- Połączenie cech URL, WHOIS, treści tweeta i sieci społecznej daje istotnie lepszą detekcję niż same cechy URL.
- Random Forest najlepszy klasyfikator (92,52% dokładności); najważniejsze cechy: okres własności domeny, wiek konta, warunkowe przekierowania, trendujące hashtagi.
- Detekcja w czasie rzeczywistym (godzina zerowa) przewyższa blacklisty, które łapią <20% URL przy zerowej godzinie.
- Realne wdrożenie (rozszerzenie Chrome) potwierdza praktyczną użyteczność.

## Metodologia
Nadzorowana klasyfikacja binarna (phishing/safe) z 5-krotną walidacją krzyżową na zbalansowanym zbiorze (1473 phishing + 1500 safe). Etykietowanie przez blacklisty z opóźnieniem czasowym. Ocena: precision/recall/accuracy oraz analiza ważności cech (permutacyjna w Random Forest).

## Główne Koncepcje
- **Cechy specyficzne dla Twittera**: relacje follower/followee, trendujące hashtagi, @wzmianki jako sygnały phishingu.
- **Warunkowe przekierowanie**: phisher kieruje boty do legalnej strony, a przeglądarki do strony phishingowej.
- **Detekcja w godzinie zerowej**: wykrycie zanim URL trafi na blacklisty.

## Relevancja dla graph-phishing-detection
Praca jest klasycznym, wczesnym przykładem detekcji phishingu opartej na cechach z elementami struktury sieci społecznej (follower/followee, @wzmianki) — stanowi punkt odniesienia dla podejść grafowych. W kontekście projektu jest cennym baseline'em "feature-engineering" pokazującym, że relacje społeczne niosą sygnał phishingowy, który grafowe modele (GNN) mogą wykorzystać bardziej systemowo niż płaskie cechy sieciowe. Dataset etykietowany blacklistami z opóźnieniem ilustruje też problem niedoskonałych etykiet (label inaccuracy) i ewaluacji leak-aware, istotny przy projektowaniu rzetelnych eksperymentów grafowych na phishingu URL/social.
