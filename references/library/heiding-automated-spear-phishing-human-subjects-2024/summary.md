---
title: "Evaluating Large Language Models' Capability to Launch Fully Automated Spear Phishing Campaigns: Validated on Human Subjects"
date: 2024-01-01
authors: "Fredrik Heiding, Simon Lermen, Andrew Kao, Bruce Schneier, Arun Vishwanath"
status: read
doi: "arxiv:2412.00586"
category: "Security"
tags:
  - spear-phishing
  - llm
  - social-engineering
  - osint
  - vulnerability-profiling
  - phishing-detection
  - human-subjects-study
  - ai-automation
  - project/personalized-phishing-defense
---

# Evaluating Large Language Models' Capability to Launch Fully Automated Spear Phishing Campaigns: Validated on Human Subjects

## Metadane
- **Autorzy**: Fredrik (Fred) Heiding (Harvard Kennedy School), Simon Lermen (Independent), Andrew Kao (Harvard Kennedy School), Bruce Schneier (Harvard Kennedy School), Arun Vishwanath (Avant Research Group)
- **Rok**: 2024
- **Zrodlo**: arXiv:2412.00586 (v1, 30 listopada 2024, cs.CR)
- **DOI/Link**: arxiv:2412.00586
- **Status**: `#read`
- **Kategoria**: Security
- **Tagi**: `#spear-phishing` `#llm` `#social-engineering` `#osint` `#vulnerability-profiling` `#phishing-detection` `#human-subjects-study` `#ai-automation` `#project:personalized-phishing-defense`

## Streszczenie

Praca empirycznie ocenia zdolnosc duzych modeli jezykowych (LLM) do przeprowadzania w pelni zautomatyzowanych, spersonalizowanych kampanii spear phishingowych, walidujac wyniki na realnych uczestnikach badania. Autorzy przeprowadzili eksperyment z 101 uczestnikami podzielonymi na cztery grupy mailowe: grupe kontrolna (zwykle wiadomosci spam/phishing, 12% click-through), maile pisane przez ekspertow-ludzi (54%), maile w pelni generowane przez AI (54%) oraz maile AI z interwencja czlowieka (human-in-the-loop, 56%). Ataki w pelni zautomatyzowane przez AI osiagnely wyniki na poziomie ekspertow-ludzi i byly o 350% skuteczniejsze niz grupa kontrolna. Jest to istotna poprawa wzgledem analogicznych badan z roku poprzedniego (2023), gdzie modele AI wymagaly interwencji czlowieka, aby dorownac ekspertom.

Centralnym elementem pracy jest **autorskie narzedzie (custom-built tool), ktore automatyzuje caly proces spear phishingu**: rekonesans (OSINT przez agenta opartego na GPT-4o z dostepem do wyszukiwarki i przegladarki), **tworzenie spersonalizowanych "profili podatnosci" (personalized vulnerability profiles) dla kazdego celu**, generowanie i wysylke maili (glownie Claude 3.5 Sonnet), sledzenie klikniec w czasie rzeczywistym oraz samodoskonalenie na podstawie wynikow. Informacje zebrane automatycznie przez narzedzie byly dokladne i uzyteczne w 88% przypadkow, a tylko 4% profili bylo blednych (dotyczylo niewlasciwej osoby).

Praca pokazuje rowniez defensywne zastosowanie LLM: Claude 3.5 Sonnet w detekcji intencji maili osiagnal ponad 90% skutecznosci przy niskim odsetku falszywych alarmow (97,25% true-positive na 363 mailach phishingowych, 0 falszywych pozytywow), wykrywajac nawet subtelne ataki, ktore zmylily ludzi. Dodatkowo autorzy przedstawiaja analize ekonomiczna pokazujaca, ze AI zwieksza rentownosc phishingu nawet 50-krotnie dla wiekszych grup odbiorcow.

## Kluczowe Wnioski

