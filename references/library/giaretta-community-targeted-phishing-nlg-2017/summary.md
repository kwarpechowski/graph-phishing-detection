---
title: "Community Targeted Phishing: A Middle Ground Between Massive and Spear Phishing through Natural Language Generation"
date: 2017-01-01
authors: "Alberto Giaretta, Nicola Dragoni"
status: read
doi: "10.1007/978-3-030-14687-0_8"
category: "Security"
tags:
  - phishing
  - natural-language-generation
  - social-engineering
  - spear-phishing
  - email-security
  - personalization
  - threat-modeling
  - project/personalized-phishing-defense
---

# Community Targeted Phishing: A Middle Ground Between Massive and Spear Phishing through Natural Language Generation

## Metadane

- **Autorzy**: Alberto Giaretta (Centre for Applied Autonomous Sensor Systems, Örebro University, Szwecja), Nicola Dragoni (Örebro University / DTU Compute, Technical University of Denmark, Dania)
- **Rok**: 2017 (arXiv v1: 2017; v2: 23 czerwca 2018)
- **Źródło**: arXiv:1708.07342 [cs.CR]; opublikowane w materiałach konferencyjnych (Springer, seria LNCS)
- **DOI**: `10.1007/978-3-030-14687-0_8`
- **Status**: `#read`
- **Kategoria główna**: Security
- **Podkategorie**: Phishing, Social Engineering, Natural Language Generation
- **Tagi**: `#phishing` `#natural-language-generation` `#social-engineering` `#spear-phishing` `#email-security` `#personalization` `#threat-modeling` `#project:personalized-phishing-defense`

## Streszczenie

Artykuł jest pracą wizjonersko-koncepcyjną (position paper), która identyfikuje dwa diametralnie przeciwstawne podejścia we współczesnym phishingu: **phishing masowy** (massive/global), kierowany do jak największej liczby odbiorców przy użyciu generycznych, preformowanych tekstów i minimalnego wysiłku, oraz **spear phishing**, wymierzony w wartościowe cele za pomocą ręcznie tworzonych, dopracowanych wiadomości, które są kosztowne w produkcji i wymagają umiejętności inżynierii społecznej.

Autorzy wprowadzają nowe pojęcie pośrednie — **Community Targeted Phishing (CTP)** — jako "złoty środek" pomiędzy tymi dwoma biegunami. CTP zakłada podział populacji odbiorców na sensowne podgrupy (społeczności) o wspólnych zainteresowaniach i relacjach, a następnie atakowanie ich wiadomościami dopasowanymi maszynowo. Kluczową technologią umożliwiającą skalowanie takiej personalizacji jest **Natural Language Generation (NLG)** — generowanie tekstu w językach naturalnych, które pozwala automatycznie produkować dopasowane treści bez ręcznego wysiłku spear phishingu.

Praca przedstawia przegląd technik NLG (Canned Text, Template-Driven, Advanced NLG), studium przypadku ataku na społeczność naukową z dwoma konkretnymi szablonami e-maili oraz workflowami ich generowania, a także scenariusze zaawansowanego NLG, w których atakujący wydobywa "ukrytą" informację ze złożonych źródeł danych (np. Google Scholar, profile w sieciach społecznościowych) i wykorzystuje ją do uwiarygodnienia ataku. Autorzy podkreślają, że CTP może osłabić skuteczność bayesowskich filtrów antyspamowych, które zależą od masowości i powtarzalności phishingu.

## Kluczowe Wnioski

