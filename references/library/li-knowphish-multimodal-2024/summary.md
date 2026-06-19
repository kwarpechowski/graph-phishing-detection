---
title: "KnowPhish: Large Language Models Meet Multimodal Knowledge Graphs for Enhancing Reference-Based Phishing Detection"
date: 2024-01-01
authors: "Yuexin Li, Chengyu Huang, Shumin Deng, Mei Lin Lock, Tri Cao, Nay Oo, Bryan Hooi, Hoon Wei Lim"
status: read
tags: []
---
# KnowPhish: Large Language Models Meet Multimodal Knowledge Graphs for Enhancing Reference-Based Phishing Detection

## Metadane
- **Autorzy**: Yuexin Li, Chengyu Huang, Shumin Deng, Mei Lin Lock, Tri Cao, Nay Oo, Bryan Hooi, Hoon Wei Lim
- **Rok**: 2024
- **Źródło**: arXiv:2403.02253
- **Link**: https://arxiv.org/abs/2403.02253
- **Status**: read
- **Cytowania**: 70
- **Kategoria**: Security / NLP / Computer Vision
- **Tagi**: #to-read #knowphish #knowledge-graph #llm #multimodal #reference-based #brand-knowledge-base #high-impact

## Streszczenie

KnowPhish rozwiązuje kluczowe ograniczenie reference-based phishing detectors (RBPD): ręcznie budowaną bazę wiedzy o markach. Proponuje **zautomatyzowany pipeline** do zbierania bazy z 20 000 marek z bogatymi informacjami multimodalnymi (loga, nazwy, URL, opisy). 

**KnowPhish Detector (KPD)** łączy dwa moduły: (1) visual similarity (istniejący RBPD + ulepszona baza) + (2) LLM-based text extraction z HTML strony. Wykrywa phishing nawet **bez logo** na stronie (pure text-based brand extraction). Oceniony w Singapore's local context — istotne dla polskiego kontekstu bankowego.

## Kluczowe Wnioski

- 70 cytowań (2024) — jedna z najszybciej rosnących prac w phishing detection
- **KPD+KnowPhish = SOTA**: F1=**92.05%**, Recall=**86.90%**, Precision=97.84%, 2.02s/sample (Table 2, TR-OP dataset)
- Phishpedia+KnowPhish: F1=83.67%, Recall=72.80% (vs Phishpedia original: F1=57.17%, Recall=40.16%)
- PhishIntention+KnowPhish: F1=71.60%, Recall=55.84% (vs PhishIntention original: F1=49.96%, Recall=33.32%)
- Wykrywa phishing bez logo (Text Brand Extractor) — ważne dla logo-less pages
- Runtime: KPD+KnowPhish = 2.02s/sample (LLM overhead); Phishpedia+KnowPhish = 0.22s/sample

## Wyniki adversarial (Table 4 — HTML text attacks)

| Attack | Brand Acc (no defense) | Brand Acc (defense) |
|--------|------------------------|---------------------|
| None | 81.00% | — |
| Typosquatting (title) | 78.00% | — |
| Typosquatting (all texts) | 72.00% | — |
| Prompt injection (prefix) | 75.00% | 76.00% |
| Prompt injection (suffix) | 55.50% | 63.50% |
| **Text-to-image** | **5.00%** | **60.00%** |

**Krytyczna luka**: adversarial testy dotyczą TYLKO HTML text attacks. **GAN logos, diffusion logos, delayed rendering — nie testowane.** CLIP zero-shot nie był ewaluowany w żadnej z tych kategorii.

## Metodologia

- Knowledge graph: 20k brands, web crawling + entity resolution z Wikidata + Whois
- LLM text extractor (TBE): wydobywa brand z HTML gdy logo-based extractor (LBE) zawodzi
- Fusion: LBE (visual) → jeśli fail → TBE (text) → domain check
- Datasets: TR-OP (main), SG-SCAN (field study, Singapore)

## Luki / Ograniczenia (gap analysis)

- **Nie testowano na visual adversarial attacks** (GAN logos, diffusion logos → CLIP jako rozwiązanie)
- Error analysis: "Bank Promerica, Minnesota Unemployment Insurance... not even included in Wikidata" → neobanki i fintech underrepresented
- 2.02s/sample zbyt wolno dla browser extension (target: <500ms)
- Brak delayed rendering defense (Yuan 2026 nie rozważany)

## Notatki

*Jedno z NAJWAŻNIEJSZYCH referencji dla projektu — KnowPhish to state-of-the-art RBPD (2024). Nasz projekt powinien opierać się na KnowPhish i dodawać: (1) adversarial robustness, (2) banking trademark registry integration, (3) polskie/europejskie regestry. Pobierz PDF z arxiv:2403.02253 i uruchom `/summarize-paper li-knowphish-multimodal-2024`*

**Rola w projekcie**: Bazowa architektura do rozszerzenia + benchmark (20k brand knowledge base).
