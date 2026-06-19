---
title: "Prompted Contextual Vectors for Spear-Phishing Detection"
date: 2024-01-01
authors: "Daniel Nahmias, Gal Engelberg, Dan Klein, Asaf Shabtai"
status: read
doi: "arxiv:2402.08309"
category: "Security"
tags:
  - spear-phishing
  - phishing-detection
  - llm
  - document-vectorization
  - social-engineering
  - concept-drift
  - ensemble-learning
  - email-security
  - project/spear-phishing-context
---

# Prompted Contextual Vectors for Spear-Phishing Detection

## Metadane
- **Autorzy**: Daniel Nahmias, Gal Engelberg, Dan Klein, Asaf Shabtai
- **Rok**: 2024
- **Zrodlo**: arXiv (cs.LG), v3 Dec 2024
- **DOI**: arxiv:2402.08309
- **Afiliacja**: Ben-Gurion University of the Negev; Accenture Cyber Research Lab
- **Status**: `#read`
- **Kategoria**: Security
- **Tagi**: `#spear-phishing` `#phishing-detection` `#llm` `#document-vectorization` `#social-engineering` `#concept-drift` `#ensemble-learning` `#email-security`

## Streszczenie

Artykul proponuje nowa metode wektoryzacji dokumentow opartej na ensemble LLM do wykrywania spear-phishingu. Kluczowa innowacja jest technika "prompted contextual vectors": kazdy email jest reprezentowany jako wektor liczb zmiennoprzecinkowych, gdzie kazdy element to prawdopodobienstwo udzielone przez konkretny LLM w odpowiedzi na konkretne pytanie dotyczace perswazji i zloslwego contentu. Pytania sa projektowane recznie na podstawie znanych zasad perswazji Cialdiniego (wzajemnosc, konsekwencja, spoleczny dowod slusznosci, lubienie, autorytet, niedobor).

Metoda jest oceniana na unikalnym zbiorze 333 wysokiej jakosci spear-phishingowych emaili generowanych przez autorski system automatyzujacy wywiad OSINT i tworzenie spersonalizowanych emaili opartych na grafie wiedzy organizacji. Kluczowa innowacja eksperymentalna polega na trenowaniu klasyfikatora wylacznie na tradycyjnych emailach phishingowych i benign, a testowaniu na spear-phishingu - co naturalnie symuluje concept drift.

Metoda osiaga 91% F1 score przy uzyciu slabego klasyfikatora kNN (i 99% F1 przy CatBoost/XGBoost). Generalizuje rowniez do smishingu (SMS phishing) z 90% F1, mimo trenowania wylacznie na emailach - co potwierdza, ze wektory uchwytuja intencje zlosliwa, nie cechy stylometryczne.

## Kluczowe Wnioski
- Prompted contextual vectors (PCV) znacznie przewyzszaja state-of-the-art document embeddings (DistilBERT, MiniLM, MPnet, ada-002) w zadaniu wykrywania spear-phishingu przy symulowanym concept drift
- Recall=0.96 przy FPR=0.05 dla kNN vs recall 0.04-0.63 dla pozostalych metod
- Wizualizacja t-SNE pokazuje, ze PCV grupuja spear-phishing razem z tradycyjnym phishingiem (pozadane), podczas gdy DistilBERT tworzy osobny klaster - podatny na concept drift
- Gemini Pro jest najwazniejszym modelem w ensemble; kombinacja GPT-4 + Gemini Pro dorownuje pelemu ensemble (F1=0.91)
- Pytanie o suspicious link daje najsilniejszy sygnal (F1 loss = 0.13 po usunieciu)
- Wektory sa inherentnie interpretowalne - analiza bledow mozliwa przez badanie odpowiedzi poszczegolnych LLM
- Metoda dziala z open-source modelami (Llama 3.1 8B, Phi 3 Medium, Mistral Nemo) - F1=0.85 z kNN, F1=0.89 z Extra Trees

## Metodologia

**Architektura pipeline:**
1. Email jest wczytywany jako tekst
2. Kazdy LLM w ensemble (GPT-3.5, GPT-4, Gemini Pro) odpowiada na 7 pytan, uzywajac Chain-of-Thought prompting
3. Odpowiedz jest kwantyfikowana jako prawdopodobienstwo (float 0-1)
4. Wektor = konkatenacja prawdopodobienstw dla wszystkich kombinacji LLM x pytanie = 21 wymiarow
5. Wektor jest inputem dla klasyfikatora (kNN w eksperytmencie glownym)

