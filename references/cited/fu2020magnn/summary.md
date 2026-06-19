---
title: "MAGNN: Metapath Aggregated Graph Neural Network for Heterogeneous Graph Embedding"
date: 2020-01-01
authors: "Xinyu Fu, Jiani Zhang, Ziqiao Meng, Irwin King"
status: read
doi: "10.1145/3366423.3380297"
category: "Machine Learning"
tags:
  - heterogeneous-graph
  - graph-neural-network
  - metapath
  - graph-embedding
  - attention-mechanism
  - link-prediction
  - project/graph-phishing-detection
---

# MAGNN: Metapath Aggregated Graph Neural Network for Heterogeneous Graph Embedding

## Metadane
- **Autorzy**: Xinyu Fu, Jiani Zhang, Ziqiao Meng, Irwin King
- **Rok**: 2020
- **Źródło**: Proceedings of The Web Conference 2020 (WWW '20), Taipei
- **DOI/Link**: 10.1145/3366423.3380297 (arXiv:2002.01680)
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
MAGNN to model sieci grafowej (GNN) do osadzania heterogenicznych grafów informacyjnych (HIN), czyli grafów z wieloma typami węzłów i krawędzi. Autorzy wskazują trzy ograniczenia istniejących metod opartych na metaścieżkach (metapaths): (1) pomijanie cech treściowych węzłów, (2) odrzucanie węzłów pośrednich wzdłuż metaścieżki (tylko węzły końcowe), (3) korzystanie z pojedynczej metaścieżki. MAGNN adresuje wszystkie trzy przez trzy komponenty.

Architektura składa się z: (1) transformacji treści węzła — projekcja cech różnych typów węzłów do wspólnej przestrzeni latentnej przez transformacje liniowe specyficzne dla typu; (2) agregacji wewnątrz-metaścieżkowej (intra-metapath) — koder instancji metaścieżki z mechanizmem atencji, włączający również węzły pośrednie; (3) agregacji między-metaścieżkowej (inter-metapath) — fuzja informacji z wielu metaścieżek z atencją. Zaproponowano trzy kodery instancji: mean, linear oraz oparty na rotacji relacyjnej w przestrzeni zespolonej (inspirowany RotatE).

Eksperymenty na trzech zbiorach (IMDb, DBLP — klasyfikacja i klastrowanie węzłów; Last.fm — predykcja powiązań) pokazują, że MAGNN konsekwentnie przewyższa silne bazy (LINE, node2vec, metapath2vec, HERec, GCN, GAT, GATNE, HAN). Ablacja potwierdza wkład każdego z trzech komponentów oraz przewagę kodera rotacji relacyjnej.

## Kluczowe Wnioski
- Instancje metaścieżek niosą bogatszą informację niż jedynie sąsiedzi metaścieżkowi (boost ~4-7% nad HAN na IMDb).
- Łączenie wielu metaścieżek przez atencję przewyższa wybór pojedynczej metaścieżki.
- Cechy treściowe węzłów i węzły pośrednie są istotne dla jakości osadzeń.
- MAGNN osiąga SOTA w klasyfikacji, klastrowaniu i predykcji powiązań (Last.fm AUC 98.91%).

## Metodologia
GNN z atencją na grafach heterogenicznych; trening semi-nadzorowany (cross-entropy) lub nienadzorowany (negative sampling). Metryki: Macro/Micro-F1 (klasyfikacja), NMI/ARI (klastrowanie), AUC/AP (link prediction). 8 głów atencji, wymiar osadzenia 64, optymalizator Adam.

## Główne Koncepcje
- **Graf heterogeniczny (HIN)** — wiele typów węzłów i krawędzi.
- **Metaścieżka** — uporządkowana sekwencja typów węzłów/krawędzi opisująca relację złożoną (np. APVPA).
- **Intra-/inter-metapath aggregation** — agregacja w obrębie i pomiędzy metaścieżkami z atencją.
- **Koder rotacji relacyjnej** — modelowanie kolejności węzłów w instancji metaścieżki.

## Relevancja dla graph-phishing-detection
MAGNN jest kluczowym odniesieniem metodologicznym dla wątku "GNN multipleks/heterogeniczny" w projekcie. Graf phishingu/BEC jest z natury heterogeniczny (domeny, URL, IP, nameservery, nadawcy, odbiorcy, kampanie), a metaścieżki pozwalają modelować relacje złożone (np. Domena-IP-Domena, Nadawca-Domena-Nadawca). Mechanizm agregacji instancji metaścieżek z węzłami pośrednimi i atencją między metaścieżkami stanowi bazę projektową dla uczonego GNN nad grafem domenowym. Praca dostarcza też silnych baselinów (HAN, metapath2vec, GATNE) do porównań i sprawdzony schemat ewaluacji w trzech zadaniach (klasyfikacja, klastrowanie, link prediction), które mapują się na detekcję węzłów-phishingowych i przewidywanie powiązań w grafie.

## Przydatne Cytaty
- "metapath instances contain richer information than metapath-based neighbors" (Sekcja 5.3).
- Definicje metaścieżki, instancji metaścieżki i grafu opartego na metaścieżce (Sekcja 2).

## Datasety
- IMDb (filmy/reżyserzy/aktorzy), DBLP (autorzy/prace/terminy/venue), Last.fm (użytkownicy/artyści/tagi).

## Powiązane Tematy
- HAN i inne GNN heterogeniczne.
- Osadzenia grafów wiedzy (RotatE).
- Projektowanie metaścieżek dla grafów bezpieczeństwa.

## Notatki
