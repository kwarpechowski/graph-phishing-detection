---
title: "Phishsense-1B: A Technical Perspective on an AI-Powered Phishing Detection Model"
date: 2025-01-01
authors: "S.E. Blake"
status: read
category: "Machine Learning"
tags: []
---
# Phishsense-1B: A Technical Perspective on an AI-Powered Phishing Detection Model

## Metadane
- **Autorzy**: S.E. Blake
- **Rok**: 2025
- **Źródło**: arXiv:2503.10944v1 [cs.CR]
- **DOI/Link**: https://arxiv.org/abs/2503.10944
- **Status**: read
- **Kategoria główna**: Machine Learning
- **Podkategorie**: Security, Natural Language Processing
- **Tagi**: #phishing-detection #llm #lora #parameter-efficient #llama-guard #fine-tuning #email-security

## Streszczenie

Phishsense-1B to fine-tuned wariant modelu meta-llama/Llama-Guard-3-1B zaadaptowany do wykrywania phishingu przez Low-Rank Adaptation (LoRA) i metodologię GuardReasoner. Model osiąga near-perfect recall z 97.5% accuracy na custom dataset i utrzymuje robust performance (70% accuracy) na challenging real-world dataset RealDaten.

Kluczowa innowacja polega na dwuetapowym podejściu: (1) fine-tuning base model (llama-3.2-1B) dla enhanced reasoning capabilities, (2) zastosowanie LoRA adapter na llamaguard-3-1B dla phishing-specific patterns. LoRA aktualizuje tylko 0.3-0.6% parametrów modelu, drastycznie redukując computational overhead przy zachowaniu wysokiej wydajności.

Eksperymenty pokazują że Phishsense-1B znacząco przewyższa zarówno unadapted models (Llama-Guard-3-1B osiąga tylko 50% accuracy, F1=0.0) jak i BERT-based detectors (62.5% accuracy). Model osiąga ROC AUC = 1.0 na custom dataset i 0.795 na RealDaten.

## Kluczowe Wnioski

- **Parameter-efficient fine-tuning działa**: LoRA aktualizując tylko 0.3-0.6% parametrów osiąga 97.5% accuracy, eliminując potrzebę full model retraining
- **Dwuetapowe podejście jest kluczowe**: oddzielenie "reasoning" (base model) od "phishing-specific" (LoRA adapter) zapewnia balans między generality a domain specificity
- **Near-perfect recall możliwy**: Phishsense-1B osiąga 100% recall na custom dataset (żaden phishing email nie został pominięty)
- **Real-world robustness**: nawet na challenging RealDaten dataset model utrzymuje 90% recall z 70% accuracy
- **Unadapted LLMs zawodzą**: Llama-Guard-3-1B bez adaptation osiąga F1=0.0, pokazując konieczność domain-specific fine-tuning
- **BERT ma trade-offs**: BERT-based detector osiąga perfect recall (100%) ale kosztem excessive false positives (precision 52.6% na RealDaten)

## Metodologia

**Architektura dwuetapowa:**

1. **Base Model Training (Stage 1)**:
   - Start: pre-trained llama-3.2-1B
   - Fine-tuning dla improved reasoning (GuardReasoner methodology)
   - Rezultat: PhishSense-1B Base Model

2. **LoRA-Based Phishing Adapter (Stage 2)**:
   - Start: llamaguard-3-1B weights (security-centric checkpoint)
   - LoRA: low-rank matrices inserted w attention i feed-forward layers
   - Base model weights frozen, tylko LoRA adapter updated
   - Rezultat: PhishSense-1B LoRA Adapter

**Dataset i preprocessing:**
- Balanced corpus: phishing + benign emails, URLs, short messages
- Stratified sampling: train/val/test splits z balanced class distribution
- Preprocessing: lowercasing, markup removal, special character normalization, subword tokenization
- Custom Dataset: balanced phishing/benign samples
- RealDaten Dataset: noisier, more diverse real-world data
- Evaluation set: 3000 positive + 3000 negative z zefang-liu/phishing-email-dataset

**Training details:**
- Loss: cross-entropy z label smoothing
- Optimizer: AdamW (lr = 1×10⁻³)
- Mixed-precision training dla speedup i memory reduction
- Parameter updates: tylko LoRA adapter (base model frozen)

**Inference pipeline:**
- Base model pozostaje unchanged
- LoRA adapter "bolted on" dla phishing-specific detection
- Input: email body lub URL text
- Output: True/False verdict (phishing vs legitimate)

## Główne Koncepcje

- **Low-Rank Adaptation (LoRA)**: Parameter-efficient fine-tuning technique aktualizująca tylko 0.3-0.6% parametrów przez low-rank decomposition. Drastycznie redukuje computational cost i memory usage vs traditional full fine-tuning.

- **GuardReasoner Methodology**: Framework do fine-tuning LLMs dla security-focused reasoning tasks. Adaptuje base models do specialized security domains.

- **Two-Tiered Approach**: Separation of concerns - base model dla general reasoning, LoRA adapter dla domain-specific phishing patterns. Minimalizuje overfitting risk przy maksymalizacji domain performance.

- **Parameter-Efficient Fine-Tuning (PEFT)**: Rodzina technik (w tym LoRA) umożliwiających adaptation large models z minimal parameter updates. Kluczowe dla deployment na resource-constrained devices.

- **Balanced Precision-Recall Trade-off**: W przeciwieństwie do BERT (perfect recall, low precision) Phishsense-1B balansuje obie metryki - kluczowe dla operational efficiency (unikanie overwhelm security teams z false positives).

## Wyniki

**Custom Dataset Performance:**

