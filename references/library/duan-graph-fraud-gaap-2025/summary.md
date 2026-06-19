---
title: "Global Attribute-Association Pattern Aggregation for Graph Fraud Detection"
date: 2025-01-01
authors: "Mingjiang Duan, Da He, Tongya Zheng, Lingxiang Jia, Mingli Song, Xinyu Wang, Zunlei Feng"
status: read
category: "Machine Learning"
tags: []
---
# Global Attribute-Association Pattern Aggregation for Graph Fraud Detection

## Metadane
- **Autorzy**: Mingjiang Duan, Da He, Tongya Zheng, Lingxiang Jia, Mingli Song, Xinyu Wang, Zunlei Feng
- **Rok**: 2025
- **Źródło**: The Thirty-Ninth AAAI Conference on Artificial Intelligence (AAAI-25)
- **DOI/Link**: https://github.com/AtwoodDuan/GAAP
- **Status**: read
- **Kategoria główna**: Machine Learning
- **Podkategorie**: Fraud Detection, Graph Neural Networks, Cybersecurity
- **Tagi**: #fraud-detection #graph-neural-networks #gnn #attribute-pattern #association-pattern #dynamic-binning #e-commerce #financial-fraud #social-networks #cross-attention #gaap #aaai2025

## Streszczenie

Publikacja prezentuje nowatorskie podejście do wykrywania oszustw w danych grafowych oparte na globalnej agregacji wzorców atrybut-asocjacja (GAAP - Global Attribute-Association Pattern Aggregation). Autorzy identyfikują kluczowe ograniczenia istniejących metod: tradycyjne modele Random Forest tracą krytyczne informacje o grafowej strukturze danych, podczas gdy Graph Neural Networks (GNNs) błędnie łączą cechy atrybutów (np. uśrednianie wieku 60 i 6 lat daje nonsensowny wynik 33 lata).

Framework GAAP składa się z trzech komponentów: (1) Dynamic Binning Embedding (DyBEM) - adaptacyjne dzielenie wartości atrybutów na przedziały (bins) z pełną różniczkowalnością, eliminując nieprawidłowe fuzje cech, (2) Message-Passing GNN - agregacja wzorców asocjacji między węzłami poprzez przekazywanie komunikatów w grafie (wykorzystując GraphSAGE), oraz (3) Pattern Global Aggregation - globalna agregacja wzorców atrybut-asocjacja z wykorzystaniem cross-attention o zredukowanej złożoności O(N·M) zamiast O(N²).

Ekstensywne eksperymenty na 7 datasetach wykrywania oszustw (YelpChi, Amazon, T-Finance, T-Social, Elliptic, Tolokers, DGraph-Fin) wykazały, że GAAP osiąga state-of-the-art performance, przewyższając 24 metody bazowe ze średnim wynikiem Rec@K=70.88% (najlepszy wynik na 5/7 datasetach, drugi najlepszy na Amazon).

## Kluczowe Wnioski

- **Problem incorrect attribute fusion w GNNs**: Tradycyjne GNNs błędnie łączą cechy poprzez uśrednianie (np. averaging ages 60+6=33), co prowadzi do nonsensownych wartości i utraty interpretability. Dynamic Binning Embedding rozwiązuje ten problem poprzez reprezentację cech jako fragment-wise vectors zamiast skalarów.

- **Przewaga attribute-association patterns**: Fraudulent behaviors można odróżnić po kategoriach - np. fraudsters często targetują "high-income elderly" (instytucje finansowe) lub "low-income young users" padają ofiarą fake rebate schemes (e-commerce). Łączenie attribute patterns (binning) z association patterns (GNN) daje lepsze wyniki niż podejścia wykorzystujące tylko jeden typ patterns.

- **State-of-the-art performance**: GAAP osiągnął najlepsze wyniki na 5/7 datasetów z average Rec@K=70.88%, przewyższając najlepszą baseline (DGA-GNN) o 1.48pp. Największa poprawa na YelpChi: +4.3pp (88.54% vs 84.23%), T-Social: +1.28pp (97.25% vs 95.97%).

