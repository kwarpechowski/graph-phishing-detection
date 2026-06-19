---
title: "From ML to LLM: Evaluating the Robustness of Phishing Webpage Detection Models against Adversarial Attacks"
date: 2024-01-01
authors: "Aditya Kulkarni, Vivek Balachandran, Dinil Mon Divakaran, Tamal Das"
status: to-read
doi: "arXiv:2407.20361"
tags: []
---
# From ML to LLM: Evaluating the Robustness of Phishing Webpage Detection Models against Adversarial Attacks

## Metadane
- **Autorzy**: Aditya Kulkarni, Vivek Balachandran, Dinil Mon Divakaran, Tamal Das
- **Rok**: 2024
- **Źródło**: arXiv 2407.20361
- **DOI**: arXiv:2407.20361
- **Status**: to-read
- **Cytowania**: N/A (nowy)
- **Kategoria**: Security / Adversarial ML
- **Tagi**: #to-read #phishing #adversarial #phishoracle #robustness #visualphishnet #phishpedia #evasion #divakaran-group

## Streszczenie

**PhishOracle** — narzędzie do generowania adversarial phishing stron przez osadzanie różnorodnych phishing cech (logo marek, elementy wizualne) w legalnych stronach. Testowane na Stack model, VisualPhishNet i Phishpedia — wszystkie pokazują **znaczące spadki detection rate**. Multimodal LLM (MLLM) okazuje się bardziej odporny, ale wciąż podatny. User study potwierdza że adversarial strony mylą również ludzi.

Praca ta jest bezpośrednim "atakiem" na systemy z których korzystamy jako baseline. Dostarcza metodologii generowania adversarial examples alternatywnej do Lee 2023 (GAN) i Hao 2024 (diffusion).

## Kluczowe Wnioski

- VisualPhishNet i Phishpedia tracą znaczną skuteczność na adversarial pages
- MLLM (Lee et al. 2024) odporniejszy ale nie odporny na PhishOracle
- Adversarial page generation: embedding brand logo/colors w legalną strukturę strony
- User study: ludzie też nie wykrywają adversarial phishing stron
- Divakaran group — spójność z resztą ich ekosystemu (Phishpedia/PhishIntention/KnowPhish)

## Metodologia PhishOracle

Generuje adversarial strony przez:
1. Bazowa legalna strona (duże, znane domeny)
2. Osadzenie logo i motywu wizualnego atakowanej marki
3. Dodanie formularza logowania
4. Zachowanie legalnej domeny URL (omija URL-based detektory)

Kluczowe: atak na **content/visual channel** przy legalnym URL — dokładnie ta synergia którą broni nasz M2+M3 moduł.

## Znaczenie dla projektu

**Gap uzasadniający naszą pracę**:
- "Kulkarni et al. (2024) show that VisualPhishNet and Phishpedia collapse under adversarial brand-embedding attacks (PhishOracle). We address this vulnerability through PGD adversarial training and CLIP-based semantic matching."

**Potencjalne użycie PhishOracle**:
- Jako dodatkowa klasa ataku w naszym protokole (A5: PhishOracle-style)
- Narzędzie open-source? → sprawdź GitHub

**EXP-3 rozszerzenie**: dodaj PhishOracle jako Attack Class A5 obok A1-A4.

## Powiązane Tematy

- Lee et al. 2024 (MLLM) — ta sama grupa, system odporniejszy ale podatny
- Lee 2023 (GAN logos) — inna klasa adversarial attack
- Yuan 2026 (timing) — kolejna klasa
- Nasz system: hardening vs A1 (GAN) + A2 (diffusion) + A3 (timing) + A5 (PhishOracle)

## Notatki

*Kluczowa praca — dostarcza gotową klasę ataków (PhishOracle) do włączenia do naszego protokołu eksperymentalnego jako A5. Jeśli kod dostępny, użyj do generowania adversarial stron testowych. Przeczytaj przed pisaniem Sekcji 3 Threat Model.*
