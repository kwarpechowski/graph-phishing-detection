---
title: "Evaluating the Effectiveness and Robustness of Visual Similarity-based Phishing Detection Models"
date: 2024-01-01
authors: "Fujiao Ji, Kiho Lee, Hyungjoon Koo, Wenhao You, Euijin Choo, Hyoungshick Kim, Doowon Kim"
status: read
tags: []
---
# Evaluating the Effectiveness and Robustness of Visual Similarity-based Phishing Detection Models

## Metadane
- **Autorzy**: Fujiao Ji, Kiho Lee, Hyungjoon Koo, Wenhao You, Euijin Choo, Hyoungshick Kim, Doowon Kim
- **Rok**: 2024
- **Źródło**: arXiv:2405.19598
- **Link**: https://arxiv.org/abs/2405.19598
- **Status**: read
- **Cytowania**: 15
- **Kategoria**: Security / Adversarial ML
- **Tagi**: #to-read #robustness-evaluation #visual-phishing #real-world #large-scale #adversarial #451k-dataset

## Streszczenie

Największa jak dotąd **empiryczna ocena odporności** wizualnych detektorów phishingu na rzeczywistych danych. Dataset: **451,000 prawdziwych stron phishingowych** (2024). Kluczowe odkrycie: modele osiągające 99% w kontrolowanych warunkach laboratorynych mają **dramatycznie niższą** skuteczność na real-world data.

Kategoryzacja strategii evasion przez atakujących: (1) direct model pipeline attacks, (2) mimicking benign logos, (3) simple strategies (removing logos from screenshots). Ostatnia kategoria jest najtańsza i najbardziej popularna w praktyce!

## Kluczowe Wnioski

**Table 2 — Phishing Detection na 451k real-world (DDDlearn = 312,355 learned brands):**

| Model | Recall (Baseline Ref.) | Recall (Extended Ref.) | FPR |
|-------|----------------------|----------------------|-----|
| EMD | 30.62% | 31.34% | 26.36% |
| VisualPhishNet | 39.09% | 40.58% | 13.52% |
| DynaPhish | — | — | 0% |
| PhishIntention | **65.59%** | 66.22% | **0%** |
| Phishpedia | 74.46% | **87.97%** | 16.24% |
| Involution | 81.31% | 84.77% | 3.96% |
| PhishZoo | 77.22% | 86.36% | 93.92%(!!) |

**Na 451k ALL brands (DDDall)**: PhishIntention 52.23%, Phishpedia 60.97%, VisualPhishNet 40.13%

**Table 3 — Sampled 4,190 phishing (Dsample):**
- DynaPhish: **22.03%** (najgorszy, mimo że 0 FP)
- PhishIntention: **49.07%**, brand ID rate: 98.56%
- Phishpedia: **57.16%**
- VisualPhishNet: **33.84%**

**Kluczowe wnioski:**
- Lab accuracy 90%+ → real-world 33-66% recall (dramatyczny spadek!)
- DynaPhish (dynamic expansion): 0 FP ale tylko 22% recall — praktycznie bezużyteczny
- Phishpedia najlepsza w phishing detection ale 16% FPR
- PhishIntention: 0 FP ale tylko 49-66% recall
- Najprostsza evasion: usunięcie logo ze screenshota → immediate failure dla logo-based systemów
- Statyczne reference listy (PhishIntention: ~180 brands, Phishpedia: 181) nie nadążają za nowymi brandami

## Metodologia

- Dataset: 451,514 phishing URLs (APWG eCX, July 2021 – July 2023), + 4,190 sampled + 2,500 benign (Tranco Top 1000)
- 7 modeli: PhishIntention, Phishpedia, DynaPhish, Involution, PhishZoo, VisualPhishNet, EMD
- Re-training z dwoma reference listami: Rbase (oryginalna) i Rext (rozszerzona do 2023)
- Perturbacje: visible manipulations (kolor, layout, usunięcie logo) + pixel-level (PGD style)
- Metryki: TPR, FPR, brand identification rate

## Luki / Ograniczenia (gap analysis)

- Tylko analiza ataków, brak nowych obron
- Banking brands nie analizowane osobno
- Brak temporal analysis (jak zmieniają się ataki w czasie)

## Notatki

*Kluczowa praca benchmarkowa — pokazuje jak duży jest gap między lab a real-world. Nasz projekt powinien cytować ten paper jako motywację (istniejące systemy zawodzą w praktyce). 451k dataset — potencjalnie dostępny przez autorów. Pobierz PDF z arxiv:2405.19598.*

**Rola w projekcie**: Empiryczna motywacja projektu + dataset benchmark + taksonomia strategii ataku.
