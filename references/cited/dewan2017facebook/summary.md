---
title: "It Doesn't Break Just on Twitter: Characterizing Facebook Content During Real World Events (Facebook Inspector)"
date: 2017-01-01
authors: "Prateek Dewan, Ponnurangam Kumaraguru"
status: read
doi: "10.1007/s13278-017-0434-5"
category: "Security"
tags:
  - social-media-security
  - spam-detection
  - malicious-content
  - facebook
  - stylometry
  - real-time-detection
  - project/graph-phishing-detection
---

# Facebook Inspector (FbI): Towards Automatic Real-Time Detection of Malicious Content on Facebook

## Metadane
- **Autorzy**: Prateek Dewan, Ponnurangam Kumaraguru
- **Rok**: 2017
- **Zrodlo**: Social Network Analysis and Mining (SNAM) / IIIT-Delhi
- **DOI/Link**: https://doi.org/10.1007/s13278-017-0434-5
- **Status**: read
- **Kategoria glowna**: Security

## Streszczenie
Praca charakteryzuje tresci publikowane na Facebooku podczas 16 rzeczywistych wydarzen (real world events) i porownuje je z trescia z Twittera, a nastepnie buduje system detekcji zlosliwych tresci. Autorzy podkreslaja, ze - mimo iz Facebook jest piec razy wiekszy od Twittera - jego tresci byly slabo badane ze wzgledu na restrykcyjne ustawienia prywatnosci (ok. 72% uzytkownikow ustawia posty jako prywatne).

Analiza ujawnia, ze ponad 30% publicznych tresci obecnych na Facebooku podczas wydarzen wystepowalo rownież na Twitterze, a ponad 10% najaktywniejszych uzytkownikow w obu sieciach publikuje spam. Wykorzystujac cechy stylometryczne tekstu postow i tweetow, autorzy klasyfikuja tresci zlosliwe, osiagajac dokladnosc ponad 99% dla Facebooka i ponad 98% dla Twittera. Praca prowadzi do narzedzia Facebook Inspector (FbI) do wykrywania zlosliwych tresci w czasie rzeczywistym.

## Kluczowe Wnioski
- Istotna czesc publicznych tresci pokrywa sie miedzy Facebookiem a Twitterem podczas duzych wydarzen.
- Ponad 10% najaktywniejszych uzytkownikow rozsiewa spam podczas wydarzen.
- Cechy stylometryczne pozwalaja klasyfikowac zlosliwe tresci z bardzo wysoka dokladnoscia (>98-99%).
- Mozliwa jest detekcja zlosliwych tresci w czasie rzeczywistym (FbI).

## Metodologia
Zbieranie publicznych tresci z Facebooka i Twittera wokol 16 wydarzen; analiza ilosciowa i jakosciowa; ekstrakcja cech stylometrycznych z tekstu; trening klasyfikatora rozrozniajacego tresci zlosliwe/spam od legalnych; wdrozenie jako narzedzie czasu rzeczywistego.

## Glowne Koncepcje
- **Stylometria** - cechy stylu pisania uzyte do klasyfikacji.
- **Malicious / spam content** - zlosliwe tresci w sieciach spolecznosciowych.
- **Cross-platform analysis** - porownanie tresci Facebook vs Twitter.
- **Real-time detection** - detekcja w czasie zblizonym do rzeczywistego.

## Relevancja dla graph-phishing-detection
Praca dostarcza kontekstu dla detekcji zlosliwych tresci w sieciach spolecznosciowych - srodowiska, w ktorym phishing i spam sa rozsiewane przez aktorow o charakterystycznych wzorcach behawioralnych. Identyfikacja najaktywniejszych uzytkownikow-spammerow oraz cech stylometrycznych moze zasilac atrybuty wezlow w grafowej detekcji fraudu/anomalii. Cross-platformowa propagacja tych samych tresci motywuje warstwowe (multipleksowe) ujecie roznych kanalow oraz potrzebe rozdzielczosci tozsamosci aktorow miedzy platformami w grafie wiedzy domenowej.
