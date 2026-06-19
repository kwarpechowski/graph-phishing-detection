---
title: "Evaluation of Federated Learning in Phishing Email Detection"
date: 2020-01-01
authors: "Chandra Thapa, Jun Wen Tang, Alsharif Abuadbba, Yansong Gao, Seyit Camtepe, Surya Nepal, Mahathir Almashor, Yifeng Zheng"
status: read
doi: "arxiv:2007.13300"
category: "Security"
tags:
  - federated-learning
  - phishing-detection
  - privacy
  - bert
  - rnn
  - email-security
  - deep-learning
  - gdpr
  - distributed-learning
  - project/personalized-phishing-defense
---

# Evaluation of Federated Learning in Phishing Email Detection

## Metadane

- **Autorzy**: Chandra Thapa, Jun Wen Tang, Alsharif Abuadbba, Yansong Gao, Seyit Camtepe, Surya Nepal, Mahathir Almashor, Yifeng Zheng (Data61 CSIRO, Cyber Security Cooperative Research Centre, Australia)
- **Rok**: 2020 (wersja v3: maj 2021)
- **Źródło**: arXiv preprint, arXiv:2007.13300v3 [cs.LG]
- **DOI**: `arxiv:2007.13300`
- **Status**: `#read`
- **Kategoria główna**: Security
- **Podkategorie**: Privacy-Preserving Machine Learning, Phishing Detection, Federated Learning
- **Tagi**: `#federated-learning` `#phishing-detection` `#privacy` `#bert` `#rnn` `#email-security` `#deep-learning` `#gdpr` `#distributed-learning` `#project:personalized-phishing-defense`

## Streszczenie

Praca jest — według deklaracji autorów — pierwszym badaniem zastosowania uczenia federacyjnego (Federated Learning, FL) do detekcji phishingu w wiadomościach e-mail. Punktem wyjścia jest obserwacja, że skuteczne modele AI do wykrywania phishingu wymagają dużych, scentralizowanych zbiorów danych, a centralizacja e-maili jest problematyczna z powodu wrażliwości danych, ryzyka wycieku informacji handlowych oraz ograniczeń prawnych (GDPR, HIPAA). Organizacje niechętnie udostępniają korespondencję, a anonimizacja e-maili jest zawodna (re-identyfikacja przez np. grafy społecznościowe). FL pozwala wspólnie trenować model głębokiego uczenia bez udostępniania surowych danych — każdy klient (organizacja) trenuje model lokalnie, a serwer agreguje jedynie parametry modeli (FedAvg).

Autorzy budują na dwóch najlepszych scentralizowanych modelach: THEMIS (Recurrent Convolutional Neural Network / RCNN, modelujący e-mail wielopoziomowo — char-level i word-level nagłówka oraz treści, z mechanizmem uwagi) oraz BERT (bert-base-uncased, 110 mln parametrów, fine-tuning, tylko treść e-maila). Wariant THEMISb używa wyłącznie treści e-maila (bez nagłówka). Eksperymenty przeprowadzono na zbiorze 23 916 e-maili z pięciu źródeł (IWSPA-AP, Nazario, Enron, CSIRO, Phishbowl), analizując FL pod kątem sześciu pytań badawczych (RQ1–RQ6) obejmujących: porównywalność z uczeniem scentralizowanym (CL), skalowalność (liczba klientów), narzut komunikacyjny, korzyści na poziomie pojedynczego klienta oraz odporność na asymetryczny i ekstremalnie zróżnicowany rozkład danych.

Główny wniosek: FL osiąga wydajność porównywalną z uczeniem scentralizowanym przy zrównoważonym rozkładzie danych i niewielkiej liczbie organizacji, zapewniając jednocześnie ochronę prywatności jako kompromis za niewielki spadek dokładności. Zachowanie modelu przy wzroście liczby klientów oraz przy ekstremalnej asymetrii danych jest zależne od modelu (THEMIS vs BERT).

## Kluczowe Wnioski

