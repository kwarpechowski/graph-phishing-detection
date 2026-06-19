---
title: "PhishDebate: An LLM-Based Multi-Agent Framework for Phishing Website Detection"
date: 2025-01-01
authors: "Wenhao Li, Selvakumar Manickam, Yung-wey Chong, Shankar Karuppayah"
status: read
category: "Machine Learning"
tags: []
---
# PhishDebate: An LLM-Based Multi-Agent Framework for Phishing Website Detection

## Metadane
- **Autorzy**: Wenhao Li, Selvakumar Manickam, Yung-wey Chong, Shankar Karuppayah
- **Rok**: 2025
- **Źródło**: arXiv:2506.15656v2 [cs.CR]
- **DOI/Link**: https://arxiv.org/abs/2506.15656v2
- **Status**: read
- **Kategoria główna**: Machine Learning
- **Podkategorie**: Security, Natural Language Processing
- **Tagi**: #phishing-detection #llm #multi-agent #debate-framework #cybersecurity #analyst-augmentation #gpt-4o #gemini

## Streszczenie

PhishDebate to nowatorski framework oparty na wieloagentowym systemie LLM do wykrywania stron phishingowych. System wykorzystuje czterech wyspecjalizowanych agentów analizujących różne aspekty strony internetowej: strukturę URL, kompozycję HTML, zawartość semantyczną i podszywanie się pod marki. Agenci prowadzą strukturalną debatę pod nadzorem Moderatora, a ostateczną decyzję podejmuje agent Judge.

Framework osiąga 98.2% recall na rzeczywistych danych phishingowych i przewyższa podejścia single-agent oraz Chain-of-Thought (CoT). Kluczową innowacją jest redukcja niepewnych predykcji i zapewnienie transparentnego uzasadnienia decyzji, co czyni system narzędziem wspomagającym analityków bezpieczeństwa. Modularny design umożliwia konfigurację na poziomie agentów, dostosowując się do różnych wymagań zasobowych i aplikacyjnych.

## Kluczowe Wnioski

- Multi-agent debate framework znacząco poprawia wykrywanie phishingu poprzez collaborative reasoning i różnorodność perspektyw analitycznych
- GPT-4o osiąga najlepszą równowagę z 96.50% accuracy, 94.97% precision i 96.56% F1 score
- PhishDebate eliminuje problem "uncertain" predictions obecny w CoT (50 przypadków u CoT vs 0 w PhishDebate)
- Wykluczenie HTML Structure Agent prowadzi do najwyższego F1 score (94.71%), co sugeruje optymalizacje task-specific
- System działa jako analyst-augmentation tool, redukując cognitive load i wspierając early, left-of-exploit detection
- Koszt operacyjny pozostaje umiarkowany: ~$3.36 za 1000 próbek

## Metodologia

**Architektura systemu:**
- 4 wyspecjalizowane agenty: URL Analyst, HTML Structure, Content Semantic, Brand Impersonation
- 2 agenty koordynujące: Moderator (ocena konsensusu) i Judge (finalna decyzja)
- Proces 4-fazowy: Initial Analysis → Consensus Evaluation → Multi-round Debate → Final Judgment

**Pipeline:**
1. **Round 1**: Każdy agent niezależnie analizuje stronę bez kontaktu z innymi
2. **Consensus Evaluation**: Moderator ocenia czy osiągnięto konsensus
3. **Rounds 2+**: Agenci widzą argumenty innych i refinują swoje oceny przez debatę
4. **Final Judgment**: Judge podejmuje ostateczną decyzję na podstawie całej debaty

**Datasety:**
- Mendeley Phishing Websites Dataset: 500 phishing + 500 legitimate
- TR-OP Dataset: 500 phishing + 500 legitimate (balanced, manually labeled)

**Modele testowane:**
- GPT-4o, GPT-4o-mini, Gemini-2.0-Flash, Qwen2.5-vl-72b-instruct

**Baseline comparison:**
- Single-Agent with Direct Prompt
- Single-Agent with Chain-of-Thought (CoT)

## Główne Koncepcje

- **Multi-Agent Debate System**: System gdzie multiple agents z różnymi specjalizacjami debatują aby osiągnąć lepsze decyzje niż single-agent approaches
- **Analyst-Augmentation System**: Narzędzie wspierające analityków poprzez redukcję uncertain predictions i dostarczanie transparent reasoning
- **Left-of-Exploit Detection**: Proaktywne wykrywanie zagrożeń na wczesnym etapie, zanim dojdzie do eksploitacji
- **Modular Design**: Elastyczna architektura pozwalająca na włączanie/wyłączanie agentów w zależności od wymagań
- **Consensus Evaluation**: Mechanizm oceny czy agenci osiągnęli wspólne stanowisko, umożliwiający early termination
- **Brand Impersonation Detection**: Specjalistyczna analiza prób podszywania się pod znane marki i organizacje

