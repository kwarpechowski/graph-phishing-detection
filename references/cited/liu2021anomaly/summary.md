---
title: "Anomaly Detection on Attributed Networks via Contrastive Self-Supervised Learning (CoLA)"
date: 2021-01-01
authors: "Yixin Liu, Zhao Li, Shirui Pan, Chen Gong, Chuan Zhou, George Karypis"
status: read
doi: "10.1109/TNNLS.2021.3068344"
category: "Machine Learning"
tags:
  - anomaly-detection
  - attributed-networks
  - contrastive-learning
  - self-supervised-learning
  - graph-neural-networks
  - unsupervised-learning
  - project/graph-phishing-detection
---

# Anomaly Detection on Attributed Networks via Contrastive Self-Supervised Learning (CoLA)

## Metadane
- **Autorzy**: Yixin Liu, Zhao Li, Shirui Pan, Chen Gong, Chuan Zhou, George Karypis (Monash University, Alibaba Group i in.)
- **Rok**: 2021
- **Źródło**: IEEE Transactions on Neural Networks and Learning Systems (TNNLS)
- **DOI/Link**: https://doi.org/10.1109/TNNLS.2021.3068344 (`#anomaly`, `#contrastive`, `#CoLA`)
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca dotyczy detekcji anomalii na sieciach atrybutowanych (attributed networks) — wszechobecnych w finansach, mediach społecznościowych i e-commerce. Autorzy wskazują dwa typy anomalii: strukturalne (atrybuty normalne, ale nietypowe połączenia) oraz kontekstowe (naturalna struktura sąsiedztwa, ale zaburzone atrybuty). Istniejące metody głębokie oparte na grafowym autoenkoderze (np. DOMINANT, SpecAE) mają trzy wady: nie celują bezpośrednio w detekcję anomalii (uczą się rekonstrukcji), nie wykorzystują w pełni bogactwa informacji grafu oraz nie skalują się do dużych sieci przez trening na pełnym grafie.

Proponowany framework CoLA (Contrastive self-supervised Learning for Anomaly detection) rozwiązuje te ograniczenia. W pełni wykorzystuje informację lokalną poprzez próbkowanie nowego typu par instancji kontrastywnych, które przechwytują relację między węzłem a jego sąsiednią podstrukturą w sposób nienadzorowany. Zaprojektowano dedykowany model kontrastywny oparty na GNN, uczący informatywnych embeddingów z wysokowymiarowych atrybutów i lokalnej struktury oraz mierzący zgodność (agreement) par instancji za pomocą zwracanych score'ów. Wielokrotnie przewidywane score'y są następnie używane do oceny anomalności każdego węzła metodą estymacji statystycznej.

Dzięki przetwarzaniu wsadowemu par instancji (zamiast całego grafu) CoLA elastycznie skaluje się do dużych sieci. Wyniki eksperymentów pokazują, że CoLA przewyższa metody SOTA na wszystkich siedmiu zbiorach benchmarkowych.

## Kluczowe Wnioski
- CoLA przewyższa baseline'y na 7 zbiorach benchmarkowych.
- Para kontrastywna węzeł–podstruktura przechwytuje anomalie lepiej niż rekonstrukcja autoenkodera.
- Uczenie ma cel bezpośrednio związany z detekcją anomalii (a nie tylko rekonstrukcję).
- Przetwarzanie wsadowe par instancji zapewnia skalowalność do dużych grafów.

## Metodologia
Próbkowanie par kontrastywnych typu węzeł docelowy vs. jego lokalna podstruktura (ego-network). Model kontrastywny oparty na GNN uczy embeddingów i mierzy zgodność par (score). Wielorundowe score'y agregowane przez estymację statystyczną dają wynik anomalności węzła. Trening wsadowy (batch) par instancji zamiast pełnego grafu. Ewaluacja na 7 zbiorach atrybutowanych.

## Główne Koncepcje
- **Anomalie strukturalne vs kontekstowe** w sieciach atrybutowanych
- **Para kontrastywna węzeł–podstruktura** jako instancja uczenia
- **Self-supervised contrastive learning** zamiast rekonstrukcji
- **Statystyczna estymacja score'u anomalności**

## Relevancja dla graph-phishing-detection
CoLA jest istotnym baseline'em nienadzorowanej detekcji anomalii na grafach atrybutowanych — bezpośrednio relevantnym dla phishingu, gdzie etykiety są rzadkie. Idea kontrastowania węzła z jego lokalną podstrukturą inspiruje budowę reprezentacji w grafie wiedzy domenowej i wspiera niezmiennik projektu dotyczący uczenia samonadzorowanego/kontrastywnego. Rozróżnienie anomalii strukturalnych i kontekstowych mapuje się na typy nieprawidłowości kont phishingowych, a skalowalność wsadowa jest kluczowa przy dużych grafach transakcji/komunikacji.
