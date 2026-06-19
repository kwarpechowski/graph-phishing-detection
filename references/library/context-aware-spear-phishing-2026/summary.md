---
title: "Context-Aware Spear Phishing: Generative AI-Enabled Attacks Against Individuals via Public Social Media Data"
date: 2026-05-11
authors: "Elham Pourabbas Vafa, Sayak Saha Roy, Shirin Nilizadeh"
status: read
doi: "arxiv:2605.11268"
category: "Security"
tags:
  - spear-phishing
  - context-aware
  - generative-ai
  - llm
  - social-media
  - osint
  - attack-taxonomy
  - prompt-level-defense
  - user-study
  - project/personalized-phishing-defense
---

# Context-Aware Spear Phishing: Generative AI-Enabled Attacks Against Individuals via Public Social Media Data

## Metadane
- **Autorzy**: Elham Pourabbas Vafa, Sayak Saha Roy, Shirin Nilizadeh (UT Arlington; Louisiana State University)
- **Rok**: 2026
- **Zrodlo**: arXiv:2605.11268v1 [cs.CR], 11 maja 2026
- **DOI**: arxiv:2605.11268
- **Status**: `#read`
- **Kategoria**: Security
- **Tagi**: `#spear-phishing` `#context-aware` `#generative-ai` `#llm` `#social-media` `#osint` `#attack-taxonomy` `#prompt-level-defense` `#user-study`

## Streszczenie

Praca OFENSYWNO-pomiarowa: pokazuje jak publiczne dane z social media (Instagram) + GenAI umozliwiaja zautomatyzowane, skalowalne, kontekstowo-swiadome ataki spear phishing na osoby prywatne. Modularny framework: (1) Contextual Extraction (multimodalna ekstrakcja sygnalow przez GPT-4o), (2) Attack Type x Context Integration, (3) Style Mimicry, (4) Output Formatting. Taksonomia DWUOSIOWA: 7 typow atakow (baiting, scareware, honey trap, quid pro quo, tailgating, impersonation, personalized emotional exploitation) x 5 wymiarow kontekstowych (location, relationships, interests, sentiment, events) = 7x5 = 35 kombinacji (to "7x5 taxonomy" z claimu).

Skala: 200 publicznych profili Instagram (3268 postow), ~18K wygenerowanych emaili przez 5 modeli (GPT-4, Claude 3-haiku, Gemini 1.5-flash, Gemma 7B, LLaMA 3.3). Wystarcza 10-15 postow na uzytkownika (analiza information gain: entropia plateau po poscie 5). Ewaluacja: 8 wymiarow jakosci, anotacja tri-LLM majority vote (kappa=0.76) + walidacja ludzka (kappa=0.93, 98.3% accuracy). Benchmark vs 4K realnych phishingow APWG eCrimeX.

Wyniki: emaile GenAI WYRAZNIE przewyzszaja realny phishing APWG (personalizacja 85-90% vs 8.6%, naturalnosc ~100% vs 51%, perswazja >90% vs 32.7%). Badanie na ludziach (IRB, 70 os. Prolific): emaile LLM ocenione jako MNIEJ podejrzane (suspiciousness 2.75 vs 4.44 APWG); detection gap UJEMNY w warunku LLM (-0.36) - czyli phishing LLM mniej podejrzany niz benign. Tailgating i impersonation szczegolnie skuteczne.

Obrona: prompt-level. Klasyfikator RoBERTa (98.13% acc, 0 FP) blokuje zlosliwe prompty PRZED generacja; DeBERTa do detekcji sub-prompt (adaptacyjny atakujacy budujacy prompt przyrostowo). Testowano tez SOTA safety filters (ShieldGemma, LlamaGuard, WildGuard) - domyslnie slabe, poprawia je policy injection i SI+CoT.

