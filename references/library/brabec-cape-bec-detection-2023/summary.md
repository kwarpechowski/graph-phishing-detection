---
title: "A Modular and Adaptive System for Business Email Compromise Detection"
date: 2023-01-01
authors: "Jan Brabec, Filip Srajer, Radek Starosta, Tomas Sixta, Marc Dupont, Milos Lenoch, Jiri Mensik, Florian Becker, Jakub Boros, Tomas Pop, Pavel Novak"
status: read
doi: "arxiv:2308.10776"
category: "Security"
tags:
  - business-email-compromise
  - spear-phishing
  - phishing-detection
  - transformer
  - explainable-ai
  - communication-context
  - project/personalized-phishing-defense
---

# A Modular and Adaptive System for Business Email Compromise Detection

## Metadane

- **Autorzy:** Jan Brabec, Filip Srajer, Radek Starosta, Tomas Sixta, Marc Dupont, Milos Lenoch, Jiri Mensik, Florian Becker, Jakub Boros, Tomas Pop, Pavel Novak (Cisco Systems; Czeski Uniwersytet Techniczny w Pradze; Uniwersytet Karola)
- **Rok:** 2023
- **Zrodlo:** arXiv preprint (arXiv:2308.10776v1 [cs.CR], 21 Aug 2023)
- **DOI/ID:** `arxiv:2308.10776`
- **Status:** `#read`
- **Kategoria glowna:** `#Security`
- **Podkategorie:** detekcja BEC, spear phishing, email security, explainable AI, NLU
- **Tagi:** `#business-email-compromise` `#spear-phishing` `#phishing-detection` `#transformer` `#explainable-ai` `#communication-context` `#bayesian` `#logistic-regression` `#production-system` `#project:personalized-phishing-defense`

## Streszczenie

Artykul opisuje CAPE -- modularny, produkcyjny system do wykrywania atakow typu Business Email Compromise (BEC) i zaawansowanego spear phishingu, sprawdzony w srodowisku produkcyjnym przez ponad dwa lata jako czesc komercyjnego produktu Cisco do ochrony poczty. Tradycyjne techniki (filtry Bayesa dla spamu, uslugi reputacyjne) nie radza sobie z BEC, poniewaz wspolczesne ataki sa silnie spersonalizowane, wystepuja w niskich wolumenach i wtapiaja sie w ruch benign. Autorzy argumentuja, ze w praktycznym systemie -- ze wzgledu na ograniczenia danych, koszty operacyjne, wymog wyjasnialnosci werdyktow i potrzebe ciaglej ewolucji -- konieczne jest laczenie wielu podejsc, a nie poleganie na pojedynczym modelu end-to-end.

Kluczowa idea CAPE polega na tym, ze nie jest to pojedynczy model, lecz system laczacy niezalezne modele ML i algorytmy wykrywajace zachowania zwiazane z BEC w roznych modalnosciach e-maila: tekscie, obrazach, metadanych oraz -- co szczegolnie wazne -- w kontekscie komunikacji (tozsamosci i relacje miedzy nadawca a odbiorca). Ta dekompozycja na niezalezne detektory czyni werdykty naturalnie wyjasnialnymi: zamiast binarnej decyzji system pokazuje zbior zachowan, ktore czynia e-mail podejrzanym, i podswietla je w interfejsie dla analitykow SOC.

System adresuje problem zimnego startu (cold start) wynikajacy z braku reprezentatywnych, etykietowanych danych (zwlaszcza klasy benign) oraz skrajnej nierownowagi klas (prawdziwa prewalencja BEC szacowana na 10^-4 do 10^-5). Rozwiazaniem jest podejscie bayesowskie laczace ograniczone dane zwrotne z wiedza dziedzinowa wstrzykiwana poprzez rozklad a priori. CAPE jest ciagle aktualizowany w sposob iteracyjny, a jego skutecznosc monitorowana jest w produkcji (precyzja utrzymywana powyzej 80% przez ponad dwa lata).

## Kluczowe Wnioski

