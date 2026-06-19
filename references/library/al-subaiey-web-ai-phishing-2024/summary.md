---
title: "Novel Interpretable and Robust Web-based AI Platform for Phishing Email Detection"
date: 2024-01-01
authors: "Abdulla Al-Subaiey, Mohammed Al-Thani, Naser Abdullah Alam, Kaniz Fatema Antora, Amith Khandakar, SM Ashfaq Uz Zaman"
status: read
tags: []
---
# Novel Interpretable and Robust Web-based AI Platform for Phishing Email Detection

## Metadane
- **Autorzy**: Abdulla Al-Subaiey, Mohammed Al-Thani, Naser Abdullah Alam, Kaniz Fatema Antora, Amith Khandakar, SM Ashfaq Uz Zaman
- **Rok**: 2024
- **Źródło**: Computers and Electrical Engineering, Volume 119
- **DOI/Link**: 10.1016/j.compeleceng.2024.109625
- **Status**: read
- **Tagi**: #phishing-detection #email-classification #web-application #explainable-ai #svm #tf-idf #machine-learning #real-world-deployment #lime

## Streszczenie

Publikacja przedstawia wysokowydajny model uczenia maszynowego do klasyfikacji phishingowych emaili, osiągający F1-score 0.99 na największym dostępnym publicznie zbiorze danych (~82,500 emaili). Kluczową innowacją jest deployment modelu w działającej aplikacji webowej (https://phishingdetection.onrender.com/) z integracją Explainable AI (LIME) dla zwiększenia zaufania użytkowników. Badanie adresuje fundamentalne ograniczenia istniejących prac: (1) poleganie na prywatnych/małych datasetach, (2) brak real-world deployment, (3) brak interpretowalności predykcji.

Model SVM z TF-IDF preprocessing osiągnął 99.1% accuracy, 99% precision, 99% recall i 99% F1-score na merged dataset (6 źródeł: Enron, Ling, CEAS, SpamAssassin, Nazario, Nigerian Fraud). Aplikacja webowa umożliwia real-time klasyfikację emaili przez paste tekstu (sender, subject, body) i natychmiastową predykcję spam/safe z wizualizacją LIME pokazującą features contributing to classification.

## Kluczowe Wnioski

- **Best Performance**: SVM + TF-IDF osiąga 99.1% accuracy vs 83.8% dla Word2Vec, demonstrując przewagę statistical weighting nad semantic embeddings dla email classification
- **Feature Engineering Crucial**: Merging textual features (sender, date, subject, body) zwiększa F1 score z 0.71 → 0.82, capturing contextual relationships
- **Real-World Deployment Success**: Działająca aplikacja Flask deployment proves practical applicability (gap in previous research - większość kończy na benchmarking)
- **XAI for Trust**: LIME visualization identyfikuje spam indicators (words: "scan" +0.11, "miss" +0.10, "Fill" +0.10, "phone" +0.08) vs legitimate indicators ("edu" -0.03)
- **Largest Public Dataset**: 82,486 emails (42,891 spam, 39,595 ham) - comprehensive vs small datasets w literaturze (typowo <10k samples)
- **Feature Ablation Insights**: Receiver email i URL binary features mają minimal predictive power; text combination jest key driver
- **Comparable to SOTA**: Outperforms most prior work (Table 3): vs BERT 98.67%, GCN 98.2%, RNN 98.91%

## Metodologia

### Data Pipeline
1. **Dataset Merging**: 6 public datasets → unified corpus
   - mdf_1: Enron + Ling (subject, body, label)
   - mdf_2: CEAS, Nazario, Nigerian Fraud, SpamAssassin (sender, receiver, subject, body, date, label)

2. **Preprocessing**:
   - Tokenization + punctuation removal + stop word removal
   - Text combination: mdf_1 (subject+body → text_combined), mdf_2 (sender+date+subject+body → text_combined)
   - Final dataset: 42,891 spam, 39,595 ham ≈ 82,500 total

3. **Vectorization**: TF-IDF vs Word2Vec comparison
   - **TF-IDF**: TF-IDF(w,d) = TF(w,d) × IDF(w,D) gdzie IDF = log(|D|/df(w))
   - Highlights unique keywords w phishing (reduces common words weight)
   - **Word2Vec**: Neural embeddings (semantic similarity) - underperformed

4. **Train/Test Split**: 80/20 → 65,988 training, 16,498 testing samples

### Models Evaluated
- **Support Vector Classifier (SVC)**: Linear kernel, maximizes margin, random_state=42
- **Multinomial Naive Bayes (MNB)**: Probabilistic, suited for discrete features (word counts)
- **Random Forest**: 100 decision trees, ensemble voting, prevents overfitting

### Evaluation Metrics
- Accuracy: (TP + TN) / Total
- Precision: TP / (TP + FP) - avoiding false positives
- Recall: TP / (TP + FN) - capturing all phishing
- F1-Score: 2 × (Precision × Recall) / (Precision + Recall) - balanced metric

### Explainability: LIME
- Local Interpretable Model-Agnostic Explanations
- Approximates complex model locally z simpler interpretable model
- Highlights features (words/phrases) contributing most to classification
- Critical for deployment: users need to understand WHY email classified as phishing

### Deployment
- Flask web application: https://phishingdetection.onrender.com/
- User workflow: paste email text → model processes (vectorization) → prediction (spam/safe) + LIME visualization
- Real-time classification for practical use

## Główne Koncepcje

- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Statistical weighting scheme valuing words by uniqueness across corpus; reduces weight of common words, emphasizes distinctive terms (e.g., phishing-specific keywords)

- **Word2Vec**: Neural network-based word embeddings representing words as vectors where semantically similar words have closer representations; underperformed vs TF-IDF w email classification

- **Feature Ablation**: Systematyczne usuwanie features aby identify most informative; receiver email i URL binary minimal impact; text merging critical improvement

- **LIME (Local Interpretable Model-Agnostic Explanations)**: XAI technique approximating black-box model locally z interpretable model; visualizes feature importance per prediction

- **Support Vector Machine (SVM)**: Finds hyperplane maximizing margin between classes; linear kernel efficient w high dimensions; considers word relationships (vs Naive Bayes independence assumption)

- **Real-World Deployment Gap**: Większość research kończy na benchmarking; brak practical applications; ta publikacja bridges gap z Flask web app

- **Dataset Limitations in Prior Work**: Reliance on proprietary (inaccessible) lub small public datasets (<10k samples); hinders generalizability

## Wyniki

### Model Performance Comparison (Table 2 - Best Results)

| Model | Preprocessing | Dataset Size | Accuracy | Precision | Recall | F1-score |
|-------|--------------|--------------|----------|-----------|--------|----------|
| **SVM (proposed)** | **TF-IDF** | **42891[1], 39595[0]** | **0.991** | **0.99** | **0.99** | **0.99** |
| SVM | TF-IDF | 28457[1], 21403[0] | 0.994 | 0.99 | 0.99 | 0.99 |
| MNB | TF-IDF | 28457[1], 21403[0] | 0.985 | 0.98 | 0.99 | 0.99 |
| RF | TF-IDF | 42891[1], 39595[0] | 0.984 | 0.98 | 0.99 | 0.98 |
| RF | Word2Vec | 42891[1], 39595[0] | 0.838 | 0.83 | 0.84 | 0.83 |
| SVM | Word2Vec | 42891[1], 39595[0] | 0.821 | 0.82 | 0.81 | 0.82 |

**Key Finding**: TF-IDF consistently outperforms Word2Vec (F1: 0.99 vs 0.83 max)

### Literature Comparison (Table 3 - Selected)

| Author | Dataset Size | Method | Result |
|--------|-------------|--------|--------|
| **Proposed** | **82,486 (42891 spam, 39595 ham)** | **SVC + TF-IDF + LIME** | **Acc: 99.10%, F1: 99.00%** |
| [24] | 5,000 (3000 spa, 2000 ham) | Fine-tuned BERT | Acc: 98.67%, F1: 98.66% |
| [21] | 8,579 (3685 spam, 4894 ham) | GCN + NLP | Acc: 98.2%, FPR: 0.015 |
| [26] | 26,962 | RNN | Acc: 98.91%, F1: 98.63% |
| [27] | 36,715 | GA-SGD | Acc: 99.21%, Recall: 99.54% |
| [30] | 6,051 | Random Forest | Acc: 99.30% |
| [33] | Unspecified | RCNN + Word2Vec | Acc: 99.00% |

**Observations**:
- Proposed model competitive z SOTA przy znacznie większym datasecie
- Previous works: mostly proprietary datasets, NO real-world deployment
- Only this work provides: public dataset + deployed web application + XAI

### LIME Visualization Example
Demo phishing email: "Personal Assistant Opportunity - Dr. Sheldon Cooper"
- **Prediction**: Spam (0.92 probability) vs Not Spam (0.08)
- **Spam indicators** (red, positive weights):
  - "scan" (+0.11) - request for passport scan
  - "miss" (+0.10) - urgency ("Don't miss out!")
  - "Fill" (+0.10) - form filling request
  - "phone" (+0.08) - personal info request
  - "Dear" (+0.08) - generic greeting
- **Legitimate indicators** (blue, negative weights):
  - "edu" (-0.03) - educational domain slightly reduces spam score

### Web Application
- **URL**: https://phishingdetection.onrender.com/
- **Input**: User pastes email text (sender, subject, body)
- **Output**: Prediction (Spam/Safe) + LIME visualization highlighting contributing words
- **Processing**: Text → vectorization (TF-IDF) → SVM model → prediction + explanation
- **Real-world validation**: Successfully classifies unseen real-life emails

## Przydatne Cytaty

> "Literature review exposes limitations in phishing email detection. Most research relies on inaccessible private datasets or small public ones, hindering model generalizability and real-world deployment. Additionally, a gap exists between high-performing models and their practical application." (str. 5)

> "This study addresses these shortcomings by proposing a robust model trained on a comprehensive public dataset and designed for practical use." (str. 5)

> "The best-performing model, SVM with TF-IDF preprocessing on the merged dataset, achieved 99.1% accuracy, 99% precision, 99% recall, and f1-score 99." (str. 12)

> "A more impactful observation was the significant improvement in model performance achieved by merging all textual features (sender email, date, subject, and body) into a single column. This merged feature yielded a notable increase in F1 score, from 0.71 to 0.82." (str. 16)

> "TF-IDF achieved superior results, with an F1 score of 0.99 compared to the maximum F1 score of 0.83 obtained using word2vec." (str. 15)

> "While achieving high performance is crucial, understanding the rationale behind a model's predictions is equally valuable." (str. 10)

> "90% of successful cyber-attacks originate from phishing attempts, therefore making developing robust detection and prevention strategies imperative." (str. 2)

> "According to the FBI, BEC attacks alone have cost victims worldwide over $50 billion." (str. 2)

## Datasety

- [Enron Email Corpus](../../datasets/enron-corpus.md) - Part of merged dataset; one of 6 public sources combined for training (~500k emails in full corpus, subset used)
- [SpamAssassin Public Email Corpus](../../datasets/spamassassin-corpus.md) - Part of merged dataset; contributed to 82,486 total emails (6,051 emails in standard distribution: 1,897 spam, 4,150 ham)
- **Merged Email Corpus** (custom dataset, 82,486 emails total) - 6 public sources combined:
  - Enron Corpus (spam + ham emails)
  - Ling Dataset (spam + ham)
  - CEAS Dataset
  - Nazario Dataset
  - Nigerian Fraud Dataset
  - SpamAssassin Public Email Corpus
  - Final composition: 42,891 spam, 39,595 legitimate (ham)
  - 80/20 split: 65,988 training, 16,498 testing
  - Availability: "can be made available upon reasonable request to corresponding author"

## Powiązane Tematy

- **Deployment Gap w ML Research**: Transition from benchmarking to production systems
- **Explainable AI (XAI) for Security**: LIME, SHAP dla trust w cybersecurity applications
- **Feature Engineering Strategies**: Text combination vs isolated features, TF-IDF vs embeddings trade-offs
- **Phishing Evolution**: AI-generated phishing (Kaspersky warning), increasing sophistication
- **Public Dataset Availability**: Importance for reproducibility i generalization testing
- **Browser Extension Deployment**: Future work - Chrome/Firefox plugins dla real-time protection
- **Model Interpretability vs Performance**: Balancing accuracy with explainability dla user trust
- **Email Security Ecosystem**: Integration z mail servers, antivirus, user training
- **Cross-Domain Transfer**: Phishing detection → spam detection → fraud detection generalization
- **Real-Time Classification Challenges**: Latency, scalability, false positive tolerance
- **Adversarial Robustness**: Evolving phishing tactics, concept drift, lifelong learning needs
- **Multi-Modal Phishing Detection**: Combining text (email body) + visual (logos, layouts) + metadata

## Notatki

