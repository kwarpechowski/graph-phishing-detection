---
title: "Mathematical Formulation of Multilayer Networks"
date: 2013-01-01
authors: "Manlio De Domenico, Albert Sole-Ribalta, Emanuele Cozzo, Mikko Kivela, Yamir Moreno, Mason A. Porter, Sergio Gomez, Alex Arenas"
status: read
doi: "10.1103/PhysRevX.3.041022"
category: "Theory"
tags:
  - multilayer-networks
  - multiplex-networks
  - tensor-formulation
  - network-science
  - centrality
  - project/graph-phishing-detection
---

# Mathematical Formulation of Multilayer Networks

## Metadane
- **Autorzy**: Manlio De Domenico, Albert Sole-Ribalta, Emanuele Cozzo, Mikko Kivela, Yamir Moreno, Mason A. Porter, Sergio Gomez, Alex Arenas
- **Rok**: 2013
- **Zrodlo**: Physical Review X, vol. 3, 041022
- **DOI/Link**: https://doi.org/10.1103/PhysRevX.3.041022
- **Status**: read
- **Kategoria glowna**: Theory

## Streszczenie
Praca wprowadza spojny formalizm matematyczny do opisu sieci wielowarstwowych (multilayer networks). Autorzy argumentuja, ze klasyczna reprezentacja macierza sasiedztwa jest niewystarczajaca dla sieci multipleksowych i zaleznych od czasu, ktore wystepuja w wiekszosci rzeczywistych i inzynierskich systemow posiadajacych wiele podsystemow i warstw lacznosci.

Rozwiazaniem jest framework tensorowy: sieci wielowarstwowe opisuje sie tensorami wyzszego rzedu zamiast macierzy. Autorzy uogolniaja na ten formalizm szereg kluczowych deskryptorow sieci i procesow dynamicznych - miedzy innymi centralnosc stopnia, wspolczynniki klasteryzacji, centralnosc wektora wlasnego, modularnosc, entropie von Neumanna oraz dyfuzje. Pokazuja, jak z ogolnego ujecia odzyskac znane wyniki dla przypadkow szczegolnych (sieci jednowarstwowe i multipleksowe).

## Kluczowe Wnioski
- Macierze sasiedztwa nie wystarczaja do opisu sieci multipleksowych i temporalnych - potrzebny jest formalizm tensorowy.
- Klasyczne deskryptory (centralnosci, modularnosc, dyfuzja) mozna spojnie uogolnic na wiele warstw.
- Wybory konstrukcyjne (np. krawedzie miedzywarstwowe) istotnie wplywaja na wartosci deskryptorow.
- Framework umozliwia analize wplywu i przeplywu informacji w sieciach wielokanalowych.

## Metodologia
Praca teoretyczna/formalna: definicja tensorow sasiedztwa dla sieci wielowarstwowych, algebra tensorowa do reprezentacji warstw i krawedzi miedzywarstwowych, oraz wyprowadzenie uogolnionych metryk i operatorow dynamicznych.

## Glowne Koncepcje
- **Multilayer / multiplex network** - siec z wieloma typami warstw/krawedzi.
- **Tensorial framework** - reprezentacja tensorami zamiast macierzy.
- **Interlayer edges** - krawedzie laczace ten sam wezel w roznych warstwach.
- **Uogolnione deskryptory** - centralnosci, modularnosc, dyfuzja dla wielu warstw.

## Relevancja dla graph-phishing-detection
To fundament teoretyczny dla multipleksowo-temporalnej reprezentacji grafu w projekcie. Phishing/BEC obejmuje wiele typow relacji jednoczesnie: komunikacje e-mail, powiazania domen, transakcje, hosting - kazda jako odrebna warstwa multipleksu. Formalizm tensorowy De Domenico daje scisly jezyk do laczenia tych warstw i definiowania krawedzi miedzywarstwowych, co jest podstawa pierwszej (gotowej) publikacji rozprawy o multipleksie. Uogolnione miary centralnosci i dyfuzji moga sluzyc jako cechy lub baseline dla GNN dzialajacego na grafie wielowarstwowym.
