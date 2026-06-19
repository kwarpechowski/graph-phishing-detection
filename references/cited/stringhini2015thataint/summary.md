---
title: "That Ain't You: Blocking Spearphishing Through Behavioral Modelling"
date: 2015-01-01
authors: "Gianluca Stringhini, Olivier Thonnard"
status: read
doi: "10.1007/978-3-319-20550-2_5"
category: "Security"
tags:
  - spearphishing
  - behavioral-modelling
  - email-security
  - anomaly-detection
  - account-compromise
  - project/graph-phishing-detection
---

# That Ain't You: Blocking Spearphishing Through Behavioral Modelling

## Metadane
- **Autorzy**: Gianluca Stringhini (University College London), Olivier Thonnard (Amadeus)
- **Rok**: 2015 (preprint arXiv:1410.6629, 2014)
- **Źródło**: DIMVA 2015 (Springer LNCS); wersja arXiv:1410.6629
- **DOI/Link**: 10.1007/978-3-319-20550-2_5
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca podejmuje problem wykrywania spear-phishingu, czyli ukierunkowanych wiadomości e-mail, które podszywają się pod zaufaną osobę. Szczególnie trudny przypadek to wiadomości faktycznie wysyłane z przejętego, legalnego konta pracownika organizacji — tradycyjne mechanizmy oparte na reputacji IP, czarnych listach oraz SPF/DKIM są wówczas bezsilne, ponieważ wiadomość pochodzi z autentycznego źródła. Autorzy proponują zmianę paradygmatu: zamiast szukać cech złośliwości w treści, system weryfikuje, czy autorem wiadomości jest rzeczywiście osoba, za którą się podaje.

Zaproponowany system IdentityMailer buduje behawioralny profil nadawcy na podstawie historii wysyłanych przez niego e-maili. Profil obejmuje cechy takie jak typowe godziny aktywności, częstość kontaktów z konkretnymi odbiorcami, używane zwroty grzecznościowe, formuły powitalne i zamykające oraz słowa modalne. Każda nowa wiadomość jest porównywana z modelem zachowania właściciela konta; znaczące odstępstwa są traktowane jako sygnał podszycia. Eksperymenty na rzeczywistych zbiorach e-maili wykazały, że system skutecznie blokuje zaawansowane ataki wysyłane z autentycznych kont oraz że jest odporny na próby uchylania się atakującego.

## Kluczowe Wnioski
- Spear-phishing różni się od spamu i wymaga innego podejścia niż detekcja oparta na treści/reputacji.
- Modelowanie behawioralne autora pozwala wykryć przejęcie konta, którego nie wykrywają SPF/DKIM ani filtry antyspamowe.
- Cechy stylometryczne i metadanowe (czas, odbiorcy, styl) skutecznie odróżniają legalnego nadawcę od atakującego.
- System wykazuje odporność na próby ewazji ze strony świadomego atakującego.

## Metodologia
Uczenie profili behawioralnych per użytkownik na podstawie historycznych wiadomości; ekstrakcja cech stylometrycznych, czasowych i sieci kontaktów; klasyfikacja nowych wiadomości jako zgodnych lub niezgodnych z profilem (wykrywanie anomalii). Ewaluacja na rzeczywistych firmowych zbiorach e-maili wraz z analizą odporności na ewazję.

## Główne Koncepcje
- **Spear-phishing z przejętego konta**: atak wysyłany z autentycznego konta ofiary.
- **Profil behawioralny nadawcy**: model typowego sposobu pisania i wysyłania e-maili.
- **Walidacja autorstwa**: weryfikacja tożsamości autora zamiast detekcji treści.
- **Lateral movement**: poruszanie się atakującego wewnątrz sieci organizacji.

## Relevancja dla graph-phishing-detection
Praca jest klasycznym punktem odniesienia dla detekcji ukierunkowanego phishingu opartej na zachowaniu nadawcy i strukturze kontaktów (sieć korespondencji jako graf komunikacyjny). Cechy takie jak częstość kontaktu między parami nadawca-odbiorca oraz typowe wzorce komunikacji bezpośrednio odpowiadają krawędziom i atrybutom w grafie komunikacyjnym wykorzystywanym w projekcie. Stanowi historyczny kontrapunkt dla podejść grafowo-uczonych (GNN): pokazuje, że proweniencja i kontekst nadawcy są silnym sygnałem, który można sformalizować jako cechy grafowe i wzbogacić o uczenie reprezentacji w grafie wiedzy domenowej dla detekcji BEC/spear-phishingu.
