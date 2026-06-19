---
title: "Hopper: Modeling and Detecting Lateral Movement"
date: 2021-01-01
authors: "Grant Ho, Mayank Dhiman, Devdatta Akhawe, Vern Paxson, Stefan Savage, Geoffrey M. Voelker, David Wagner"
status: read
doi: "arXiv:2105.13442"
category: "Security"
tags:
  - lateral-movement
  - intrusion-detection
  - authentication-graph
  - anomaly-detection
  - enterprise-security
  - project/graph-phishing-detection
---

# Hopper: Modeling and Detecting Lateral Movement

## Metadane
- **Autorzy**: Grant Ho, Mayank Dhiman, Devdatta Akhawe, Vern Paxson, Stefan Savage, Geoffrey M. Voelker, David Wagner
- **Rok**: 2021
- **Źródło**: USENIX Security Symposium 2021
- **DOI/Link**: arXiv:2105.13442 — https://arxiv.org/abs/2105.13442
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca przedstawia Hopper — system do modelowania i wykrywania ruchu poprzecznego (lateral movement) w sieciach korporacyjnych. Ruch poprzeczny to faza ataku, w której napastnik po uzyskaniu początkowego dostępu (np. przez phishing) przemieszcza się między hostami, eskalując uprawnienia i zbierając dane uwierzytelniające. Hopper buduje graf logowań (login graph), w którym węzłami są użytkownicy i maszyny, a krawędziami zdarzenia uwierzytelniania, i analizuje ścieżki ruchu jako sekwencje powiązanych logowań.

Kluczową ideą jest wykrywanie podejrzanych ścieżek, w których dochodzi do zmiany tożsamości (switch w poświadczeniach) prowadzącej do dostępu, którego dany użytkownik normalnie by nie uzyskał. Hopper rekonstruuje przyczynowe ścieżki logowań, identyfikuje te ze zmianą poświadczeń i braku jasnej legalnej przyczyny, a następnie stosuje detektor oparty o rzadkość/anomalię, aby ograniczyć liczbę alarmów. Na danych z dużej firmy (ponad 700 mln zdarzeń logowania) Hopper wykrywał ataki przy bardzo niskim wskaźniku fałszywych alarmów.

## Kluczowe Wnioski
- Ruch poprzeczny da się modelować jako przyczynowe ścieżki w grafie logowań.
- Ścieżki ze zmianą poświadczeń i nowym dostępem są silnym sygnałem ataku.
- Połączenie reguł przyczynowych z detekcją anomalii drastycznie redukuje fałszywe alarmy.
- System skaluje się do setek milionów zdarzeń uwierzytelniania w przedsiębiorstwie.

## Metodologia
Hopper agreguje logi uwierzytelniania w graf, rekonstruuje ścieżki ruchu (path inference) łącząc powiązane logowania, oznacza ścieżki ze zmianą tożsamości oraz dostępem do nowych hostów. Dla ścieżek bez jednoznacznej legalnej przyczyny stosuje probabilistyczny model rzadkości, by oszacować nietypowość. Ewaluacja na realnych danych korporacyjnych oraz symulowanych scenariuszach ataków red team.

## Główne Koncepcje
- **Lateral movement** — przemieszczanie się napastnika między hostami.
- **Login/authentication graph** — graf użytkownik-maszyna.
- **Causal path inference** — rekonstrukcja przyczynowych sekwencji logowań.
- **Credential switch** — zmiana tożsamości jako sygnał ataku.

## Relevancja dla graph-phishing-detection
Phishing (w tym spear phishing i BEC) jest typowym wektorem początkowego dostępu, po którym następuje ruch poprzeczny. Hopper pokazuje, jak modelować zachowanie po-kompromisowe na grafie uwierzytelniania i wykrywać anomalie ścieżkowe przy ekstremalnie niskim FPR — co bezpośrednio odpowiada celowi projektu (ewaluacja typu Recall@FPR1%). Podejście „graf + ścieżka przyczynowa + detekcja rzadkości" jest przenośne na grafy komunikacji e-mail, gdzie analogiczne ścieżki nadawca-odbiorca ze zmianą wzorca mogą sygnalizować przejęte konto. Stanowi też argument za leak-aware ewaluacją na realnych danych korporacyjnych.
