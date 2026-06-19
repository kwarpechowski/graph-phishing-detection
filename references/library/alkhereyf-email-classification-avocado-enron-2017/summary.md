---
title: "Work Hard, Play Hard: Email Classification on the Avocado and Enron Corpora"
date: 2017-01-01
authors: "Sakhar Alkhereyf, Owen Rambow"
status: read
doi: ""
category: "Natural Language Processing"
tags:
  - email-classification
  - avocado-corpus
  - enron-corpus
  - social-network-features
  - graph-features
  - business-personal
  - svm
  - extra-trees
  - cross-corpus
  - project/personalized-phishing-defense
---

# Work Hard, Play Hard: Email Classification on the Avocado and Enron Corpora

## Metadane
- **Autorzy**: Sakhar Alkhereyf, Owen Rambow (Columbia University)
- **Rok**: 2017
- **Zrodlo**: Proceedings of TextGraphs-11: Workshop on Graph-based Methods for NLP, ACL 2017, str. 57-65 (ACL Anthology W17-2408)
- **DOI**: brak (ACL Anthology W17-2408)
- **Status**: `#read`
- **Kategoria**: Natural Language Processing
- **Tagi**: `#email-classification` `#avocado-corpus` `#enron-corpus` `#social-network-features` `#graph-features` `#business-personal` `#svm` `#extra-trees` `#cross-corpus`

## Streszczenie

Praca przedstawia empiryczne studium klasyfikacji emaili do dwoch kategorii: "Business" (sluzbowe) i "Personal" (prywatne). Modele sa trenowane wylacznie na korpusie Enron, a testowane na Enron oraz na korpusie Avocado, co pozwala badac jak bardzo nauczone modele zaleza od korpusu treningowego (setting cross-corpora: trenuj na jednej firmie, stosuj na innej). Kluczowy wynik: cechy wyekstrahowane z sieci wymiany emaili (email exchange network) reprezentowanej jako graf spoleczny poprawiaja klasyfikacje ponad to, co daja same cechy leksykalne.

Avocado to istotny wklad metodologiczny: w lutym 2015 Linguistic Data Consortium udostepnilo (LDC2015T03) zbior emaili z anonimowej, nieistniejacej juz firmy IT okreslanej jako "Avocado". Stanowi to drugi, obok publicznie dostepnego Enronu, duzy korpus prawdziwych emaili firmowych - wazna alternatywa dla Enrona dla badan wymagajacych realnych danych przedsiebiorstwa. Autorzy reprezentuja siec wymiany emaili na dwa sposoby (email-centered bipartite graph oraz address-centered graph) i ekstrahuja z grafow (skierowanych/nieskierowanych, wazonych/niewazonych) bogaty zestaw cech sieciowych: stopnie wierzcholkow, miary centralnosci (degree, betweenness, eigenvector, closeness), wspolne sasiedztwo, wspolczynnik Jaccarda, liczbe trojkatow oraz HITS (authority/hub).

Cechy leksykalne to usrednione wektory GloVe (najlepszy zestaw: 42B.300d) plus meta-informacje (liczba odbiorcow, dlugosc emaila). Porownywane klasyfikatory to SVM i Extra-Trees (scikit-learn). Polaczenie cech grafowych z leksykalnymi poprawia wydajnosc obu klasyfikatorow, a poprawa jest statystycznie istotna (paired t-test, p < 0.05) przy treningu na wiekszym, mniej pewnym zbiorze Enron-union. Praca dostarcza tez recznie zaanotowane podzbiory Enron (AMTurk, 3 anotatorow) i Avocado (in-house, 2 studentow - licencja Avocado zabrania uzycia AMTurk).

## Kluczowe Wnioski
- Cechy z sieci wymiany emaili (graf spoleczny) laczone z cechami leksykalnymi poprawiaja klasyfikacje Business/Personal na obu klasyfikatorach (SVM i Extra-Trees)
- Avocado (LDC2015T03) to realna alternatywa dla Enrona - drugi duzy korpus prawdziwych emaili firmowych; tu kluczowa rola: walidacja modeli na "innej firmie" niz treningowa
- Mozliwa jest sensowna klasyfikacja cross-corpora: model trenowany na Enron daje dobre wyniki na Avocado (np. SVM, all features: 93.5% accuracy, F-1 Personal 64.7% na Avocado test)
- W setting cross-corpora dodanie cech sieciowych zwieksza precyzje klasy Personal kosztem recall; najlepszy F-measure daje kombinacja cech sieciowych i leksykalnych z SVM
- Najlepszy model na trening korpusu mniejszego, ale o wyzszej jakosci etykiet (Enron-intersection) daje lepsza generalizacje cross-corpora niz wiekszy, slabiej oznaczony zbior
- Odsetek emaili prywatnych spada z ~20% (Enron) do <10% (Avocado) - niejasne czy to natura firm, czy upowszechnienie darmowej poczty (Hotmail/Gmail) do spraw prywatnych
- Najlepszy GloVe: 42B.300d (95.4% acc na Enron dev), lepszy niz wiekszy 840B.300d - wiecej danych i wymiarow ogolnie pomaga, ale nie monotonicznie

## Metodologia

