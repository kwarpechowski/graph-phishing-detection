---
title: "GNNGuard: Defending Graph Neural Networks against Adversarial Attacks"
date: 2020-01-01
authors: "Xiang Zhang, Marinka Zitnik"
status: read
doi: "arXiv:2006.08149"
category: "Security"
tags:
  - adversarial-robustness
  - graph-neural-networks
  - defense
  - edge-pruning
  - attention
  - poisoning-attacks
  - project/graph-phishing-detection
---

# GNNGuard: Defending Graph Neural Networks against Adversarial Attacks

## Metadane
- **Autorzy**: Xiang Zhang, Marinka Zitnik (Harvard University)
- **Rok**: 2020
- **Źródło**: NeurIPS 2020
- **DOI/Link**: arXiv:2006.08149 — https://arxiv.org/abs/2006.08149
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
GNNGuard to ogólny, modułowy mechanizm obrony, który można dołączyć do dowolnej architektury GNN, aby uodpornić ją na adwersaryjne ataki na strukturę grafu (dodawanie/usuwanie krawędzi, perturbacje). Obserwacją wyjściową jest to, że ataki strukturalne tworzą krawędzie łączące węzły o niepodobnych cechach/osadzeniach, co zaburza propagację komunikatów w GNN.

Mechanizm działa przez estymację podobieństwa sąsiadów (neighbor importance estimation): dla każdej krawędzi oblicza wagę opartą na podobieństwie reprezentacji łączonych węzłów i przycina/odważa krawędzie podejrzane (łączące niepodobne węzły). Dodatkowo wprowadza "layer-wise graph memory", utrzymując spójność przyciętej struktury między warstwami, co stabilizuje obronę. Mechanizm jest wpięty w agregację komunikatów i uczony razem z modelem.

Eksperymenty z atakami (Nettack, Metattack, RL-S2V) na GCN, GAT, GIN i GraphSAGE pokazują, że GNNGuard znacząco przywraca dokładność klasyfikacji węzłów pod atakiem, przewyższając wcześniejsze obrony, przy zachowaniu skuteczności na czystych grafach.

## Kluczowe Wnioski
- Ataki strukturalne łączą węzły niepodobne — to wykrywalny sygnał.
- Re-ważenie/przycinanie krawędzi wg podobieństwa odbudowuje odporność.
- "Layer-wise graph memory" stabilizuje obronę między warstwami.
- GNNGuard jest modułowy — działa z dowolnym backbone GNN.

## Metodologia
Dla każdej krawędzi liczone podobieństwo reprezentacji węzłów; wagi normalizowane, krawędzie poniżej progu odważane/usuwane; pamięć grafu zachowuje spójność wag między warstwami. Ewaluacja pod atakami poisoning/evasion (Nettack, Metattack) na standardowych grafach cytowań, metryka dokładności klasyfikacji węzłów.

## Główne Koncepcje
- **Neighbor importance estimation** — ważenie krawędzi po podobieństwie.
- **Edge pruning / re-weighting** — usuwanie podejrzanych krawędzi.
- **Layer-wise graph memory** — spójność między warstwami.
- **Adversarial robustness** GNN wobec perturbacji struktury.

## Relevancja dla graph-phishing-detection
Odporność adwersaryjna jest krytyczna dla phishingu, bo atakujący aktywnie manipuluje strukturą grafu, aby zmylić detektor (np. domieszanie legalnych krawędzi, podszywanie się pod zaufane konta, sztuczne tworzenie wspólnych sąsiadów — atak adaptacyjny z planu P3 rozprawy). GNNGuard dostarcza konkretnego mechanizmu obrony, który można wpiąć w multipleksowy/temporalny GNN projektu, a jego zasada (podejrzane krawędzie łączą niepodobne węzły) jest naturalnie zgodna z intuicją, że krawędzie atakujących łączą rozłączne społeczności. Stanowi referencję dla wątku odporności i przeciwdziałania atakom adaptacyjnym oraz dryfowi.
