---
title: "Scalable Multiplex Network Embedding"
date: 2018-01-01
authors: "Hongming Zhang, Liwei Qiu, Lingling Yi, Yangqiu Song"
status: read
doi: "10.24963/ijcai.2018/428"
category: "Machine Learning"
tags:
  - multiplex-network
  - network-embedding
  - representation-learning
  - scalability
  - multi-relation
  - node-embedding
  - project/graph-phishing-detection
---

# Scalable Multiplex Network Embedding

## Metadane
- **Autorzy**: Hongming Zhang, Liwei Qiu, Lingling Yi, Yangqiu Song (HKUST / Tencent)
- **Rok**: 2018
- **Źródło**: IJCAI 2018
- **DOI/Link**: https://doi.org/10.24963/ijcai.2018/428
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca wprowadza MNE (Multiplex Network Embedding) — skalowalną metodę osadzania sieci multipleksowych, czyli grafów, w których ta sama para węzłów może być połączona wieloma typami relacji (warstwami). Problem polega na nauczeniu reprezentacji, które jednocześnie oddają wspólną tożsamość węzła w całej sieci oraz specyfikę poszczególnych warstw relacji.

Kluczowa idea modelu: każdy węzeł ma jedno wspólne osadzenie (common embedding) reprezentujące informację dzieloną między wszystkimi warstwami oraz dodatkowe, niskowymiarowe osadzenia specyficzne dla każdej warstwy (additional/relation-specific embedding), łączone z osadzeniem wspólnym przez transformację. Dzięki współdzieleniu reprezentacji bazowej model jest oszczędny parametrowo i skalowalny do dużych, wielorelacyjnych sieci, a jednocześnie zachowuje rozróżnialność warstw.

Uczenie odbywa się w stylu skip-gram (na losowych spacerach w obrębie warstw), co umożliwia trening na dużych grafach. Eksperymenty na sieciach wielorelacyjnych (klasyfikacja węzłów, predykcja linków per warstwa) pokazują przewagę MNE nad metodami traktującymi warstwy niezależnie lub agregującymi je naiwnie.

## Kluczowe Wnioski
- Reprezentacja = wspólne osadzenie + osadzenia specyficzne dla warstw.
- Współdzielenie bazy zapewnia skalowalność i oszczędność parametrów.
- MNE przewyższa podejścia per-warstwa i naiwną agregację.
- Model zachowuje informację o specyfice każdego typu relacji.

## Metodologia
Trening skip-gram na losowych spacerach w obrębie warstw; dla węzła uczone jedno osadzenie wspólne oraz niskowymiarowe osadzenia per warstwa łączone transformacją. Ewaluacja: klasyfikacja węzłów i predykcja linków osobno dla każdej warstwy na wielorelacyjnych benchmarkach.

## Główne Koncepcje
- **Multiplex network** — wiele typów relacji między tymi samymi węzłami.
- **Common embedding** — współdzielona reprezentacja bazowa.
- **Relation-specific embedding** — osadzenie per warstwa.
- **Skalowalność** przez współdzielenie parametrów.

## Relevancja dla graph-phishing-detection
MNE jest bezpośrednim fundamentem multipleksowego ujęcia grafu phishingu (publikacja P1 rozprawy — multipleks). W detekcji phishingu naturalnie współistnieje wiele warstw relacji między tymi samymi podmiotami: komunikacyjna (e-mail/połączenie), domenowa (rejestracja/hosting/certyfikat) i transakcyjna. Rozdział na osadzenie wspólne i specyficzne dla warstwy pozwala uchwycić zarówno globalną tożsamość konta/domeny, jak i sygnały charakterystyczne dla konkretnej relacji (np. anomalna warstwa transakcyjna przy normalnej komunikacyjnej). To uzasadnia architekturę wielowarstwową projektu i stanowi klasyczny baseline embeddingowy względem nowszych GNN multipleksowych.