**7 pytan (crafted recznie, oparte na Cialdini):**
- Czy email przekazuje poczucie pilnosci? (Scarcity)
- Czy jest znaczna ilosc pochlebstw? (Likeability)
- Czy link w emailu wydaje sie podejrzany?
- Czy email wyglada jak marketing?
- Czy email adresuje odbiorce z imienia i ze specyficznymi detalami?
- Czy sa grozby konsekwencji za niedzialanie? (Authority)
- Czy email prosi o aktualizacje konta lub podpisanie dokumentu przez link?

**Dane treningowe/testowe:**
- Train: 3317 tradycyjnych emaili phishingowych (1998-2022) + 2183 ham (Enron + SpamAssassin hard ham)
- Test: 333 spear-phishing LLM-generated + 999 losowych ham
- Kluczowe: spear-phishing WYLACZNIE w zbiorze testowym - symulacja concept drift

## Glowne Koncepcje

**Prompted Contextual Document Vectors**: Reprezentacja dokumentu jako wektora odpowiedzi LLM na pytania kontekstowe. Przechwytuje intencje zlosliwa, nie cechy stylometryczne. Explainable z definicji.

**Concept Drift w cybersecurity**: Zmiana rozkladu danych pomiedzy treningiem a testem. Trzy typy: covariate shift (zmiana rozkladu cech X), label shift (zmiana rozkladu klas Y), concept drift sensu stricto (zmiana P(y|x)). W phishingu: ewolucja od prostych scamow do sofistykowanych AI-generated emails.

**LLM Ensemble dla wektoryzacji**: Roznorodnosc jest wprowadzana do wektora wejsciowego zamiast do procesu uczenia klasyfikatora - odwrotnie niz w klasycznym ensemble ML.

**Attribution approach vs Binary classification**: Wiekszosc dotychczasowych prac stosuje attribution (email -> znana kampania/autor). Autorzy jako pierwsi stosuja binary classification na LLM-generated spear-phishingu.

## Wyniki

| Metoda | Recall | Precision | F1 | FPR |
|--------|--------|-----------|----|-----|
| Prompted Contextual Vectors (kNN) | 0.96 | 0.87 | **0.91** | 0.05 |
| DistilBERT Mean Tokens | 0.63 | 0.70 | 0.67 | 0.09 |
| DistilRoberta | 0.13 | 0.65 | 0.21 | 0.02 |
| MiniLM | 0.41 | 0.86 | 0.55 | 0.02 |
| ada-002 (OpenAI) | 0.38 | 0.91 | 0.53 | 0.01 |
| CountVectorizer | 0.36 | 0.64 | 0.46 | 0.07 |
| PCV - single question | 0.30 | 0.77 | 0.43 | 0.03 |

Z CatBoost/XGBoost: F1=0.99, FPR=0.01

Smishing generalizacja (train on email, test on SMS): PCV F1=0.90, DistilBERT F1=0.40

## Przydatne Cytaty

"although spear-phishing attacks represent just 0.1% of all email-based attacks, they account for 66% of the security breaches resulting from email-based attacks." (Barracuda 2023, str. 1)

"In the era of LLMs, phishing detectors should be robust to semantic shifts, since different prompting techniques and LLM variations can produce phishing attacks that deviate significantly from the stylometric features present in the training data." (str. 12)

"A real-world phishing detection system that incorporates prompted contextual vectors as part of its input should avoid using public LLM APIs due to significant privacy and security concerns." (str. 13)

## Datasety
- Enron Email Corpus - 1781 ham emaili (Klimt & Yang 2004)
- SpamAssassin Public Corpus - 402 hard ham emaili
- Phishing Email Curated Datasets - Zenodo DOI: 10.5281/zenodo.8339691 - 3317 tradycyjnych emaili
- Custom Spear-Phishing Dataset - 333 LLM-generated spear-phishing emails (publiczne repo GitHub autorow)
- UCI SMS Corpus + SmiShTank - eksperytment smishingowy

## Powiazane Tematy
- Persuasion principles w social engineering (Cialdini)
- LLM-based feature extraction (CHILL - Flan-T5 dla clinical notes)
- Chain-of-Thought prompting (Wei et al. 2022)
- Concept drift mitigation w ML
- Smishing (SMS phishing) detection
- Automated spear-phishing generation / red team tools
- Knowledge graph-based OSINT rekonesans

## Notatki

