---
title: "Attacking Logo-Based Phishing Website Detectors with Adversarial Perturbations"
date: 2023-01-01
authors: "Jehyun Lee, Zhe Xin, Melanie Ng Pei See, Kanav Sabharwal, Giovanni Apruzzese, Dinil Mon Divakaran"
status: read
tags: []
---
# Attacking Logo-Based Phishing Website Detectors with Adversarial Perturbations

## Metadane
- **Autorzy**: Jehyun Lee, Zhe Xin, Melanie Ng Pei See, Kanav Sabharwal, Giovanni Apruzzese, Dinil Mon Divakaran
- **Rok**: 2023
- **Źródło**: arXiv:2308.09392
- **Link**: https://arxiv.org/abs/2308.09392
- **Status**: read
- **Kategoria**: Security / Computer Vision / Adversarial ML
- **Tagi**: #read #adversarial-logo #gan #evasion #logo-based #visual-phishing #siamese-network #high-relevance

## Streszczenie

Pierwsza praca demonstrująca skuteczne **adversarial attacks na logo-based phishing detectors** (Siamese networks). Atakujący generuje **"adversarial logos"** przy pomocy GAN-based perturbacji — loga wyglądają identycznie dla człowieka (user study: nieodróżnialne), ale oszukują detektor.

**Kluczowy wynik**: Evasion (fooling) rate do **95%** (white-box), minimum **42%** (black-box, GViT vs Siamese) przy perturbacjach niewidocznych dla użytkownika.

## Kluczowe Wnioski

**Fig. 6d — Fooling ratio przy FPR=10⁻³ (kluczowe liczby):**
- **White-box**: attacker z wiedzą o discriminatorze → **>95% fooling ratio** dla wszystkich modeli
- **Black-box (GViT generator)**: fooling ratio **42–95%** przeciwko różnym discriminatorom
- Siamese (= PhishIntention/Phishpedia's model): **~42% fooling ratio** — najlepszy defender ale wciąż 42% evasion
- ViT discriminator: najodporniejszy na adversarial, ale gorszy TPR od Siamese na czystych danych (6-12pp niższy @ FPR=10⁻³)
- **ViT jako GENERATOR** (GViT): najtęższy atakujący — 42-95% fooling ratio niezależnie od discriminatora
- CLIP **nie był testowany** — to luka którą adresujemy

**Table 1 — Training time for generators:**
- GSiamese: **8 minut** do fooling ratio 0.9 (1 epoch!) — tanie dla atakującego
- GViT: 744 minut do 0.9 fooling ratio (kosztowne ale najskuteczniejsze)

**User study (VS N=30, HS N=287):** Użytkownicy nie widzą różnicy między oryginalnymi i adversarial logos.

**Dataset**: 181 brands (z Phishpedia target list)

## Metodologia

- GAN-based perturbation generation: zachowanie perceptual similarity
- Target models: Siamese network-based logo detectors
- Evaluation: evasion rate, user study (perceptual similarity)
- Adversarial training jako defense

## Luki / Ograniczenia (gap analysis)

- Ataki na loga (visual), nie testuje URL/HTML modalities
- Adversarial training jako obrona: brak oceny na certifiably robust models
- Brak testów na bankowych markach specyficznie
- Brak kombinacji z innymi evasion strategies (multi-space)

## Notatki

*KRYTYCZNA praca dla projektu — definiuje zagrożenie adversarial logos przeciwko logo detectors. Nasza hipoteza: banking logos szczególnie podatne (rozpoznawalne, ale perturbowalne). Pobierz PDF z arxiv:2308.09392.*

**Rola w projekcie**: Główna klasa ataku którą nasz system musi być odporny. Evasion rate 95% = baseline do pokonania.