- **BEC wymaga kontekstu komunikacji** -- wiele atakow BEC (np. krotka prosba "od CEO" bez tresci szkodliwej) jest niemozliwych do wykrycia na podstawie samej tresci e-maila; konieczna jest informacja o historii komunikacji i tozsamosci stron (tzw. *email context*).
- **Modularnosc daje wyjasnialnosc** -- rozbicie na niezalezne detektory zachowan zamiast monolitycznego modelu czyni werdykty interpretowalnymi i ulatwia rownolegly rozwoj oraz utrzymanie.
- **Laczenie ML z wiedza dziedzinowa jest niezbedne** -- z powodu braku reprezentatywnych danych model uczony wylacznie z danych uczylby sie skrotow (shortcut learning) i generowal nadmierne false positives w produkcji.
- **Precyzja jako twarde ograniczenie** -- ze wzgledu na skrajna nierownowage klas system musi miec ekstremalnie niski FPR; precyzja jest utrzymywana jako stala, a recall (mierzony posrednio jako conviction-rate) zwiekszany w czasie.
- **Slabe sygnaly lacza sie w werdykt** -- pojedyncze detekcje (np. pilnosc, call-to-action) wystepuja czesto w ruchu benign; dopiero ich kombinacja w warstwie klasyfikacji daje konwikcje.
- **Bayesowska aktualizacja zapewnia stabilnosc** -- kolejne modele maja wagi bliskie poprzednim (analogia do konserwatywnego learning rate), co zapobiega gwaltownym, nieprzewidzianym zmianom skutecznosci.
- **Generatywne LLM (GPT-4) offline do etykietowania** -- generatywne modele sluza do automatycznego etykietowania danych treningowych offline, z ktorych trenuje sie tansze klasyfikatory do produkcji.
- **Brak publicznego benchmarku** -- przyznane ograniczenie: nie istnieje publiczny dataset z reprezentatywna proba BEC i pelna zlozonoscia ruchu benign, wiec ewaluacja opiera sie na danych produkcyjnych.

## Metodologia

System ma dwuwarstwowa architekture tworzaca *classification pipeline* f: E x C -> Y, gdzie e to e-mail, c to jego kontekst z komponentu Mail Graph, a y to werdykt:

1. **Warstwa detekcji** (g: E x C -> D) -- modularny zbior ponad 90 niezaleznych detektorow, kazdy zwraca detekcje ze score d_s w [0,1] i metadane. Detektory targetuja rozne modalnosci (tekst, obrazy z OCR, metadane, kontekst). Czesc detektorow wykrywa sygnaly benign i moze zatrzymac dalsza analize (oszczednosc zasobow). Detektory dokumentowane sa za pomoca *model cards*.
2. **Warstwa klasyfikacji** (h: D -> Y) -- pojedynczy model **regresji logistycznej** h(d; w, t) = [logistic(w^T d) >= t], wybrany zamiast drzew decyzyjnych ze wzgledu na gladkosc funkcji (zgodnosc z paradygmatem bayesowskim) i latwosc interpretacji (kazdy typ detekcji ma jedna wage skalarna). Warstwa moze potencjalnie laczyc wiele klasyfikatorow przez h(d) = max_i h_i(d).

**Aktualizacja bayesowska:** model regresji logistycznej aktualizowany jest iteracyjnie. Prior normalny N(w_b, Sigma) wokol wag modelu bazowego w_b pozwala wstrzyknac wiedze dziedzinowa; macierz kowariancji Sigma (diagonalna) kontroluje kompromis miedzy bliskoscia do modelu bazowego a dopasowaniem do danych. Posterior p(w|D) ~ p(D|w)*p(w) z likelihood Bernoulliego. Estymacja przez MCMC lub gradient descent z uzyciem pakietu Turing.jl (Julia).

**Mail Graph** -- komponent modelujacy tozsamosci i relacje nadawcow/odbiorcow na trzech poziomach (globalnym, firmowym/klienta, uzytkownika), z dostepem odczytu o latencji jednocyfrowych milisekund; aktualizowany asynchronicznie przez batching i agregacje.