- **Efektywność modułu DyBEM**: Ablation study wykazało, że usunięcie Dynamic Binning Embedding najbardziej wpłynęło na YelpChi (spadek z 87.51% do 47.62% Rec@K), ponieważ dataset ten ma najwięcej atrybutów (32 features) z high information density. Zastąpienie dynamic binning statycznym one-hot encoding również pogorszyło wyniki (75.33% vs 87.51% na YelpChi).

- **Znaczenie global aggregation**: Cross-attention based global aggregation redukuje computational complexity z O(N²) do O(N·M) poprzez computing attention między current batch nodes (M) a historical embeddings from previous epoch (N). Usunięcie tego modułu spowodowało spadek performance (86.29% vs 87.51% Rec@K na YelpChi).

- **Combined methods > specialized GNNs > traditional ML**: Metody łączące zalety ML i GNN (Combined Methods) osiągnęły najlepsze wyniki (ave. 68.28%), przewyższając specialized GNNs (ave. 53.12%) i traditional methods (ave. 52.83%). General GNNs były najsłabsze (ave. 45.61%) przez brak task-specific design.

- **Interpretable fraud patterns**: Framework ujawnia interpretowalne wzorce oszustw - np. fraudulent websites mają minimal tech stack (avg 3-5 technologies vs 15-20 dla legit), brak real social media profiles (2.68% vs 83.78% legit), repetitive prices dla większości produktów.

## Metodologia

### Problem formulation
- **Graf**: G = (N, E) z N węzłami i E krawędziami
- **Cechy węzłów**: X ∈ R^(N×d), gdzie każdy węzeł u ma cechy x_u ∈ R^(1×d) i label y_u ∈ {0, 1}
- **Zadanie**: Binary classification - wykrycie fraudulent nodes w graph-structured data

### Dynamic Binning Embedding (DyBEM)

**1. Dynamic Splitting** - learnable binning strategy:
- Min-Max normalization: x̃ = (x - x_min) / (x_max - x_min) → [0,1]
- Inicjalizacja wektora α ∈ R^T (T = liczba bins)
- Softmax transformation: α̃_t = exp(α_t) / Σexp(α_j) → suma = 1
- Partition coordinates: b_t = Σ(α̃_i) for i=1 to t, with b_0=0, b_T=1
- Bins: B_t = [b_(t-1), b_t) są dynamicznie uczenie podczas treningu

**2. Binary Encoding** - dwa schematy kodowania:
- **One-hot encoding** (σ₁): r_t = 1 if x̃ ∈ [b_(t-1), b_t), else 0
- **PLE encoding** (σ₂): r_t = (x̃ - b_(t-1))/(b_t - b_(t-1)) zachowuje więcej precision
- Matrix form: r = σ((x̃ - Lα̃) ⊙ α̃^(-1)) gdzie L to lower triangular matrix
- Fully differentiable - umożliwia end-to-end gradient backpropagation

**3. Binning Embedding**:
- Każdy bin B_t ma trainable embedding v_t ∈ R^d
- Final embedding: DyBEM(x) = v_0 + Σ(r_t · v_t)
- Multi-head binning: multiple independent α initializations (inspirowane Random Forests)
- Output π: concatenation wszystkich binning embeddings z różnych atrybutów

### Message-Passing GNN
- **GraphSAGE** jako GNN backbone
- Aggregation function: h^l_u = AGG(h^(l-1)_u, {h^(l-1)_v | v ∈ M(u)})
- Inicjalizacja: h^0_u = π_u (output z DyBEM)
- L layers (L ∈ {1,2,3,4} depending on dataset)
- Final embedding: z_u = h^L_u wykorzystane do global aggregation
- Framework compatible z innymi message-passing GNNs (GAT, PMP)

