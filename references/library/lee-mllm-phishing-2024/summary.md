---
title: "Multimodal Large Language Models for Phishing Webpage Detection and Identification"
date: 2024-01-01
authors: "Jehyun Lee, Peiyuan Lim, Bryan Hooi, Dinil Mon Divakaran"
status: to-read
doi: "arXiv:2408.05941"
tags: []
---
# Multimodal Large Language Models for Phishing Webpage Detection and Identification

## Metadane
- **Autorzy**: Jehyun Lee, Peiyuan Lim, Bryan Hooi, Dinil Mon Divakaran
- **Rok**: 2024
- **Źródło**: arXiv 2408.05941
- **DOI**: arXiv:2408.05941
- **Status**: to-read
- **Cytowania**: N/A (nowy)
- **Kategoria**: Security / Multimodal AI
- **Tagi**: #to-read #phishing #mllm #llm #brand-detection #zero-reference #visual-phishing #divakaran-group #no-reference-list

## Streszczenie

Praca z grupy Divakaran (NTU Singapore) — tego samego zespołu który stworzył Phishpedia, PhishIntention i KnowPhish. System dwufazowy używający multimodal LLM: **Phase 1** — LLM identyfikuje markę impersonowaną z logo, motywu, favicony (bez żadnej reference list); **Phase 2** — weryfikacja domeny URL vs identified brand.

**Kluczowy przełom**: eliminuje problem maintenance reference list (główna słabość Phishpedia/KnowPhish). LLM posiada wbudowaną wiedzę o markach z pretrainingu. System "significantly outperforms a state-of-the-art brand-based detector" i jest "robust to two known adversarial attacks."

## Kluczowe Wnioski

- Eliminuje konieczność utrzymywania bazy marek — LLM ma pretrained brand knowledge
- Dwufazowe: brand identification (visual) → domain verification (text)
- Pokonuje KnowPhish/PhishIntention na ich własnych benchmarkach
- Odporny na dwa znane ataki adwersaryjne (które ataki? — sprawdzić w PDF)
- **Ograniczenie**: nie testowany na GAN logos (Lee 2023) ani delayed rendering (Yuan 2026)

## Znaczenie dla projektu — WAŻNE

**To jest aktualny SOTA (2024) — musimy z nim się zmierzyć.**

Nasza przewaga vs ten system:
1. **Adversarial hardening**: ten system nie ma PGD training ani certyfikowanej robustności
2. **DOM timing defense**: ten system nie broni delayed rendering
3. **Szybkość**: MLLM inference = 800ms-3s; nasz CLIP = 80-150ms
4. **Koszt**: MLLM API (OpenAI/Gemini) = kosztowny; nasz system = self-hosted

**Pozycja w naszej pracy**:
- Section 2.1 Related Work: "Most recently, Lee et al. (2024) propose an MLLM-based system eliminating the reference list. However, their approach has not been evaluated against adversarial logo attacks (Lee 2023) or timing-based evasion (Yuan 2026)."
- EXP-5: dodaj jako Baseline #3 (obok PhishIntention i KnowPhish) — jeśli mamy dostęp do modelu

## Powiązane Tematy

- KnowPhish (Li 2024) — poprzednia praca tej samej grupy (Divakaran)
- PhishIntention (Liu 2022) — poprzednia praca tej grupy
- PhishOracle (Kulkarni 2024) — adversarial attacks na te systemy
- CLIP (Radford 2021) — nasza alternatywa: zero-shot bez API costs

## Notatki

*MUST-READ: to jest najnowszy SOTA od czołowej grupy badawczej w tej dziedzinie. Pobierz i przeczytaj dokładnie przed pisaniem related work. Sprawdź: jakie dwa ataki adwersaryjne testowali? Czy są inne słabości?*
