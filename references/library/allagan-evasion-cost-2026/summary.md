---
title: "Robustness, Cost, and Attack-Surface Concentration in Phishing Detection"
date: 2026-03-19
authors: "Julian Allagan, Mohamed Elbakary, Zohreh Safari, Weizheng Gao, Gabrielle Morgan, Essence Morgan, Vladimir Deriglazov"
status: read
doi: "arxiv:2603.19204"
category: "Security"
tags:
  - phishing-detection
  - adversarial-robustness
  - evasion-cost
  - attack-surface
  - cost-aware-evasion
  - minimal-evasion-cost
  - feature-economics
  - shortest-path
  - uci-phishing
  - representation-dependence
  - project/personalized-phishing-defense
---

# Robustness, Cost, and Attack-Surface Concentration in Phishing Detection

## Metadane
- **Autorzy**: Julian Allagan, Mohamed Elbakary, Zohreh Safari, Weizheng Gao, Gabrielle Morgan, Essence Morgan, Vladimir Deriglazov (Elizabeth City State University, NC, USA)
- **Rok**: 2026
- **Zrodlo**: arXiv:2603.19204v1 [cs.LG], 19 Mar 2026
- **DOI**: arxiv:2603.19204
- **Status**: `#read`
- **Kategoria**: Security
- **Tagi**: `#phishing-detection` `#adversarial-robustness` `#evasion-cost` `#attack-surface` `#minimal-evasion-cost` `#feature-economics` `#shortest-path` `#uci-phishing` `#representation-dependence`

## Streszczenie

Praca bada luke miedzy niemal doskonala accuracy detektorow phishingu pod ewaluacja i.i.d. a ich realnym bezpieczenstwem wdrozeniowym przy manipulacji cech po wdrozeniu. Autorzy proponuja framework ewazji swiadomy kosztu (cost-aware evasion), w ktorym dyskretne, monotoniczne edycje cech sa modelowane pod jawnymi budzetami atakujacego. Ewazja jest formalizowana jako problem najkrotszej sciezki na grafie przejsc wazonych kosztem, rozwiazywany dokladnie przez uniform-cost search (Algorytm 1).

Wprowadzaja trzy diagnostyki: minimal evasion cost (MEC) - najmniejszy kumulatywny koszt wywolania blednej klasyfikacji; evasion survival rate S(B) = Pr(MEC > B) - odpornosc przy budzecie B; oraz robustness concentration index (RCI) - czy edycje minimalnego kosztu sa rozproszone czy skoncentrowane na malym podzbiorze cech. Model zagrozenia jest dolnym ograniczeniem zdolnosci atakujacego (tylko monotoniczne usuwanie wskaznikow phishingu, bez wstrzykiwania anty-cech).

Glowny wynik formalny (Proposition 3.1, cost floor): jesli frakcja alpha > 0 poprawnie wykrytych instancji phishingu dopuszcza ewazje przez pojedyncze przejscie cechy o minimalnym koszcie c_min, to zaden klasyfikator nie moze podniesc odpowiedniego kwantyla MEC powyzej c_min bez modyfikacji reprezentacji cech lub modelu kosztu. To "action-set-limited invariance" - odpornosc adwersarialna w detekcji phishingu jest rzadzona przez ekonomie cech, nie przez zlozonosc modelu.

## Kluczowe Wnioski
- Na UCI Phishing Websites (11,055 instancji, 30 cech ternary) LR, RF, GBDT, XGBoost osiagaja AUC >= 0.979 pod ewaluacja statyczna, ale wszystkie zbiegaja do tej samej odpornosci pod budzetowana ewazja
- Mediana MEC = 2 dla pelnego zestawu cech we wszystkich architekturach; ponad 80% udanych ewazji minimalnego kosztu koncentruje sie na trzech tanich cechach powierzchniowych (URL_of_Anchor, SSLfinal_State, SFH)
- Twierdzenie cost-floor: kwantyl MEC nie moze przekroczyc c_min dopoki wszystkie przejscia o tym koszcie nie zostana usuniete - niezaleznie od architektury (Corollary 3.1: invariancja architektoniczna)
- Restrykcja cech poprawia odpornosc TYLKO gdy usuwa wszystkie dominujace tanie przejscia; pod strict schedule RA-8 daje 17-19% infeasible mass dla modeli ensemble (zablokowana wykonalnosc), ale mediana MEC wsrod evadable pozostaje 2
- Wyzsza accuracy NIE daje wyzszej mediany odpornosci gdy tanie przejscia pozostaja dostepne (Figure 5: wszystkie modele na poziomej linii MEC=2)
- Skalowanie kosztow powierzchniowych przesuwa mediane MEC liniowo (x2 koszt -> MEC z 2 do 4) zachowujac kolejnosc cech i koncentracje

## Metodologia