## Kluczowe Wnioski
- 7x5 taksonomia (7 typow atakow x 5 wymiarow kontekstowych) - pierwsza zunifikowana taksonomia + ewaluacja spear phishingu
- 10-15 postow Instagram wystarcza (entropia plateau po ~5 postach); koszt <$0.004/email
- GenAI phishing bije realny APWG na WSZYSTKICH 8 wymiarach jakosci; szczegolnie personalizacja (85-90% vs 8.6%)
- User study: emaile LLM MNIEJ podejrzane niz APWG, a nawet mniej niz benign (ujemny detection gap -0.36); tailgating + impersonation najgrozniejsze
- Tylko 1-2 realne cue uzytkownika przenoszone do emaila; reszta encji (17-50) fabrykowana przez model
- OBRONA prompt-level: RoBERTa 98.1% acc/0 FP, DeBERTa dla sub-prompt; testy ADAPTACYJNEGO atakujacego (1750 wariantow promptow, ablacje komponentow)
- Open science: kod + anonimizowany subset emaili udostepnione

## Metodologia
- **Sampling**: CrowdTangle -> 10K profili -> 200 losowych; 3268 postow (czerwiec 2023 - czerwiec 2024); GPT-4o do opisow obrazow
- **Generacja**: 5 LLM, abstain gdy brak kontekstu; 17916 emaili
- **Ewaluacja jakosci**: 8 wymiarow binarnych (contextual relevance, persuasiveness, emotional manipulation, personalization, linguistic naturalness, specificity of CTA, credibility of sender, technical sophistication); tri-LLM majority vote + human (150 emaili, kappa=0.93)
- **Baseline**: 6000 emaili APWG eCrimeX -> 3937 sklasyfikowanych jako spear phishing
- **User study**: IRB, 70 Prolific (US, 18+), between-subjects, Likert, Kruskal-Wallis/Welch, attention checks
- **Obrona**: RoBERTa (1750 mal. promptow + 2000 benign z Enron; 98.13% acc); DeBERTa-v3-large sub-prompt (94.4% acc); benchmark ShieldGemma/LlamaGuard/WildGuard + policy injection + SI+CoT
- **Adaptacyjny atak**: 50 wariantow/seed, round-robin ablacja komponentow (1)(2)(3), 82% wciaz generuje phishing

## Glowne Koncepcje
- **Two-axis taxonomy (7x5)**: attack types (psychologia manipulacji) x contextual dimensions (wektory personalizacji)
- **Information gain analysis**: ile postow trzeba (entropia, entity diversity, incremental gain) - plateau ~5-10 postow
- **Prompt-level defense**: blokowanie zlosliwego INTENTU przed generacja tresci (RoBERTa/DeBERTa)
- **Detection gap**: S_malicious - S_benign; ujemny w LLM = phishing mniej podejrzany niz benign

## Wyniki
- Table 1: GPT-4 >98% persuasiveness/emotional; APWG personalizacja 8.6%, persuasiveness 32.7%, naturalnosc 51%
- User study: suspiciousness LLM 2.75 vs APWG 4.44 (H=27.22, p<1e-6); detection gap LLM -0.36 vs APWG +1.61
- RoBERTa: Acc 98.13%, Precision 100%, Recall 96%, F1 97.95%, 0 FP; generalizacja 100% na 175 cross-model promptach
- DeBERTa sub-prompt: Acc 94.4%, macro-F1 0.945
- SOTA filters default slabe (pass-through 80-100% zlosliwych); policy injection do 96%, SI+CoT do 98.7% (WildGuard)
- Koszt $0.002-0.004/email

## Przydatne Cytaty

"a small amount of public activity per target is sufficient for GenAI models to extract interests and contextual cues, producing persuasive messages that mirror a target's style while bypassing generic content-moderation safeguards." (Abstract)

"those in the LLM condition had a negative gap (delta_susp = -0.36), meaning LLM-generated phishing emails were, on average, rated as less suspicious than benign ones." (Sec. 7.7.4)

"Our RoBERTa-based detector achieves 98.1% accuracy, generalizes across models and attack types, and remains robust under adaptive evasion strategies." (Contributions)

## Datasety
- 200 publicznych profili Instagram via CrowdTangle (3268 postow) - nieudostepnione (prywatnosc)
- APWG eCrimeX - 6000 realnych phishingow (3937 spear phishing)
- Enron Email Dataset - 2000 benign promptow
- Udostepniony: anonimizowany subset wygenerowanych emaili + kod (USENIX open science)

