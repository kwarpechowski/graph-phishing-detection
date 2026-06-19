---
title: "Contrastive Multi-View Representation Learning on Graphs"
date: 2020-01-01
authors: "Kaveh Hassani, Amir Hosein Khasahmadi"
status: read
doi: "arXiv:2006.05582"
category: "Machine Learning"
tags:
  - graph-representation-learning
  - contrastive-learning
  - self-supervised
  - graph-neural-networks
  - graph-diffusion
  - project/graph-phishing-detection
---

# Contrastive Multi-View Representation Learning on Graphs

## Metadane
- **Autorzy**: Kaveh Hassani, Amir Hosein Khasahmadi
- **Rok**: 2020
- **Źródło**: ICML 2020 (Proceedings of the 37th International Conference on Machine Learning)
- **DOI/Link**: arXiv:2006.05582 — https://arxiv.org/abs/2006.05582
- **Status**: read
- **Kategoria główna**: Machine Learning

## Streszczenie
Praca wprowadza metodę samonadzorowanego (self-supervised) uczenia reprezentacji grafów opartą o uczenie kontrastywne między wieloma widokami struktury grafu. Zamiast polegać na etykietach, model maksymalizuje wzajemną informację (mutual information) między reprezentacjami uzyskanymi z różnych widoków tego samego grafu — najczęściej widoku oryginalnej macierzy sąsiedztwa oraz widoku uzyskanego przez dyfuzję grafu (graph diffusion, np. Personalized PageRank lub jądro ciepła). Kontrast prowadzony jest między reprezentacjami węzłów jednego widoku a reprezentacją całego grafu (graph-level) drugiego widoku.

Autorzy pokazują, że — wbrew intuicji z obrazów — zwiększanie liczby widoków powyżej dwóch nie poprawia wyników, a kluczowe okazuje się kontrastowanie reprezentacji na poziomie węzła z reprezentacją na poziomie grafu. Metoda nie wymaga skomplikowanych regularizacji ani próbkowania negatywnych przykładów na dużą skalę i osiąga stan techniki (state of the art) w klasyfikacji węzłów oraz klasyfikacji grafów na wielu benchmarkach.

## Kluczowe Wnioski
- Kontrast między widokami strukturalnymi (sąsiedztwo vs. dyfuzja) daje silne reprezentacje bez etykiet.
- Najskuteczniejszy jest kontrast lokalny (węzeł) względem globalnego (cały graf), nie węzeł-węzeł.
- Więcej niż dwa widoki nie poprawia jakości reprezentacji.
- Metoda przewyższa wcześniejsze podejścia samonadzorowane oraz część metod nadzorowanych.

## Metodologia
Architektura wykorzystuje dwa kodery GNN, po jednym dla każdego widoku, funkcję odczytu (readout) do reprezentacji grafu oraz dyskryminator szacujący wzajemną informację (oparty o Deep InfoMax / Jensen-Shannon). Trening jest kontrastywny: pary pozytywne pochodzą z tego samego grafu, negatywne z innych grafów lub przetasowanych cech. Ewaluacja liniowa (linear probing) i fine-tuning na klasyfikacji węzłów i grafów.

## Główne Koncepcje
- **Uczenie kontrastywne na grafach** — maksymalizacja MI między widokami.
- **Dyfuzja grafu** — alternatywny widok struktury (PPR, heat kernel).
- **Kontrast lokalny-globalny** — węzeł vs. reprezentacja grafu.
- **Self-supervised pretraining** GNN.

## Relevancja dla graph-phishing-detection
Detekcja phishingu na grafach często cierpi na niedobór wiarygodnych etykiet (mało potwierdzonych przypadków BEC/spear phishing). Samonadzorowane uczenie kontrastywne pozwala wstępnie wytrenować enkodery GNN na grafach komunikacji/domen/transakcji bez etykiet, a następnie dostroić je na nielicznych etykietach. Idea dwóch widoków (sąsiedztwo vs. dyfuzja) jest naturalna dla grafów wiedzy domenowej, gdzie dyfuzja modeluje pośrednie relacje zaufania. Kontrast lokalny-globalny może wzmocnić wykrywanie anomalnych węzłów odbiegających od kontekstu grafu — przydatne przy wykrywaniu nadawców impersonujących markę lub nietypowych ścieżek komunikacji.
