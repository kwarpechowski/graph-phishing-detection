---
title: "Multimodal and Contrastive Learning for Click Fraud Detection"
date: 2021-01-01
authors: "Weibin Li, Qiwei Zhong, Qingyang Zhao, Hongchun Zhang, Xiaonan Meng"
status: read
tags: []
---
# Multimodal and Contrastive Learning for Click Fraud Detection

## Metadane
- **Autorzy**: Weibin Li, Qiwei Zhong, Qingyang Zhao, Hongchun Zhang, Xiaonan Meng
- **Rok**: 2021
- **Źródło**: DeMaL@WWW '21 (April 19-23, 2021, Ljubljana, Slovenia)
- **DOI/Link**: arXiv:2105.03567v1 [cs.LG]
- **Status**: read
- **Kategoria**: Machine Learning, Fraud Detection
- **Tagi**: #fraud-detection #multimodal-learning #contrastive-learning #ecommerce #deep-learning #graph-neural-networks #bert

## Streszczenie

Publikacja przedmiotuje problem detekcji oszustw kliknięć w platformach e-commerce, który stanowi istotne zagrożenie dla biznesu reklam internetowych. Autorzy proponują innowacyjne podejście MCCF (Multimodal and Contrastive learning network for Click Fraud detection), które łączy trzy źródła informacji: cechy statystyczne i kategoryczne (Wide & Deep), sekwencje zachowań użytkowników (BERT) oraz heterogeniczne sieci mediów (GNN). Model wykorzystuje contrastive learning do rozwiązania problemu braku zrównoważenia danych treningowych (zaledwie ~10% oszustw).

Badania przeprowadzone na rzeczywistym zbiorze danych z platformy Alibaba.com zawierającym 3,29 miliona kliknięć wykazały, że proponowana metoda osiąga znaczące poprawy wydajności: AUC wzrasta o 7,2%, a F1-score o 15,6% w porównaniu z metodami istniejącymi. Model wykazuje szczególną skuteczność w wykrywaniu zaawansowanych oszustw, w tym oszustw grupowych, które starają się imitować naturalne zachowanie użytkowników.

## Kluczowe Wnioski

- Fraudsterzy wykazują wyraźnie różne charakterystyki statystyczne od użytkowników autentycznych: więcej kliknięć na IP, krótsze przedziały czasowe między kliknięciem a utworzeniem pliku cookie
- Zachowania w przeglądarce różnią się znacząco: fraudsterzy koncentrują się na stronach głównych i szczegółów (>99%), podczas gdy użytkownicy autentyczni mają bardziej zróżnicowany wzór
- Liczba powiązanych mediów (IP, CookieID, DeviceID) jest znacznie wyższa dla oszustów: 21,86% fraudsterów ma co najmniej 3 powiązane media vs 6,31% dla użytkowników autentycznych
- Multimodalne podejście jest istotne: każda z trzech modalności wnosi pozytywny wkład do wydajności modelu
- Contrastive learning (NT-Xent loss) jest bardziej efektywny niż tradycyjna cross-entropy do obsługi niezrównoważonego zbioru danych

## Metodologia

Proponowany model MCCF składa się z czterech głównych komponentów:

1. **Wide and Deep Network**: Przetwarza cechy statystyczne (szerokość: wartości pierwotne, kombinacje cech, informacje demograficzne) i cechy kategoryczne (AdvertiserID, KeywordID) przez wielowarstwową sieć neuronową

2. **Behavior Sequence Network**: Wykorzystuje model BERT do analizy sekwencji stron odwiedzonych przez użytkownika przed kliknięciem (do 300 kroków), zwracając uwagę na typy stron rozróżniające oszustwa od autentycznych kliknięć

3. **Multi-media Heterogeneous Network**: Buduje graf z trzema typami węzłów (IP, CookieID, DeviceID) i agreguje informacje o sąsiadach używając średniej agregacji. Każdy węzeł posiada 542 atrybuty (informacje demograficzne, częstotliwość kliknięć), każda relacja ma 90 atrybutów

