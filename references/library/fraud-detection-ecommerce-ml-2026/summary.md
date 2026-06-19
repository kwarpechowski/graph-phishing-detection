---
title: "Fraud detection in e-commerce: a comparative analysis of features to enhance machine learning models"
date: 2026-01-01
authors: "Manuel Sánchez-Paniagua, Eduardo Fidalgo, Enrique Alegre, Francisco Jáñez-Martino"
status: read
category: "Machine Learning"
tags: []
---
# Fraud detection in e-commerce: a comparative analysis of features to enhance machine learning models

## Metadane
- **Autorzy**: Manuel Sánchez-Paniagua, Eduardo Fidalgo, Enrique Alegre, Francisco Jáñez-Martino
- **Rok**: 2026 (opublikowane online: 9 września 2025, zaakceptowane: 22 lipca 2025)
- **Źródło**: Electronic Commerce Research, Vol. 26, pp. 2467-2502
- **DOI/Link**: https://doi.org/10.1007/s10660-025-10029-9
- **Status**: read
- **Kategoria główna**: Machine Learning
- **Podkategorie**: E-commerce Security, Fraud Detection, Cybersecurity
- **Tagi**: #fraud-detection #e-commerce #machine-learning #feature-engineering #xgboost #cybersecurity #dataset #supervised-learning #classification

## Streszczenie

Publikacja prezentuje zaawansowany system wykrywania oszukańczych stron e-commerce wykorzystujący techniki uczenia maszynowego. Autorzy stworzyli nowy zbiór danych ELFW-2031 (E-commerce Legitimate Fraudulent Websites) zawierający 2031 ręcznie zweryfikowanych stron - 1292 legalnych i 739 oszukańczych.

Głównym wkładem pracy jest zaprojektowanie 50 nowatorskich cech ekstrahowanych z 6 różnych zasobów: URL, HTML, certyfikaty SSL, nagłówki HTTP, technologie webowe oraz media społecznościowe. Autorzy zaproponowali dwa modele klasyfikacyjne: (1) pełny model wykorzystujący wszystkie cechy wraz z zewnętrznymi usługami, osiągający F1-score 96.88% oraz (2) model standalone niezależny od usług zewnętrznych z F1-score 96.53%, oba przy użyciu algorytmu XGBoost.

Badanie wykazało, że nowatorskie cechy związane z analizą technologii webowych i metryk mediów społecznościowych (liczba followersów, aktywność profili) mają największy wpływ na wydajność modelu. System może być zintegrowany z rozszerzeniami przeglądarek i oprogramowaniem antywirusowym, chroniąc użytkowników przed oszustwami w czasie rzeczywistym.

## Kluczowe Wnioski

- **Nowatorski zbiór danych ELFW-2031**: Pierwszy publicznie dostępny dataset zawierający kompletne zasoby webowe (HTML, screenshoty, certyfikaty SSL, informacje z social media) dla 2031 stron e-commerce, umożliwiający obiektywne porównanie różnych metod detekcji
- **Przewaga nowych cech nad tradycyjnymi**: Cechy związane z technologiami webowymi (liczba użytych technologii, Google Analytics, live-chat) i metrykami social media (total_followers, total_posts) uzyskały wyższe rankingi feature importance niż klasyczne cechy z URL
- **Skuteczność modelu standalone**: Model niezależny od usług zewnętrznych osiągnął F1-score 96.53%, tylko 0.35 punktu procentowego poniżej modelu pełnego, co czyni go praktycznym do wdrożenia w rzeczywistych środowiskach produkcyjnych
- **HTML jako najważniejszy zasób**: Grupa 17 cech HTML osiągnęła najlepsze wyniki (F1-score 95.41%) w testach izolowanych zasobów, potwierdzając kluczową rolę analizy zawartości strony
- **Słabość cech URL**: W przeciwieństwie do phishingu, oszukańcze strony e-commerce używają normalnie wyglądających domen, co czyni cechy URL mało skutecznymi (pominięcie URL zmniejszyło wydajność minimalnie)
- **Przewaga social media jako wskaźnika**: Tylko 2.68% oszukańczych stron ma prawdziwe profile social media (vs 83.78% legalnych), po wykluczeniu linków typu "share" - to najbardziej dyskryminująca cecha
- **Wyższa wydajność niż state-of-the-art**: Model standalone przewyższył Wu et al. (90.03% F1-score) i Wadleigh et al. (71.11% F1-score), przy jednoczesnej niezależności od WHOIS i innych zewnętrznych usług niedostępnych w EU (GDPR)