**Model zagrozenia**: f: X -> {-1,+1}; cechy w {-1,0,+1}^d (phishing-indicative/neutral/legitimate). Edycje monotoniczne (v' >= v), przejscia odwrotne = koszt nieskonczony (sanitization-style). Atakujacy zna cechy ale nie ma dostepu do parametrow/gradientow/confidence.

**Schematy kosztow** (Tabela 1): base - surface c=1,2; semi-domain c=3,6; infrastructure c=4,8. Strict - jak base ale upgrade infrastruktury do w pelni legalnego stanu zabroniony (c=inf). Kalibracja "time-to-effect": 1 jednostka = zmiana w 1 dzien, 4 jednostki = wielotygodniowa akumulacja (DNS, ruch, reputacja). B_max = 18.

**Metryki**: MEC (uniform-cost search, exact); FRI (feature robustness index = znormalizowane pole pod krzywa S(B), uwzglednia infeasible mass); RCIk (koncentracja na top-k cechach); FirstTop1 (waskie gardlo pierwszej edycji).

**Dane/modele**: UCI Phishing Websites (4,898 phishing / 6,157 legit), split 75/25 seed 1337. 4 rodziny: LR (L2, C=1.0), RF (100 drzew, depth 10), GBDT (100 est, lr 0.1, depth 6), XGBoost. Conditioning set P0 = poprawnie wykryte phishingowe; intersekcja 4 modeli, sample n=300.

**6 konfiguracji cech**: Full (30), AAS-12a, AAS-11b (high info-gain), RA-8 (infrastruktura + SSLfinal_State), VA-8a, VA-7b (tylko presentation-layer).

## Glowne Koncepcje

**Minimal Evasion Cost (MEC)**: najmniejszy koszt manipulacji cech do wywolania misclassyfikacji - dokladny shortest path.

**Cost floor / action-set-limited invariance**: strukturalny limit odpornosci wynikajacy z najtanszego dostepnego przejscia, niezalezny od modelu.

**Feature economics**: surface features (URL, HTML, certyfikat) sa tanie do edycji; infrastructure (wiek domeny, DNS, ruch) drogie - asymetria kosztow rzadzi odpornoscia.

**Representation-dependence**: odpornosc da sie podniesc tylko przez zmiane reprezentacji cech / kosztu, nie przez zmiane modelu.

## Wyniki

| Model | Acc | AUC | Median MEC (Full/base) | RCI3 |
|-------|-----|-----|------------------------|------|
| LR | 0.927 | 0.979 | 2 | 0.96 |
| RF | 0.950 | 0.993 | 2 | 0.84 |
| GBDT | 0.953 | 0.990 | 2 | 0.89 |
| XGB | 0.965 | 0.995 | 2 | 0.82 |

RA-8/strict: infeasible mass 17-19% (ensemble), FRI 0.23-0.25. VA-7b: median MEC 1, FRI < 0.05.
Surface cost scaling: lambda=1->MEC 2, lambda=4->MEC 8 (RCI3 >= 0.80 utrzymane).

## Przydatne Cytaty

"if a positive fraction of correctly detected phishing instances admit evasion through a single feature transition of minimal cost c_min, no classifier can raise the corresponding MEC quantile above c_min without modifying the feature representation or cost model." (Abstract)

"Adversarial robustness in phishing detection is governed by feature economics rather than model complexity." (Abstract)

"A feature may be highly predictive under i.i.d. evaluation yet operationally brittle if it is inexpensive to edit." (str. 11, Discussion)

"Proposition 3.1 is a property of the action set and cost model, not the dataset; it applies whenever a nontrivial fraction of instances admit single-transition evasion at minimal cost." (str. 12)

## Datasety
- [UCI Phishing Websites](../../datasets/uci-phishing-websites.md) - 11,055 instancji, 30 cech ternary {-1,0,+1}, 4,898 phishing / 6,157 legit (Mohammad, Thabtah, McCluskey 2015)

## Powiazane Tematy
- Problem-space adversarial ML (Pierazzi et al., Apruzzese "Real Attackers Don't Compute Gradients")
- Cykl zycia kampanii phishingowych (Oest et al. Sunrise to Sunset, Bijmans phishing kits)
- Evasion attacks at test time (Biggio & Roli)
- Cost-aware / budget-constrained adversarial evaluation
- Feature representation hardening

## Notatki

**CLOSENESS verdict (iteration-2 prior art): METRYCZNIE NAJBLIZSZE - zrodlo formalizmu, ktory ADOPTUJEMY.** Nie jest to praca o personalizacji, ale dostarcza dokladnie tego aparatu metrycznego (MEC, S(B), cost floor), ktorego uzywamy do kwantyfikacji odpornosci.

**DELTA-vs-ours**: Allagan et al. mierza evasion-cost na cechach STRONY WWW (website features) w modelu sanitization-style, bez jakiegokolwiek pojecia odbiorcy/profilu. My ADOPTUJEMY ich metryke (MEC, survival S(B), FRI) i stosujemy ja do kondycjonowania per-user: zamiast "koszt zmiany cechy strony do ominiecia klasyfikatora" liczymy "koszt zmiany ataku spersonalizowanego dla danego profilu". Co kluczowe, ich twierdzenie o representation-dependence (Prop. 3.1 / Cor. 3.1) MOTYWUJE nasze podejscie: skoro odpornosci nie da sie podniesc zmiana modelu a tylko zmiana reprezentacji, to wzbogacenie reprezentacji o profil odbiorcy (per-user conditioning) jest wlasnie ta dozwolona modyfikacja reprezentacji, ktora moze przesunac cost floor. Roznice: oni - website features, monotone sanitization, brak odbiorcy; my - personalizowany atak/obrona, ta sama matematyka kosztu ewazji przeniesiona na os profilu uzytkownika.