- W pelni zautomatyzowane przez AI spear phishingi osiagaja skutecznosc na poziomie ekspertow-ludzi (54% vs 54%), a interwencja czlowieka daje znikoma poprawe (56%) — human-in-the-loop staje sie zbedny w kontekscie jakosc/koszt.
- Autorskie narzedzie automatyzuje caly lancuch ataku, w tym budowe spersonalizowanych "profili podatnosci" dla kazdego celu na podstawie OSINT (hyper-personalizacja, kategoria 3).
- Automatyczny rekonesans OSINT dal dokladne i uzyteczne informacje w 88% przypadkow (poziom 3), 8% poprawna osoba z ograniczona informacja (poziom 2), tylko 4% blednych (poziom 1).
- Personalizacja zwiekszala zaufanie: ~40% uczestnikow w grupach AI wskazalo personalizacje jako powod zaufania (vs 0% w grupie kontrolnej, ~20% u ekspertow).
- Mechanizmy bezpieczenstwa (guardrails) modeli mozna obejsc prostym przeformulowaniem promptu (zamiana "phishing email" na "email") i resamplingiem; w trybie agentowym (rekonesans) modele nigdy nie odmawialy.
- LLM jako obrona: Claude 3.5 Sonnet osiagnal ponad 90% detekcji intencji, a po "primingu na podejrzliwosc" (pytanie czy mail jest podejrzany zamiast o intencje) skutecznosc rosla bez wzrostu falszywych alarmow.
- Ekonomia: AI zwieksza rentownosc phishingu do 50x; w pelni automatyczny tryb AI jest zawsze najbardziej oplacalny dzieki oszczednosci czasu.
- "Profile podatnosci" maja charakter dual-use — te same profile moga sluzyc obronie (uczeniu uzytkownikow, na jakie ataki sa najbardziej podatni, oraz czyszczeniu cyfrowego sladu).

## Metodologia

**Eksperyment z udzialem ludzi (101 uczestnikow).** Rekrutacja przez ulotki kampusowe i maile do grup uniwersyteckich, za 5 USD (karta podarunkowa lub darowizna). Analiza mocy statystycznej: alpha = 0,05, moc = 0,80, co dalo wymagane okolo 100-125 uczestnikow; przyjeto 101. Badanie zatwierdzone przez IRB. Zastosowano dozwolona dezinformacje — uczestnikom powiedziano o "marketingowych" mailach, nie ujawniono sledzenia klikniec; po zakonczeniu pelny debriefing.

**Cztery grupy (losowy przydzial przez Google Sheets, po ok. 1/4):**
1. Kontrolna (n=26) — zwykly spam dostosowany, by przeszedl filtry.
2. Ekspert-czlowiek (n=24) — semi-personalizacja, V-Triad i 6 zasad Cialdiniego (autorytet, niedobor).
3. AI w pelni automatyczne (n=26) — Claude 3.5 Sonnet, hyper-personalizacja.
4. AI z human-in-the-loop (n=25) — mozliwa interwencja w OSINT lub tresc.

**Autorskie narzedzie AI-phishingowe** (6 funkcji): rekonesans (agent GPT-4o + Google Search API + tekstowa przegladarka, 2-5 zrodel na cel), baza promptow (szablon ponad 2000 znakow), generowanie maili (Anthropic/OpenAI/Meta/Mistral), wysylka (partie po 10, godz. 10:30-14:00), live tracking klikniec przez unikalne URL przekierowujace do logujacego serwera, raportowanie. Narzedzie samodoskonali sie na podstawie udanych/nieudanych prob.

**Detekcja intencji (defensywna czesc).** Test 5 modeli (Claude 3.5 Sonnet, GPT-4o, Mistral Large, Gemini, Llama 3.1 405B) na 20 mailach; nastepnie poglebiona analiza Claude vs GPT-4o na zbiorze 381 maili (18 legalnych, 363 phishingowych) z 9 kategorii. Wykorzystano function calling do ocen liczbowych (suspicion, importance, relevance, quality, ai_likelihood w skali 0-100).

