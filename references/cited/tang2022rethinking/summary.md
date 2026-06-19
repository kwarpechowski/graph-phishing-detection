---
title: "BWGNN: Rethinking Graph Neural Networks for Anomaly Detection"
date: 2022-01-01
authors: "Jianheng Tang, Jia Li, Ziqi Gao, Jia Li"
status: to-read
tags: []
---
# BWGNN: Rethinking Graph Neural Networks for Anomaly Detection

## Metadane
- **Autorzy**: Jianheng Tang, Jia Li, Ziqi Gao, Jia Li
- **Rok**: 2022
- **Źródło**: International Conference on Machine Learning (ICML)
- **Status**: to-read
- **Pochodzenie**: Wyekstrahowane z duan-graph-fraud-gaap-2025
- **Tagi**: #to-read #reference #spectral-gnn #anomaly-detection #fraud-detection #low-pass #high-pass #filters

## Streszczenie

BWGNN (Bi-Wave Graph Neural Network) rethinks message passing w GNN dla anomaly detection z perspektywy spektralnej. Wykorzystuje low-pass i high-pass filters do targeted fraud adaptation, adresując problem over-smoothing i heterophily w fraud detection graphs. Osiąga 57.55% average Rec@K jako jedna z najlepszych specialized GNN methods.

## Kluczowe Wnioski

- Spectral perspective: low-pass filters (homophily) + high-pass filters (heterophily)
- Specialized GNN dla fraud detection (nie general-purpose GCN/GAT)
- 57.55% average Rec@K - best w spectral GNN category
- Adresuje over-smoothing problem w fraud graphs

## Notatki

*Publikacja dodana automatycznie z bibliografii GAAP. Jest to reprezentatywna praca dla spectral GNN approaches w fraud detection, osiągająca najlepsze wyniki w kategorii specialized GNNs obok GHRN i PMP. Dodaj PDF aby wygenerować pełne podsumowanie używając `/summarize-paper tang-bwgnn-rethinking-gnn-2022`*

**Context z GAAP**: "From the spectral perspective, AMnet, BWGNN, and GHRN use low-pass and high-pass filters for targeted fraud adaptation designs. However, these methods rarely focus on the targeted mining of feature patterns of node attributes on fraud detection graphs."
