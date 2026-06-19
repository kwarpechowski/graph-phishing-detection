---
title: "VisualPhishNet: Zero-Day Phishing Website Detection by Visual Similarity"
date: 2020-01-01
authors: "Sahar Abdelnabi, Katharina Krombholz, Mario Fritz"
status: to-read
tags: []
---
# VisualPhishNet: Zero-Day Phishing Website Detection by Visual Similarity

## Metadane
- **Autorzy**: Sahar Abdelnabi, Katharina Krombholz, Mario Fritz
- **Rok**: 2020
- **Źródło**: ACM CCS 2020
- **Link**: https://arxiv.org/abs/1909.00300
- **Status**: to-read
- **Kategoria**: Security / Computer Vision
- **Tagi**: #to-read #visual-phishing #triplet-cnn #brand-impersonation #zero-day #reference-based #benchmark

## Streszczenie

Fundamentalna praca wprowadzająca podejście oparte na wizualnym podobieństwie do detekcji phishingu. VisualPhishNet wykorzystuje sieć CNN z **uczeniem tripletowym** (triplet CNN), która uczy się profili wizualnych legalnych stron i wykrywa phishing przez metrykę podobieństwa. Kluczowa innowacja: zdolność generalizacji na **niespotykane wcześniej strony phishingowe (zero-day)** bez re-treningu.

Autorzy wprowadzają też dataset **VisualPhish** — największy ówcześnie zbiór do wizualnej detekcji phishingu, zebrany w ekologicznie walidowany sposób (prawdziwe kampanie phishingowe).

## Kluczowe Wnioski

- Triplet CNN uczy się metryki podobieństwa, nie klasyfikatora — generalizes to unseen
- Outperforms poprzednie visual similarity approaches "by a large margin"
- Testowana odporność na część evasion attacks (ale nie na GAN/diffusion — te pojawiły się później)
- VisualPhish dataset: największy ówcześnie zbiór visual phishing

## Metodologia

- Triplet CNN: anchor (legalna strona) + positive (inna legalna) + negative (phishing)
- Embedding space: strony podobne wizualnie → blisko siebie
- Screenshot-based: przechwytywanie wizualnej reprezentacji strony

## Luki / Ograniczenia (gap analysis)

- Dataset z 2019-2020 — nie zawiera AI-generated phishing
- Nie testowano przeciwko GAN adversarial logos (Lee et al. 2023) — evasion rate 95%
- Nie testowano przeciwko diffusion-based evasion (Hao et al. 2024)
- Nie testowano przeciwko delayed rendering attacks (Yuan et al. 2026)
- Brak bankowej bazy trademark → false negatives dla nieznanych banków

## Notatki

*Kluczowa bazowa publikacja dla projektu bank-brand-phishing-detection. VisualPhishNet to najczęściej atakowany baseline w pracach adversarial (Lee 2023, Ji 2024, Yuan 2024). Dodaj PDF z arxiv:1909.00300v4 i uruchom `/summarize-paper abdelnabi-visualphishnet-2020`*

**Rola w projekcie**: Baseline visual similarity method + VisualPhish dataset jako benchmark.