## Glowne Koncepcje

- **Personalized vulnerability profile (profil podatnosci)**: automatycznie budowany przez agenta AI profil celu (zainteresowania, profil zawodowy/akademicki, wspolpracownicy) na bazie OSINT, uzywany do hyper-personalizacji maila i jako wektor ataku.
- **Hyper-personalizacja (kategoria 3)**: znajomosc najnowszych projektow, konkretnych zainteresowan i kontaktow celu — w odroznieniu od semi-personalizacji (kategoria 2: gdzie/co studiuje) i braku personalizacji (kategoria 1).
- **Human-in-the-loop (tryb hybrydowy)**: czlowiek moze interweniowac w fazie OSINT (gdy zla osoba) lub redakcji tresci; w badaniu interwencje byly marginalne (75% to drobne zmiany jezykowe).
- **Priming for suspicion**: technika detekcyjna — pytanie modelu wprost, czy mail jest podejrzany, zamiast o jego intencje, znaczaco poprawia wykrywalnosc bez wzrostu false positives.
- **V-Triad i zasady Cialdiniego**: ramy perswazji (wiarygodnosc, relewancja; wzajemnosc, konsekwencja, dowod spoleczny, autorytet, sympatia, niedobor) wbudowane w szablony promptow.
- **Stylizowany model ekonomiczny phishingu**: rentownosc jako funkcja prawdopodobienstwa sukcesu, czasu, kosztow stalych, wyplaty i wspolczynnika konwersji q.

## Wyniki

- **Click-through rate**: grupa kontrolna **12%**, eksperci-ludzie **54%**, w pelni AI **54%**, AI hybryda (human-in-the-loop) **56%**. AI dorownuje ekspertom i jest 350% skuteczniejsze od kontroli.
- **Jakosc OSINT (profile podatnosci)**: **88% poziom 3** (dokladne, wystarczajace info), 8% poziom 2, **4% poziom 1** (bledna osoba). Vs 2023 — dramatyczna poprawa jakosci tresci (Content score 5: 71% w 2024 vs 25% w 2023).
- **Czas i koszt**: pelna automatyzacja redukuje koszt do okolo **4 centow za mail** (API OpenAI/Anthropic). Manualne odtworzenie procesu: ok. 23:27 min OSINT + ok. 10:10 min tresc = ok. 34 min/cel. Human-in-the-loop byl o ok. 92% szybszy od manualnego; interwencja OSINT potrzebna w 8% maili, interwencja w tresci w 48% (z czego 75% to drobne korekty jezykowe).
- **Detekcja (Claude 3.5 Sonnet)**: w tescie wstepnym wykryl 100% z pierwszych 20 maili; w duzym zbiorze **97,25% true-positive na 363 mailach phishingowych, 0 falszywych pozytywow** (wazone wg kategorii 97,64%). Po primingu na podejrzliwosc poprawnie sklasyfikowal wszystkie phishingowe jako podejrzane i wszystkie legalne jako bezpieczne. Najslabiej w kategorii "Phishing" (81% TP), 100% w kategorii "Expert". GPT-4o znacznie slabszy. Mistral cierpial na liczne false positives.
- **Wskazniki zaufania/podejrzliwosci**: ~40% w grupach AI wskazalo personalizacje jako powod zaufania (0% kontrola); nadawca (sender) byl najczestszym wskaznikiem podejrzliwosci (spoofing domeny).
- **Ekonomia (Tabela 4)**: phishing AI oplacalny w niemal wszystkich warunkach; tryb w pelni AI najbardziej rentowny. Wyplata kalibrowana na 136 USD/udany phish, koszt rozwoju narzedzia ok. 260 h = ok. 16 120 USD. Punkty break-even wg grupy: 2 859 osob (wysokie q), 10 213 (srednie q), 54 123 (niskie q). Dla grup ok. 5 000 AI bije ekspertow-ludzi niezaleznie od q. AI zwieksza rentownosc do ok. 50x.
- **Aktywnosc**: tylko 60 ze 101 uczestnikow wykazalo aktywnosc w ciagu tygodnia, co sugeruje, ze realny odsetek "zlapanych" moze byc jeszcze wyzszy.
- **Projekcja**: liniowa ekstrapolacja sugeruje, ze modele AI przescigna ekspertow-ludzi w 2025 (155% vs 99% wydajnosci eksperta).