| Model | Accuracy | F1 | Precision | Recall | ROC AUC |
|-------|----------|-----|-----------|--------|---------|
| **Phishsense-1B** | **97.5%** | **97.6%** | **95.2%** | **100%** | **1.000** |
| BERT-finetuned | 62.5% | 59.5% | 64.7% | 55.0% | 0.585 |
| Llama-Guard-3-1B | 50.0% | 0.0% | 0.0% | 0.0% | 0.000 |

**RealDaten Dataset (Challenging Real-World):**

| Model | Accuracy | F1 | Precision | Recall | ROC AUC |
|-------|----------|-----|-----------|--------|---------|
| **Phishsense-1B** | **70%** | **75%** | **64.3%** | **90%** | **0.795** |
| BERT-finetuned | 55% | 69% | 52.6% | 100% | 0.640 |
| Llama-Guard-3-1B | 50% | 0.0% | 0.0% | 0.0% | 0.563 |

**Kluczowe insights:**
- **Custom Dataset**: Phishsense-1B osiąga near-perfect performance (ROC AUC = 1.0), 100% recall ensures no phishing missed
- **RealDaten**: Accuracy drops do 70% ale pozostaje competitive, balancing high recall (90%) z acceptable precision (64.3%)
- **BERT trade-off**: Perfect recall na RealDaten (100%) ale excessive false positives (precision 52.6%) - impractical dla operational environments
- **Unadapted baseline fails**: Llama-Guard-3-1B bez adaptation całkowicie zawodzi (F1=0.0), demonstrując necessity of domain-specific tuning

**Comparative ROC Analysis:**
- efang-liu/phishing-email-dataset: Phishsense-1B (AUC=0.98) vs Llama-Guard-3-1B (AUC=0.51)
- Dramatic improvement po LoRA adaptation

## Przydatne Cytaty

> "By updating only a small subset of parameters, our approach significantly reduces computational overhead while maintaining high detection performance." (str. 1)

> "Our experiments show that Phishsense-1B achieves near-perfect recall with an accuracy of 97.5% on a custom dataset and maintains robust performance (70% accuracy) on a challenging real-world dataset." (str. 1)

> "LoRA updates only a small fraction (typically 0.3% to 0.6%) of the model's parameters while keeping the majority of pre-trained weights fixed, thereby reducing computational overhead without sacrificing performance." (str. 4)

> "By separating the 'reasoning' step from the 'phishing-specific' step, we ensure that the base model remains broadly competent, while the LoRA adapter rapidly assimilates phishing-related features." (str. 5-6)

> "The exceptional performance of Phishsense-1B confirms the effectiveness of LoRA-based adaptation. By updating only a small fraction of parameters, the model achieves near-perfect recall, ensuring that no phishing email is missed—a critical requirement in cybersecurity scenarios." (str. 8)

> "In security-sensitive environments, models with extremely high recall (like the BERT-based approach) may overwhelm security teams with false positives. In contrast, Phishsense-1B offers a balanced solution suitable for deployment on resource-constrained devices." (str. 9)

## Datasety

- [Custom Phishing Dataset](../../datasets/custom-phishing-dataset.md) - Balanced corpus phishing + benign emails, URLs, messages; primary evaluation (97.5% accuracy achieved)
- [RealDaten Dataset](../../datasets/realdaten-phishing.md) - Challenging real-world dataset z noisier, more diverse data; robustness testing (70% accuracy achieved)
- [zefang-liu/phishing-email-dataset](../../datasets/zefang-liu-phishing-email.md) - 3000 positive + 3000 negative evaluation set dla ROC comparison (AUC=0.98 achieved)

*Uwaga: Datasety używane do evaluation, nie do treningu (train dataset nie opisany szczegółowo w paper)*

## Powiązane Tematy

- Parameter-efficient fine-tuning techniques (LoRA, Adapters, Prefix Tuning)
- LLM security applications (GuardReasoner, safety-critical AI)
- Phishing detection evolution: signatures → ML → DL → LLMs
- LSTM vs CNN vs Hybrid architectures dla phishing detection
- Real-time browser extension deployment dla end-user protection
- Adversarial robustness w phishing detection systems
- Multi-modal phishing detection (text + visual cues)
- Explainable AI dla security-critical decisions
- Active learning dla continuous model adaptation
- Edge deployment strategies dla resource-constrained environments
- False positive management w operational security settings
- Transfer learning cross-domain (email phishing → SMS phishing → URL phishing)

## Notatki

**Strengths:**
- Pierwszy comprehensive paper o LoRA dla phishing detection w email domain
- Strong empirical validation na 2 różnych datasets (custom + real-world)
- Practical deployment focus (Chrome extension mentioned)
- Excellent balance precision-recall vs BERT baseline
- Parameter efficiency enables deployment na resource-constrained devices

**Limitations (wymienione przez autora):**
- Dataset diversity may not capture full range evolving phishing tactics
- Standard metrics may not fully reflect operational impact
- Adversarial robustness nie testowana systematycznie
- Static data limitations - need for dynamic online adaptation
- Interpretability gap - model nie explainuje individual predictions

**Future Work (wskazany przez autora):**
- Explainable AI techniques (attention visualization, gradient attribution)
- Multilingual i multimodal extensions (visual cues)
- Browser extension deployment dla real-time protection
- Dynamic model updates przez active learning
- AI-powered EDR integration

**Implementacja:**
- Model available: Hugging Face (AcuteShrewdSecurity/Llama-Phishsense-1B)
- Code: GitHub repository (mentioned but link not provided)
- Based on: llamaguard-3-1B + llama-3.2-1B
- Framework: GuardReasoner methodology

**Related Models Compared:**
- ealvaradob/bert-finetuned-phishing (baseline)
- meta-llama/Llama-Guard-3-1B (unadapted base)
- meta-llama/Llama-3.2-1B (base pre-training)
