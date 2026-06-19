---
title: "Actionable Cyber Threat Intelligence using Knowledge Graphs and Large Language Models"
date: 2024-01-01
authors: "Romy Fieblinger, Md Tanvirul Alam, Nidhi Rastogi"
status: read
doi: "arXiv:2407.02528"
category: "Security"
tags:
  - cyber-threat-intelligence
  - knowledge-graphs
  - large-language-models
  - triple-extraction
  - link-prediction
  - information-extraction
  - project/graph-phishing-detection
---

# Actionable Cyber Threat Intelligence using Knowledge Graphs and Large Language Models

## Metadane
- **Autorzy**: Romy Fieblinger, Md Tanvirul Alam, Nidhi Rastogi
- **Rok**: 2024
- **Źródło**: 6th Workshop on Attackers and Cyber-Crime Operations (WACCO 2024)
- **DOI/Link**: arXiv:2407.02528
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca dotyczy automatyzacji ekstrakcji praktycznej (actionable) wiedzy o zagrożeniach (Cyber Threat Intelligence, CTI) z nieustrukturyzowanych raportów przez połączenie dużych modeli językowych (LLM) z grafami wiedzy (Knowledge Graphs, KG). Autorzy testują otwarte modele open-source (seria Llama 2 w wariantach 7B/13B/70B, Mistral 7B Instruct, Zephyr-7B-beta) do wydobywania trójek `<encja_glowna, relacja, encja_ogon>` z tekstu CTI, porównując trzy techniki: prompt engineering (few-shot), framework guidance firmy Microsoft (wymuszanie formatu wyjścia) oraz dostrajanie metodą QLoRA (4-bit).

Eksperymenty oparto na dwóch zbiorach Alam et al.: anotowanym ręcznie (120 raportów CTI o 36 rodzinach malware na Androida) oraz dużym (~12 000 raportów). Najlepszy okazał się dostrojony Llama 2 7B chat (najwyższe wyniki ROUGE i ocena ludzka). Z dużego korpusu model wygenerował graf wiedzy, który następnie poddano predykcji powiązań (link prediction) z użyciem TuckER (ustawienie transduktywne) i NodePiece (ustawienie induktywne, obsługujące niewidziane encje).

Kluczowe ustalenia: (1) guidance przewyższa zwykły prompt engineering przy mniejszym nakładzie pracy; (2) dostrajanie poprawia wyniki, krótsze prompty działają lepiej niż długie; (3) modele dobre na małym zbiorze testowym dają zaszumione wyniki na dużej skali — włączenie typów encji do przykładów/danych treningowych jest niezbędne dla zgodności z ontologią; (4) KG zbudowany z CTI przez LLM wykazuje obiecujące zdolności predykcji powiązań i generalizacji induktywnej.

## Kluczowe Wnioski
- Guidance (wymuszanie formatu) > prompt engineering w trybie few-shot dla ekstrakcji trójek CTI.
- Dostrajanie QLoRA poprawia jakość trójek; format separacji instrukcja/tekst silnie wpływa na wynik.
- Skalowanie z małego testu na duży korpus generuje szum — konieczny postprocessing i jawne typy encji.
- KG z CTI umożliwia predykcję powiązań (TuckER transduktywnie, NodePiece induktywnie), wspierając proaktywną detekcję zagrożeń.

## Metodologia
Pipeline: adaptacja modelu (few-shot/guidance lub QLoRA) -> ewaluacja (ROUGE-N, ROUGE-L + ocena ludzka) -> generacja trójek -> budowa KG -> predykcja powiązań (metryki MRR, Hits@n). Ontologia: encje (Malware, MalwareType, Organization, ThreatActor, Indicator, AttackPattern itp.) i 10 relacji (isA, targets, uses, hasAuthor, indicates, exploits, variantOf...). Sprzęt: NVIDIA A100, biblioteki HuggingFace (transformers, peft, trl, bitsandbytes), pykeen do osadzeń KG.

## Główne Koncepcje
- **CTI** — wiedza o aktorach zagrożeń, IoC i TTP.
- **Knowledge Graph** — strukturalna reprezentacja trójek encja-relacja-encja.
- **Link Prediction** — uzupełnianie brakujących faktów w KG (transduktywne vs induktywne).
- **Guidance / QLoRA** — kontrola wyjścia LLM i wydajne dostrajanie.

## Relevancja dla graph-phishing-detection
Praca jest bezpośrednio relewantna dla wątku "graf wiedzy domenowej" w projekcie: pokazuje, jak z nieustrukturyzowanych źródeł (raporty, blogi) zbudować graf wiedzy o zagrożeniach i wykonać na nim predykcję powiązań — analogicznie można budować graf domenowy phishingu (domeny, IP, nameservery, aktorzy, kampanie BEC/spear) i przewidywać brakujące powiązania. Istotne dla projektu jest rozróżnienie ustawienia transduktywnego vs induktywnego (NodePiece radzi sobie z niewidzianymi encjami), co wprost wiąże się z indukcyjnością modeli GNN i ewaluacją na nowych domenach/encjach. Ostrzeżenie o spadku jakości przy skalowaniu i potrzebie ewaluacji świadomej szumu/przecieku jest cenne dla rygorystycznej ewaluacji w projekcie.

## Przydatne Cytaty
- "guidance framework significantly improved the output beyond what is achievable with few-shot prompt engineering alone" (Conclusion).
- "models trained on extracted triples showing enhanced performance and robust generalization from known to unknown data relationships" (Finding 4).

## Datasety
- Anotowany zbiór CTI Alam et al. (120 raportów, 36 rodzin malware Android, 2015-2022).
- Duży korpus ~12 000 raportów open-source CTI.

## Powiązane Tematy
- Budowa grafów wiedzy domenowej z tekstu.
- Induktywna vs transduktywna predykcja powiązań.
- Osadzenia KG (TuckER, RotatE, NodePiece).

## Notatki