- **FL jest wykonalne dla detekcji phishingu e-mail** i osiąga wydajność porównywalną z uczeniem scentralizowanym (CL) przy zrównoważonym rozkładzie danych i małej liczbie klientów — kosztem niewielkiego spadku dokładności w zamian za ochronę prywatności.
- **Prywatność by-design**: surowe e-maile nigdy nie opuszczają organizacji; przesyłane są wyłącznie parametry modeli. To rozwiązuje problem braku możliwości centralizacji danych per-organizacja / per-użytkownik (GDPR, HIPAA, dane wrażliwe).
- **Wpływ liczby klientów jest zależny od modelu**: przy stałym całkowitym zbiorze danych globalny model RNN (THEMIS) traci ~1.8% dokładności przy wzroście z 2 do 10 organizacji, podczas gdy BERT zyskuje 0.6% przy wzroście z 2 do 5 organizacji.
- **Nagłówek e-maila jest krytyczny dla THEMIS**: pełny THEMIS (nagłówek + treść) osiąga 99.301% dokładności w CL, a THEMISb (sama treść) tylko 95.085% — spadek o ~4%.
- **Korzyść na poziomie klienta**: dołączenie nowej organizacji powiększającej łączny zbiór danych poprawia wydajność i przyspiesza zbieżność (np. wzrost globalnej dokładności o ~2.98% dla nowego klienta przy var=80; skok ~4.9% przy dołączeniu drugiego klienta).
- **Odporność na asymetrię rozmiaru**: dzięki ważonemu uśrednianiu (FedAvg) FL jest odporne na różnice w rozmiarach lokalnych zbiorów (utrzymuje ~97% dokładności przy var od 0% do 80%).
- **Ekstremalna asymetria (różne źródła jako różni klienci) jest problematyczna**: modele wykazują silne fluktuacje; BERT jest stabilniejszy niż THEMIS/THEMISb dla klientów z małą liczbą próbek.
- **Narzut komunikacyjny zależy wyłącznie od rozmiaru modelu** (nie od liczby klientów ani epok): ~0.192 GB/epokę/klienta dla THEMIS, ~0.438 GB dla BERT — nieistotny dla zasobnych organizacji.

## Metodologia

- **Modele**: (1) THEMIS — RCNN z czterema Bi-LSTM, modelowanie char-/word-level nagłówka i treści, mechanizm uwagi łączący reprezentacje; (2) THEMISb — wariant THEMIS używający tylko treści; (3) BERT (bert-base-uncased, 12 warstw, 768 hidden, 12 głów uwagi, 110 mln parametrów) z fine-tuningiem, wejście tylko treść (limit 512 tokenów).
- **Architektura FL**: algorytm FedAvg (Algorithm 1) — serwer inicjalizuje i rozsyła model globalny; każdy klient k trenuje lokalnie na D_k, odsyła W_k; serwer wykonuje ważone uśrednianie (W_{t+1} = Σ (n_k/n) W_k) i synchronizuje model. Jedna runda = jedna epoka globalna.
- **Pytania badawcze**: RQ1 (porównanie FL vs CL, rozkład zrównoważony), RQ2 (skalowalność / liczba klientów), RQ3 (narzut komunikacyjny), RQ4 (korzyści na poziomie klienta), RQ5 (asymetria rozmiaru i ratio P/L), RQ6 (ekstremalna różnorodność danych).
- **Przygotowanie danych**: ekstrakcja nagłówka (pola Subject, Content-Type) i treści (email.header, RE), czyszczenie (BeautifulSoup4, HTML parser, usuwanie stop-words nltk). Tokenizacja: Keras Tokenizer dla THEMIS (długości sekwencji 50/100/150/300 dla word-header/char-header/word-body/char-body); BertTokenizer (z [CLS]/[SEP]) dla BERT. Podział train/test 80:20.
- **Scenariusze rozkładu**: zrównoważony (var=0), asymetria rozmiaru (var = 10/20/50/80%), asymetria ratio phishing/legit (10:90, 30:70, 50:50, 70:30), oraz ekstremalna różnorodność (każde z 5 źródeł jako osobny klient).
- **Środowisko**: HPC Dell EMC PowerEdge, GPU Tesla P100-SXM2-16GB, Python 3.6.1, TensorFlow 2.2.5 + Keras 2.2.5 (THEMIS), Huggingface transformers (BERT). Seed=123. Hiperparametry: THEMIS lr=0.0001, batch=256; BERT lr=0.00001, batch=4.

## Główne Koncepcje

