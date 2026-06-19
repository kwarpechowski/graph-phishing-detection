---
title: "Image-Based Recommendations on Styles and Substitutes"
date: 2015-01-01
authors: "Julian McAuley, Christopher Targett, Qinfeng Shi, Anton van den Hengel"
status: read
doi: "10.1145/2766462.2767755"
category: "Machine Learning"
tags:
  - recommender-systems
  - graph-inference
  - network-of-products
  - large-scale-dataset
  - visual-features
  - project/graph-phishing-detection
---

# Image-Based Recommendations on Styles and Substitutes

## Metadane
- **Autorzy**: Julian McAuley, Christopher Targett, Qinfeng (Javen) Shi, Anton van den Hengel (UC San Diego, University of Adelaide)
- **Rok**: 2015
- **Źródło**: SIGIR '15
- **DOI/Link**: 10.1145/2766462.2767755
- **Status**: read
- **Kategoria główna**: Machine Learning (rekomendacje / sieci produktów)
- **Tagi**: `#recommender-systems` `#graph-inference` `#network-of-products` `#large-scale-dataset` `#visual-features`

## Streszczenie
Praca modeluje ludzkie pojęcie relacji między obiektami na podstawie ich wyglądu — rozróżniając obiekty będące **substytutami** (alternatywami, np. dwie pary dżinsów) od **komplementarnych** (pasujących do siebie, np. dżinsy i koszula). Zamiast drobnoziarnistego modelowania adnotacji użytkownika, autorzy stawiają na pozyskanie możliwie największego zbioru danych i skalowalną metodę odkrywania wizualnych relacji. Zadanie jest sformułowane jako **problem wnioskowania o sieci** (network inference) zdefiniowanej na grafach powiązanych obrazów.

Autorzy udostępniają duży zbiór z serwisu Amazon obejmujący ponad 180 mln relacji między blisko 6 mln obiektów (rekomendacje „kupowane/oglądane razem", „także oglądane"). Cechy wizualne wydobyte z obrazów produktów służą do uczenia metryki/odległości przewidującej, które przedmioty do siebie pasują, a które są wymienne. System rekomenduje pasujące ubrania i akcesoria oraz pomaga łagodzić problem zimnego startu (cold start), gdyż opiera się na wyglądzie, a nie wyłącznie na historii zakupów.

## Kluczowe Wnioski
- Relacje substytut vs. komplement między produktami można wnioskować z cech wizualnych.
- Sformułowanie jako wnioskowanie o grafie relacji skaluje się do ogromnych zbiorów.
- Duży, luźno powiązany zbiór danych przewyższa małe, ręcznie etykietowane korpusy.
- Podejście wizualne łagodzi problem zimnego startu w rekomendacjach.

## Metodologia
Konstrukcja grafu relacji między produktami z danych Amazon; ekstrakcja cech wizualnych z obrazów; uczenie parametryzowanej metryki/transformacji odróżniającej pary komplementarne od substytucyjnych; ewaluacja jako predykcja krawędzi w sieci produktów na zbiorze ponad 180 mln relacji.

## Główne Koncepcje
- **Substytuty vs. komplementy**: dwa typy relacji między obiektami.
- **Network inference**: predykcja krawędzi w grafie powiązanych obrazów.
- **Cechy wizualne**: reprezentacja produktu wydobyta z obrazu.
- **Cold start**: rekomendacja bez historii interakcji.

## Relevancja dla graph-phishing-detection
Mimo domeny e-commerce praca jest istotna metodologicznie: dostarcza wzorca **wnioskowania o relacjach w wielkoskalowym grafie obiektów** oraz źródło danych (Amazon co-purchase/review), często wykorzystywane jako benchmark dla metod osadzania grafów i klasyfikacji węzłów stosowanych następnie w detekcji nadużyć. Rozróżnienie typów relacji (komplement/substytut) jest analogią do wielowarstwowego/heterogenicznego modelowania krawędzi w grafie phishingu (różne semantyki połączeń: współdzielona infrastruktura, transakcje, komunikacja). Sformułowanie detekcji jako predykcji krawędzi i nacisk na skalowalność do milionów węzłów współgra z projektowym celem trenowania GNN na realistycznie dużych grafach z zachowaniem rygoru ewaluacji.