## Metodologia

### Zbiór danych
- **Źródła legitnych stron**: "Confianza Online" - hiszpański znak zaufania dla e-commerce (1292 zweryfikowanych domen)
- **Źródła oszukańczych stron**: Okresowe raporty od INCIBE (Spanish National Cybersecurity Institute) - 739 ręcznie zweryfikowanych domen
- **Okres zbierania**: Listopad 2020 - Listopad 2022
- **Metoda ekstrakcji**: Selenium WebDriver + custom Python3 aplikacja symulująca zachowanie użytkownika w przeglądarce

### Zebrane zasoby dla każdej strony
1. **URL** - kompletny URL po redirectach
2. **HTML** - pełny kod źródłowy włącznie z CSS i JavaScript
3. **Screenshots** - 2 high-resolution zrzuty ekranu (top i bottom, 1848px x 911px)
4. **HTTP headers** - nagłówki odpowiedzi HTTP związane z bezpieczeństwem
5. **Web technologies** - JSON z Wappalyzer (fingerprinting do 1950 technologii w 71 kategoriach)
6. **SSL certificate** - informacje o certyfikacie i jego ważności
7. **Social media** - metryki z Facebook, Instagram, Twitter (API calls) i Trustpilot
8. **Text pages** - HTML stron z regulaminami, polityką prywatności
9. **Offline copy** - kompletna kopia offline strony (WGET)

### Grupy cech (50 total)
- **URL (8 cech)**: liczba cyfr w domenie, długość domeny/subdomeny, NLP features (liczba słów, średnia długość, odchylenie standardowe)
- **HTML (17 cech)**: długość tekstu, domena w tytule/HTML, base64 resources, linki (wewnętrzne/zewnętrzne/puste), liczba walut, cechy cen (total prices, repetitions, average discount), linki social media
- **Technologies (9 cech)**: liczba technologii, kategorie (e-commerce, live-chat, cookie-compliance, analytics, payment-processors), specific tech (Google Analytics, reCaptcha)
- **SSL (2 cechy)**: valid certificate, liczba zarejestrowanych nazw w certyfikacie
- **HTTP Headers (6 cech)**: Content-Security-Policy, Strict-Transport-Security, X-Content-Type-Options, X-Frame-Options, Cache-Control, Expect-CT
- **External/Social Media (8 cech)**: total_followers, total_following, total_posts, fb_likes, fb_visits, tw_age, trustpilot_score, trustpilot_reviews

### Algorytmy uczenia maszynowego
Testowano 9 klasyfikatorów z optymalizacją hiperparametrów (5-fold cross-validated grid search):
- **XGBoost** (najlepszy: F1=96.88% full set, 96.53% standalone)
- **Gradient Boosting Classifier** (GBC)
- **Random Forest** (RF)
- **Support Vector Machines** (SVM)
- **Logistic Regression** (LR)
- **k-Nearest Neighbours** (kNN)
- **AdaBoost**
- **Naive Bayes**

### Preprocessing
- StandardScaler dla normalizacji cech
- 5-fold cross-validation (shuffle=True, random_state=42)
- Metryki: Accuracy, Precision, Recall, F1-Score

## Główne Koncepcje

