---
title: "Non-Intrusive Graph-Based Bot Detection for E-Commerce Using Inductive Graph Neural Networks"
date: 2026-01-01
authors: "Sichen Zhao, Zhiming Xue, Yalun Qi, Xianling Zeng, Zihan Yu"
status: read
category: "Machine Learning"
tags: []
---
# Non-Intrusive Graph-Based Bot Detection for E-Commerce Using Inductive Graph Neural Networks

## Metadane
- **Autorzy**: Sichen Zhao, Zhiming Xue, Yalun Qi, Xianling Zeng, Zihan Yu
- **Rok**: 2026
- **Źródło**: arXiv:2601.22579v6 [cs.LG]
- **Data publikacji**: 17 lutego 2026
- **Status**: read
- **Kategoria główna**: Machine Learning
- **Podkategorie**: Graph Neural Networks, Anomaly Detection, Security
- **Tagi**: #graph-neural-networks #bot-detection #graphsage #ecommerce #security #fraud-detection #gnn #bipartite-graphs #inductive-learning

## Streszczenie

Publikacja opisuje nieintuzywny system detekcji botów w platformach e-commerce, który modeluje interakcje sesji-URL jako graf dwudzielny i wykorzystuje indukcyjną sieć neuronową (GraphSAGE) do klasyfikacji węzłów sesji. Tradycyjne podejścia, takie jak blokowanie IP lub CAPTCHA, są podatne na obejście poprzez rotację proxy lub mogą być uciążliwe dla użytkowników. Proponowana metoda łączy topologię grafu z lekkimi cechami behawioralnymi i semantyką URL, umożliwiając wykrycie "feature-normal" automatyzacji - botów, które wyglądają normalnie w agregowanych cechach, ale wykazują atypową łączność w grafie sesji-URL.

Eksperyment na rzeczywistym ruchu e-commerce z etykietami botów o wysokim poziomie pewności wykazuje, że GraphSAGE przewyższa bazową sieć MLP w AUC i F1, jednocześnie pozostając odpornym na łagodne perturbacje krawędzi grafu oraz w ewaluacji cold-start, co umożliwia wdrożenie w czasie rzeczywistym bez instrumentacji po stronie klienta.

## Kluczowe Wnioski

- GraphSAGE (grafu rafinowanego) uzyskuje AUC 0.9705 w porównaniu do bazowej sieci MLP (AUC 0.9102), poprawiając precision, recall i F1-score
- Filtrowanie statycznych zasobów (CSS, JavaScript) z grafu jest krytyczne dla stabilności i wydajności modelu
- Model zachowuje wysoką wydajność w warunkach cold-start (AUC 0.963 vs 0.970 in-sample z spadkiem tylko 0.8%), wskazując na efektywne generalizowanie na nowe sesje i URL
- Pod łagodnymi perturbacjami niezamierzonych (dodawanie/usuwanie 1-3 krawędzi na sesję), GraphSAGE utrzymuje AUC >0.95, podczas gdy baseline MLP spada poniżej 0.90
- Wymóg praktyczny: minimalna liczba odwiedzonych URL dla niezawodnej klasyfikacji wynosi około 3 wizyty
- Łączenie struktury topologicznej z cechami semantycznymi jest kluczowe - struktura sama w sobie osiąga ~0.88 AUC, podczas gdy tylko cechy osiągają ~0.85

## Metodologia

Badanie wykorzystuje pięć głównych komponentów:

**1. Konstruowanie Grafu**: Zbudowanie heterogenicznego grafa dwudzielnego G = (V, E), gdzie węzły sesji reprezentują sekwencje żądań/akcji w oknie czasowym, a węzły URL reprezentują unikalne strony/zasoby. Krawędzie łączą sesję z URL, jeśli sesja odwiedziła ten URL. Proces refinacji usuwa haby statycznych zasobów (CSS, JavaScript itp.), aby uzyskać czystszy graf dla propagacji wiadomości.

**2. Projektowanie Cech**: Przypisanie lekkich wektorów cech węzłom sesji i URL. Cechy sesji obejmują: czas sesji, liczbę żądań, szybkość żądań, liczbę odrębnych stron, indykatory akcji wieloetapowych (koszyk, logowanie), grube odciski palców (user-agent). Cechy URL są celowo grube i zachowujące prywatność: kategoria strony (produkt, kategoria, wyszukiwanie, checkout), globalne statystyki dostępu (popularność/rarość), tagi czułości dla specjalnych punktów końcowych. Wszystkie identyfikatory URL są anonimizowane poprzez hashing jednokierunkowy.