**Ograniczenia projektowe:** wrazliwosc danych (scisle polityki prywatnosci, brak dostepu do typowego ruchu benign), skrajna nierownowaga klas, koszty operacyjne (sredni e-mail 300 KB; pipeline przetwarza latwe e-maile szybko -- 50% w 50 ms, 75% ponizej 100 ms, 99% ponizej 1 s), latencja (maks. kilka sekund na e-mail).

**Ewaluacja skutecznosci:** ciagly monitoring precyzji, conviction-rate, rates false positives/negatives ze sprzezenia od klientow; rotacyjny dyzur zespolu (1 osoba etykietuje 10-50 losowych konwikcji dziennie) dla nieobciazonej estymacji precyzji; pomiar wplywu detektorow przez *relative impact* (ile konwikcji znika bez detektora) i srednie *wartosci Shapleya*.

## Glowne Koncepcje

- **Business Email Compromise (BEC)** -- atak socjotechniczny celujacy w organizacje przez e-mail, czesto reczne i ukierunkowane (blizej spear phishingu niz klasycznego phishingu). Wedlug FBI obejmuje: eksploatacje relacji miedzy organizacjami, CEO-fraud, prosbe o platnosc z przejetego konta, podszywanie sie pod prawnika, kradziez danych przez podszywanie sie pod kierownictwo.
- **Email context (kontekst e-maila)** -- zbior informacji uzytecznych do klasyfikacji, ale nieobecnych w samym e-mailu (np. czy istniala wczesniejsza komunikacja, tozsamosc odbiorcy). Kluczowy do wykrycia wyrafinowanych BEC.
- **Weak signal / strong signal** -- slaby sygnal (np. pilnosc, call-to-action) nie wskazuje BEC sam w sobie, tylko w kombinacji; silny sygnal jest bardziej wskazujacy, ale moze wystepowac legalnie.
- **Cold start problem** -- brak wystarczajacych danych i etykiet na poczatku do trenowania modelu wysokopoziomowego; rozwiazany przez laczenie wiedzy dziedzinowej z ML i iteracyjne dostrajanie na danych produkcyjnych.
- **Shortcut learning** -- uczenie sie skrotow nieuogolniajacych sie na dane produkcyjne, zagrozenie przy modelach end-to-end na niereprezentatywnych danych.
- **Conviction-rate** -- (TP+FP)/(TP+FP+TN+FN), proxy dla recall przy ustalonej precyzji (recall niemierzalny bezposrednio, bo liczba false-negatives nieznana).
- **Detektory wybrane:** Call-to-action / urgency (modele Transformer fine-tunowane, z lekkim pre-filtrem student-teacher odsiewajacym ~75% segmentow), Email Address Masquerade (falszywy adres w display name), Unicode Masquerade (homoglify, zero-width spaces, soft hyphen U+00AD), Communication Frequency (rzadka vs czesta komunikacja z Mail Graph).
- **Relative impact / wartosci Shapleya** -- dwie metryki kwantyfikujace wklad pojedynczego detektora do konwikcji.

## Wyniki

- **CAPE w produkcji ponad 2 lata** -- system wdrozony jako czesc komercyjnego produktu email security Cisco, chroniacy duzy wolumen skrzynek w wielu organizacjach.
- **Precyzja > 80% utrzymywana przez ponad 2 lata** (Rysunek 5) -- po poczatkowej fazie "silent mode" (konwikcje bez efektu) precyzja ustabilizowala sie powyzej 80%; pojedynczy spadek wykryto i szybko naprawiono dzieki procesowi rotacyjnej ewaluacji.
- **Ponad 90 detektorow** dzialajacych rownolegle w warstwie detekcji.
- **Wydajnosc przetwarzania:** 50% e-maili w 50 ms, 75% ponizej 100 ms, 99% ponizej 1 s.
- **Pre-filtr call-to-action** odsiewa ok. 75% segmentow, redukujac koszt drogiego modelu Transformer.
- **Kompromis prior vs elastycznosc (Rysunek 4):** na probie 20 000 slabo-podejrzanych nieetykietowanych e-maili model elastyczny poprawil AUC o 0.153, ale jest nadmiernie pewny (overconfident) i niepraktyczny w produkcji; model z silnym priorem poprawil AUC tylko o 0.035, lecz zachowuje sie rozsadnie na danych produkcyjnych -- ilustracja kompromisu miedzy dopasowaniem a stabilnoscia.
- **Prewalencja BEC** szacowana na 10^-4 do 10^-5 (zgodnie z wczesniejsza praca Cidona i in.).