- **Federated Learning (FL)**: rozproszone, prywatność-zachowujące uczenie, w którym wiele klientów trenuje wspólny model bez wymiany surowych danych — przesyłane są tylko parametry modeli.
- **FedAvg (Federated Averaging)**: algorytm agregacji modeli przez ważone uśrednianie parametrów lokalnych proporcjonalnie do rozmiaru lokalnego zbioru (n_k/n).
- **Centralized Learning (CL)**: uczenie na zagregowanym, centralnym zbiorze danych — punkt odniesienia (baseline); nieodpowiednie dla danych wrażliwych jak e-maile.
- **THEMIS / THEMISb**: najlepszy scentralizowany model RCNN dla detekcji phishingu e-mail; THEMIS używa nagłówka + treści, THEMISb tylko treści.
- **Global epoch**: jedna pełna runda FL (lokalny trening → upload → agregacja → broadcast).
- **var**: parametr asymetrii — maksymalny procent wariacji rozmiaru lokalnych zbiorów między klientami (np. var=10% → [-10%,-5%,0%,+5%,+10%]).
- **Ratio P/L**: stosunek liczby e-maili phishingowych do legalnych w lokalnym zbiorze klienta.
- **Personalizacja modelu**: lokalny model dobrze dopasowuje się do niektórych klientów, ale nie do wszystkich; przy dużej liczbie klientów efekt pogarsza globalny model.

## Wyniki

**RQ1 — FL vs CL (rozkład zrównoważony, 5 klientów):**
- THEMIS @ epoka 45: CL = 99.301% dokładności (FPR 0.0035, FNR 0.0105); FL = 97.9% globalnej dokładności.
- BERT @ epoka 15: CL = 96.183% (FPR 0.0091, FNR 0.0576); FL = 96.11% globalnej dokładności.
- THEMISb (sama treść) w CL: tylko 95.085% (spadek ~4% względem pełnego THEMIS).
- Wniosek: FL osiąga porównywalną wydajność z CL, lecz nie dorównuje mu w pełni (kompromis za prywatność).

**RQ2 — wpływ liczby klientów (stały całkowity zbiór, delty dokładności):**
- **THEMIS (RNN)**: globalna dokładność @ epoka 45 spada o **1.8%** przy przejściu z 2 do 10 klientów (~0.5% spadku z 2 do 5 klientów).
- **THEMISb**: spadek ~**6%** z 2 do 10 klientów (znacznie większy niż THEMIS).
- **BERT**: dokładność **rośnie o 0.6%** przy przejściu z 2 do 5 klientów (@ epoka 15); spadek względem CL przy 2 klientach to tylko ~0.6% — BERT nie degraduje się ze wzrostem liczby klientów.
- Wniosek: zbieżność i wydajność przy wzroście liczby klientów są zależne od modelu — THEMIS degraduje, BERT przeciwnie.

**RQ3 — narzut komunikacyjny:** stały, zależny tylko od rozmiaru modelu: ~0.192 GB/epokę globalną/klienta (THEMIS), ~0.438 GB (BERT); niezależny od liczby klientów i epok. CL = 0.

**RQ4 — korzyści na poziomie klienta (THEMIS):**
- Eksp. 1 (5 klientów, klient 5 dołącza po 15 epokach, var=80): globalna dokładność klienta 5 rośnie o **2.98%** (FPR -3.5%, FNR -2.2%); dla var=50/30/0 odpowiednio +2.91%/+2.87%/+2.24%.
- Eksp. 2 (klienci dodawani co 10 epok): globalna dokładność klienta 2 skacze o ~**4.9%** przy dołączeniu.
- Eksp. 3: klient 1 osiąga szybszą i stabilniejszą zbieżność z FL niż z CL (finalnie ~98% w obu przypadkach @ epoka 50).
- Wniosek: FL przyspiesza zbieżność i poprawia wydajność na poziomie klienta.

**RQ5 — asymetria (5 klientów):**
- Różny rozmiar lokalny (var 0–80%): utrzymanie ~97% dokładności @ epoka 45 dla wszystkich var (odporność dzięki FedAvg).
- Różne ratio P/L (10:90, 30:70, 50:50, 70:30): po epoce 15 zbieżność do ~97% poza przypadkiem 30:70 (~93%). Globalna wydajność lekko spada ze wzrostem udziału phishingu (10%→70%).

