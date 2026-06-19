---
title: "Dos and Don'ts of Machine Learning in Computer Security"
date: 2022-01-01
authors: "Daniel Arp, Erwin Quiring, Feargus Pendlebury, Alexander Warnecke, Fabio Pierazzi, Christian Wressnegger, Lorenzo Cavallaro, Konrad Rieck"
status: read
doi: "arXiv:2010.09470"
category: "Security"
tags:
  - machine-learning-pitfalls
  - experimental-methodology
  - sampling-bias
  - data-snooping
  - evaluation-metrics
  - threat-model
  - project/graph-phishing-detection
---

# Dos and Don'ts of Machine Learning in Computer Security

## Metadane
- **Autorzy**: Daniel Arp, Erwin Quiring, Feargus Pendlebury, Alexander Warnecke, Fabio Pierazzi, Christian Wressnegger, Lorenzo Cavallaro, Konrad Rieck
- **Rok**: 2022
- **Źródło**: USENIX Security Symposium 2022 / arXiv
- **DOI/Link**: https://arxiv.org/abs/2010.09470
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Jest to fundamentalna praca metodologiczna identyfikująca dziesięć powszechnych, lecz subtelnych pułapek w stosowaniu uczenia maszynowego w bezpieczeństwie komputerowym. Autorzy grupują je według etapów standardowego workflow ML: zbieranie i etykietowanie danych (P1 sampling bias, P2 label inaccuracy), projektowanie systemu i uczenie (P3 data snooping, P4 spurious correlations, P5 biased parameter selection), ocena wydajności (P6 inappropriate baseline, P7 inappropriate measures, P8 base rate fallacy) oraz wdrożenie (P9 lab-only evaluation, P10 inappropriate threat model).

Aby udowodnić powszechność problemu, przeanalizowano 30 prac z czołowych konferencji (CCS, S&P, USENIX Security, NDSS) z ostatniej dekady. Każda praca cierpiała na co najmniej trzy pułapki; najczęstsze to sampling bias (≥90%) i data snooping (≥73%). Ankieta wśród 49 autorów (response rate 36%) potwierdziła brak świadomości tych problemów w środowisku.

W analizie wpływu autorzy empirycznie demonstrują skutki pułapek w czterech domenach: detekcja malware mobilnego (klasyfikator uczył się rozpoznawać pochodzenie aplikacji play.google.com zamiast malware), wykrywanie podatności (VulDeePecker korzystał z artefaktów rozmiaru bufora; prosty SVM z n-gramami osiągał lepszy TPR), atrybucja autorstwa kodu (spadek dokładności o 48% po usunięciu nieużywanych szablonów) oraz detekcja włamań sieciowych (prosta metoda boxplot pobiła KITSUNE przy niskim FPR).

## Kluczowe Wnioski
- Dziesięć pułapek ML w bezpieczeństwie jest endemiczne — każda z 30 analizowanych prac cierpiała na ≥3.
- Sampling bias i data snooping (zwłaszcza temporalne) są najczęstsze i najgroźniejsze.
- Precision-recall i miary uwzględniające nierównowagę klas (MCC) są właściwsze niż accuracy/ROC przy rzadkich zdarzeniach (base rate fallacy).
- Konieczne są: proste baseline'y, ścisła izolacja danych, realistyczna ewaluacja oraz modelowanie adaptacyjnego przeciwnika.

## Metodologia
Praca typu SoK/systematization: (1) identyfikacja pułapek z rekomendacjami, (2) analiza prevalencji w 30 pracach przez 6 niezależnych recenzentów (Krippendorff alpha=0,832), (3) analiza wpływu — empiryczna reprodukcja 4 systemów state-of-the-art i pokazanie, jak pułapki zawyżają wyniki.

## Główne Koncepcje
- **Data snooping (test/temporalny/selektywny)**: użycie informacji niedostępnej w praktyce podczas uczenia.
- **Spurious correlations**: model uczy się artefaktów skorelowanych z zadaniem, nie samego zadania.
- **Base rate fallacy**: ignorowanie nierównowagi klas prowadzi do zawyżonej interpretacji wydajności.
- **Inappropriate threat model / lab-only evaluation**: brak adaptacyjnego przeciwnika i realistycznych warunków.

## Relevancja dla graph-phishing-detection
To kluczowa praca metodologiczna dla całego projektu — definiuje standard rzetelnej ewaluacji, którego należy przestrzegać przy modelach GNN na grafach phishingowych. Bezpośrednio motywuje "leak-aware" ewaluację (przeciw data snooping temporalnemu), ostrożne traktowanie etykiet (label inaccuracy istotne przy BEC/lateral phishing, gdzie ground-truth jest trudny), oraz nacisk na precision/recall i Recall@FPR1% zamiast accuracy (base rate fallacy — phishing to rzadka klasa). Pułapka P10 (threat model) jest fundamentem dla planowanych eksperymentów z adaptacyjnym atakiem na grafy (P3 rozprawy). Praca uzasadnia również potrzebę prostych baseline'ów (np. proweniencja binarna) przy ocenie złożonych modeli grafowych.
