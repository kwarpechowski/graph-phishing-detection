---
title: "Analysis and Prevention of AI-Based Phishing Email Attacks"
date: 2024-01-01
authors: "Chibuike Samuel Eze, Lior Shamir"
status: read
doi: "arxiv:2405.05435"
category: "Security"
tags:
  - phishing-detection
  - ai-generated-phishing
  - email-security
  - generative-ai
  - text-classification
  - stylometry
  - dataset
  - project/spear-phishing-context
---

# Analysis and Prevention of AI-Based Phishing Email Attacks

## Metadane
- **Autorzy**: Chibuike Samuel Eze, Lior Shamir
- **Rok**: 2024
- **Zrodlo**: arXiv:2405.05435 (Kansas State University)
- **DOI**: arxiv:2405.05435
- **Status**: `#read`
- **Kategoria**: Security
- **Tagi**: `#phishing-detection` `#ai-generated-phishing` `#email-security` `#generative-ai` `#text-classification` `#stylometry` `#dataset`

## Streszczenie

Praca bada problem detekcji emaili phishingowych generowanych przez generatywna AI, ktore sa szczegolnie trudne do wykrycia przez tradycyjne systemy antyspamowe - poniewaz kazdy email jest unikalny, systemy identyfikujace powielone wiadomosci nie sa skuteczne. Autorzy tworza i publikuja korpus 865 emaili phishingowych wygenerowanych przez DeepAI (OpenAI-enabled), bedacy pierwszym publicznie dostepnym datasetem AI-generated phishing emails. Dataset dostepny pod adresem: https://people.cs.ksu.edu/~lshamir/data/ai_phishing/

Praca testuje kilka roznych podejsc do klasyfikacji tekstowej: MALLET (topic modeling, Naive Bayes/MaxEntropy/Winnow), UDAT (Universal Data Analysis of Text - analiza stylistyczna: POS, sentyment, dywersytet leksykalny), LSTM (deep neural network) oraz ensemble (MALLET + UDAT + DNN, majority voting). Wszystkie metody osiagaja >97% accuracy (p<10^-5), co jest zachecajace. Kluczowe odkrycie: emaile AI sa statystycznie rozroznialne od emaili ludzkich przez cechy stylistyczne, nie tylko tresc - nawet bez wiedzy o tematyce ataku.

## Kluczowe Wnioski
- Emaile phishingowe generowane przez AI sa wykrywalne z wysokim accuracy (>97-99.5%) przez rozne metody ML, nawet bez specjalizowanych algorytmow
- AI-generated emaile roznia sie stylistycznie od emaili ludzkich: wiecej czasownikow i zaimkow, dluzsze slowa (5.7 vs 4.8 znakow srednio), bardziej pozytywny sentyment, wyzsza dywersytet leksykalna, krotsze zdania (8.8 vs 16 slow)
- Klasyfikator musi byc trenowany na AI-generated emailach - nie wystarczy trening na ludzkich phishach, bo emaile AI sa stylowo odmienne
- DeepAI (nie ChatGPT/Copilot) zostalo uzyte bo inne chatboty odmowily generowania phishingu
- Ensemble (MALLET+UDAT+DNN) osiaga 99.5% - minimalna poprawa nad samym MALLET
- 48% AI-phishing emails: prosba o weryfikacje konta; 36%: alerty o podejrzanej aktywnosci
- Pierwszy publicznie dostepny dataset AI-generated phishing emails (865 emaili)

## Metodologia

**Dataset tworzenia**:
- DeepAI API (OpenAI-enabled) do generowania 865 emaili phishingowych
- ChatGPT, Copilot, Character.ai odmowily generowania - DeepAI nie
- Emaile plain text, srednia dlugosc 545 znakow (280-1810)

**Datasety porownawcze (klasy negatywne)**:
- Enron email corpus (~500k emaili normalnych)
- Nigerian scam emails (recznie pisane phishing)
- Ling-Spam dataset (2,412 normalnych + 481 spam emaili)