## Przydatne Cytaty

- "Rather than being a single model, CAPE is a system that combines independent ML models and algorithms detecting BEC-related behaviors across various email modalities such as text, images, metadata and the email's communication context. This decomposition makes CAPE's verdicts naturally explainable." (Abstract, s. 1)
- "the sample BEC attack at Figure 1 is almost non-identifiable as BEC without contextual information such as whether there exists a previous communication between the sender and recipient, the recipient's identity, etc. We call this set of information that is useful for classification but is not included in the email itself the email's context." (s. 3)
- "Not having research access to regular benign emails, which form the vast majority of the traffic, makes this task not suited for a fully end-to-end ML solution." (s. 4)
- "Precision acts as a constraint. Recall [...] is a measure that is being increased over time. In practice, it is impossible to measure recall because the number of false-negatives is unknown. As a proxy [...] we can measure and aim to increase conviction-rate [...] over time." (s. 5)
- "The prior distribution allows us to inject domain knowledge into the estimation process." (s. 10)
- "Compared to baseline model, the flexible model improved the area under ROC curve (AUC) by 0.153 [...] However, due to biases in D, the flexible model is overconfident and would convicts too many emails in production to be practical. The strong prior model [...] provides a modest improvement on D but behaves reasonably on production data." (Figure 4, s. 11)
- "This period was essential for stabilizing the precision above 80%, a level that has been consistently maintained over an extended period." (Figure 5, s. 12)

## Datasety

Praca celowo NIE polega na publicznych benchmarkach (autorzy wskazuja brak reprezentatywnego publicznego datasetu BEC z pelnym ruchem benign jako ograniczenie). Wymienione/uzyte zbiory pomocnicze:

- **Enron corpus** -- wykorzystany do trenowania detektora pilnosci (urgency) z danych publicznych.
- **SpamAssassin public corpus**, **TREC 2007 spam corpus**, **Nazario Phishing corpus** -- wspomniane jako publiczne korpusy, lecz uznane za stare/malo reprezentatywne dla wspolczesnego BEC.
- **PhishTank**, **OpenPhish** -- feedy IOC (URL, hashe), o ograniczonej przydatnosci dla BEC (ataki czesto nie zawieraja IOC).
- **Dane produkcyjne Cisco** -- glowne, niepubliczne zrodlo (np. proba 20 000 slabo-podejrzanych e-maili, feed sprzezenia od klientow).

## Powiazane Tematy

- Context-aware / per-user spersonalizowana detekcja phishingu i spear phishingu (kontekst komunikacji jako sygnal)
- Modele Transformer / LLM w detekcji socjotechniki w e-mailach (CATBERT, BERT, end-to-end vs feature-based)
- Wyjasnialna AI (explainable AI) w bezpieczenstwie: LIME, wartosci Shapleya, model cards
- Bayesowska regresja logistyczna i wstrzykiwanie wiedzy dziedzinowej przy ograniczonych danych
- Uczenie przy skrajnej nierownowadze klas i niereprezentatywnym samplingu (selection bias, ewaluacja przy non-constant class imbalance)
- Automatyczne etykietowanie danych treningowych przez generatywne LLM (distillation GPT-4 -> tanszy klasyfikator)
- Modelowanie grafu komunikacji (Mail Graph) jako kontekst tozsamosci i relacji
- Psychologia socjotechniki: zasady wplywu Cialdiniego (Authority, Scarcity) w phishingu/BEC
- Detekcja podszywania sie: homoglify, masquerade adresu nadawcy, Unicode evasion

## Notatki