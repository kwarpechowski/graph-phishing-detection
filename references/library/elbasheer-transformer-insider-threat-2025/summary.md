---
title: "User-Based Sequential Modeling with Transformer Encoders for Insider Threat Detection"
date: 2025-01-01
authors: "Mohamed Elbasheer, Adewale Akinfaderin"
status: read
doi: "arxiv:2506.23446"
category: "Security"
tags:
  - insider-threat
  - transformer
  - sequential-modeling
  - anomaly-detection
  - ueba
  - self-supervised
  - project/behavioral-security-ueba
---

# User-Based Sequential Modeling with Transformer Encoders for Insider Threat Detection

## Metadane
- **Autorzy**: Mohamed Elbasheer, Adewale Akinfaderin
- **Rok**: 2025
- **Źródło**: arXiv:2506.23446
- **DOI**: arxiv:2506.23446
- **Status**: `#read`
- **Kategoria**: Security / Deep Learning
- **Tagi**: `#insider-threat` `#transformer` `#sequential-modeling` `#anomaly-detection` `#ueba`

## Streszczenie

Paper proponuje metodę sekwencyjnego modelowania zachowań użytkowników z użyciem Transformer Encoders dla detekcji insider threats. Podejście oparte na unsupervised/self-supervised anomaly scoring — model uczy się reprezentacji normalnego zachowania, anomalie wykrywane przez odchylenie od nauczonej reprezentacji.

Transformer Encoders pozwalają na modelowanie długoterminowych zależności w sekwencjach akcji użytkownika, co jest kluczowe dla detekcji subtelnych zmian wzorców charakterystycznych dla insider threats (np. stopniowa eskalacja dostępu, zmiana tematyki pobieranych dokumentów).

## Kluczowe Wnioski
- Transformer Encoders skutecznie modelują temporalne sekwencje akcji użytkownika
- Wyniki na CERT: 96.61% accuracy, 99.43% recall, 96.38% F1, 95.00% AUROC
- Unsupervised anomaly scoring eliminuje potrzebę labeled anomalies
- Sequential modeling przewyższa statyczne metody (Isolation Forest, One-Class SVM) dla danych temporalnych

## Metodologia
- Architektura: Transformer Encoder (self-attention) na sekwencjach zdarzeń per użytkownik
- Training: self-supervised — reconstruction loss na normalnych danych
- Anomaly score: reconstruction error per sekwencja
- Dataset: CERT Insider Threat Dataset v6.2
- Evaluation: accuracy, recall, F1, AUROC

## Główne Koncepcje
- **Sequential behavioral modeling**: traktowanie akcji użytkownika jako sekwencja temporalna (nie bag-of-features)
- **Self-attention**: mechanizm uwagi pozwalający modelować zależności między odległymi zdarzeniami
- **Reconstruction-based anomaly scoring**: anomalia = wysoki błąd rekonstrukcji sekwencji

## Wyniki
- Accuracy: 96.61%
- Recall: 99.43%
- F1: 96.38%
- AUROC: 95.00%

## Przydatne Cytaty
- "Sequential modeling via Transformer Encoders captures long-range temporal dependencies in user activity"

## Datasety
- [CERT Insider Threat Dataset](../../datasets/cert-insider-threat.md)

## Powiązane Tematy
- BPP modele dla workplace telemetry (#BSU-1)
- Porównanie: Isolation Forest vs. Transformer vs. LSTM Autoencoder
- Sequential patterns w Git/Jira/Calendar telemetry

## Notatki
Uwaga: CERT dataset jako primary benchmark — paper z 2025, ale tier-2 venue. Wyniki imponujące, ale zewnętrzna walidacja konieczna.