**Metody klasyfikacji**:
- MALLET (topic modeling): tokenizacja, stop word removal, lemmatyzacja, POS → bag-of-words → Naive Bayes/MaxEntropy/Winnow
- UDAT (stylometric): 297 numerycznych deskryptorow stylu (POS distribution, sentiment, punctuation, word diversity, sentence length, readability) → Fisher discriminant → kNN
- LSTM: embedding 20k words × 100 dims, LSTM 100 units, dropout 0.2, tanh/sigmoid, 10 epochs
- Ensemble: MALLET (NB) + UDAT + LSTM, majority voting
- Ewaluacja: 600 train / 100 test per klasa, 10-fold cross-validation
- Metryki: accuracy, precision, recall, F1

## Glowne Koncepcje

**AI-Generated Phishing Evasion**: Tradycyjne systemy antyspamowe identyfikuja identyczne lub bardzo podobne emaile wysylane masowo. Generatywna AI pozwala na tworzenie unikalnych emaili dla kazdego odbiorcy, omijajac ta obrone.

**UDAT (Universal Data Analysis of Text)**: Narzedzie do analizy stylistycznej tekstu uzywajace 297 numerycznych deskryptorow. Nie analizuje tematow ani slow kluczowych - analizuje styl pisania: distribucje POS, sentymenty, dywersytet leksykalna, dlugosci zdan. Interpretowalne - wskazuje konkretne cechy rozrozniajace klasy.

**Stylometric Fingerprinting AI**: AI pisze inaczej niz ludzie stylistycznie: dluzsze slowa, wiecej zaimkow i czasownikow, mniej liczb kardynalnych, mniej czasow przeszlych, wyzszy Coleman-Liau index (13.9 vs 10.2-11.4), krotsze zdania.

**Ensemble Defense**: Uzycie wielu roznych podejsc do klasyfikacji (topic + style + DNN) zapewnia odpornosc: jesli atakujacy zoptymalizuje atak pod jeden klasyfikator, inne nadal wykryja atak.

## Wyniki

Wyniki 4-klasowej klasyfikacji (AI-generated vs Enron vs Ling-Spam vs Nigerian phishing):
- MALLET Naive Bayes: **99.3%** (recall AI: 0.99, precision: 0.98, F1: 0.985)
- MALLET Max Entropy: 99.2%
- MALLET Winnow: 97.0%
- UDAT: **98.0%** (recall AI: 1.0, precision: 0.97, F1: 0.985) - AI-generated: 100% accuracy!
- DNN (LSTM): ~99% w klasyfikacjach 2-klasowych (AI vs kazda klasa z osobna)
- Ensemble: **99.5%**

Kluczowe cechy stylistyczne (LDA scores, ANOVA p<10^-5):
- Pronoun frequency: AI 0.101 vs Enron 0.06
- Verb frequency: AI 0.107 vs Enron 0.052
- Word length mean: AI 5.67 vs Nigerian 4.76
- Sentiment mean: AI 1.68 vs Nigerian 1.26 (bardziej pozytywny)
- Coleman-Liau index: AI 13.89 vs Enron 10.20 (trudniejszy do czytania)
- Cardinal number frequency: AI 0.0037 vs Enron 0.037 (10x mniej liczb)
- Sentence length mean: AI 8.8 vs Enron 16.0 slow (krotsze zdania)
- Lemma diversity: AI 0.719 vs Nigerian 0.526 (bogatsze slownictwo)

## Przydatne Cytaty

"instead of a single email format sent to a large number of recipients, generative AI can be used to send each potential victim a different email, making it more difficult for cybersecurity systems to identify the scam email" (Abstract)

"AI-generated phishing emails are different from regular phishing emails, and therefore it is important to train machine learning systems also with AI-generated emails in order to repel future phishing attacks that are powered by generative AI." (Abstract)

"An effective solution would therefore be based on several algorithms that work in concert rather than a single approach." (Section 5)

"The email corpus described in this paper is the first corpus of AI-generated phishing emails." (Section 5)

## Datasety
- [AI-Generated Phishing Email Corpus](https://people.cs.ksu.edu/~lshamir/data/ai_phishing/) - 865 emaili generowanych przez DeepAI (OpenAI); plain text; dostepny publicznie; Kansas State University 2024

## Powiazane Tematy
- AI-generated text detection (watermarking, stylometric identification)
- Generative AI misuse: deep fakes, plagiarism, phishing
- Email spam detection: SVM, RCNN, deep learning approaches
- Enron email corpus jako benchmark
- Stylometric analysis (UDAT) vs topic modeling (MALLET)
- Adversarial evasion: jak atakujacy moga ominac stylometric classifiers?

## Notatki

