---
title: "Alleviating the Inconsistency Problem of Applying Graph Neural Network to Fraud Detection (GraphConsis)"
date: 2020-01-01
authors: "Zhiwei Liu, Yingtong Dou, Philip S. Yu, Yutong Deng, Hao Peng"
status: read
doi: "10.1145/3397271.3401253"
category: "Security"
tags:
  - fraud-detection
  - graph-neural-networks
  - inconsistency-problem
  - heterogeneous-graph
  - neighbor-sampling
  - camouflage
  - project/graph-phishing-detection
---

# Alleviating the Inconsistency Problem of Applying Graph Neural Network to Fraud Detection (GraphConsis)

## Metadane
- **Autorzy**: Zhiwei Liu, Yingtong Dou, Philip S. Yu, Yutong Deng, Hao Peng (University of Illinois at Chicago i in.)
- **Rok**: 2020
- **Źródło**: SIGIR '20 (43rd International ACM SIGIR Conference)
- **DOI/Link**: https://doi.org/10.1145/3397271.3401253 (`#fraud`, `#GNN`, `#inconsistency`)
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca podejmuje fundamentalny problem stosowania grafowych sieci neuronowych (GNN) do detekcji oszustw. Modele GNN opierają się na założeniu, że sąsiedzi w grafie dzielą podobny kontekst, cechy i relacje — agregacja sąsiedztwa zakłada homofilię. Jednak oszuści celowo to założenie łamią. Autorzy identyfikują trzy rodzaje niespójności (inconsistency): (1) niespójność kontekstu — sprytni oszuści łączą się z regularnymi (benign) podmiotami jako kamuflaż, a ponadto są rzadcy; (2) niespójność cech — węzły połączone tą samą relacją mogą mieć bardzo różne cechy (np. recenzje tego samego użytkownika o różnych produktach); (3) niespójność relacji — różne typy relacji niosą różną siłę sygnału o oszustwie, a równe ich traktowanie zaburza detekcję.

Aby rozwiązać te problemy, autorzy projektują nowy framework GNN o nazwie GraphConsis, działający na grafie heterogenicznym z wieloma relacjami. Wprowadza trzy techniki: (1) dla niespójności kontekstu — łączenie trenowalnych embeddingów kontekstowych z cechami węzła; (2) dla niespójności cech — metryka oceny spójności (consistency score) filtrująca niespójnych sąsiadów i generująca prawdopodobieństwo próbkowania; (3) dla niespójności relacji — uczenie wag uwagi (attention) powiązanych z próbkowanymi węzłami i embeddingami relacji.

Analizy empiryczne pokazują, że problem niespójności jest krytyczny w zadaniach detekcji oszustw, a rozległe eksperymenty potwierdzają skuteczność GraphConsis. Autorzy udostępnili też toolbox detekcji oszustw GNN (DGFraud).

## Kluczowe Wnioski
- Założenie homofilii GNN jest łamane przez oszustów stosujących kamuflaż — to krytyczny problem.
- Trzy typy niespójności: kontekstu, cech i relacji wymagają osobnego potraktowania.
- Consistency score pozwala filtrować niespójnych sąsiadów przed agregacją.
- Mechanizm uwagi po relacjach waży różne typy krawędzi heterogenicznego grafu.

## Metodologia
GraphConsis działa na heterogenicznym grafie wielorelacyjnym. (1) Trenowalne embeddingi kontekstowe dołączane do cech węzłów. (2) Metryka spójności embeddingów do odrzucania sąsiadów o niskim score i wyznaczania prawdopodobieństwa próbkowania. (3) Atencja po embeddingach relacji do ważenia próbkowanych sąsiadów. Uczenie semi-nadzorowane, end-to-end. Towarzyszy mu toolbox DGFraud z implementacjami modeli SOTA.

## Główne Koncepcje
- **Inconsistency problem** (kontekst / cechy / relacje)
- **Camouflage** oszustów łamiący homofilię
- **Consistency score** i filtrowanie sąsiadów przy próbkowaniu
- **Relation attention** na grafie heterogenicznym

## Relevancja dla graph-phishing-detection
GraphConsis dostarcza teoretyczny fundament dla projektu: kamuflaż i niespójność to centralne zjawiska także w phishingu na grafie (konta phishingowe łączą się z legalnymi, by się ukryć). Mechanizmy consistency score i atencji relacyjnej wspierają niezmiennik projektu dotyczący spójności reprezentacji i wielowarstwowego/multipleksowego grafu (wiele typów relacji). Stanowi klasyczny baseline detekcji oszustw GNN oraz uzasadnienie, dlaczego naiwna agregacja GNN zawodzi na grafie wiedzy domenowej z adwersarialnymi połączeniami.
