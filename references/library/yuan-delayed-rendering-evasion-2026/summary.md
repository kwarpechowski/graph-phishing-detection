---
title: "I Can't Recognize (Yet): Delayed Rendering to Defeat Visual Phishing Detectors"
date: 2026-01-01
authors: "Ying Yuan, Cristiano Alex Rado, Giovanni Apruzzese, Mauro Conti, Luigi V. Mancini"
status: read
tags: []
---
# I Can't Recognize (Yet): Delayed Rendering to Defeat Visual Phishing Detectors

## Metadane
- **Autorzy**: Ying Yuan, Cristiano Alex Rado, Giovanni Apruzzese, Mauro Conti, Luigi V. Mancini
- **Rok**: 2026
- **Źródło**: arXiv:2605.00183
- **Link**: https://arxiv.org/abs/2605.00183
- **Status**: read
- **Kategoria**: Security / Adversarial ML
- **Tagi**: #read #delayed-rendering #timing-attack #visual-phishing #evasion #browser-extension #defense #2026

## Streszczenie

Odkrywa nową klasę ataków na wizualne detektory phishingu: **timing-based evasion przez delayed rendering**. Atakujący opóźnia renderowanie logo/brand elements tak, że screenshot detektora pokazuje stronę bez logo → klasyfikacja jako bezpieczna.

## Kluczowe Wnioski

**Fig. 4 — Attack Success Rate na screenshot (preliminary):**
- Curtain Effect (top 1/5 visible): ASR = **0.58** vs PhishIntention
- Curtain Effect (top 4/5 visible): ASR = **0.01** (prawie nieskuteczny)
- Pixelation 5×5px: ASR = **0.89**; 2×2px: ASR = **0.34**

**Main Evaluation (on actual websites, 24 phishing pages):**
- Curtain Effect na logos: **ASR=100%** dla PhishIntention i PhishPedia
- Pixelation 5×5px: **ASR=0.62 (PhishIntention), 0.50 (PhishPedia)**
- Combination attacks: **do 100% evasion** PhishIntention, PhishPedia, PhishLLM; ~50% VisualPhishNet

**Table 2 — User Study (n=247):** User trust rate = **72%** — użytkownicy ufają adversarial stronm; najniższy trust rate = 57% (kombinacja ataków, 5s delay)

**Implementacja ataku (kluczowe dla H3 — statyczna detekcja):**
- CSS: `clip-path: inset(0px, 0px, value)` — stopniowe odsłanianie
- JS: `PhishMe` module — setTimeout/setInterval kontroluje rendering
- Delay: 2-5 sekund wystarczy
- **Detekcja statyczna**: sygnały ATAku są w HTML/CSS/JS — możliwa PRZED renderowaniem

**Literatura**: 20 z 24 prac na visual phishing detection nie mierzy czasu przed screenshot; tylko 3 podają czas (~2s — za krótko vs avg 7.2s ładowania strony)

## Metodologia

- Dataset: 24 phishing webpages (nowy, APWG eCX), ze wszystkimi JS/CSS/UI komponentami (inne datasety niewystarczające)
- 4 detektory: PhishPedia, PhishIntention, VisualPhishNet, PhishLLM
- 60 wariantów ataków: 4 Curtain Effect + 4 Pixelation + 12 kombinacji × logo/background/both
- n=247 user study (Prolific, $11/h)

## Luki / Ograniczenia (gap analysis)

- Obrona jest tylko proof-of-concept
- Nie integruje z URL/content modalities
- Specjalizacja bankowa nie analizowana

## Notatki

*KRYTYCZNA praca — najaktualsza (2026). Definiuje nową, tanią i skuteczną klasę ataków które ŻADEN istniejący system nie jest odporny. Nasz projekt musi uwzględnić tę klasę ataków. Pobierz PDF z arxiv:2605.00183.*

**Rola w projekcie**: Definiuje trzecią klasę zagrożeń (timing-based) obok GAN logos i diffusion logos. Wymaga wielomodalne podejście (nie tylko screenshot).
