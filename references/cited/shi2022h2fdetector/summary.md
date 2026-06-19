---
title: "H2-FDetector: A GNN-based Fraud Detector with Homophilic and Heterophilic Connections"
date: 2022-01-01
authors: "Fengzhao Shi, Yanan Cao, Yanmin Shang, Yuchen Zhou, Chuan Zhou, Jia Wu"
status: read
doi: "10.1145/3485447.3512195"
category: "Security"
tags:
  - fraud-detection
  - gnn
  - homophily
  - heterophily
  - graph-neural-networks
  - anomaly-detection
  - project/graph-phishing-detection
---

# H2-FDetector: A GNN-based Fraud Detector with Homophilic and Heterophilic Connections

## Metadane
- **Autorzy**: Fengzhao Shi, Yanan Cao, Yanmin Shang, Yuchen Zhou, Chuan Zhou, Jia Wu
- **Rok**: 2022
- **Źródło**: WWW 2022 (The Web Conference)
- **DOI/Link**: 10.1145/3485447.3512195
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
H2-FDetector to detektor fraudu oparty na grafowych sieciach neuronowych, zaprojektowany do radzenia sobie z faktem, że w grafie fraudowym oszuści celowo wchodzą w interakcje z licznymi uczciwymi podmiotami, aby się ukryć. W efekcie graf zawiera nie tylko połączenia homofilne (między węzłami o tej samej etykiecie, podobnymi), lecz także połączenia heterofilne (między węzłami o różnych etykietach, niepodobnymi).

Autorzy zwracają uwagę, że dotychczasowe metody GNN do detekcji fraudu wzmacniają wyłącznie homofilię i stosują filtry dolnoprzepustowe (low-pass), które uśredniają cechy sąsiadów, przez co tracą różnicę informacyjną wynikającą z połączeń heterofilnych. To prowadzi do gubienia sygnału fraudowego ukrytego w nietypowych powiązaniach.

H2-FDetector najpierw identyfikuje połączenia homofilne i heterofilne pod nadzorem etykietowanych węzłów, a następnie projektuje nową strategię agregacji informacji: dla połączeń homofilnych zachowuje wspólność cech, a dla heterofilnych zachowuje i wykorzystuje ich odmienność (różny tryb propagacji). Mechanizm ten pozwala modelowi adekwatnie reprezentować obie role połączeń. Eksperymenty na benchmarkach detekcji fraudu pokazują przewagę nad istniejącymi metodami GNN.

## Kluczowe Wnioski
- Grafy fraudowe są mieszane: zawierają zarówno połączenia homofilne, jak i heterofilne.
- Klasyczne GNN z filtrem dolnoprzepustowym tracą sygnał z połączeń heterofilnych.
- Rozróżnianie typu połączenia pod nadzorem etykiet poprawia wykrywanie fraudu.
- Osobne strategie agregacji dla homofilii i heterofilii dają przewagę nad SOTA.

## Metodologia
Nadzorowana identyfikacja typu krawędzi (homofilna/heterofilna) na podstawie etykiet węzłów. Zróżnicowana agregacja: zachowanie wspólności dla homofilii, zachowanie różnicy (komponent high-pass) dla heterofilii, z dodatkowym mechanizmem uwagi/prototypów klas. Ewaluacja na publicznych benchmarkach detekcji fraudu (m.in. zbiory Amazon, YelpChi) z metrykami AUC, Recall, F1.

## Główne Koncepcje
- **Homofilia / heterofilia połączeń**: krawędzie między tą samą / różną klasą.
- **Kamuflaż oszustów (camouflage)**: ukrywanie się fraudu wśród uczciwych węzłów.
- **Filtr dolno- vs górnoprzepustowy**: zachowanie wspólności vs różnicy cech.
- **Etykietowana identyfikacja krawędzi**: nadzorowane rozpoznanie typu połączenia.

## Relevancja dla graph-phishing-detection
H2-FDetector adresuje rdzeniowy problem grafowej detekcji phishingu/fraudu: kamuflaż przez heterofilię. W grafach phishingowych konto/domena atakującego celowo łączy się z wieloma legalnymi węzłami (zaufani kontakci, popularne domeny), co rozmywa sygnał przy klasycznej agregacji homofilnej. Mechanizm rozróżniania połączeń homo/heterofilnych jest bezpośrednio przenośny na graf komunikacji (nadawca-odbiorca) i graf domen/transakcji w projekcie, gdzie krawędź „atakujący-ofiara" jest z natury heterofilna. To uzasadnia użycie operatorów high-pass / per-edge attention zamiast czystego uśredniania, a także stanowi konkurencyjny baseline detekcji fraudu, względem którego projekt może mierzyć Recall@FPR1%.
