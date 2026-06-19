---
title: "Efficient Phishing URL Detection Using Graph-based Machine Learning and Loopy Belief Propagation"
date: 2025-01-01
authors: "Wenye Guo, Qun Wang, Hao Yue, Haijian Sun, Rose Qingyang Hu"
status: read
doi: "arXiv:2501.06912"
category: "Security"
tags:
  - phishing-detection
  - url-detection
  - loopy-belief-propagation
  - graph-based-ml
  - heterogeneous-graph
  - network-features
  - project/graph-phishing-detection
---

# Efficient Phishing URL Detection Using Graph-based Machine Learning and Loopy Belief Propagation

## Metadane
- **Autorzy**: Wenye Guo, Qun Wang, Hao Yue, Haijian Sun, Rose Qingyang Hu
- **Rok**: 2025
- **Źródło**: arXiv preprint (San Francisco State Univ. i in.)
- **DOI/Link**: arXiv:2501.06912
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca proponuje grafowy model uczenia maszynowego do detekcji phishingowych URL, integrujący cechy struktury URL z cechami sieciowymi (adresy IP, autorytatywne serwery nazw / nameservery). Motywacją jest fakt, że tradycyjne metody oparte na cechach łańcuchowych URL (słowa, interpunkcja, długość) są łatwo manipulowane przez atakujących, podczas gdy IP i nameservery są stabilniejsze i trudniejsze do podrobienia.

Zbudowano graf heterogeniczny z krawędziami: URL-domena, domena-IP, domena-nameserver, URL-podłańcuchy. Inferencja realizowana jest przez Loopy Belief Propagation (LBP) wariantem min-sum, gdzie obserwowane encje to oznaczone URL treningowe (benign/phishing), a ukryte to URL testowe i encje cech. Wkłady pracy: (1) hybrydowe cechy (URL + IP + nameserver) zwiększające odporność na manipulacje, (2) udoskonalony mechanizm potencjału krawędzi adaptujący się do podobieństwa i relacji etykiet (z karą/progami ths+, ths-), (3) nowa strategia zbieżności polegająca na usuwaniu nieznanych cykli między zmiennymi ukrytymi (poprawia stabilność i powtarzalność), (4) testy na większych i nowo zebranych zbiorach.

Prawdopodobieństwa a priori węzłów pochodzą z modelu Random Forest. Eksperymenty: bazy to Logistic Regression, Random Forest, Naive Bayes. Wektoryzacja encji przez word2vec + Locally Linear Embedding (LLE). Wyniki: nowy model osiąga F1 do 98.77% na największym zbiorze (306 354 próbek), z konsekwentną poprawą nad RF (>4% F1) i wzrostem dzięki strategii zbieżności (>7% F1).

## Kluczowe Wnioski
- Cechy sieciowe (IP, nameservery) są stabilniejsze niż cechy łańcuchowe URL i zwiększają odporność na ewazję.
- Potencjał krawędzi oparty na podobieństwie z progami przewyższa schemat statyczny 0.5+-epsilon.
- Strategia "usuwania nieznanych cykli" poprawia zbieżność LBP (+88% wskaźnika zbieżności, +3.4% F1) i powtarzalność.
- Prior z Random Forest poprawia F1 o ~8.86%; model skaluje się do dużych zbiorów (F1 98.77% przy 306k próbek).

## Metodologia
Konstrukcja grafu heterogenicznego URL/domena/IP/nameserver/podłańcuchy; min-sum LBP z propagacją wiadomości do zbieżności; potencjał krawędzi z cosine/RBF similarity + progi; prior z RF; 5-fold CV równoległe; selekcja cech metodą łokcia (elbow). Metryki: accuracy, precision, recall, F1; ROC dla progu klasyfikacji (optymalny 0.5).

## Główne Koncepcje
- **Loopy Belief Propagation (LBP)** — propagacja wiadomości na grafie z cyklami (min-sum).
- **Potencjał krawędzi** — łączne prawdopodobieństwo etykiet sąsiadów, adaptowane podobieństwem.
- **Cechy sieciowe** — IP i autorytatywne nameservery jako odporne sygnały.
- **Usuwanie nieznanych cykli** — strategia zapewniająca zbieżność.

## Relevancja dla graph-phishing-detection
To jest wręcz rdzeniowa referencja dla projektu — łączy phishing URL z grafowym podejściem nad strukturą domena/IP/nameserver, czyli dokładnie "graf domenowy" w projekcie. Stanowi konkretny baseline metodyczny (LBP + RF prior) oraz silny punkt odniesienia wynikowy (F1 98.77%), który projektowy uczony GNN ma starać się pobić, zwłaszcza pod kątem Recall przy niskim FPR. Idea wykorzystania stabilnych cech sieciowych (IP, NS) odpornych na manipulację adwersarza jest bezpośrednio przenośna do modelowania struktur grafowych domeny/transakcji. Praca pokazuje też proceduralnie konstrukcję grafu heterogenicznego phishingu i znaczenie powtarzalnej, stabilnej inferencji, co wspiera rygorystyczną ewaluację projektu.

## Przydatne Cytaty
- "modifying nameservers and IP addresses is more difficult" (Sekcja III).
- "deleting unknown cycles, boosts the F1 score of the phishing detection model by more than 7%" (Conclusions).

## Datasety
- Zbiór z Kim et al. [7] (network-based, robust to evasion) oraz nowo zebrane zbiory (53 871 / 100 000 / 306 354 próbek URL benign+phishing).

## Powiązane Tematy
- Network-based inference dla phishingu (Polonium, Kim et al.).
- Osadzenia węzłów (node2vec, deepwalk, LLE).
- Transformerowe modele detekcji URL (URLTran).

## Notatki
