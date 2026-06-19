---
title: "It Doesn't Look Like Anything to Me: Using Diffusion Model to Subvert Visual Phishing Detectors (LogoMorph)"
date: 2024-01-01
authors: "Qingying Hao, Nirav Diwan, Ying Yuan, Giovanni Apruzzese, Mauro Conti, Gang Wang"
status: read
tags: []
---
# It Doesn't Look Like Anything to Me: Using Diffusion Model to Subvert Visual Phishing Detectors (LogoMorph)

## Metadane
- **Autorzy**: Qingying Hao, Nirav Diwan, Ying Yuan, Giovanni Apruzzese, Mauro Conti, Gang Wang
- **Rok**: 2024
- **Źródło**: arXiv / IEEE S&P (podejrzewane)
- **Link**: https://gangw.cs.illinois.edu/logomorph.pdf
- **Status**: read
- **Cytowania**: 11
- **Kategoria**: Security / Computer Vision / Adversarial ML
- **Tagi**: #read #diffusion-model #adversarial #visual-phishing #logomorph #logo-evasion #brand-impersonation

## Streszczenie

**LogoMorph** używa **modeli dyfuzyjnych** do generowania semantic-preserving adversarial logos omijających wizualne detektory phishingu. Trzy typy ataków: text logo (zmiana fontu), image logo (adversarial diffusion), image-text logo (kombinacja). Testowane end-to-end przeciwko PhishIntention, Phishpedia, VisualPhishNet.

## Kluczowe Wnioski

**Table 3 — Webpage-level success rate (Text Logo, vs PhishIntention):**
- BOA, Outlook, Spotify: **100%** bypass rate
- Amazon, Instagram, Dropbox: **98-99%** bypass rate
- Najtrudniejsze: PayPal (19%), LinkedIn (27%), Yahoo (20%) — ale wciąż >0

**Table 7 — Transferability Phishpedia (black-box, wszystkie loga):**
- DocuSign, Comcast, Yahoo: **100%** transfer do Phishpedia
- Amazon, LinkedIn, Google, Netflix, Instagram: **96-99%** transfer
- Słabsze: BOA (57%), DHL (80%)

**Table 9 — User Study (n=150):**
- Adversarial phishing pages: TPR = **0.59** (zaledwie lepsze od losowego)
- Original phishing pages: TPR = **0.45** — paradoks: adversarial pages TRUDNIEJSZE do wykrycia przez detektory, ale ŁATWIEJSZE przez ludzi (spójność stylu)

**Comparison z PhishGAP (Lee 2023 GAN)**: tylko **5.49%** adversarial logos z PhishGAP bypasses PhishIntention end-to-end, vs LogoMorph ~100% — LogoMorph dramatycznie skuteczniejszy

**CLIP nie testowany** — semantic-preserving attacks mogą być wykryte przez joint image-text embeddings

## Luki / Ograniczenia (gap analysis)

- Testowany tylko przeciwko Siamese-based detectorom (ResNet backbone) — CLIP nieewaluowane
- Gradient masking jako obrona: częściowo skuteczna (zmniejsza bypass rate)
- Adversarial retraining: poprawia odporność, ale tylko dla znanych stylów ataków

## Notatki

*Praca dostępna jako preprint na stronie autora. 11 cytowań wskazuje na rosnące zainteresowanie diffusion-based attacks. Pobierz PDF z bezpośredniego linku autorów.*

**Rola w projekcie**: Jedna z najgroźniejszych klas ataków (generatywne loga) — nasz system musi być odporny. Uzupełnia Lee et al. 2023 (GAN) i Yuan et al. 2026 (timing).