- **CTP jako poziom pośredni personalizacji**: phishing tworzy continuum wzdłuż osi stopnia personalizacji — od masowego (zero personalizacji), przez CTP (personalizacja na poziomie społeczności/grupy), aż po spear phishing (personalizacja na poziomie pojedynczego, wysokowartościowego celu). CTP zapełnia lukę między tanim-nieskutecznym a kosztownym-skutecznym.
- **NLG jako mechanizm skalowania personalizacji**: techniki generowania języka naturalnego pozwalają zautomatyzować tworzenie dopasowanych wiadomości, co przenosi "rzemieślniczą" jakość spear phishingu do skali produkcji masowej przy niższym koszcie.
- **Podział populacji osłabia filtry antyspamowe**: bayesowskie filtry korzystają ze statystycznej masowości i powtarzalności phishingu; mądry podział "blobu" użytkowników na podzbiory pozbawia filtry danych statystycznych potrzebnych do treningu i detekcji.
- **Społeczność naukowa jako podatny cel**: badacze dzielą zainteresowania, znają wielu kolegów i rutynowo wymieniają e-maile (współprace, call for papers), a badacze spoza informatyki często mają niskie kompetencje w zakresie bezpieczeństwa — co czyni ich łatwym celem.
- **Advanced NLG wydobywa "zatopioną" informację**: zaawansowane NLG nie tylko tworzy tekst, lecz wydobywa nieoczywiste informacje (np. trend h-index w ostatnich 5 latach, pozycja względem kolegów w danym polu) i wplata je w wiadomość, co radykalnie zwiększa wiarygodność.
- **Praca prognostyczna/ostrzegawcza**: autorzy nie implementują systemu, lecz przewidują przyszłe zagrożenie i wzywają do podniesienia świadomości oraz dalszych badań nad obroną.

## Metodologia

Praca ma charakter **koncepcyjny i prognostyczny (position / vision paper)**, nie zaś empiryczny — nie zawiera eksperymentów ani ewaluacji ilościowej. Metodologia obejmuje:

1. **Analizę taksonomiczną phishingu** — usytuowanie nowego pojęcia CTP na osi (Global → Targeted → Community) względem charakterystyk: popularność (popularity), wysiłek (effort) i skuteczność (efficacy), zilustrowane na schemacie (Rys. 1, wartości szacunkowe, nie statystyczne).
2. **Przegląd technik NLG** — omówienie trzech makrokategorii: Canned Text (tekst pregenerowany), Template-Driven / Template-Filling (szablony z lukami wypełnianymi danymi z zewnętrznego źródła) oraz Advanced / Proper NLG (pełny proces decyzyjny generowania tekstu).
3. **Studium przypadku (społeczność naukowa)** — projektowanie dwóch konkretnych szablonów e-maili phishingowych i opisanie workflowów generowania metodą Template-Driven NLG (parsowanie strony Google Scholar, wybór dziedziny i kolegów, odrzucenie współautorów, wypełnienie szablonu, dołączenie złośliwego linku/pliku, parsowanie adresów e-mail, wysyłka). Workflowy przedstawiono jako diagramy przepływu (Rys. 2 i 3).
4. **Scenariusze hipotetyczne dla Advanced NLG** — przykłady przekształcania heterogenicznych danych (h-index, zainteresowania w sieci społecznościowej) w naturalnie brzmiące, spersonalizowane wiadomości.

## Główne Koncepcje

- **Community Targeted Phishing (CTP)**: nowe, pośrednie podejście do phishingu, w którym atakujący dzieli populację na sensowne społeczności o wspólnych zainteresowaniach/relacjach i kieruje do nich wiadomości dopasowane maszynowo. Stanowi "middle ground" między phishingiem masowym a spear phishingiem — łączy skuteczność (effectiveness) i taniość (cheapness).
- **Oś stopnia personalizacji (Global → Targeted → Community)**: continuum phishingu według poziomu dopasowania treści: masowy (brak personalizacji, wysoka popularność, niski wysiłek), spear (maksymalna personalizacja pojedynczego celu, wysoki wysiłek), CTP (personalizacja na poziomie grupy).
- **Natural Language Generation (NLG)**: systemy generujące teksty w językach naturalnych; kluczowy enabler skalowania spersonalizowanych e-maili phishingowych.
- **Canned Text**: najprostsze NLG — tekst pregenerowany (zwykle przez człowieka); "graniczny przypadek szablonu bez luk".
- **Template-Driven / Template-Filling NLG**: szablony z lukami wypełnianymi danymi z zewnętrznego źródła (np. bazy danych, Google Scholar).
- **Advanced (Proper) NLG**: pełnoprawne generowanie tekstu z dużą liczbą decyzji; zdolne do wydobycia i streszczenia "zatopionej" informacji ze złożonych zbiorów danych.
- **Bayesowskie filtrowanie antyspamowe**: technika obronna sprawdzająca słowa wiadomości względem tabeli typowej dla spamu; zależy od masowości i powtarzalności — i dlatego jest podatna na osłabienie przez CTP.

## Wyniki

Ponieważ jest to praca koncepcyjna, "wyniki" mają charakter jakościowy i prognostyczny:

