---
title: "Spear Phishing With Large Language Models"
date: 2023-01-01
authors: "Julian Hazell"
status: read
doi: "arxiv:2305.06972"
category: "Security"
tags:
  - spear-phishing
  - llm
  - social-engineering
  - email-security
  - ai-safety
  - dual-use-ai
  - prompt-engineering
  - governance
  - project/spear-phishing-context
---

# Spear Phishing With Large Language Models

## Metadane
- **Autorzy**: Julian Hazell
- **Rok**: 2023
- **Zrodlo**: arXiv:2305.06972, Oxford Internet Institute / Centre for the Governance of AI
- **DOI**: arxiv:2305.06972
- **Status**: `#read`
- **Kategoria**: Security
- **Tagi**: `#spear-phishing` `#llm` `#social-engineering` `#email-security` `#ai-safety` `#dual-use-ai` `#prompt-engineering` `#governance`

## Streszczenie

Praca bada jak LLM moga byc uzywane do spear phishingu - od fazy rekonesansu po generowanie ataku i kompromitacje ofiary. Autor demonstruje praktycznie, ze GPT-3.5 i GPT-4 moga generowac spersonalizowane emaile phishingowe dla ponad 600 brytyjskich czlonkow parlamentu przy koszcie ulamka centa za email. Dane wejsciowe: publiczne informacje ze stron Wikipedia scrapowane przez GPT-4.

Kluczowe odkrycia: LLM obnizyly trzy bariery dla atakujacych: (1) workload kognitywny - LLM generuje emaile bez udzialu czlowieka; (2) koszt finansowy - GPT-3.5 <$0.01/email, GPT-4 ~$0.02/email; (3) wymagania umiejetnosci - nawet niewyspecjalizowani atakujacy moga tworzyc przekonujace ataki. Autor rowniez demonstruje, ze proste prompt engineering obchodzi safeguardy RLHF w LLM.

Praca proponuje dwa rozwiazania obronne: (1) structured access schemes (API z kontrola dostepu, monitoringiem i wspolpraca z organami scigania); (2) LLM-based defensive systems (analiza przychodzacych emaili przez LLM w poszukiwaniu sygnatur phishingowych). Praca ma charakter policy-oriented i jest jednym z pierwszych empirycznych dowodow na skalowalne LLM-driven spear phishing.

## Kluczowe Wnioski
- LLM (GPT-3.5, GPT-4, Claude) sa zdolne do generowania realistycznych, spersonalizowanych spear-phishingowych emaili dla setek celow przy koszcie ponizej $10/1000 emaili
- Jakosc rosnie drastycznie miedzy modelami: GPT-3 (ogolnikowe) -> GPT-3.5 (srednie) -> GPT-4 (wysoka personalizacja, odwolania do partii politycznej, historii, wartosci celu)
- Prompt engineering (bez jailbreakow) wystarczy do obejscia safeguardow; LLM nie rozroznia miedzy phishingiem a kampania marketingowa
- Spear phishing przez LLM pokrywa caly cyber kill chain: collect (Wikipedia scraping) -> contact (email generation) -> compromise (VBA macro generation)
- Darktrace odnotowalo 135% wzrost novel social engineering attacks w I/II 2023, przypisuje to popularyzacji ChatGPT
- Open-source LLM (LLaMA 30B) rowniez zdolny do generowania convincing emails, co utrudnia governance przez API-controlled access
- Agentic AI (Auto-GPT) moze w przyszlosci automatyzowac caly lancuch ataku bez udzialu czlowieka

## Metodologia

**Zbieranie danych (Collect phase):**
- GPT-4 napisal Python script do scrapowania Wikipedii dla wszystkich brytyjskich MP wybranych w 2019 r.
- GPT-3.5 przetwarza surowe dane Wikipedia na ustrukturyzowane biografie (imie, okrag, partia, zainteresowania, historia zawodowa)

**Generowanie emaili (Contact phase):**
- Autor poprosil GPT-4 o opisanie cech skutecznego spear-phishingowego emaila
- Identyfikowane cechy: personalizacja, kontekstowa trafnosc, psychologia (strach/ciekawosc/pilnosc), autorytet
- Te cechy + biografia = prompt -> GPT-3.5/GPT-4 generuje email
- Przetestowani: GPT-3, GPT-3.5, GPT-4, Claude Instant, Claude-v1, LLaMA 30B (HuggingChat)

**Kompromitacja (Compromise phase):**
- GPT-4 poproszony (jako "badacz cyberbezpieczenstwa") o VBA macro pobierajace payload z zewnetrznego URL

**Dane: 600+ brytyjskich MP** - dane publiczne z Wikipedii

## Glowne Koncepcje

**Cyber Kill Chain dla spear phishingu**: Collect (wywiad OSINT) -> Contact (generowanie i wyslanie emaila) -> Compromise (malware delivery). LLM pomaga na wszystkich etapach.

**Misuse-Use Tradeoff**: Blokowanie LLM na poziomie modelu ogranicza zarowno nuzywanie jak i misuse - zbyt grube narzedzie. Lepszym podejsciem jest governance na poziomie dostepu (API).

**Structured Access Schemes**: Kontrolowane API zamiast open weights; umozliwia monitorowanie, banowanie naduzywajacych uzytkownikow, wspolprace z organami scigania.

**Skalowalnosc ataku**: Tradycyjnie spear phishing wymagal per-user effort -> atakujacy celowal w nielicznych najwartosciowszych. LLM obnizyly koszt krancowy, co umozliwia masowe personalizowane ataki.

## Wyniki

Koszt generowania emaili:
- GPT-3: <$0.01 per email, 2 sekundy
- GPT-3.5: <$0.01 per email, 14 sekund
- GPT-4: $0.02 per email, 40 sekund
- Claude Instant: <$0.01, 3 sekundy
- Claude-v1: $0.01, 7 sekund

1000 emaili przez Claude: ~$10 w <2 godziny

Jakosc: GPT-4 generuje emaile odwolujace sie do konkretnych wartosci politycznych, historii zawodowej, okragu wyborczego celu - przekonujace nawet przy krytycznej ocenie.

## Przydatne Cytaty

"using Claude, Anthropic's most capable model, a hacker could generate a batch of 1,000 spear phishing emails for a cost of just $10 USD, all in under 2 hours." (str. 3)

"Despite having no formal background in cybersecurity, I was able to execute key steps in a mass spear phishing campaign in as little as a few hours." (str. 9)

"Due to the inherent dual-use nature of LLMs, it is difficult to create models that can only funnel their intelligence towards positive use." (str. 10)

"LLMs have still plausibly lowered the barrier to entry for less sophisticated cybercriminals to launch spear phishing campaigns." (str. 7)

## Datasety
- UK Parliament Wikipedia dataset - ~600 publicznych profili brityjskich MP (scrapowanych na potrzeby badania, nie opublikowany publicznie)

## Powiazane Tematy
- AI safety i dual-use AI governance
- Prompt engineering i jailbreaking safeguards
- Agentic AI i autonomous cyberattacks (Auto-GPT)
- LLM-based email security (obrona przez LLM)
- Social engineering attack taxonomy (Jagatic et al. 2007)
- Structured access schemes (Shevlane 2022)
- RLHF i alignment ograniczenia

## Notatki