4. **Integration and Contrastive Training**: Łączy reprezentacje z trzech modułów przez dwie w pełni połączone warstwy, szkoląc model z wykorzystaniem NT-Xent loss (normalized temperature-scaled cross entropy) zamiast standardowej cross-entropy, co pozwala lepiej obsługiwać niezrównoważenie danych

Dane treningowe zawierają 2,54 miliona kliknięć (10,89% pozytywnych), dane testowe 0,75 miliona (10,17% pozytywnych).

## Główne Koncepcje

- **Click Fraud**: Oszustwo polegające na kliknięciu reklam w celu wyczerpania budżetu konkurenta lub inflacji przychodów
- **Wide & Deep Features**: Kombinacja cech ciągłych (szeroki component) i kategorycznych (głębokie zagnieżdżenia) dla wszechstronnej reprezentacji
- **Contrastive Learning**: Technika uczenia maszynowego, która umieszcza próbki tej samej klasy blisko siebie w przestrzeni osadzenia, a próbki różnych klas daleko od siebie
- **Heterogeneous Network**: Sieć zawierająca węzły i krawędzie wielu typów, reprezentujące różne jednostki mediów i ich interakcje
- **NT-Xent Loss**: Znormalizowana temperatura skalowana cross-entropy loss, rozszerzenie N-pair loss używane w contrastive learning

## Wyniki

Eksperymentalne wyniki na rzeczywistym zbiorze danych Alibaba:

| Metoda | Precision | Recall | F1-score | AUC |
|--------|-----------|--------|----------|-----|
| Random Forest | 0.867 | 0.403 | 0.550 | 0.685 |
| LightGBM | 0.892 | 0.416 | 0.567 | 0.686 |
| GraphSAGE | 0.973 | 0.545 | 0.699 | 0.785 |
| BiLSTM | 0.966 | 0.480 | 0.641 | 0.755 |
| TextCNN | 0.981 | 0.604 | 0.747 | 0.804 |
| BERT | 0.984 | 0.619 | 0.760 | 0.861 |
| **MCCF** | **0.987** | **0.854** | **0.916** | **0.933** |

MCCF osiąga F1-score wyższy o 21,7% od najlepszych metod drzew decyzyjnych i grafów, i o 15,6% wyższy niż BERT. Ablacyjne testy wykazują, że każda modalność wnosi wkład, ze znaczącym wpływem sekwencji zachowań.

## Przydatne Cytaty

> "Advertising click fraud detection plays one of the vital roles in current E-commerce websites as advertising is an essential component of its business model." (str. 1)

> "Fraudsters frequently switch IP and clear cookies to make their statistical features look like genuine. However, their behavior sequence might be abnormal, such as only visiting search and advertising pages." (str. 1)

> "The World Federation of Advertisers says ad fraud will cost advertisers $50 billion a year by 2025" (str. 1)

> "The main contributions of this work are summarized as follows: To the best of our knowledge, we are the first attempt to incorporate multimodal information and contrastive learning for click fraud detection." (str. 2)

## Datasety

- **Alibaba Click Fraud Dataset**: Rzeczywisty zbiór danych z platformy Alibaba.com zawierający 3,29 miliona kliknięć (2,54M do treningu, 0,75M do testowania) z bogatymi informacjami behawioralnymi i relacyjnymi między mediami

## Powiązane Tematy

- Uczenie kontrastywne (Contrastive Learning)
- Sieci neuronowe na grafach (Graph Neural Networks, GNN)
- Model BERT i transformatory
- Uczenie multimodalne
- Niezrównoważone zbiory danych w klasyfikacji
- Detektory anomalii i oszustw
- Rekomendacyjne systemy deep learning
- Feature engineering dla e-commerce

## Notatki