## Przydatne Cytaty

> "Our AI-automated emails were sent using a custom-built tool that automates the entire spear phishing process, including information gathering and creating personalized vulnerability profiles for each target." (Abstract, str. 1)

> "The AI-gathered information was accurate and useful in 88% of cases and only produced inaccurate profiles for 4% of the participants." (Abstract, str. 1)

> "Thus, the AI-automated attacks performed on par with human experts and 350% better than the control group." (Abstract, str. 1)

> "Claude 3.5 Sonnet achieved a 97.25% detection rate on the 363 phishing emails with no false positives." (str. 2)

> "simple rephrasing, such as changing 'phishing email' to just say 'email,' is sufficient to circumvent most models' safety guardrails. [...] the only difference between a high-quality phishing email and a legitimate one is the sender's intentions." (Sekcja 3.6, str. 7)

> "attackers can use AI agents to create personalized vulnerability profiles, which enable cheap and effective AI-automated spear phishing. Defenders can use the same personalized vulnerability profiles to teach users what attacks they are most susceptible to." (Sekcja 7.1, str. 13)

> "By using language models, attackers can effortlessly create phishing emails that are uniquely adapted to every target, rendering signature detection schemes obsolete." (Konkluzja, str. 13)

## Datasety

W badaniu nie uzyto formalnego, nazwanego datasetu benchmarkowego — kluczowym "zbiorem" sa grupy uczestnikow i wygenerowane maile:

- **Grupy 101 uczestnikow (human subjects)** — 4 grupy mailowe (kontrolna n=26, ekspert n=24, AI n=26, AI hybryda n=25); klastry zawodowe: Technology/CS 28%, Life Sciences/Healthcare 25%, Physical Sciences/Math 15%, Business/Management 12%, Education/Social Sciences 11%, Engineering 10%.
- **Zbior detekcyjny 381 maili** (9 kategorii): 18 legalnych, 51 "AI combined" (Claude, badanie realne), po 50 Claude/o1-preview/GPT-4o/GPT-3.5/Llama (cele syntetyczne), 53 phishing z baz online, 9 ekspert.
- **Zrodla maili phishingowych do detekcji**: dataset NIST (TREC 2007 spam/phishing), archiwum phishingowe grupy bezpieczenstwa UC Berkeley, skrzynka jednego z autorow.

## Powiazane Tematy

- Spersonalizowane mechanizmy obrony (personalized mitigation) oparte na profilach podatnosci — kierunek bezposrednio relewantny dla projektu personalized-phishing-defense.
- Kategoryzacja cyfrowego sladu uzytkownika (4 typy informacji: uzyteczne dla uzytkownika/atakujacego) i selektywne usuwanie danych podwyzszonego ryzyka.
- Jailbreaking i obchodzenie guardrails w trybie agentowym LLM (refusal-vector ablation, AgentHarm).
- LLM jako detektor phishingu (PhishLLM, DynaPhish, ChatGPT detection) i "priming for suspicion".
- Ekonomia cyberprzestepczosci i modelowanie rentownosci atakow.
- Detekcja sygnaturowa vs adaptacyjna — dezaktualizacja klasycznych filtrow antyspamowych.
- Przyszle kanaly ataku: media spolecznosciowe, glos, computer-use agents.
- Aspekty etyczne i regulacyjne (EU AI Act art. 5, profilowanie AI na danych publicznych).

## Notatki