- **ELFW-2031 Dataset**: E-commerce Legitimate Fraudulent Websites - pierwszy comprehensive, publicznie dostępny dataset zawierający surowe dane z 2031 stron e-commerce (nie tylko ekstrakcje cech jak w innych pracach), umożliwiający rozwój różnych metod detekcji
- **Feature Engineering**: Proces projektowania 50 cech w 6 grupach zasobów, z naciskiem na cechy trudne do obejścia przez atakujących (technologie, social media metrics) zamiast łatwych do sfałszowania (content copying)
- **Standalone vs Full Set Models**: Dwa podejścia - model pełny maksymalizujący accuracy kosztem zależności od external services (social media APIs, Trustpilot) vs model standalone działający lokalnie z minimalnym spadkiem wydajności (0.35 pp)
- **Technology Fingerprinting**: Wykorzystanie Wappalyzer do detekcji technologii webowych - legalne sklepy używają zaawansowanych frameworków (e-commerce platforms, analytics, live-chat), oszukańcze to często sklonowane HTML templates z minimalnymi zasobami
- **Social Media Validation**: Głęboka analiza profili social media wykraczająca poza obecność linków - ekstrahowanie rzeczywistych metryk (followers, posts, account age) przez API, wykrywanie fake "share links" vs prawdziwych profili
- **Price Pattern Analysis**: Wykrywanie powtarzających się cen - oszukańcze strony często wyświetlają identyczne ceny dla wielu produktów (np. wszystko po €61.71), podczas gdy legalne sklepy mają zróżnicowane ceny
- **GDPR Impact on Features**: Unikanie cech opartych na WHOIS (niedostępne w EU przez GDPR) i Alexa ranking (płatne API, sunseted w 2022) - projektowanie cech działających globalnie i długoterminowo
- **Resource Ablation Study**: Systematyczne testowanie wpływu poszczególnych grup zasobów - HTML miał największy wpływ (spadek o 0.0191 F1 po usunięciu), URL minimalny (niemal żaden spadek)

## Wyniki

### Porównanie modeli (XGBoost)
| Model | Precision | Recall | F1-Score | Accuracy |
|-------|-----------|--------|----------|----------|
| Full Set | 97.78% | 96.01% | **96.88%** | 97.78% |
| Standalone | 96.47% | 96.60% | **96.53%** | 97.49% |

### Feature Importance (top features dla Full Set - GBC)
1. **total_followers** (0.175) - suma followersów ze wszystkich social media
2. **total_following** (0.150) - liczba obserwowanych przez profile
3. **total_posts** (0.125) - łączna liczba postów Instagram + tweets
4. **n_tech** (0.105) - liczba wykrytych technologii webowych
5. **google-analytics** (0.095) - czy używa Google Analytics
6. **avg_discount** (0.080) - średni procent zniżek na stronie
7. **link_ext** (0.075) - liczba zewnętrznych linków
8. **analytics** (0.070) - liczba technologii analytics
9. **domain_in_html** (0.065) - ile razy domena pojawia się w HTML
10. **trustpilot_score** (0.060) - ocena na Trustpilot

### Standalone Model Top Features
1. **num_social_html** (0.14) - liczba linków do social media w HTML
2. **google-analytics** (0.13)
3. **n_tech** (0.12)
4. **analytics** (0.10)
5. **domain_in_html** (0.09)

### Ablation Study - wpływ usunięcia grup zasobów (F1-Score XGBoost)
- Wszystkie cechy: **96.87%**
- Bez URL: 96.84% (-0.03% - minimalny wpływ)
- Bez External: 96.29% (-0.58%)
- Bez HTML: 94.64% (-2.23% - największy spadek)
- Bez Tech: 95.90% (-0.97%)
- Bez SSL: 96.73% (-0.14%)
- Bez Headers: 96.85% (-0.02%)

### Izolowane grupy zasobów (tylko jedna grupa cech)
- **HTML only**: F1=95.41% (XGBoost) - najlepszy pojedynczy zasób
- **External only**: F1=86.67% (GBC)
- **Tech only**: F1=83.29% (XGBoost)
- **URL only**: F1=59.91% (GBC) - najsłabszy zasób
- **SSL only**: F1=68.03% (GBC) - tylko 2 cechy
- **Headers only**: F1=77.40% (GBC) - wysoki recall 90.94%, ale precision 67.46%

