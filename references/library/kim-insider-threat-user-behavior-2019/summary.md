---
title: "Insider Threat Detection Based on User Behavior Modeling and Anomaly Detection Algorithms"
date: 2019-01-01
authors: "Junhong Kim, Minsik Park, Haedong Kim, Suhyoun Cho, Pilsung Kang"
status: read
doi: "10.3390/app9194018"
category: "Security"
tags:
  - insider-threat
  - anomaly-detection
  - user-behavior-modeling
  - ueba
  - one-class-classification
  - topic-modeling
  - lda
  - email-network
  - behavioral-analytics
  - project/personalized-phishing-defense
---

# Insider Threat Detection Based on User Behavior Modeling and Anomaly Detection Algorithms

## Metadane
- **Autorzy**: Junhong Kim, Minsik Park, Haedong Kim, Suhyoun Cho, Pilsung Kang (School of Industrial Management Engineering, Korea University, Seoul)
- **Rok**: 2019 (Received: 28.08.2019; Accepted: 23.09.2019; Published: 25.09.2019)
- **Zrodlo**: Applied Sciences (MDPI), tom 9, nr 19, artykul 4018
- **DOI**: `10.3390/app9194018`
- **Status**: `#read`
- **Kategoria glowna**: `#Security`
- **Podkategorie**: `#anomaly-detection` `#machine-learning` `#behavioral-modeling`
- **Tagi**: `#insider-threat` `#anomaly-detection` `#user-behavior-modeling` `#ueba` `#one-class-classification` `#topic-modeling` `#lda` `#email-network` `#behavioral-analytics` `#project:personalized-phishing-defense`
- **Licencja**: Open Access (CC BY 4.0)

## Streszczenie

Praca proponuje ramowy system detekcji zagrozen wewnetrznych (insider threats) oparty na modelowaniu zachowania uzytkownika oraz algorytmach detekcji anomalii. Insider threats to zlosliwe dzialania autoryzowanych uzytkownikow (kradziez wlasnosci intelektualnej lub informacji, oszustwo, sabotaz). Choc wystepuja rzadziej niz ataki zewnetrzne, ich skala szkod jest wieksza, a ze wzgledu na znajomosc systemow organizacji przez insiderow sa one trudne do wykrycia. Tradycyjne metody oparte na regulach tworzonych przez ekspertow dziedzinowych sa malo elastyczne i nieodporne na zmieniajace sie techniki atakow.

Autorzy konstruuja z surowych logow uzytkownika **trzy typy ustrukturyzowanych zbiorow danych**: (1) dzienne podsumowanie aktywnosci uzytkownika, (2) rozklad tematow tresci e-maili (topic distribution) oraz (3) tygodniowa historie komunikacji e-mailowej w postaci sieci. Na kazdym z tych zbiorow niezaleznie trenuja **cztery algorytmy klasyfikacji jednoklasowej** (one-class classification) oraz ich kombinacje. Kluczowa decyzja metodologiczna: w warunkach skrajnego niezbalansowania klas (tylko nieliczne przypadki anomalne) klasyfikacja binarna jest niemozliwa do wytrenowania, dlatego stosuje sie modele uczone wylacznie na danych "normalnych", ktore ucza sie typowego profilu zachowania i sygnalizuja odchylenia.

Eksperymenty na zbiorze CERT R6.2 (4000 uzytkownikow, z czego tylko 5 zlosliwych) pokazuja, ze proponowany framework dziala skutecznie na niezbalansowanych danych i bez wiedzy ekspertow dziedzinowych. Model na podstawie dziennego podsumowania aktywnosci wykrywa do 53,67% rzeczywistych zagrozen monitorujac tylko top 1% najbardziej podejrzanych instancji, a ponad 90% przy rozszerzeniu do top 30%. Modele oparte na tresci e-maili i sieci komunikacyjnej uzupelniaja detekcje, a w trzech z czterech testowanych uzytkownikow detekcja sieciowa wykrywa wszystkie zlosliwe instancje.

## Kluczowe Wnioski

