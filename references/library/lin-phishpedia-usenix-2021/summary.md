---
title: "Phishpedia: A Hybrid Deep Learning Based Approach to Visually Identify Phishing Webpages"
date: 2021-01-01
authors: "Yun Lin, Ruofan Liu, Dinil Mon Divakaran, J. Y. Ng, Qing Zhou Chan, Yiwen Lu, Yu Si, Fan Zhang, Jin Song Dong"
status: read
tags: []
---
# Phishpedia: A Hybrid Deep Learning Based Approach to Visually Identify Phishing Webpages

## Metadane
- **Autorzy**: Yun Lin, Ruofan Liu, Dinil Mon Divakaran, J. Y. Ng, Qing Zhou Chan, Yiwen Lu, Yu Si, Fan Zhang, Jin Song Dong
- **Rok**: 2021
- **Źródło**: USENIX Security 2021
- **DOI/ID**: Semantic Scholar 15d06f25f1af95db15d7252dfdc953f176c68d52
- **PDF**: http://linyun.info/publications/usenix21.pdf
- **Status**: read
- **Cytowania**: 164
- **Kategoria**: Security / Computer Vision
- **Tagi**: #to-read #phishing #rbpd #logo-detection #brand-matching #usenix #high-citations #phishpedia

## Streszczenie

Phishpedia to poprzednik PhishIntention (Liu et al. 2022) od tych samych autorów. Hybrydowe podejście łączące object detection (Faster R-CNN) do lokalizacji logo i elementów brandowych z siecią do rozpoznawania marek (EfficientNet + metric learning). System działa w dwóch etapach: (1) wykryj elementy brandowe na stronie, (2) dopasuj do bazy znanych marek, (3) sprawdź czy URL pasuje do detected brand.

Phishpedia ugruntowała paradygmat RBPD (Reference-Based Phishing Detection) który dominuje literaturę do dziś. Jest używana jako jeden z dwóch głównych baseline'ów w Ji & Kim 2025 (obok PhishIntention).

## Kluczowe Wnioski

**Table 2 (własny testowy zbiór ~30K phishing + ~30K benign, 181 brands):**
- Precision: **98.2%**, Recall: **87.1%**, Brand identification rate: **99.2%**, Runtime: 0.19s
- Baselines porównanie: EMD-normal (52% recall, 76.2% precision), LogoSENSE (20.5% recall!), PhishZoo (81.8% precision, 68.9% recall)
- 98.6% phishing stron ma logo → logo-based detection sensowna strategia

**Adversarial defense (Table 7, BPDA na Siamese model):**
- 3 masked layers: accuracy drops 93.5%→64.6% (∆=29pp)
- 17 masked layers: accuracy drops 93.5%→92.6% (∆=0.9pp) — Step-ReLU gradient masking działa przy pełnym maskowaniu
- Ale: ta obrona chroni przed gradient-based attacks (BPDA), NIE przed GAN-generated logos (Lee 2023)

**PhishCatcher field study (Table 10):** Precision=87.5%, Recall=87.5% — dobry balans

**Cross-evaulation (inne prace):**
- Ji 2024 (451k real-world): Phishpedia recall **57-88%** zależnie od split
- Li 2024 (TR-OP): Phishpedia recall **40.16%**, F1=57.17%  
- PhishOracle (Kulkarni 2024): Phishpedia recall spada 81.63%→**~40%** pod logo transformations (−42pp!)

164 cytowania (USENIX 2021) — fundamentalna praca, predecessor PhishIntention.

## Metodologia

- Object detection: Faster R-CNN (ResNet-50 backbone, FPN)
- Brand recognition: EfficientNet fine-tuned z contrastive/metric loss
- Brand KB: ~181 popularnych marek (login pages)
- URL verification: porównanie detected brand vs extracted domain

## Luki / Ograniczenia

- Mała baza marek (~181) — fintech/payment gateways nieobecne
- Nie testowana adversarially
- Zastąpiona przez PhishIntention (2022) i KnowPhish (2024)
- Ji & Kim 2025: recall spada drastycznie na real-world dataset

## Zastosowanie w projekcie

**Baseline #2** w EXP-5 (obok PhishIntention jako Baseline #1):
- Ji & Kim 2025 testuje ten model → bezpośrednie porównanie
- Łańcuch ewolucji: Phishpedia (2021) → PhishIntention (2022) → DynaPhish (2023) → KnowPhish (2024)
- Section 2.1 Related Work: jeden akapit opisujący ewolucję

## Notatki

*Konieczna referencja — ji & Kim 2025 używa jej jako baseline. Brak w bazie był luką.*