## Wyniki

**Performance Evaluation (GPT-4o):**
- Accuracy: 96.50%
- Precision: 94.97%
- Recall: 98.2%
- F1 Score: 96.56%
- True Negative Rate: 94.8%
- False Positive Rate: 5.2%
- Czas inferencji: 22.2s

**Comparative Results (GPT-4o-mini):**
| Metoda | Precision | Accuracy | Recall | F1 | Czas |
|--------|-----------|----------|--------|-----|------|
| Single Agent | 60.57% | 67.00% | 97.40% | 74.69% | 4.7s |
| CoT | 88.61% | 90.70% | 93.40% | 90.94% | 10.5s |
| **PhishDebate** | **90.57%** | **93.90%** | **98.00%** | **94.14%** | 37.5s |

**Scenario Analysis (Agent Exclusion):**
- All Agents: Recall 98.5%, F1 94.44%
- W/O HTML Agent: **Najwyższe** F1 94.71%, Accuracy 94.55% (najlepiej dla precision-critical scenarios)
- W/O URL Agent: Najgorszy Recall 95.2% (pokazuje kluczową rolę URL analysis)
- W/O Brand Agent: F1 93.63% (umiarkowany spadek)

**Case Study Insights:**
- System wykrył phishing page ukrytą jako error page przez suspicious path "/wp-includes/wells/wells/"
- Round 1: Split 2-2 (URL i Brand agents: phishing, HTML i Content: legitimate)
- Round 2: Po debacie wszystkie agenty converged na "Likely Phishing" z confidence 0.88
- Demonstracja strengths: wykrywanie cloaked/dormant phishing infrastructure i transparent justifications

## Przydatne Cytaty

> "PhishDebate comprises four specialized agents, each targeting a distinct dimension of phishing evidence, including URL structure, HTML composition, semantic content, and brand impersonation." (str. 1)

> "By reducing uncertain predictions and providing transparent reasoning, PhishDebate functions as an analyst-augmentation system that lowers cognitive load and supports early, left-of-exploit detection of phishing threats." (str. 1)

> "Notably, while CoT prompting provides reasonably strong results (e.g., 90.94% F1 score), it suffers from lower recall and precision compared to PhishDebate, especially when factoring in the 50 cases it labeled as 'uncertain' instead of providing definitive classifications." (str. 6)

> "The PhishDebate framework significantly improves the confidence and decisiveness of LLM-based predictions by leveraging multi-agent debate, thereby reducing indecisive outputs and promoting consistent judgment." (str. 7)

> "This multi-view debate can uncover dormant or cloaked phishing infrastructure that content-only scanners miss, and the step-wise trace provides transparent justifications that facilitate analyst review." (str. 8)

## Datasety

- [Mendeley Phishing Websites Dataset](../../datasets/mendeley-phishing-websites.md) - Performance benchmarking (sampel 500 phishing + 500 legitimate)
- [TR-OP Dataset](../../datasets/tr-op-phishing.md) - Scenario analysis dla robustness testing (sampel 500 phishing + 500 legitimate)

## Powiązane Tematy

- Multi-agent LLM systems w cybersecurity
- Phishing email detection using debate frameworks (MultiPhishGuard, PhishEmail Debate)
- Explainable AI (XAI) w security applications
- Brand impersonation detection techniques
- Real-time phishing detection systems
- LLM hallucination mitigation through multi-agent collaboration
- Spam detection using collaborative AI agents
- Adversarial phishing tactics (obfuscation, cloaking)
- Human-in-the-loop security systems
- Cost-effective deployment of LLM-based security tools

## Notatki

**Mocne strony:**
- Pierwszy comprehensive debate-based framework dla phishing websites (nie tylko emails)
- Modularny design pozwalający na task-specific optimization
- Znacząca redukcja "uncertain" classifications vs CoT
- Transparentne uzasadnienia decyzji (analyst-friendly)
- Competitive cost (~$3.36/1000 samples)

**Ograniczenia (wymienione przez autorów):**
- Performance zależy od biases i knowledge gaps underlying LLMs
- Input length restrictions w commercial APIs prowadzą do truncation
- Wyższy latency (37.5s) vs single-agent (4.7s) i CoT (10.5s)
- Gemini-2.0 miał problem z 8 przypadkami uncertain output (non-compliance z binary classification)

**Przyszłe kierunki:**
- Testowanie resilience przeciw adversarial phishing tactics
- Deployment z locally deployed LLMs dla reduction cost/latency
- Scaling do high-velocity, large-scale security environments