- **Wprowadzenie i zdefiniowanie pojęcia CTP** jako trzeciego, pośredniego paradygmatu phishingu, uzupełniającego dychotomię massive/spear.
- **Dwa konkretne szablony e-maili** dla studium przypadku społeczności naukowej:
  - *Template 1* (luźna relacja): podszywanie się pod uznanego badacza proponującego współpracę nad cytowaną pracą, z linkiem do fałszywej strony logowania Google.
  - *Template 2* (bliska relacja): podszywanie się pod kolegę proszącego o przejrzenie załączonego "draftu" pracy.
- **Dwa workflowy Template-Driven NLG** (Rys. 2 i 3) ilustrujące automatyzację całego procesu od wyboru ofiary po wysyłkę.
- **Scenariusze Advanced NLG** pokazujące, jak dane z Google Scholar (trend h-index) lub z sieci społecznościowych (zainteresowania muzyczne) mogą zostać przekształcone w wysoce wiarygodne, spersonalizowane wiadomości (np. fałszywa oferta pracy w laboratorium).
- **Teza obronna**: CTP może podważyć skuteczność bayesowskich filtrów antyspamowych poprzez eliminację masowości i powtarzalności, na których te filtry bazują.
- **Kierunki dalszych badań** zadeklarowane przez autorów: porównanie różnych technik NLG pod kątem wiarygodności i skuteczności, badanie zmienności tekstu w Advanced NLG oraz ewaluacja odporności filtrów bayesowskich na takie teksty.

## Przydatne Cytaty

- "We envision a future where Natural Language Generation (NLG) techniques will enable attackers to target populous communities with machine-tailored emails. In this paper, we introduce what we call Community Targeted Phishing (CTP)." (Abstract, s. 1)
- "Although they have the same goal, until today these two worlds have been somehow distinct from each other: massive production on one side, craftsmanship on the other one. We envision a future where a middle ground will be prominent." (s. 1-2)
- "What massive phishing lacks is a deeper comprehension about recipients relationships [...]. Yet, dividing users in meaningful subsets could help phishers to impersonate some group members, and attack the others, in a much more effective way." (Sekcja 3, s. 4)
- "Such filters require training and leverage the strong points of phishing, which are massiveness and repetitiveness, to get statistically meaningful data. If phishers could smartly divide this huge user blob in smart subsets, they could forge more complex emails and deprive Bayesian spam filters of the aforementioned vital statistical data." (Sekcja 3, s. 4)
- "Through Advanced NLG techniques attackers do much more than creating automatic text: they pinpoint submerged information which would take a huge effort to manually discover." (Sekcja 4, s. 7)
- "We believe that using a NLG approach to target people with similar interests could be worthwhile, since it would allow to create emails more effective than the general ones, and cheaper than the spear phishing ones." (Sekcja 5, s. 7-8)

## Datasety

Praca ma charakter koncepcyjny i **nie wykorzystuje ani nie wprowadza żadnych formalnych datasetów**. Jako potencjalne źródła danych dla atakującego autorzy wskazują publicznie dostępne profile (np. **Google Scholar** — strony badaczy, trend h-index, współautorzy, dziedziny) oraz profile w sieciach społecznościowych, lecz nie są to ustrukturyzowane zbiory badawcze.

## Powiązane Tematy

- Stopień personalizacji jako oś projektowa w obronie przed phishingiem (mass → community → spear)
- Generatywne ataki phishingowe oparte na LLM/NLG (rozwinięcie tej wizji w erze dużych modeli językowych)
- Personalized phishing defense — detekcja wiadomości dopasowanych do społeczności/zainteresowań
- Odporność bayesowskich i ML-owych filtrów antyspamowych na ataki niskoobjętościowe (low-volume / targeted)
- Adversarial machine learning i zatruwanie filtrów antyspamowych (poisoning)
- OSINT i profilowanie ofiar (Google Scholar, sieci społecznościowe) jako faza rekonesansu w phishingu
- Email masquerade attacks z wykorzystaniem NLG (Baki et al., ASIA CCS 2017 — bezpośredni punkt odniesienia)
- Wykrywanie e-maili phishingowych metodami NLP (Verma et al.) jako strona obronna względem NLG
- Inżynieria społeczna wymierzona w społeczność naukową (shady conferences, predatory journals, impersonacja badaczy)

## Notatki