**3. Architektura Modelu GraphSAGE**: Dwie warstwy sieci, każda aktualizująca reprezentację węzła poprzez agregację próbkowanych sąsiadów. Warstwa 1 wychwytuje kontekst 1-hopowy, warstwa 2 kontekst 2-hopowy. Agregator średniowy (mean aggregator), wymiary embeddings 128-D. Głowica klasyfikatora MLP na embeddings sesji do produkcji P(bot | sesja). Indukcyjność: GraphSAGE uczy się funkcji agregacji (nie per-węzłowych embeddings), umożliwiając ocenę nowych sesji/URL z cech i sąsiedztw.

**4. Trening**: Nadzorowany trening na etykietowanych sesjach. Etykiety otrzymane poprzez hybrydową (quasi-syntetyczną) strategię łączącą zweryfikowane ataki w rzeczywistym świecie (honeypots, pułapki URL) z kontrolowanymi wstrzyknięciami różnorodnych skryptów botów. Binarna entropia krzyżowa, Adam optimizer (lr=0.001), early stopping na AUC walidacji, wagi klas dla nierównowagi.

**5. Wnioskowanie**: Dla nowej sesji, dodanie węzła/krawędzi, obliczenie cech, agregacja ograniczonego sąsiedztwa, wyjście prawdopodobieństwa bota. Wnioskowanie na ograniczonym podgrafie sąsiedztwa umożliwia ocenę bliską czasowi rzeczywistemu.

## Główne Koncepcje

- **Bipartite Session-URL Graph**: Heterogeniczny graf dwudzielny reprezentujący interakcje między sesjami użytkowników a stronami internetowymi. Struktura relacyjna umożliwia "podejrzenie przez asocjację" dzięki wspólnym sąsiedztwom URL.

- **Inductive GraphSAGE**: Indukcyjny algorytm reprezentacji zbudowany na dużych grafach. W przeciwieństwie do podejść transdyktywnych, uczy się funkcji agregacji umożliwiającej ocenę nowych węzłów bez retrainingu.

- **Feature-Normal Bots**: Automaty, które wyglądają normalnie w agregowanych cechach behawioralnych (prędkość myszy, częstotliwość kliknięć, czas przebywania), ale wykazują atypową topologię w grafie sesji-URL (np. rzadkie kombinacje stron, szerokie pokrycie, skoordynowane cele).

- **Message Passing**: Maszyna propagacji wiadomości w GNN, gdzie każdy węzeł aktualizuje swoją reprezentację poprzez agregację informacji od sąsiednich węzłów, umożliwiając łączenie behawioralnych cech z kontekstem relacyjnym.

- **Cold-Start Scenario**: Problem oceny nowych sesji i URL, które nie były widoczne podczas treningu. GraphSAGE radzić sobie poprzez naukę uogólnionych funkcji agregacji opartych na cechach.

- **Graph Refinement**: Proces filtrowania haba statycznych zasobów (CSS, JavaScript) z surowego grafu w celu uzyskania czystszych, bardziej znaczących klastrów dla propagacji wiadomości.

## Wyniki

**1. Porównanie Wydajności (Tabela 1)**:
- GraphSAGE (rafinowany graf): AUC 0.9705 ± 0.0085, Precision 0.8055, Recall 0.9002, F1-Score 0.8501
- GraphSAGE (surowy graf): AUC 0.8756 ± 0.1042 (wyraźnie gorsza, mniej stabilna)
- Baseline MLP: AUC 0.9102 ± 0.0150, Precision 0.7505, Recall 0.7510, F1-Score 0.7508

GraphSAGE odzyskuje "feature-normal" boty, które wyglądają łagodnie w agregowanych cechach, ale wykazują atypową łączność sesji-URL. Jest to sygnał nieobecny w baseline'u MLP.

**2. Odporność na Perturbacje Niezamierzone (Rysunek 6)**:
- Przy łagodnych perturbacjach (1-3 krawędzie zmodyfikowane na sesję), GraphSAGE utrzymuje AUC >0.95
- MLP spada szybko, przechodząc poniżej 0.90 przy 2-3 perturbacjach
- Pod silnymi perturbacjami obie metody ulegają degradacji, ale GraphSAGE utrzymuje wyraźną przewagę

**3. Symulacja Cold-Start (Tabela 2)**:
- Week 1 (in-sample): GraphSAGE AUC 0.9705, MLP AUC 0.9100
- Week 2 (cold-start, nowe sesje/URL): GraphSAGE AUC 0.9630 (spadek tylko 0.8%), MLP AUC 0.8500 (spadek 6.6%)
- Fine-tuning (opcjonalnie): GraphSAGE AUC 0.9720

**4. Zmiana Rozkładu i Sesje z Niewidocznymi Celami (Tabela 3)**:
- Week 2 ogółem: MLP AUC 0.8500, GraphSAGE AUC 0.9630
- Podzbiór z całkowicie niewidu­ocznym celami (all session-URL edges to nowe URL nodes): MLP AUC 0.7210 (spadek 15.2%), GraphSAGE AUC 0.8890 (spadek tylko 7.7%)
- Dywergencja Jensen-Shannon między Week 1 a Week 2: 0.083 (nietrywialny drift behawioralny)
- 19.2% węzłów URL w Week 2 nie było widoczne w Week 1

