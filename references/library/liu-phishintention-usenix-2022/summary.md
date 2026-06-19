---
title: "PhishIntention: Identifying Phishing Websites Through Visual Combination"
date: 2022-01-01
authors: "Ruofan Liu, Yun Lin, Xianglin Yang, Siang Hwee Ng, Dinil Mon Divakaran, Jin Song Dong"
status: read
doi: "10.5555/3548606.3560643"
tags: []
---
# PhishIntention: Identifying Phishing Websites Through Visual Combination

## Metadane
- **Autorzy**: Ruofan Liu, Yun Lin, Xianglin Yang, Siang Hwee Ng, Dinil Mon Divakaran, Jin Song Dong
- **Rok**: 2022
- **Źródło**: USENIX Security 2022
- **DOI**: 10.5555/3548606.3560643
- **Status**: read
- **Cytowania**: 92
- **Kategoria**: Security / Computer Vision
- **Tagi**: #to-read #phishing #visual-phishing #rbpd #brand-detection #logo-detection #ocr #deep-learning #usenix #high-citations

## Streszczenie

PhishIntention to system wizualnej detekcji phishingu oparty na głębokim uczeniu, który identyfikuje intencję podszywania się poprzez analizę wyglądu strony. W odróżnieniu od wcześniejszych systemów (VisualPhishNet), PhishIntention nie polega na globalnym podobieństwie wizualnym, lecz na wykrywaniu logo i tekstów brandowych osobno, a następnie weryfikacji czy domena URL odpowiada zidentyfikowanej marce.

System składa się z czterech modułów: (1) wykrycie elementów brandowych (logo + tekst) przez object detection (Faster R-CNN), (2) dopasowanie logo do bazy marek (ResNet-50 + triplet loss), (3) ekstrakcja tekstu brandowego (OCR), (4) weryfikacja URL vs marka. PhishIntention stała się de facto standardowym punktem odniesienia dla wszystkich późniejszych prac o wizualnym phishingu.

## Kluczowe Wnioski

- **Własny 50K dataset (25K phish + 25K benign), 277 brands w reference list**
- **At FPR=10⁻³: recall = 0.90 (90%)** vs Phishpedia recall ~0.45 (2× gorszy) — z ROC curves (Figure 11)
- Field study (2 miesiące): 1,942 phishing wykrytych, **86.5% mniej false positives** niż Phishpedia (139 vs 1,033 FP), 6% mniej TP (1,942 vs 2,071)
- FPR na misleading legitimacy: **5.10%** vs baselines 45.5%–60.1%
- Runtime: 0.58s/sample vs Phishpedia 0.39s (marginalnie wolniejszy, ale dramatycznie lepsza precision)
- **KnowPhish (Li 2024) reeval na TR-OP**: PhishIntention original recall **33.32%**, F1=49.96% na standardowym zbiorze — wyraźnie gorszy niż KPD+KnowPhish (86.90%)
- Adversarial defense: gradient masking (słaby) — BPDA bypass redukuje ochronę do ↓0.07 (CRP classifier)

## Metodologia

- **Object detection**: Faster R-CNN (Detectron2) do lokalizacji logo i elementów brandowych
- **Logo matching**: ResNet-50 + triplet loss, baza ~180 marek
- **OCR**: PaddleOCR do ekstrakcji tekstu brandowego
- **URL verification**: porównanie detected brand vs domena, spacja Levensteina
- **Training data**: własny zbiór (nieupubliczniony)

## Główne Koncepcje

- **Phishing intention detection**: wykrywanie zamiaru podszywania, nie tylko wizualnego podobieństwa
- **Reference-Based Phishing Detector (RBPD)**: klasa systemów porównujących stronę z bazą legalnych marek
- **Brand knowledge base**: baza logo i nazw marek używana do referencji

## Wyniki

| Metryka | Wartość | Źródło |
|---------|---------|--------|
| Recall @ FPR=10⁻³ | **90%** | Figure 11, ROC curve (własny 50K dataset) |
| FPR misleading legitimacy | **5.10%** | vs baselines 45.5–60.1% |
| Field study TP | 1,942 phishing (2 miesiące) | vs Phishpedia 2,071 (−6%) |
| Field study FP | 139 | vs Phishpedia 1,033 (−86.5%!) |
| Recall (TR-OP, Li 2024 eval) | **33.32%** | F1=49.96%, Precision=99.76% |
| Runtime | 0.58s/sample | vs Phishpedia 0.39s |

**Uwaga**: Ji et al. 2024 pokazuje dramatyczny spadek recall do ~40-50% na 451k real-world phishing stron. KnowPhish (Li 2024) ewaluuje PhishIntention na TR-OP i otrzymuje recall tylko 33.32% — różnica wynika z dataset i konfiguracji. Na własnym 50K zbiorze: recall=90% @ FPR=10⁻³. Na TR-OP: recall=33.32%.

## Przydatne Cytaty

- "PhishIntention detects phishing intent rather than visual similarity, making it more robust to superficial visual changes"
- "The modular design allows each component to be independently evaluated and replaced"

## Datasety

- `datasets/custom-phishing-dataset.md` — VisualPhish (własny, nieupubliczniony; benchmark z pracy)
- Benchmark w: Ji & Kim 2025 (19,131 stron) — dostępny zewnętrznie

## Powiązane Tematy

- RBPD evolution: VisualPhishNet (2020) → PhishIntention (2022) → DynaPhish (2023) → KnowPhish (2024)
- Adversarial attacks: Lee 2023 (GAN logos), Yuan 2026 (timing) — wszystkie testowane vs ten baseline
- Real-world failure modes: Ji et al. 2024, Ji & Kim 2025

## Notatki