- **Profil bazowy per-uzytkownik + detekcja anomalii** jest praktyczna alternatywa dla podejsc regulowych i binarnych w warunkach skrajnie niezbalansowanych danych (handful/zero przypadkow anomalnych).
- Heterogeniczne zrodla danych (aktywnosc dzienna, tresc e-maili, siec e-mail) daja komplementarna informacje - zaden pojedynczy zbior ani algorytm nie jest najlepszy we wszystkich przypadkach.
- **Analiza tresci e-maili przez topic modeling (LDA)** pozwala wykrywac odchylenia semantyczne: jesli rozklad tematow danego e-maila znaczaco rozni sie od typowego rozkladu w roli, e-mail jest podejrzany - mechanizm uzyteczny jako "personalny baseline" tresci.
- Kombinacja **Parzen + PCA** dawala najlepsza skutecznosc w najwiekszej liczbie przypadkow (10 z 21) na zbiorze dziennej aktywnosci; ensemble (ranking-based) przewyzsza pojedyncze algorytmy szczegolnie dla roli "Salesman".
- Modele budowane sa **per rola** (Electrical Engineer, IT Admin, Salesman), bo zaklada sie, ze uzytkownicy tej samej roli maja podobne wzorce aktywnosci - uproszczona forma peer-group baseline.
- Detekcja jest **batchowa** (jednostka czasu = dzien/tydzien), nie strumieniowa - autorzy wskazuja rozwoj modeli sekwencyjnych/online jako kierunek przyszly.

## Metodologia

System sklada sie z dwoch faz: modelowania zachowania uzytkownika (transformacja nieustrukturyzowanych logow w wektory liczbowe) oraz detekcji anomalii (uczenie jednoklasowe). Z pieciu tabel logow CERT (logon, USB/device, http, file, email) budowane sa **trzy niezalezne zbiory danych**:

**1. Dzienne podsumowanie aktywnosci (daily activity summary).** Fragmentaryczne dzienne rekordy uzytkownika sa integrowane chronologicznie i agregowane w wektory liczbowe opisujace intensywnosc aktywnosci (np. liczba logowan, podlaczen USB, wyslanych e-maili z zalacznikami - z rozroznieniem godzin pracy i poza nimi). Z CERT wyekstrahowano 60 zmiennych kandydujacych; po sumaryzacji uzyskano 1 394 010 instancji (kazda = podsumowanie jednego dnia jednego uzytkownika), z czego tylko 73 to potencjalne zagrozenia. Selekcja zmiennych: test rozkladu Gaussa jednowymiarowego (poziom istotnosci alfa = 0,1) - zmienna wchodzi do modelu, jesli przynajmniej jedna anomalia lezy w obszarze odrzucenia. Modele budowane per rola (Electrical Engineer, IT Admin, Salesman, ~90% anomalii).

**2. Rozklad tematow tresci e-maili (e-mail content topic distribution).** Tresc kazdego e-maila przeksztalcana topic modelingiem **Latent Dirichlet Allocation (LDA)** w wektor 50 prawdopodobienstw tematow (liczba tematow = 50, alfa = 1; suma = 1). Kazdy e-mail staje sie obserwacja o wymiarze 50 z etykieta normalny(0)/anomalny(1). Zalozenie: rozklady tematow w obrebie roli sa podobne, wiec e-mail o nietypowym rozkladzie jest podejrzany. ~1,5 mln e-maili, 68 zlosliwych.

**3. Tygodniowa siec komunikacji e-mailowej (weekly e-mail network).** Z informacji nadawca/odbiorca budowana skierowana siec tygodniowa (wezel = konto e-mail, krawedzie wazone liczba wiadomosci). Obliczono 28 cech sieciowych na uzytkownika, m.in. in/out-degree dla konta firmowego/prywatnego, **podobienstwo Jaccarda** in/out-degree miedzy kolejnymi oknami czasowymi (stabilnosc profilu w czasie) oraz **betweenness centrality** (czy konto pelni role bramy informacyjnej). Czterech uzytkownikow z nietypowa komunikacja (CDE1846, CMP2946, DNS1758, HIS1706).