### Pattern Global Aggregation
**Cross-attention mechanism** z reduced complexity:
- **Query**: H₁ = [z^τ_1, z^τ_2, ..., z^τ_M] ∈ R^(M×d₁) - current batch nodes
- **Key/Value**: H₂ = [z^τ_1, ..., z^τ_M, z^(τ-1)_(M+1), ..., z^(τ-1)_N] ∈ R^(N×d₁) - current batch + historical embeddings from previous epoch
- Q = H₁W_Q, K = H₂W_K, V = H₂W_V
- Z = Attention(Q, K, V) = sim(QK^T)V
- **Complexity reduction**: O(N²) → O(N·M) gdzie M << N (batch size)
- Caching historical GNN embeddings at end of each epoch
- No positional encoding needed (GNN output already contains structural info)

### Training procedure
- **Loss**: Standard binary classification loss
- **Optimization**: Random search hyperparameter tuning (GADBench recommendations)
- **Validation**: Early stopping on validation set
- **Hyperparameters**: T bins ∈ [4,40], L layers ∈ [1,4], batch size ∈ [32,5000]
- **Hardware**: Intel Xeon Gold 5318Y @ 2.10GHz, NVIDIA A6000 GPUs

## Główne Koncepcje

- **Attribute-Pattern**: Reprezentacja pojedynczych atrybutów jako fragment-wise vectors zamiast skalarów. Np. income i age są dzielone na bins (low/mid/high) i (youth/mid/old), co zachowuje correct meanings podczas fusion operations. Rozwiązuje problem non-additive features - nie można dodawać/uśredniać różnych typów atrybutów (age + income = nonsense).

- **Association-Pattern**: Wzorce relacji między węzłami w grafie wydobyte przez GNN message passing. Np. fraudsters często targetują "high-income elderly" - ten pattern jest visible tylko po aggregation neighbor features w grafie, nie w izolowanych node attributes.

- **Dynamic Binning Embedding (DyBEM)**: Fully differentiable, end-to-end learnable binning strategy eliminująca two-stage optimization problem wcześniejszych metod. Bins są automatycznie uczenie podczas treningu zamiast być określane preprocessing. Multi-head binning (multiple α initializations) zwiększa stability podobnie jak w Random Forests.

- **Global Aggregation with Cross-Attention**: Mechanizm agregujący patterns z całego grafu poprzez computing cross-attention między current batch nodes a historical embeddings z previous epoch. Redukuje computational complexity z O(N²) do O(N·M) i addressuje over-smoothing oraz long-range dependencies problems typowe dla standardowych GNNs.

- **Fraud Pattern Categories**: Różne typy fraud behaviors można odróżnić po category. Financial institutions: fraudsters target "high-income elderly individuals". E-commerce: "low-income young users" fall victim to fake rebate schemes. Te category-specific patterns są kluczowe do accurate differentiation fraudulent vs legitimate behaviors.

- **Combined Methods Paradigm**: Łączenie zalet traditional ML (attribute feature patterns, binning, interpretability) z GNNs (association patterns z graph structure) daje lepsze wyniki niż podejścia wykorzystujące tylko jedną metodę. GAAP to end-to-end solution w przeciwieństwie do two-stage approaches (XGBGraph, RFGraph).

- **Feature Binning Industrial Practice**: Binning remains active w industrial fraud detection (credit scoring) mimo że to traditional technique. DyBEM improves upon static binning przez introducing lossless piecewise linear representations (PLE encoding) oraz learnable bin boundaries zamiast fixed preprocessing.

## Wyniki

### Comparison with SOTA (Rec@K metric)

**Overall performance** (average across 7 datasets):
- **GAAP (ours)**: 70.88%
- DGA-GNN: 69.40% (+1.48pp)
- XGBGraph: 68.56% (+2.32pp)
- RFGraph: 66.30% (+4.58pp)
- PMP (best specialized GNN): 58.04% (+12.84pp)

**Per-dataset performance** (Rec@K %):

| Dataset | GAAP | Best Baseline | Improvement |
|---------|------|---------------|-------------|
| **YelpChi** | **88.54** | DGA-GNN: 84.23 | +4.31pp |
| **Amazon** | 87.50 | PNA: 90.78 | -3.28pp (2nd best) |
| **T-Finance** | **85.71** | PMP: 85.99 | -0.28pp (2nd best) |
| **Elliptic** | **73.32** | DGA-GNN: 72.76 | +0.56pp |
| **Tolokers** | **56.08** | DGA-GNN: 55.14 | +0.94pp |
| **DGraph-Fin** | **7.73** | DGA-GNN: 7.52 | +0.21pp |
| **T-Social** | **97.25** | DGA-GNN: 95.97 | +1.28pp |

