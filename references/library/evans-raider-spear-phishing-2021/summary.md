---
title: "RAIDER: Reinforcement-aided Spear Phishing Detector"
date: 2021-01-01
authors: "Keelan Evans, Alsharif Abuadbba, Tingmin Wu, Kristen Moore, Mohiuddin Ahmed, Ganna Pogrebna, Surya Nepal, Mike Johnstone"
status: read
doi: "10.1007/978-3-031-23020-2_2"
category: "Security"
tags:
  - phishing-detection
  - spear-phishing
  - reinforcement-learning
  - feature-selection
  - knn
  - zero-day-attack
  - email-header
  - sender-profiling
  - project/spear-phishing-context
---

# RAIDER: Reinforcement-aided Spear Phishing Detector

## Metadane
- **Autorzy**: Keelan Evans, Alsharif Abuadbba, Tingmin Wu, Kristen Moore, Mohiuddin Ahmed, Ganna Pogrebna, Surya Nepal, Mike Johnstone
- **Rok**: 2021 (arXiv:2105.07582)
- **Źródło**: DIMVA 2022 (Edith Cowan University / CSIRO's Data61 / Cybersecurity CRC, Australia)
- **DOI/Link**: 10.1007/978-3-031-23020-2_2
- **Status**: read
- **Kategoria główna**: Security
- **Tagi**: `#phishing-detection` `#spear-phishing` `#reinforcement-learning` `#feature-selection` `#knn` `#zero-day-attack` `#email-header` `#sender-profiling`

## Streszczenie

Artykuł prezentuje RAIDER (Reinforcement AIded Spear Phishing DEtectoR) — system detekcji spear phishingu oparty na Reinforcement Learning (RL) do automatycznego doboru cech. Problem spear phishingu różni się od ogólnego phishingu: zamiast binarnej klasyfikacji phishing/benign, wymaga wieloklasowego modelu, gdzie każda klasa odpowiada nadawcy, a klasyfikator wykrywa rozbieżności między cechami emaila a profilem domniemanego nadawcy.

Kluczowa motywacja: istniejące systemy (jak Gascon et al. 2018) wymagają ręcznej inżynierii cech, co generuje wektory >8000 wymiarów, niestabilne w czasie i nieadaptowalne do nowych ataków. RAIDER używa algorytmu RL opartego na polityce Average of Rewards (AOR) z KNN jako klasyfikatorem — agent RL ocenia wpływ każdej cechy na dokładność i automatycznie wybiera optymalny podzbiór.

Ewaluacja na 11,000+ emailach z publicznych datasetów (Enron, SpamAssassin, IWSPA-AP) w 3 scenariuszach ataków: Blind Spoofing (atakujący bez wiedzy o nadawcy), Known Domain (atakujący ma emaile z tej samej domeny), Known Sender (najtrudniejszy — atakujący ma dostęp do emaili impersonowanego nadawcy). RAIDER redukuje wymiarowość wektora cech o 55% zachowując porównywalną dokładność, a dla zero-day ataków unika spadku dokładności do 14%.

## Kluczowe Wnioski

- **Redukcja wymiarowości o 55%**: automatycznie generowane cechy z RL są znacznie kompaktowsze niż ręcznie ekstrakcjonowane (Gascon et al. >8000 wymiarów)
- **Wyniki wg scenariusza ataku**: Blind Spoofing 94% (vs 90% bazowe), Known Domain 83% (=), Known Sender 62% (=)
- **Zero-day adaptacja**: aktualizacja feature subset przy nowym typie ataku unika spadków dokładności do 14%
- **Stabilność cech**: PCA RAIDER wykazuje stabilniejsze, skondensowane reprezentacje cech w czasie (2016-2020) vs rozstrzelone, wysokowymiarowe wektory Gascon et al.
- **Ograniczenie Known Sender**: nawet z aktualizacją, detekcja zatrzymuje się na 62% — najbardziej zaawansowany wariant ataku pozostaje trudny do wykrycia
- **Header-only**: RAIDER nie analizuje treści emaila — opiera się wyłącznie na metadanych nagłówka, co jest podejściem privacy-friendly

## Metodologia

Architektura: Raw Feature Extraction (wszystkie pola nagłówka emaila jako bag-of-words) → RL Agent (Epsilon-Greedy policy, AOR feature table) → Feature Evaluation (KNN accuracy per subset) → Feature Subset Generation (cechy z pozytywnym AOR) → Spear Prediction (KNN na ostatecznym zbiorze cech).

Trzy scenariusze ataków z Gascon et al. 2018: (1) Blind Spoofing — tylko zmiana adresu nadawcy, (2) Known Domain — emaile z tej samej domeny co impersonowany, (3) Known Sender — pełny dostęp do historycznych emaili impersonowanego nadawcy.

Trening: 7,518 benignowych emaili (87 unikalnych nadawców, min. 2 emaile/nadawca), testing: 50/50 benign/spear phishing (1201+1201), 10-fold cross-validation. Zero-day symulacja: trenowanie na jednym typie ataku, testowanie na innym.

## Główne Koncepcje

- **RAIDER**: Reinforcement AIded Spear Phishing DEtectoR — system RL+KNN do automatycznego doboru cech detekcji spear phishingu
- **Spear phishing jako wieloklasowa klasyfikacja**: każda klasa = nadawca; wykrywanie polega na porównaniu cech emaila z profilem nadawcy, nie binarnej klasyfikacji
- **Blind Spoofing**: najprostszy atak — atakujący fałszuje tylko adres nadawcy bez wiedzy o jego stylu
- **Known Domain**: atakujący ma dostęp do emaili z tej samej domeny co impersonowany nadawca
- **Known Sender**: najtrudniejszy — atakujący ma dostęp do historycznych emaili samego impersonowanego nadawcy
- **AOR (Average of Rewards)**: polityka RL oceniająca średni wpływ każdej cechy na dokładność klasyfikacji
- **Sender profile**: model cech charakterystycznych dla konkretnego nadawcy, budowany z jego historycznych emaili
- **Zero-day attack**: typ ataku niewidoczny w danych treningowych; statyczne klasyfikatory tracą nawet 14% dokładności

## Wyniki

| Scenariusz | RAIDER (auto) | KNN (manual) | TPR RAIDER | TPR Gascon |
|-----------|---------------|--------------|------------|------------|
| Blind Spoofing | **94%** | 90% | 91.9% | 90.6% |
| Known Domain | **83%** | 83% | 78.4% | 77.0% |
| Known Sender | **62%** | 62% | 71.2% | 53.2% |

Zero-day robustness: z aktualizacją feature subset — uniknięcie spadku 14% vs brak aktualizacji (49→62% dla Known Sender).

Runtime: RL feature generation ~24.83 min (jednorazowo); prediction time lepsza niż manual (0.0086 vs 0.0100 s/email).

## Przydatne Cytaty

> "RAIDER is the first spear phishing detector that can account for changing data over time by generating new feature subsets for specific types of attacks." (str. 2)

> "Using reinforcement learning to automatically identify the significant features could reduce the dimensions of the required features by 55% in comparison to existing ML-based systems." (Abstract)

> "For the known sender attack, more than half of the spear phishing emails were correctly identified by RAIDER's automatically extracted features, whereas less than 20% were correctly identified by KNN using the manually-engineered features." (str. 10)

> "By utilising the RAIDER's automatic feature generator, we can avoid accuracy drops of up to 14% when encountering new (previously unseen) attacks." (str. 16)

## Datasety

- [Enron Email Dataset](../../datasets/enron-corpus.md) — 4,279 emaili do budowania profili nadawców
- SpamAssassin easy/hard ham (Apache): 2,551 + 250 legit emaili
- IWSPA-AP 2018: 4,082 emaili politycznych
- Uni. Buffalo Bread Secured: 75 emaili
- CSIRO phishing dataset (2016-2020): 32,959 emaili do analizy stabilności cech

## Powiązane Tematy

- Gascon et al. 2018 (RAID) — baseline: 46 ręcznie ekstrakcjonowanych cech z nagłówka emaila, KNN
- Dewan et al. 2014: stylometryczne + LinkedIn features do detekcji spear phishingu
- Zero-day problem w spear phishing: ataki ewoluują w czasie, klasyfikatory statyczne degradują
- Contextual-aware detekcja: RAIDER nie analizuje konwersacji (wątek emailowy); to kierunek przyszłych prac
- RL dla feature selection: alternatywa dla stochastycznych metod optymalizacji cech
- Privacy-friendly detekcja: wyłącznie metadata nagłówka, bez treści emaila

## Notatki

