---
title: "Graph Structure Learning for Robust Graph Neural Networks"
date: 2020-01-01
authors: "Wei Jin, Yao Ma, Xiaorui Liu, Xianfeng Tang, Suhang Wang, Jiliang Tang"
status: read
doi: "10.1145/3394486.3403049"
category: "Machine Learning"
tags:
  - graph-structure-learning
  - robust-gnn
  - adversarial-attacks
  - graph-neural-networks
  - graph-denoising
  - project/graph-phishing-detection
---

# Graph Structure Learning for Robust Graph Neural Networks

## Metadane
- **Autorzy**: Wei Jin, Yao Ma, Xiaorui Liu, Xianfeng Tang, Suhang Wang, Jiliang Tang
- **Rok**: 2020
- **Źródło**: KDD 2020 (Proceedings of the 26th ACM SIGKDD)
- **DOI/Link**: https://doi.org/10.1145/3394486.3403049
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca prezentuje Pro-GNN — framework wspólnego uczenia struktury grafu i parametrów sieci neuronowej grafowej, odporny na ataki adwersarialne na strukturę. GNN są wrażliwe na zaburzenia krawędzi: nawet niewielka liczba dodanych/usuniętych krawędzi (atak poisoning) potrafi drastycznie obniżyć trafność. Autorzy wykorzystują obserwację, że czyste, rzeczywiste grafy mają właściwości takie jak niska rangowość (low rank), rzadkość (sparsity) oraz gładkość cech (feature smoothness) wzdłuż krawędzi, podczas gdy ataki adwersarialne te właściwości naruszają.

Pro-GNN uczy się oczyszczonej macierzy sąsiedztwa, regularyzując ją tak, by była niskiej rangi, rzadka i zgodna z gładkością cech, jednocześnie trenując GNN do zadania klasyfikacji. Eksperymenty pokazują, że metoda odzyskuje znaczną część wydajności przy różnych typach ataków (np. metattack, nettack) i przewyższa wcześniejsze obrony nawet przy dużych poziomach zaburzeń struktury.

## Kluczowe Wnioski
- Ataki adwersarialne na strukturę grafu naruszają low-rank, sparsity i smoothness.
- Wspólne uczenie struktury i parametrów GNN przywraca odporność.
- Regularizacje oparte na właściwościach czystych grafów skutecznie usuwają złośliwe krawędzie.
- Pro-GNN przewyższa wcześniejsze obrony przy silnych atakach poisoning.

## Metodologia
Optymalizacja łącznej funkcji celu: strata klasyfikacji GNN + regularyzacja jądrową normą (low rank) + L1 (sparsity) + człon gładkości cech (Dirichlet energy) na uczonej macierzy sąsiedztwa. Naprzemienna optymalizacja struktury i wag sieci. Ewaluacja na benchmarkach (Cora, Citeseer, Polblogs, Pubmed) pod atakami metattack/nettack/random.

## Główne Koncepcje
- **Graph structure learning** — uczenie oczyszczonej struktury grafu.
- **Odporność adwersarialna** GNN.
- **Low-rank / sparsity / feature smoothness** — własności czystych grafów.
- **Poisoning attack** — zatruwanie struktury treningowej.

## Relevancja dla graph-phishing-detection
Grafy w cyberbezpieczeństwie są naturalnie adwersarialne: napastnik phishingowy aktywnie manipuluje strukturą (tworzy fałszywe krawędzie komunikacji, podszywające się domeny, sztuczne relacje zaufania), by uniknąć detekcji. Pro-GNN dostarcza mechanizm odpornego uczenia GNN przy zatrutej strukturze — bezpośrednio istotny dla planowanego adaptacyjnego ataku i analizy odporności (P3). Idea oczyszczania krawędzi może też redukować szum w grafach komunikacji i transakcji, poprawiając wykrywanie spear phishingu przy zachowaniu rygoru ewaluacji odpornej na manipulację (leak-aware, robust).