**SOTA on 5/7 datasets**, second-best on 2/7 datasets.

### Ablation Study (YelpChi, T-Finance, T-Social)

**Component removal impact** (YelpChi Rec@K):
- **Full model**: 87.51%
- w/o DyBEM (dynamic binning): 47.62% (-39.89pp) - **największy spadek**
- w OHT (static one-hot): 75.33% (-12.18pp)
- w/o GNN (no association patterns): 61.62% (-25.89pp)
- w/o GA (global aggregation): 86.29% (-1.22pp)
- w GP (graph partition attention): 68.19% (-19.32pp)

**Key findings z ablation**:
1. DyBEM ma największy impact na YelpChi (32 features, high density)
2. GNN ma największy impact na T-Social (graph structure critical)
3. Dynamic binning > static one-hot (learns optimal bins)
4. Cross-attention > graph partition (avoids information loss)

### Number of bins analysis
- **YelpChi**: Performance rośnie monotonically z liczbą bins (4→40), ale z diminishing marginal returns
- **T-Finance**: Optimal ~8 bins, więcej bins nie pomaga (lower attribute complexity)
- Sweet spot: T ∈ [8, 20] dla większości datasetów

### Batch size impact
- **Minimal impact** on overall performance (tested 100, 300, 500)
- Cross-attention mechanism ensures completeness of information transmission niezależnie od batch size
- Practical implication: można użyć większych batches dla faster training bez performance degradation

### Method groups comparison (average Rec@K)
1. **Combined Methods**: 68.28% (best)
   - GAAP: 70.88%
   - DGA-GNN: 69.40%
   - XGBGraph: 68.56%
   - RFGraph: 66.30%

2. **Specialized GNNs**: 53.12%
   - PMP: 58.04% (best in group)
   - GHRN: 57.93%
   - BWGNN: 57.55%

3. **Traditional Methods**: 52.83%
   - RF: 56.34%
   - XGBoost: 54.02%

4. **General GNNs**: 45.61% (worst)
   - GraphSAGE: 55.65% (best in group)
   - GAT: 48.27%
   - GCN: 42.28%

## Przydatne Cytaty

> "For example, averaging two ages (e.g. 60: older and 6: child) leads to erroneous feature values (e.g. 33: middle-aged). Furthermore, merging disparate attributes, such as age and income, can result in nonsensical outcomes. This mixing complicates the model's ability to identify attribute patterns accurately." (str. 11616)

> "In fraud scenarios, fraudulent behaviors can be distinguished from legitimate ones by category. For instance, financial institutions have noted that fraudsters often target high-income elderly individuals. Similarly, e-commerce platforms report that low-income young users fall victim to fake rebate schemes, resulting in lost prepaid funds." (str. 11617)

> "Overall, our contribution is the first to introduce a Global Attribute-Association Pattern aggregation framework (GAAP) for fraud detection. In addition, a differentiable binning strategy is devised to construct attribute-pattern features, thereby improving the distinguishability of non-additive and distinct attribute combinations." (str. 11617)

> "The primary computational and storage bottleneck of traditional self-attention lies in its O(N²) complexity. We observe that in message-passing-based spatial GNNs, the final layer of each step after information aggregation typically contains only a small number of nodes. [...] This approach reduces the O(N²) complexity to O(N·M), where M represents the batch size." (str. 11619)

> "On the YelpChi dataset, an improvement of 4.3% was achieved. Additionally, state-of-the-art (SOTA) performance was reached on 5 datasets, while the second-best performance was achieved on the Amazon dataset, possibly due to noise in the graph structure information of Amazon." (str. 11621)

> "Combined methods performed the best, as they leverage the strengths of both attribute and association pattern mining. [...] Ours outperformed DGA-GNN due to the double optimization problem in the attribute pattern of DGA-GNN, whereas our proposed end-to-end architecture effectively overcomes this issue." (str. 11621)