**5. Wpływ Długości Sesji (Tabela 4)**:
- Bardzo krótko (0-2): MLP AUC 0.6200, GraphSAGE AUC 0.6640 (Δ +0.0440)
- Krótko (3-10): MLP AUC 0.7800, GraphSAGE AUC 0.8880 (Δ +0.1080)
- Średnio (11-50): MLP AUC 0.8200, GraphSAGE AUC 0.9430 (Δ +0.1230)
- Długo (>50): MLP AUC 0.7600, GraphSAGE AUC 0.9000 (Δ +0.1400)
- Całość: MLP AUC 0.8100, GraphSAGE AUC 0.9300 (Δ +0.1200)

Praktyczne minimum ~3 odwiedzenia URL dla niezawodnej klasyfikacji.

## Przydatne Cytaty

> "Non-intrusive graph formulation: We formulate bot detection on a session–URL graph from standard server logs, avoiding CAPTCHAs and client-side instrumentation." (str. 1)

> "GraphSAGE recovers 'feature-normal' bots that look benign in aggregates but exhibit atypical session–URL connectivity (e.g., rare-page mixtures), a signal absent from the MLP." (str. 4)

> "By encoding temporal information implicitly through session structure (e.g., URL transitions) and node attributes, a static graph formulation provides a robust and computationally efficient representation." (str. 5)

> "Graph predictions can be inspected via a session's local neighborhood (unique/rare URLs, shared target sets, or coordinated clusters), providing actionable explanations for analysts that are less transparent in feature-only models." (str. 6)

> "Scoring a session with up to ~50 page visits takes under 50 ms on CPU." (str. 6)

## Datasety

- Anonimizowane logi serwera z reprezentatywnej średniej platformy e-commerce przez dwa tygodnie (~80K sesji tła, ~5% botów)
- Hybrydowa strategia etykietowania: zweryfikowane ataki rzeczywistego świata (honeypots/pułapki URL) + kontrolowane wstrzyknięcia (scrapers, headless browsers)
- Sesji-URL graf: na rzędzie 10^5 krawędzi (dziesiątki tysięcy sesji; tysiące URL) z rozkładem potęgowym
- Podziały: 10% walidacja, 10% test, z podobnymi proporcjami klas i chronologicznie późniejszą podziałem testowym

## Powiązane Tematy

- Graph Anomaly Detection
- Fraud Detection using GNNs
- Inductive Representation Learning
- Message Passing Neural Networks
- E-commerce Security
- Session-based Recommendation Systems
- Adversarial Robustness in Graphs
- Temporal Graph Models (TGN, Trajectory-based Transformers)
- Heterogeneous Graphs
- Web Bot Evasion Techniques
- Privacy-Preserving Machine Learning

## Notatki

### Implementacja i Wdrażanie
- System wdrażany jako wtyczka backend: ekstraktcja cech i aktualizacje grafu zasilają serwis oceny, który wyprowadza wynik ryzyka bota na sesję, używając tylko istniejących logów
- Model może być retrenowany offline i hot-swapped; indukcyjne wnioskowanie degraduje się łagodnie na nowe wzorce aż do retrainingu
- Sampling sąsiedztwa jest limitowany aby ograniczyć czas wykonania; ocena sesji z do ~50 odwiedzeniami stron zajmuje <50 ms na CPU

### Ograniczenia i Przyszłe Prace
- Bardziej zaawansowana koordynacja, gdzie każda sesja wygląda łagodnie, pozostaje wyzwaniem
- Przyszłe kierunki: bogatsze grafy heterogeniczne (dodanie węzłów account/IP), jawne obrony przed manipulacją krawędzi niezamierzonymi, bardziej drobnoziarnista atrybuacja do wsparcia przepływów pracy analityków, ewaluacja A/B w życiu
- Temporalne metody (TGN, Transformers oparte na trajektoriach) mogą oferować korzyści w warunkach z gęstymi, długohoryzontowymi trajektoriami użytkowników (zostawione na przyszłą pracę)

### Kluczowe Obserwacje
- Struktura grafu sama osiąga AUC ~0.88, podczas gdy tylko cechy osiągają ~0.85, potwierdzając że topologia i semantyka są komplementarne
- Obserwacja przypadku badanego: klaster botów oznaczony głównie ponieważ jego sesje współdzieliły dostęp do nieaktualnego punktu końcowego API - anomalia strukturalna trudna do ujawnienia z samych agregacji sesji
- Dezintegracja między tygodniami: prędkość żądań i czas trwania sesji (JS divergence 0.083) wskazywał na znaczący drift behawioralny