## Powiazane Tematy
- E-PhishGEN (Pajola et al. 2025), SpearBot (Qi et al. 2025), PiMRef (Liu et al. 2025) - generacja/detekcja spear phishingu
- Roy et al. 2024 "From Chatbots to Phishbots" (ten sam zespol)
- Prompt injection / jailbreak defenses; LlamaGuard, WildGuard, ShieldGemma
- Menlo Report (etyka)

### CLOSENESS verdict vs nasz projekt: ADJACENT (z waznym overlapem na taksonomii)

To praca ofensywno-pomiarowa po stronie ATAKU + obrona PROMPT-LEVEL (blokowanie generacji). Nasz projekt jest defensywny, skoncentrowany na profilerze ofiary jako instrumencie i detekcji zero-day. Inny punkt ciezkosci, ale jest jeden realny overlap: TAKSONOMIA.

**Overlap do uwagi**: ich 7x5 taksonomia (7 typow x 5 kontekstow) to dokladnie obszar naszego "empirically-ranked taxonomy". ALE ich taksonomia jest opisowa/scoping-review (21 prac) + zmierzona pod katem JAKOSCI GENERACJI emaili, NIE empirycznie rankowana pod katem skutecznosci ataku jako rdzen kontrybucji. Maja czastkowy ranking (np. tailgating/impersonation najmniej podejrzane w user study) - to najblizsze prior art dla naszego rankingu i trzeba je cytowac, ale nie czyni naszego rankowanego ujecia zbednym.

**DELTA - czego ta praca NIE robi (a my robimy):**

(i) **Zwalidowany profiler ofiary jako mierzony instrument?** NIE. Robia ekstrakcje sygnalow (information gain analysis), ale to charakterystyka ile postow trzeba do ATAKU, nie zwalidowany defensywny profiler/baseline ofiary. Brak kappa profilera vs human, brak reprodukowalnosci profilu, brak odpornosci profilu na szum. Co ciekawe: pokazuja, ze tylko 1-2 realne cue sa przenoszone (reszta fabrykowana) - to wrecz argument, ze profil oparty na social media jest plytki.

(ii) **Zero-day personal-baseline bijacy supervised-on-known?** NIE. Ich obrona to SUPERVISED klasyfikator promptow (RoBERTa/DeBERTa) trenowany na znanym rozkladzie zlosliwych promptow - przeciwienstwo personal-baseline zero-day. Nie ma personal baseline ofiary ani protokolu zero-day pretekstowego.

(iii) **Odpornosc adwersarialna?** CZESCIOWO i TYLKO dla detektora promptow, nie dla profilera. Maja adaptacyjnego atakujacego (1750 wariantow, ablacje), ale to robustness ich obrony prompt-level, nie odpornosc spersonalizowanego baseline ofiary jak w naszym projekcie. Inny obiekt obrony.

Wniosek: silna, dobrze zewaluowana praca (skala 18K, user study IRB, prompt-level defense) - ale to inna gra (atak + prompt-gating). Realny punkt kolizji to taksonomia, gdzie musimy sie pozycjonowac jako dostarczajacy EMPIRYCZNY RANKING SKUTECZNOSCI/wykrywalnosci, podczas gdy oni daja taksonomie + jakosc generacji. Nasz triada (zwalidowany profiler + zero-day head-to-head + adversarial robustness profilera) nietknieta.

## Notatki

Istnienie potwierdzone: strona abstraktu arXiv:2605.11268 rozwiazuje sie, PDF pobrany z arxiv.org/pdf (4.7 MB, naglowek %PDF OK, 21 stron + appendiksy). CLI paper-search zwrocil 0 (arXiv API rate-limited HTTP 429 na hoscie podczas weryfikacji), ale pobranie PDF + strona abstraktu sa rozstrzygajace. Tytul, autorzy, 7x5 taksonomia, Instagram OSINT - wszystko zgodne z claimem.