> "Replacing dynamic binning with static one-hot binning resulted in a performance decline, which demonstrates that our proposed dynamic binning better adapts to the overall optimization process and meets the demands of downstream tasks." (str. 11622)

## Datasety

### Wykorzystane w eksperymentach

1. **[YelpChi](../../../datasets/yelp-chi.md)** - 45,954 nodes, 3,846,979 edges, 32 features. Dataset do identyfikacji abnormal reviews unfairly promoting/demoting products/businesses na Yelp.com (Rayana & Akoglu 2015). Hand-crafted review features and statistics. GAAP: 88.54% Rec@K (best).

2. **[Amazon](../../../datasets/amazon-reviews.md)** - 11,944 nodes, 4,398,392 edges, 25 features. Users writing fake reviews w musical instruments category na Amazon.com (McAuley & Leskovec 2013). Hand-crafted user features and statistics. GAAP: 87.50% Rec@K (2nd best).

3. **[T-Finance](../../../datasets/t-finance.md)** - 39,357 nodes, 21,222,543 edges, 10 features. Financial transaction fraud dataset (Tang et al. 2022). User profile details (registration days). GAAP: 85.71% Rec@K (2nd best).

4. **[T-Social](../../../datasets/t-social.md)** - 5,781,065 nodes, 73,105,508 edges, 10 features. Detecting abnormal accounts w social networks (Tang et al. 2022). User profile (logging activities). GAAP: 97.25% Rec@K (best). Largest dataset.

5. **[Elliptic](../../../datasets/elliptic-bitcoin.md)** - 203,769 nodes, 234,355 edges, 166 features. Illicit Bitcoin transaction detection (Weber et al. 2019). Timestamps and transaction information. GAAP: 73.32% Rec@K (best).

6. **[Tolokers](../../../datasets/tolokers.md)** - 11,758 nodes, 519,000 edges, 10 features. Fraudulent users detection na Toloka crowd-sourcing platform (Platonov et al. 2023). User profile with task performance statistics. GAAP: 56.08% Rec@K (best).

7. **[DGraph-Fin](../../../datasets/dgraph-fin.md)** - 3,700,550 nodes, 4,300,999 edges, 17 features. Credit default detection dataset from Finvolution Group constructed using guarantor contact information (Huang et al. 2022b). Timestamps and user profiles. GAAP: 7.73% Rec@K (best).

## Powiązane Tematy

- Graph Neural Networks (GNNs) architectures - GraphSAGE, GAT, GCN, spectral vs spatial approaches
- Fraud detection w różnych domenach - social networks, e-commerce, financial transactions, insurance, Bitcoin
- Feature binning techniques - one-hot encoding, PLE (Piecewise Linear Encoding), learnable binning
- Attention mechanisms w graphs - self-attention, cross-attention, global message aggregation, Nodeformer, SGFormer
- Non-additive features problem - averaging disparate attributes, incorrect feature fusion w GNNs
- Anomaly detection w graph-structured data - over-smoothing, long-range dependencies, heterophily
- Combined methods (ML + GNN) - XGBGraph, RFGraph, DGA-GNN, two-stage vs end-to-end optimization
- Interpretable fraud patterns - category-specific behaviors, fraudster targeting strategies
- Computational complexity reduction - O(N²) → O(N·M) poprzez cross-attention with historical embeddings
- Dynamic vs static feature engineering - learnable bins vs preprocessing, end-to-end differentiability
- Multi-modal fraud detection - attribute patterns + association patterns
- Transfer learning potencjał DyBEM - tabular data, CV, NLP tasks with statistical features
- Ensemble methods inspirations - Random Forests multi-head binning strategy
- Imbalanced learning w fraud detection - Rec@K metric vs AUROC/AUPRC w presence of imbalanced samples
- Adversarial robustness - camouflaged fraudsters, evolving fraud patterns
- Real-world deployment considerations - standalone models, scalability, interpretability requirements

## Notatki

*Sekcja pusta - miejsce na dodatkowe notatki użytkownika.*
