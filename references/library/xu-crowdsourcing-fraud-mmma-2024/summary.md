---
title: "Crowdsourcing Fraud Detection over Heterogeneous Temporal MMMA Graph"
date: 2024-01-01
authors: "Zequan Xu, Qihang Sun, Shaofeng Hu, Jieming Shi, Hui Li"
status: read
tags: []
---
# Crowdsourcing Fraud Detection over Heterogeneous Temporal MMMA Graph

## Metadane
- **Autorzy**: Zequan Xu, Qihang Sun, Shaofeng Hu, Jieming Shi, Hui Li
- **Rok**: 2024
- **Źródło**: ACM Conference, arXiv:2308.02793v2
- **DOI/Link**: https://arxiv.org/abs/2308.02793v2
- **Status**: read
- **Tagi**: #fraud-detection #graph-neural-networks #crowdsourcing #mmma #wechat #contrastive-learning #temporal-graph #heterogeneous-graph

## Streszczenie

Rozwój biznesu farm kliknięć wykorzystujących wielofunkcyjne aplikacje mobilne (MMMAs jak WeChat) kusi cyberprzestępców do perpetrowania oszustw crowdsourcingowych, które powodują straty finansowe dla pracowników farm kliknięć. W tej pracy autorzy proponują nowatorską metodę kontrastywnego uczenia wielowidokowego nazwaną CMT (Contrastive Multi-view Learning over Heterogeneous Temporal Graph) do wykrywania oszustw crowdsourcingowych nad heterogenicznym grafem czasowym (HTG) aplikacji MMMA.

CMT przechwytuje zarówno heterogeniczność jak i dynamikę HTG, generując wysokiej jakości reprezentacje do wykrywania oszustw w sposób samo-nadzorowany. Metoda została wdrożona na przemysłowej skali HTG w WeChat i znacząco przewyższa inne metody. CMT pokazuje również obiecujące wyniki na wielkoskalowym publicznym finansowym HTG, wskazując że może być zastosowany w innych zadaniach wykrywania anomalii grafowych.

## Kluczowe Wnioski

- CMT osiąga AUC 0.9014 i KS 0.6624 na zbiorze WeChat, znacząco przewyższając bazowe metody (HG-Encoder: 0.8682 AUC)
- Metoda łączy kodowanie heterogeniczności grafu z dynamicznym modelowaniem sekwencji użytkowników
- Wykorzystanie uczenia kontrastywnego zmniejsza zależność od nadzoru - krytyczne w kontekście ograniczonych etykiet
- Oszuści wykazują charakterystyczne wzorce behawioralne rozproszone w czasie (4-stopniowy proces: ADD → PULL → TRANSFER → DISAPPEAR)
- Metoda jest indukcyjna - może generować reprezentacje dla nowych węzłów pojawiających się codziennie w MMMA

## Metodologia

**Heterogeniczny Graf Czasowy (HTG)**:
- 3 typy węzłów: użytkownicy, grupy, urządzenia
- 7 typów relacji: CREATE, ENTER, LOGIN, PULL, SEND, ADD, TRANSFER
- Graf temporalny: {G_t}^T_{t=1}, gdzie każdy G_t to heterogeniczny graf w punkcie czasowym t

**Architektura CMT - faza pretreningu**:

1. **HG-Encoder** (Heterogeneous GNN Encoder):
   - Agregacja według relacji (mean, max, sum pooling)
   - Mechanizm uwagi na poziomie relacji
   - 2-warstwowy GNN z self-connection

2. **TSS-Encoder** (Temporal Snapshot Sequence):
   - Modeluje sekwencję reprezentacji użytkownika z różnych snapshotów
   - Przechwytuje ewolucję stanów użytkownika w czasie

3. **URS-Encoder** (User Relation Sequence):
   - Modeluje sekwencje akcji użytkownika (1-hop out-neighbors)
   - Przechwytuje bezpośrednie zachowania użytkownika

4. **Augmentacja danych**:
   - Reorder: losowe przestawienie ciągłej podsekwencji (γ = 0.4)
   - Substitute: zastępowanie elementów przez podobne z hipergrafu (α = 0.4)

5. **CS-Encoder** (Contrastive Sequence Encoder):
   - Transformer z multi-head self-attention (8 głów)
   - Position encoding dla zachowania kolejności
   - Contrastive loss: maksymalizuje podobieństwo między augmentacjami tej samej sekwencji, minimalizuje między różnymi

**Faza wykrywania**:
- Konkatenacja: h^(0)_u ⊕ h^seq_temp_u ⊕ h^seqrel_u
- HG-Encoder_detect + moduł scoringu (sigmoid)
- Próg: 0.5 dla klasyfikacji oszust/normalny

**Funkcja straty**:
- L = L_binary + L_cl
- L_binary: binary cross-entropy na ograniczonych etykietach
- L_cl: contrastive loss z temperatura τ i cosine similarity

## Główne Koncepcje

- **Heterogeniczny Graf Czasowy (HTG)**: Graf z wieloma typami węzłów i krawędzi, ewoluujący w czasie jako strumień snapshotów
- **Wielowidokowe uczenie**: TSS (temporal snapshots) + URS (user relations) jako dwa komplementarne widoki zachowań użytkowników
- **Uczenie kontrastywne**: Samo-nadzorowane uczenie poprzez kontrastowanie podobnych i niepodobnych obiektów
- **Soft links vs Hard links**: Połączenia oparte na podobieństwie behawioralnym zamiast współdzielonych właściwości (IP, device)
- **Augmentacja sekwencji**: Reorder (zachowuje semantykę kolejności grup akcji) i Substitute (ujawnia ukryte połączenia przez hipergrafy)
- **Indukcyjne uczenie**: Model nie przechowuje osadzeń węzłów, tylko wagi transformacji - może generalizować na nowe węzły

