---
title: "CTINexus: Automatic Cyber Threat Intelligence Knowledge Graph Construction Using Large Language Models"
date: 2024-01-01
authors: "Yutong Cheng, Osama Bajaber, Saimon Amanuel Tsegai, Dawn Song, Peng Gao"
status: read
doi: "arXiv:2410.21060"
category: "Security"
tags:
  - cyber-threat-intelligence
  - knowledge-graph-construction
  - large-language-models
  - in-context-learning
  - entity-alignment
  - relation-extraction
  - project/graph-phishing-detection
---

# CTINexus: Automatic Cyber Threat Intelligence Knowledge Graph Construction Using Large Language Models

## Metadane
- **Autorzy**: Yutong Cheng, Osama Bajaber, Saimon Amanuel Tsegai, Dawn Song, Peng Gao (Virginia Tech / UC Berkeley)
- **Rok**: 2024 (arXiv, v2 2025)
- **Źródło**: arXiv:2410.21060
- **DOI/Link**: https://arxiv.org/abs/2410.21060
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
CTINexus to framework do automatycznej ekstrakcji wiedzy z raportów Cyber Threat Intelligence (CTI) i budowy grafu wiedzy o cyberbezpieczeństwie (CSKG) z użyciem zoptymalizowanego in-context learning (ICL) dużych modeli językowych. Autorzy wskazują wady dotychczasowych metod: parsowanie składniowe (sztywne reguły/słowniki, słabo radzi sobie z osobliwościami CTI jak kropki w IP, podkreślenia w nazwach plików) oraz fine-tuning (wymaga dużych anotowanych zbiorów, "ontology lock-in"). CTINexus nie wymaga ani obszernych danych, ani strojenia parametrów i łatwo adaptuje się do różnych ontologii.

Pipeline ma trzy fazy: (1) ekstrakcja trójek encja-relacja w jednym zapytaniu LLM (end-to-end), z automatyczną konstrukcją promptu i doborem demonstracji metodą kNN (sortowanie rosnące wg podobieństwa — wykorzystuje recency bias); semi-otwarta ekstrakcja: typy encji wg ontologii MALOnt, relacje jako open RE; (2) hierarchiczne dopasowanie encji — grube grupowanie po typach (ICL) + drobne łączenie po podobieństwie embeddingów (próg 0,6, model text-embedding-3-large) z mechanizmem ochrony IOC; (3) predykcja relacji długodystansowych — wybór węzłów centralnych po degree centrality i wnioskowanie ukrytych relacji ICL, łączące rozłączne podgrafy.

Ewaluacja na 150 realnych raportach CTI z 10 platform (od maja 2023): F1 87,65% (ekstrakcja trójek), 89,94% (grupowanie grube), 99,80% (łączenie drobne), 90,99% (predykcja relacji); end-to-end F1 87,80% (minimalna propagacja błędów). CTINexus przewyższa EXTRACTOR o 25,36% F1 i LADDER o 19% w ekstrakcji encji. GPT-4 najlepszy backbone; adaptacja do ontologii STIX z niewielkim spadkiem (F1 85,6%). Koszt ~0,15 USD/raport (GPT-4).

## Kluczowe Wnioski
- ICL z LLM (bez fine-tuningu) umożliwia data-efficient ekstrakcję CTI i adaptację do nowych ontologii przez sam prompt.
- Hierarchiczne dopasowanie encji (typ → embedding) + ochrona IOC unika błędnego łączenia podobnych, lecz odrębnych encji (np. ".akira files" IOC vs "Akira" threat actor).
- Predykcja relacji długodystansowych przez degree centrality + ICL scala rozłączne podgrafy.
- GPT-4 znacząco przewyższa GPT-3.5/Llama3-70B/Qwen2.5-72B; mniejsze modele częściej halucynują.
- Minimalna propagacja błędów między fazami (brak efektu kuli śnieżnej).

## Metodologia
Zoptymalizowany ICL: kNN-retriever demonstracji (text-embedding-3-large, sortowanie rosnące), "one-CTI, one-inference" (redukcja tokenów o ~98% vs multi-turn QA). Ewaluacja na własnym zbiorze 150 raportów (Cohen's kappa 0,73), metryki F1/precision/recall na poziomie trójek i encji. Backbones: GPT-3.5/4, Llama3-70B, Qwen2.5-72B. Ontologie: MALOnt, STIX.

## Główne Koncepcje
- **CSKG (cybersecurity knowledge graph)**: węzły = encje (malware, podatności, threat actors, IOC), krawędzie = relacje.
- **In-context learning (ICL)**: adaptacja LLM z kilku przykładów bez aktualizacji wag.
- **Hierarchiczne dopasowanie encji**: grube grupowanie po typie + drobne łączenie po embeddingu z ochroną IOC.
- **Degree-centrality central entity + long-distance relation prediction**: scalanie podgrafów przez wnioskowanie ukrytych relacji.

## Relevancja dla graph-phishing-detection
CTINexus jest bezpośrednio relevantny dla rdzenia projektu — budowy grafu wiedzy domenowej w phishingu (cel publikacji P4 C&S "graf wiedzy domenowej"). Pokazuje gotowy pipeline LLM do konstrukcji grafu z nieustrukturyzowanych tekstów (raporty, opisy zagrożeń), z trzema technikami przenośnymi na domenę phishingu: ekstrakcja trójek wzbogacona ICL, hierarchiczne dopasowanie encji (kluczowe przy kanonizacji domen/marek/kont) oraz predykcja relacji długodystansowych przez centralność stopnia — analogiczna do scalania rozłącznych podgrafów komunikacja/domena/transakcje w multipleksie projektu. Wątek ochrony IOC i osobliwości encji (IP, hashe, URL) jest istotny przy grafowej detekcji phishingu URL/BEC. Praca dostarcza też ostrożnościowych wniosków o halucynacjach LLM i kosztach — relevantnych przy ewentualnym użyciu LLM do anotacji/wzbogacania grafów oraz przy rygorystycznej, leak-aware ewaluacji.