**RQ6 — ekstremalna różnorodność (5 źródeł = 5 klientów):**
- THEMIS/THEMISb: klienci z małą liczbą najnowszych próbek (klient 4 CSIRO, klient 5 Phishbowl) wykazują wysokie fluktuacje; klient 3 (sam Nazario, dużo phishingu) — doskonały lokalnie (~99.99%), słaby globalnie.
- BERT: wszyscy klienci dobrze zbiegają w treningu i lokalnym teście (99.99%, klient 1 ~97%); globalny test wykazuje fluktuacje (klienci 1,2,4), ale BERT jest stabilniejszy niż THEMIS/THEMISb.
- Wniosek: zbudowanie jednego dobrze działającego modelu globalnego dla wszystkich klientów przy ekstremalnej asymetrii nie jest proste; wynik zależny od modelu.

## Przydatne Cytaty

- "To the best of our knowledge, the work herein is the first to investigate the use of FL in email anti-phishing." (s. 1, Abstract)
- "For a fixed total email dataset, the global RNN based model suffers by a 1.8% accuracy drop when increasing organizational counts from 2 to 10. In contrast, BERT accuracy rises by 0.6% when going from 2 to 5 organizations." (s. 1, Abstract)
- "Even with the users' permission to use their data for agreed tasks (e.g., DL), handling the email data under a centralized cloud is still risky under the set of privacy regulations." (s. 1, Introduction)
- "It trains a joint DL model by harvesting the rich distributed data held by each client in a default privacy mode. The privacy of the raw data is enabled by two means; firstly, data never shared with other clients/participants. Secondly, data is always within the control of data custodians." (s. 1–2)
- "FL is feasible with comparable performance to the CL for phishing email detection. It enables privacy benefits to the system, but it could not achieve the CL performance as a trade-off in our experiments." (s. 6, Summary RQ1)
- "The convergence and performance with the increase in the number of clients in FL are model-dependent." (s. 7, Summary RQ2)
- "FL is a privacy-by-design approach, however, FL alone can not guarantee data privacy." (s. 12, sekcja 6.3)
- "Under extreme dataset diversity among clients, models suffer high fluctuation in their performances. However, BERT produces relatively stable results even for clients with few samples." (s. 11–12, Summary RQ6)

## Datasety

- [IWSPA-AP](../../../datasets/iwspa-ap.md) — First Security and Privacy Analytics Anti-Phishing Shared Task; 1132 phishing + 9174 legit (10306). E-maile z nagłówkiem i bez.
- [Nazario Phishing Corpus](../../../datasets/nazario-phishing-corpus.md) — 8890 e-maili phishingowych (z nagłówkiem + treść).
- [Enron Email Dataset](../../../datasets/enron-email-dataset.md) — 4279 e-maili legalnych (z nagłówkiem + treść).
- [CSIRO Phishing Emails](../../../datasets/csiro-phishing-emails.md) — 309 e-maili phishingowych zgłoszonych przez personel CSIRO (2017–2020), tylko treść (prywatny zbiór).
- [Cornell Phishbowl](../../../datasets/cornell-phishbowl.md) — 132 e-maile phishingowe zgłoszone (kwiecień 2019 – styczeń 2021), tylko treść.

Łącznie: 23 916 próbek (10 463 phishing + 13 453 legit). Dla RQ1–RQ5 użyto IWSPA-AP, Nazario, Enron (23 475 próbek); CSIRO i Phishbowl zarezerwowane dla RQ6 (ekstremalna różnorodność).

## Powiązane Tematy

- Personalizowane / per-użytkownik modele detekcji phishingu w warunkach niemożności centralizacji danych (GDPR)
- Privacy-preserving machine learning: differential privacy, homomorphic encryption (jako uzupełnienie FL)
- Bezpieczeństwo FL: ataki inferencyjne (privacy leakage), backdoor / data poisoning, parameter tampering
- Alternatywne algorytmy agregacji: FedCurv, FedProx, matched averaging (zamiast FedAvg)
- Model-agnostic meta-learning (MAML) dla łagodzenia efektu personalizacji w FL
- Cryptographic deep learning training (SecureML, SecureNN, ABY3) jako alternatywne podejście privacy-preserving
- Detekcja spear phishingu i business email compromise (BEC) w kontekście rozproszonym
- THEMIS / RCNN i BERT/CatBERT/DistilBERT jako bazowe modele detekcji phishingu

## Notatki
