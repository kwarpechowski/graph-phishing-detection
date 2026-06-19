---
title: "User-Centric Phishing Detection: A RAG and LLM-Based Approach"
date: 2026-01-29
authors: "Abrar Hamed Al Barwani, Abdelaziz Amara Korba, Raja Waseem Anwar"
status: read
doi: "arxiv:2601.21261"
category: "Security"
tags:
  - phishing-detection
  - llm
  - rag
  - retrieval-augmented-generation
  - email-security
  - false-positives
  - personalization
  - user-profiling
  - project/personalized-phishing-defense
---

# User-Centric Phishing Detection: A RAG and LLM-Based Approach

## Metadane
- **Autorzy**: Abrar Hamed Al Barwani, Abdelaziz Amara Korba, Raja Waseem Anwar (German University of Technology in Oman)
- **Rok**: 2026
- **Zrodlo**: arXiv:2601.21261v1 [cs.CR], 29 stycznia 2026
- **DOI**: arxiv:2601.21261
- **Status**: `#read`
- **Kategoria**: Security
- **Tagi**: `#phishing-detection` `#llm` `#rag` `#email-security` `#false-positives` `#personalization` `#user-profiling`

## Streszczenie

Praca proponuje system detekcji phishingu w emailach laczacy LLM z retrieval-augmented generation (RAG), ktorego glownym celem jest REDUKCJA FALSE POSITIVES. Kluczowa obserwacja autorow: LLM uzywane jako samodzielne klasyfikatory generuja wysokie FPR, bo analizuja email w izolacji, bez kontekstu uzytkownika. Rozwiazaniem ma byc "dual-context retrieval": dla kazdego przychodzacego emaila system (1) pobiera ze zbioru historycznych LEGITIMATE emaili uzytkownika k=5 semantycznie najbardziej podobnych (FAISS + all-MiniLM-L6-v2, cosine), oraz (2) wzbogaca decyzje o reputacje domeny/URL w czasie rzeczywistym z VirusTotal. Te dowody trafiaja do promptu LLM, ktory zwraca strukturyzowany JSON (klasyfikacja, phishing score 0-10, ryzyko, taktyki SE, akcje).

Ewaluacja: zbalansowany korpus 500 emaili (250 legit / 250 phishing), legit z prawdziwych skrzynek (IMAP read-only za zgoda), phishing z publicznych repozytoriow. Cztery modele open-source przez Groq API: Llama4-Scout (17B), DeepSeek-R1 (70B), Mistral-Saba (24B), Gemma2-9B. Porownanie z RAG vs bez RAG.

Wyniki: RAG konsekwentnie poprawia precyzje i F1 oraz obniza FPR przy zachowaniu wysokiego recall. Najlepszy: Llama4-Scout z RAG - F1=0.9703, FPR spada z 0.12 do 0.04 (redukcja FP 66.7%). Wniosek: personalizacja oparta na historii legalnej korespondencji uzytkownika dziala jako mechanizm dezambiguacji, redukujac falszywe alarmy bez utraty detekcji.

## Kluczowe Wnioski
- LLM jako standalone klasyfikatory phishingu maja wysokie FPR przez brak kontekstu uzytkownika; "nietypowy ale legalny" email jest mylnie flagowany
- RAG z historii legalnych emaili uzytkownika + threat intelligence (VirusTotal) redukuje FP o ~67% (Llama4-Scout: 12% -> 4% FPR)
- Llama4-Scout z RAG: F1=0.9703, najlepszy balans; DeepSeek-R1 z RAG blisko (F1=0.9608)
- Personalizacja skaluje sie miedzy modelami 9B-70B; mniejsze modele tez korzystaja
- Recall byl wysoki juz bez RAG (0.98-1.0); RAG poprawia glownie precyzje/FPR (kalibracja decyzji)
- Profilowanie uzytkownika to baza legalnych emaili indeksowana w FAISS - NIE zwalidowany instrument behawioralny

## Metodologia
- **Preprocessing**: dekodowanie multi-encoding, ekstrakcja {subject, sender, body}, normalizacja Unicode, strip headerow, walidacja sender
- **Embeddingi**: all-MiniLM-L6-v2 (d=384), L2-normalizacja, indeks FAISS, cosine similarity
- **Threat intel**: VirusTotal multi-engine (75 silnikow) dla domen i URL z emaila
- **Retrieval**: top-k=5 semantycznie podobnych legalnych emaili z historii uzytkownika; query wykluczany z retrievalu, FAISS budowany tylko z train-portion legit (anti-leakage)
- **Prompt**: rola "cybersecurity expert" + email + RAG context + threat intel + JSON schema; temperatura 0.2
- **Stack**: Python 3.10, LangChain, FAISS, Sentence-Transformers, Groq, Pandas
- **Dane**: 500 emaili (250/250), stratified splits