**Cztery algorytmy klasyfikacji jednoklasowej (one-class / anomaly detection):**
- **Gauss** - estymacja gestosci jednym wielowymiarowym rozkladem Gaussa (mean + macierz kowariancji); anomalia = niskie prawdopodobienstwo generacji.
- **Parzen** - nieparametryczna estymacja gestosci metoda okna Parzena (jadro Gaussa, parametr szerokosci h); brak zalozenia o rozkladzie a priori.
- **PCA** - rzutowanie na podprzestrzen k glownych skladowych; jako score anomalii uzywany **blad rekonstrukcji** (roznica miedzy oryginalem a obrazem zrekonstruowanym z przestrzeni o nizszym wymiarze).
- **KMC (K-means clustering)** - klastrowanie tylko normalnych instancji (badano K = 3, 5, 10); score anomalii = wzgledna odleglosc D_i/R od najblizszego centroidu (R = promien klastra).

**Kombinacje (ensemble).** Testowano wszystkie kombinacje czterech detektorow. Ze wzgledu na rozne zakresy score'ow laczenie odbywa sie przez **rangi** (rank-based): dla kazdej instancji liczona jest ranga w kazdym modelu, a odwrotnosc sredniej rang jest score'em ensemble.

**Protokol ewaluacji.** Brak progu cut-off typowego dla klasyfikacji - dlatego: zbior treningowy = 90% losowo wybranych instancji normalnych, zbior testowy = pozostale 10% normalnych + wszystkie anomalne. Score'y sortowane malejaco; liczona **true detection rate w top X%** (X w {1, 5, 10, 15, 20, 25, 30}) - udzial wykrytych zlosliwych aktywnosci wsrod top X% najwyzszych score'ow. Proces powtarzany 30 razy, usredniany. Dla danych sieciowych (mniej probek) trenowano na wszystkich instancjach normalnych.

## Glowne Koncepcje

- **Insider threat** - zlosliwe dzialanie autoryzowanego uzytkownika (kradziez IP/informacji, oszustwo, sabotaz); trudne do wykrycia z powodu znajomosci systemow i posiadanych uprawnien.
- **User behavior modeling** - transformacja heterogenicznych, nieustrukturyzowanych logow uzytkownika w ustrukturyzowane wektory liczbowe (instancja = user-day / e-mail / user-week).
- **One-class classification (klasyfikacja jednoklasowa)** - uczenie wylacznie na danych klasy normalnej; model uczy sie wspolnych cech "normalnosci" i ocenia prawdopodobienstwo, ze nowa instancja jest normalna. Rozwiazuje problem braku/niedoboru przypadkow anomalnych.
- **Latent Dirichlet Allocation (LDA)** - probabilistyczny model tematyczny; dokument = mieszanka tematow, temat = rozklad prawdopodobienstwa slow. Wyjscia: rozklad tematow per dokument (theta_d) i rozklad slow per temat (phi_k).
- **True detection rate (in top X%)** - metryka skrojona pod niezbalansowane dane: ile rzeczywistych anomalii znalazlo sie w top X% najwyzszych score'ow anomalii.
- **Jaccard similarity / betweenness centrality** - miary sieciowe opisujace stabilnosc profilu komunikacji w czasie oraz role pomostowa konta w sieci e-mail.
- **Personal/peer-group baseline** - zalozenie, ze odchylenie od typowego profilu (wlasnego lub roli) sygnalizuje zagrozenie - podstawa obrony "personalnego baseline" niezaleznej od znanych sygnatur ataku.

## Wyniki

**Dzienne podsumowanie aktywnosci** (true detection rate, najlepsze przypadki):
- Electrical Engineer: do 53,67% w top 1% (KMC K=10) - ponad 50x lepiej niz model losowy; rosnie do 76,33% / 79,33% / 90% przy top 5% / 10% / 15%.
- Salesman: przy top 30% (Parzen + PCA) wykryto 94,79% zlosliwych - najwyzszy wynik wsrod trzech rol.
- IT Admin: najslabsza rola dla tego zbioru, ale wciaz znacznie powyzej losowego (lift 9,71 przy 1%, 4,35 przy 5%).
- Wsrod pojedynczych algorytmow Parzen najlepszy w 8/21 przypadkach; Gauss czesto najgorszy (zbyt sztywne zalozenie jednego rozkladu). **Parzen + PCA** najlepszy w 10/21 przypadkow, a w sumarycznym rankingu ensemble wybrany jako najlepszy 10-krotnie (Tabela A7), przed Gauss + Parzen + PCA (5x).