## Wyniki

**Zbiór WeChat** (6.8M węzłów użytkowników, 151K grup, 126K urządzeń):
- CMT: AUC 0.9014, KS 0.6624
- HG-Encoder (baseline): AUC 0.8682, KS 0.5905
- Precision wzrosła z 0.82 do 0.86 przy recall=0.27 dla nowych/gościnnych kupujących
- Poprawa: +3.8% AUC, +12.2% KS względem najlepszej bazowej metody

**Zbiór FinGraph** (4.1M węzłów, 5M krawędzi):
- CMT: AUC 0.8354, KS 0.5720
- HG-Encoder: AUC 0.8194, KS 0.5485
- Potwierdza transferowalność metody do innych zadań wykrywania oszustw

**Ablacja**:
- TSS-Encoder sam: +2.0% AUC vs HG-Encoder
- URS-Encoder sam: +2.6% AUC vs HG-Encoder
- Contrastive learning: +1.0-1.2% AUC
- Pełny CMT (TSS_cl + URS_cl): najlepsze wyniki

**Odkryte wzorce oszustw** (FinGraph):
- Oszuści mają innych oszustów w 2-hop sąsiedztwie
- Krawędzie oszustów mają krótkie zakresy TS (concentrated time period)
- Typy krawędzi oszustów zwiększają się wraz z TS (eskalacja aktywności)

## Przydatne Cytaty

> "The rise of the click farm business using Multi-purpose Messaging Mobile Apps (MMMAs) tempts cybercriminals to perpetrate crowdsourcing frauds that cause financial losses to click farm workers." (str. 1)

> "CMT captures both heterogeneity and dynamics of HTG and generates high-quality representations for crowdsourcing fraud detection in a self-supervised manner." (str. 1)

> "In new/guest buyer transaction scenario, this segment is a challenge for traditional method, we can make precision increase from 0.82 to 0.86 at the same recall of 0.27, which means we can decrease false positive rate using this method." (str. 1)

> "To our knowledge, this is the first time similarity based 'soft link' has been used in graph embedding applications." (str. 1)

> "Fraudsters usually perpetrate crowdsourcing frauds as a gang rather than an individual cybercriminal." (str. 5)

## Datasety

- **WeChat Dataset** (proprietary, permission-based) - 6.8M węzłów użytkowników, 151K grup WeChat, 126K urządzeń, 29.7M krawędzi, 14 snapshotów czasowych (1 dzień = 1 snapshot), 53,660 etykiet (10,749 oszustów, 42,911 normalnych)
- **FinGraph Dataset** (publiczny, 7th Finvolution Competition) - 4.1M węzłów, 5M krawędzi, 11 typów krawędzi, 82K etykiet (1K oszustów, 81K normalnych), anonimizowany graf finansowy

## Powiązane Tematy

- Wykrywanie anomalii w grafach dynamicznych (AddGraph, StrGNN, NetWalk)
- Graph Neural Networks dla oszustw (CARE-GNN, PC-GNN, DCI)
- Uczenie kontrastywne na grafach
- Sekwencyjne modelowanie zachowań użytkowników
- Click farms i oszustwa crowdsourcingowe
- Aplikacje MMMA (WeChat, multi-purpose messaging)
- Heterogeniczne sieci grafowe (RGCN, Simple-HGN)
- Wykrywanie oszustw finansowych na grafach
- Soft links vs hard links w construction grafów
- Data augmentation dla sekwencji temporalnych

## Notatki

**Mocne strony**:
- Pierwsza metoda wykorzystująca soft links (podobieństwo behawioralne) zamiast hard links (wspólne IP/device) w osadzeniach grafowych
- Wielowidokowe podejście (temporal snapshots + user relations) kompleksowo modeluje dynamikę
- Uczenie kontrastywne zapewnia dodatkowy sygnał nadzoru przy ograniczonych etykietach
- Indukcyjność - może handle nowych użytkowników pojawiających się codziennie
- Wdrożenie produkcyjne na WeChat (przemysłowa skala)
- Kod open-source: https://github.com/KDEGroup/CMT

**Ograniczenia**:
- Wymaga GPU-based HDBSCAN clustering (własne narzędzie Tencent) - może być bottleneck
- Złożoność obliczeniowa: 3*S_HG + 2*S_CS ≈ O(f²) - akceptowalna ale nie trywialna
- Zbiór WeChat proprietary - nie da się odtworzyć eksperymentów 1:1
- Augmentacja (reorder, substitute) wymaga ręcznego tuningu hiperparametrów (γ, α)
- Model nie wykorzystuje zawartości wiadomości (privacy concerns) - potencjalnie silny sygnał pozostaje niewykorzystany

**Potencjał dla własnych badań**:
- **Ekstrakcja cech behawioralnych z HTML/JS dla phishing**: Analogia do user relation sequences - sekwencje akcji DOM (clicks, scrolls, form interactions) jako behavioral fingerprint
- **Temporal robustness**: CMT pokazuje jak modelować dynamikę czasową - można zastosować do testowania degradacji modeli phishingu 2005→2026
- **Soft links dla e-commerce fraud**: Zamiast hard links (IP, device), wykorzystać podobieństwo HTML features lub datalayer patterns
- **Contrastive learning dla fraud detection**: Augmentacja sekwencji behawioralnych + contrastive loss może działać bez dużych zbiorów etykietowanych
- **Proof-of-concept biometrii behawioralnej**: CMT inspiruje do PoC z syntetycznymi danymi behawioralnymi (mouse movement, timing)