**Dane i anotacja:**
- Enron: podzbior wersji Agarwal et al. (2012) z zachowana struktura watkow; anotacja przez Amazon Mechanical Turk (3 anotatorow/watek); finalnie 3,743 watki / 10,546 emaili (Business/Personal)
- Avocado (LDC2015T03): 62,278 watkow / 937,958 emaili w calym korpusie; recznie zaanotowano 1,976 watkow / 5,280 emaili przez 2 studentow in-house (licencja zabrania AMTurk); inter-annotator agreement kappa = 0.58
- Schemat 6-klasowy (Business, Somehow Business, Mixed, Somehow Personal, Personal, Cannot Determine) znormalizowany do binarnego Business vs Personal

**Cechy leksykalne i lokalne (Sec. 4):** usrednione wektory GloVe (testowane rozne zestawy; wybrany 42B.300d), plus meta-informacje (liczba odbiorcow, dlugosc emaila w slowach). Baseline: BOW + chi-kwadrat top-500 slow.

**Cechy sieciowe (Sec. 5):** dwie reprezentacje grafu wymiany emaili - email-centered (graf dwudzielny: emaile i adresy) oraz address-centered (wierzcholki = adresy, krawedzie = komunikacja, wagi = liczba emaili). Z grafow skierowanych/nieskierowanych i wazonych/niewazonych ekstrahowane: in/out-degree, degree, common neighbors, sender's triangles, Jaccard coefficient, fraction of triangles, degree/betweenness/eigenvector/closeness centrality, HITS authority/hub score. Caly graf (wszystkie emaile, oznaczone i nieoznaczone) uzyty do budowy sieci.

**Klasyfikacja:** SVM i Extra-Trees (scikit-learn), grid-search z 3-fold CV; metryki: accuracy, F-1 Business, F-1 Personal (glowny cel - klasa mniejszosciowa Personal). Istotnosc poprawy z cech sieciowych testowana paired t-test (10-fold CV).

## Glowne Koncepcje

**Email exchange network jako graf spoleczny**: siec kto-do-kogo pisze, modelowana jako graf; cechy strukturalne nadawcy/odbiorcow (centralnosci, sasiedztwo) niosa sygnal niezalezny od tresci leksykalnej. Bezposrednio istotne dla modelowania "typowosci" nadawcy (taksonomia C2) i baseline personalnego (EXP-4): odchylenie od normalnego wzorca komunikacji moze sygnalizowac anomalie/impersonacje.

**Email-centered vs address-centered network**: dwie reprezentacje - pierwsza laczy emaile z adresami (dwudzielna), druga laczy adresy bezposrednio (wagi = liczba wymienionych emaili).

**Cross-corpora generalization**: trening na jednej firmie (Enron), zastosowanie na innej (Avocado) - test odpornosci modelu na zmiane organizacji/domeny.

**Avocado jako alternatywa dla Enrona**: realny korpus firmowy, lecz z ograniczeniem licencyjnym LDC (restrykcyjny) vs publiczna domena Enrona.

## Wyniki

Najlepszy zestaw GloVe (Enron-intersection dev): 42B.300d - 95.4% accuracy, F-1 Personal 83.1%.

Intra-corpus (test Enron-union, SVM, all features): 91.2% accuracy, F-1 Business 94.4%, F-1 Personal 79.9%. Dodanie cech sieciowych zwieksza recall klasy Personal; cechy sieciowe szczegolnie skuteczne z Extra-Trees.

Cross-corpora (test Avocado-union, SVM trenowany na Enron-intersection, all features): 93.5% accuracy, F-1 Business 96.4%, F-1 Personal 64.7%. Dodanie cech sieciowych zwieksza precyzje Personal kosztem recall; najlepszy F-measure z kombinacja cech + SVM. Extra-Trees slabo radzi sobie z odzyskiwaniem emaili Personal w obu settingach.

Poprawa z cech sieciowych istotna statystycznie na Enron-union (p < 0.05), nieistotna na mniejszym Enron-intersection (p > 0.05).

## Przydatne Cytaty

"We show that information from the email exchange networks improves the performance of classification." (Abstract, str. 57)

"in February 2015, the Linguistic Data Consortium distributed a data set of emails from an anonymous defunct information technology company referred as Avocado (Oard et al., 2015)." (str. 57)

"We train only on the Enron corpus, but test on both the Enron and Avocado corpora for this classification task in order to investigate how dependent on the training corpus the learned models are." (str. 57)

"the best performance as measured by f-measure is achieved by combining the network and lexical features, and using SVMs" (str. 64)

"The Avocado Email Collection has 62,278 threads and 937,958 emails." (str. 60)

## Datasety
- [Avocado Research Email Collection (LDC2015T03)](../../datasets/avocado-email-collection.md) - ~938k emaili / 62k watkow z 279 kont nieistniejacej firmy IT "Avocado"; realna alternatywa dla Enrona (licencja restrykcyjna LDC)
- [Enron Email Corpus](../../datasets/enron-corpus.md) - wersja Agarwal et al. (2012) z zachowana struktura watkow (>36k watkow, >270k emaili); podzbior anotowany przez AMTurk

## Powiazane Tematy
- Modelowanie "typowosci" nadawcy i baseline personalnego (taksonomia C2, EXP-4) - cechy sieciowe jako sygnal normalnego wzorca komunikacji
- Graph-based / social network features w bezpieczenstwie emaili i detekcji anomalii
- Named entity recognition w emailach (Mitra & Gilbert 2013 - gossip; Listik et al. 2019 - phishing NER)
- Recipient recommendation z grafu komunikacji (Graus et al. 2014, trening Enron / test Avocado)
- Enron organizational hierarchy i miary centralnosci (Agarwal et al. 2012, Hardin et al. 2014)
- GloVe embeddings i porownanie BOW vs embeddings dla klasyfikacji emaili

## Notatki