### Porównanie z state-of-the-art (na ich cechach, nasz dataset)
| Method | Classifier | F1-Score |
|--------|-----------|----------|
| **Our Standalone** | XGBoost | **96.53%** |
| Wu et al. [7] | RF | 90.03% |
| Wadleigh et al. [20] | XGBoost | 71.11% |

### Rozkład kategorii stron
| Kategoria | Fraud (%) | Legit (%) |
|-----------|-----------|-----------|
| Fashion | 310 (41.95%) | 179 (13.86%) |
| Marketplace | 231 (31.27%) | 142 (10.99%) |
| Sport | 105 (14.21%) | 65 (5.03%) |
| Home | 19 (2.57%) | 208 (16.10%) |
| Health | 11 (1.49%) | 142 (10.99%) |

**Obserwacje**: Oszukańcze strony koncentrują się na Fashion (41.95%) i Marketplace (31.27%), podczas gdy legalne są bardziej zróżnicowane, z większym udziałem Home (16.10%) i Health (10.99%).

## Przydatne Cytaty

> "In recent years, e-commerce has experienced growth in sales, brands and customers. Unfortunately, cybercriminals have taken advantage of this by creating fraudulent websites to scam customers." (str. 2467)

> "We present a framework for fraudulent e-commerce website detection based on machine learning that can operate with third-party resources to optimize detection without them to achieve endpoint scalability." (str. 2470)

> "To the best of our knowledge, currently publicly available datasets are limited in terms of resources and features and, therefore, cannot be used to develop or compare techniques that depend on other uncollected resources." (str. 2477)

> "Results showed that 21.65% of fraudulent websites had at least one link to social media, significantly higher than the study mentioned above. We inspected the social media URLs used by these pages. We found that most of them were generic links with no username in the URL or share links... After removing these findings, only 2.68% of the fraudulent websites had at least one valid link to a social media profile, compared to the 83.78% of the legitimate websites." (str. 2485-2486)

> "The proposed models achieve F1 scores of 96.88% and 96.53% respectively using XGBoost. Finally, we evaluated the performance of the proposed features, showing that novel features from social media and the technology analysis were the most valuable ones." (str. 2467)

> "fraudulent websites tend to repeat prices for most of their products" (str. 2485)

> "Legitimate e-commerce websites are created by using modern technologies and frameworks to ensure security and ease of maintenance. However, attackers craft fraudulent websites effortlessly and with minimal resources to run the site." (str. 2487)

> "Novel features presented in this work ranked higher than the legacy ones, as depicted in Fig. 7. Therefore, designed features contribute to the fraudulent website detection problem." (str. 2494)

## Datasety

- [ELFW-2031](../../../datasets/elfw-2031.md) - E-commerce Legitimate Fraudulent Websites dataset: 2031 ręcznie zweryfikowanych stron e-commerce (1292 legitne, 739 oszukańcze) z comprehensive zasobami (URL, HTML, screenshots, SSL, HTTP headers, tech analysis, social media metrics, text pages, offline copy). Dostępny na żądanie przez https://gvis.unileon.es

## Powiązane Tematy

- Phishing detection techniques i różnice między phishing a fake e-commerce
- Feature engineering w cybersecurity - projektowanie cech odpornych na adversarial attacks
- Social media verification systems i wykorzystanie API do walidacji profili
- Web technology fingerprinting (Wappalyzer, BuiltWith)
- GDPR impact on security research - ograniczenia WHOIS i innych zasobów
- Evasion techniques w fraud detection - jak atakujący omijają detekcję
- Real-time fraud detection systems - integration z browser extensions i antivirus
- Counterfeit product detection - różnice między fake stores a counterfeit products
- Dataset creation metodologie dla cybersecurity research
- XGBoost i Gradient Boosting w klasyfikacji binarnej
- External service dependency w ML systems - trade-offs między accuracy a reliability
- Multi-modal fraud detection - łączenie różnych typów danych (text, images, metadata)
- Active learning dla małych datasetów cybersecurity
- Transfer learning w fraud detection
- Brandwatch i brand protection systems
- E-commerce trust seals i certification systems

## Notatki

*Sekcja pusta - miejsce na własne notatki użytkownika.*