## Glowne Koncepcje
- **Dual-context retrieval**: laczenie user-specific historical patterns (legalne emaile) z real-time threat intelligence jako baza decyzji LLM
- **Personalized spam filter**: detekcja dostosowana do indywidualnych wzorcow komunikacji, nie generyczne reguly
- **FP reduction via contextual disambiguation**: kontekst legalnych emaili pozwala odroznic uniwersalnie zlosliwe od "nietypowe ale normalne dla tego uzytkownika"

## Wyniki

Tabela (N=500), bez RAG -> z RAG:
- Llama4-Scout: F1 0.9333 -> 0.9703; FPR 0.12 -> 0.04
- DeepSeek-R1: F1 0.9009 -> 0.9608; FPR 0.22 -> 0.06
- Mistral-Saba: F1 0.8489 -> 0.9524; FPR 0.356 -> 0.10 (najwiekszy relatywny zysk)
- Gemma2-9B: F1 0.8333 -> 0.8621; FPR 0.40 -> 0.32 (najslabszy, nadal sklonny do FP)

Recall pozostal wysoki (0.98-1.0) we wszystkich konfiguracjach.

## Przydatne Cytaty

"using them as standalone classifiers often yields elevated false-positive (FP) rates, which mislabel legitimate emails as phishing and create significant operational burden." (Abstract)

"the dual-context retrieval mechanism that combines user-specific historical patterns with real-time threat intelligence... enables the system to distinguish between genuinely malicious emails and legitimate communications that may appear suspicious to generic classifiers but are normal for specific users." (Sec. I)

"Llama4-Scout attains an F1-score of 0.9703 and achieves a 66.7% reduction in FPs with RAG." (Abstract)

## Datasety
- Prywatny korpus 500 emaili (250 legit z skrzynek instytucjonalnych/osobistych GUtech via IMAP, 250 phishing z publicznych repozytoriow) - nieopublikowany

## Powiazane Tematy
- APOLLO (Desolda et al. 2024), ChatSpamDetector (Koide et al. 2024) - LLM phishing detection
- RAG (Lewis et al. 2020)
- Profilowanie uzytkownika w bezpieczenstwie email

### CLOSENESS verdict vs nasz projekt: ADJACENT

Ta praca dzieli z nami slowo "personalized/user-centric profiling", ale w ZUPELNIE innym sensie i po DEFENSYWNEJ stronie detekcji email-klasyfikacji. To NIE jest duplikat naszego rdzenia.

**DELTA - czego ta praca NIE robi (a my robimy):**

(i) **Zwalidowany profiler jako mierzony instrument?** NIE. Ich "profil" = zwykla baza legalnych emaili w FAISS. Brak jakiejkolwiek walidacji: brak kappa vs human, brak testu reprodukowalnosci, brak odpornosci na szum. Profil jest narzedziem retrievalu, nie obiektem pomiaru.

(ii) **Zero-day personal-baseline bijacy supervised-on-known?** NIE. Ich setup to klasyczna detekcja na zbalansowanym zbiorze znanych phishingow (250 legit/250 phish z publicznych repozytoriow). Nie ma head-to-head zero-day vs supervised-on-known; nie ma protokolu pretekstowego zero-day. RAG sluzy redukcji FP, nie wykrywaniu nieznanych atakow personalnych.

(iii) **Odpornosc adwersarialna?** NIE testowana. Autorzy sami wymieniaja "aggressively obfuscated URLs and domains" oraz "domain shifts" jako przyszle prace (Conclusion) - czyli explicite poza zakresem.

Brak rowniez empirycznie rankowanej taksonomii atakow. Profilowanie po stronie OBRONCY (filtr) - przeciwnie do naszego nacisku na baseline ofiary jako instrument pomiarowy.

Najblizszy punkt styku: idea, ze kontekst uzytkownika redukuje FP - mozemy cytowac jako prior art dla "personal baseline pomaga", ale ich realizacja jest plytka (retrieval), nie zwalidowany instrument.

## Notatki

Istnienie potwierdzone: strona abstraktu arXiv:2601.21261 rozwiazuje sie, PDF pobrany z arxiv.org/pdf (319 KB, naglowek %PDF OK). CLI paper-search zwrocil 0 (arXiv API rate-limited HTTP 429 na tym hoscie podczas weryfikacji), ale samo pobranie PDF + strona abstraktu sa rozstrzygajacym dowodem istnienia. Tytul i autorzy zgodni z claimem.