**Tresc e-maili (LDA):**
- Tu detekcja najlepsza dla **IT Admin**: Parzen + PCA 37,56% w top 1%, rosnaco do 98,67% w top 30%.
- Electrical Engineer i Salesman podobne: lift > 4,5 przy 1%, ~2/3 anomalii przy 30%.
- KMC najskuteczniejszy dla Electrical Engineer, ale calkowicie zawiodl dla IT Admin (0,0). Skutecznosc pojedynczych algorytmow silnie zalezy od charakterystyki zbioru.

**Siec komunikacji e-mailowej (per uzytkownik):**
- Dla 3 z 4 uzytkownikow (CDE1846, DNS1758, HIS1706) wszystkie zlosliwe instancje wykryte przy cut-off <= 25%.
- Gauss osiagnal 100% detekcji w top 5% dla CDE1846; KMC wykryl wszystkie anomalie HIS1706 w top 10%.
- Wyjatek: CMP2946 - model nie wykryl >30% zlosliwej komunikacji nawet przy top 30%.
- W odroznieniu od dwoch pozostalych zbiorow, **kombinacje nie poprawily** wynikow wzgledem pojedynczych modeli na danych sieciowych.

**Ograniczenia (wskazane przez autorow):** trzy modele trenowane niezaleznie (rozne instancje) - brak integracji wynikow; detekcja batchowa, nie strumieniowa/real-time; podejscie czysto data-driven (brak wiedzy ekspertow); CERT to dane syntetyczne - potrzebna walidacja na danych realnych.

## Przydatne Cytaty

- "To resolve these shortcomings, we propose an insider-threat detection framework based on user activity modeling and one-class classification." (s. 2)
- "Unlike binary classification, one-class classification algorithms only use the normal class data to learn their common characteristics without relying on abnormal class data." (s. 9)
- "We assumed that the e-mail topic distributions in each role are similar. Thus, if a topic distribution of a certain e-mail is significantly different from that of the other e-mails, it should be suspected as abnormal/malicious behavior." (s. 6)
- "Among the top 1% of the anomaly scores predicted by Gauss for Electrical Engineer, half of the actual abnormal behaviors are successfully detected, which is more than 50 times higher than a random model..." (s. 11)
- "In this version, the dataset includes 4000 users, among whom only five users behaved maliciously." (s. 3)
- "It could be worth developing a sequence-based insider-threat detection model that can process online stream data." (s. 16)

## Datasety

- [CERT Insider Threat Dataset](../../../datasets/cert-insider-threat.md) - wersja **R6.2** (4000 uzytkownikow, 5 zlosliwych; tabele: logon, device/USB, http, file, email + LDAP/psychometric). W tej pracy z logow zbudowano 3 pochodne zbiory: dzienne podsumowanie aktywnosci (1 394 010 instancji, 60 zmiennych kandydujacych), tresc e-maili w reprezentacji LDA (~1,5 mln e-maili, 68 zlosliwych), tygodniowa siec e-mail (28 cech, 4 uzytkownikow z anomaliami).

## Powiazane Tematy

- UEBA (User and Entity Behavior Analytics) - profilowanie bazowe zachowania uzytkownika/encji
- Detekcja anomalii w warunkach skrajnego niezbalansowania klas (one-class / novelty detection)
- Topic modeling tresci (LDA) jako wykrywanie odchylen semantycznych w komunikacji
- Personal baseline jako obrona przed nieznanymi pretekstami (spear-phishing / social engineering)
- Analiza sieci komunikacji e-mailowej (graph features: degree, Jaccard, betweenness)
- Peer-group / role-based behavioral baselines
- Sekwencyjna / strumieniowa detekcja (online stream) jako rozwiniecie podejscia batchowego
- Hybrydy data-driven + wiedza ekspercka w detekcji zagrozen wewnetrznych

## Notatki
