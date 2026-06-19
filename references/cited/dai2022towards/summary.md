---
title: "Towards Robust Graph Neural Networks for Noisy Graphs with Sparse Labels"
date: 2022-01-01
authors: "Enyan Dai, Wei Jin, Hui Liu, Suhang Wang"
status: read
doi: "10.1145/3488560.3498408"
category: "Machine Learning"
tags:
  - graph-neural-networks
  - robustness
  - noisy-edges
  - sparse-labels
  - semi-supervised-learning
  - message-passing
  - project/graph-phishing-detection
---

# Towards Robust Graph Neural Networks for Noisy Graphs with Sparse Labels

## Metadane
- **Autorzy**: Enyan Dai, Wei Jin, Hui Liu, Suhang Wang
- **Rok**: 2022
- **Zrodlo**: WSDM '22 (Fifteenth ACM Int. Conf. on Web Search and Data Mining), Tempe, AZ
- **DOI/Link**: https://doi.org/10.1145/3488560.3498408 (arXiv:2201.00232)
- **Status**: read
- **Kategoria glowna**: Machine Learning

## Streszczenie
Praca podejmuje problem trenowania grafowych sieci neuronowych (GNN) w realistycznych warunkach: grafy zawieraja szum strukturalny (zaszumione/adwersaryjne krawedzie) i maja niewiele oznaczonych wezlow. Autorzy pokazuja, ze zarowno zaszumione krawedzie, jak i ograniczona liczba etykiet psuja mechanizm propagacji wiadomosci (message passing), na ktorym opiera sie GNN, prowadzac do znacznego spadku wydajnosci.

Proponowany framework wykorzystuje zaszumione krawedzie jako sygnal nadzoru do nauczenia odszumionego i zageszczonego grafu, ktory potrafi obnizyc wage lub usunac krawedzie szumowe oraz dodac brakujace, korzystne polaczenia. Wygenerowane krawedzie sluza nastepnie do regularyzacji predykcji wezlow nieoznaczonych poprzez gladkosc etykiet (label smoothness), co lepiej trenuje GNN przy malej liczbie etykiet. Eksperymenty na rzeczywistych zbiorach potwierdzaja odpornosc podejscia.

## Kluczowe Wnioski
- Zaszumione krawedzie i rzadkie etykiety lacznie degraduja propagacje wiadomosci w GNN.
- Mozna uczyc sie odszumionego, gestszego grafu, traktujac strukture jako parametr do optymalizacji.
- Regularyzacja przez gladkosc etykiet wykorzystuje wezly nieoznaczone i lagodzi problem rzadkich etykiet.
- Wspolne uczenie struktury i klasyfikatora poprawia odpornosc na atak strukturalny.

## Metodologia
Framework laczacy: (1) uczenie struktury grafu (link prediction sterowany cechami i istniejaca topologia), (2) down-weighting/usuwanie krawedzi szumowych i dodawanie krawedzi miedzy podobnymi wezlami, (3) semi-nadzorowana klasyfikacja wezlow z regularyzacja gladkosci etykiet. Ewaluacja na benchmarkach z wstrzyknietym szumem i atakami adwersaryjnymi na strukture.

## Glowne Koncepcje
- **Noisy edges** - krawedzie bledne lub adwersaryjne zaburzajace agregacje.
- **Graph structure learning** - uczenie odszumionej macierzy sasiedztwa.
- **Label smoothness regularization** - wymuszanie podobnych predykcji na polaczonych wezlach.
- **Sparse labels** - reżim z bardzo mala liczba oznaczonych wezlow.

## Relevancja dla graph-phishing-detection
To jedna z kluczowych prac metodycznych dla projektu. Grafy w phishingu (komunikacja, domeny, transakcje) sa z natury zaszumione (bledne ER, przypadkowe wspoldzielone hosty/IP) i maja bardzo malo etykiet (potwierdzone ataki BEC sa rzadkie). Mechanizm uczenia odszumionej struktury wprost adresuje wyzwanie z planu drugiej publikacji rozprawy: uczony GNN ze spojnoscia i indukcja. Odpornosc na adwersaryjne krawedzie jest istotna wobec adaptacyjnego napastnika, a regularyzacja przez gladkosc etykiet jest bezposrednio uzyteczna w ewaluacji leak-aware przy ekstremalnie rzadkich etykietach.
