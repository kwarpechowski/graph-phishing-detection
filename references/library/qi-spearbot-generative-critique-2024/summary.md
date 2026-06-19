---
title: "SpearBot: Leveraging Large Language Models in a Generative-Critique Framework for Spear-Phishing Email Generation"
date: 2024-01-01
authors: "Qinglin Qi, Yun Luo, Yijia Xu, Wenbo Guo, Yong Fang"
status: read
doi: "arxiv:2412.11109"
category: "Security"
tags:
  - project/personalized-phishing-defense
  - spear-phishing
  - large-language-models
  - jailbreak
  - generative-critique
  - adversarial-attack
  - social-engineering
  - phishing-detection
---

# SpearBot: Leveraging Large Language Models in a Generative-Critique Framework for Spear-Phishing Email Generation

## Metadane

- **Autorzy**: Qinglin Qi (Sichuan University), Yun Luo (Zhejiang University), Yijia Xu (Sichuan University), Wenbo Guo (Nanyang Technological University), Yong Fang (Sichuan University, autor korespondencyjny)
- **Rok**: 2024 (arXiv: 15 grudnia 2024)
- **Zrodlo**: arXiv preprint, cs.CR
- **DOI / ID**: `arxiv:2412.11109` (arXiv:2412.11109v1)
- **Status**: `#read`
- **Kategoria glowna**: `#Security`
- **Podkategorie**: ofensywne wykorzystanie LLM, inzynieria spoleczna, detekcja phishingu
- **Tagi**: `#spear-phishing` `#large-language-models` `#jailbreak` `#generative-critique` `#adversarial-attack` `#social-engineering` `#phishing-detection` `#project:personalized-phishing-defense`

## Streszczenie

Praca przedstawia **SpearBot** - adwersarialny framework wykorzystujacy duze modele jezykowe (LLM) do generowania wysoce spersonalizowanych e-maili spear-phishingowych. Autorzy pokazuja, ze za pomoca specjalnie spreparowanych promptow jailbreakujacych mozna obejsc mechanizmy bezpieczenstwa komercyjnych LLM (glownie GPT-4) i zmusic je do tworzenia szkodliwych tresci phishingowych. Kluczowym elementem jest petla **generator-krytyk (generative-critique)**: jeden LLM generuje e-mail phishingowy, a kolejne instancje LLM pelnia role krytykow, ktorzy oceniaja, czy wiadomosc jest rozpoznawalna jako phishing. Jesli ktorykolwiek krytyk zidentyfikuje e-mail jako phishingowy, jego uzasadnienie jest przekazywane z powrotem do generatora, ktory iteracyjnie przepisuje tresc, ukrywajac intencje coraz subtelniej, az zaden krytyk nie rozpozna jej jako phishingu - co maksymalizuje zwodniczosc wiadomosci.

Aby ocenic skutecznosc frameworka, autorzy zaimplementowali zestaw **obroncow maszynowych (machine-based defenders)** trzech typow: klasyczne uczenie maszynowe (SVM, XGBoost, Random Forest z cechami TF-IDF), modele jezykowe pre-trenowane (BERT, RoBERTa, GPT-2) oraz duze modele jezykowe (GPT-4 w trybie in-context learning, chain-of-thought i dedykowany prompt ChatSpamDetector). E-maile SpearBota masowo omijaja te detektory. Dodatkowo przeprowadzono **badanie z udzialem ludzi** (20 uczestnikow z wyksztalceniem w cyberbezpieczenstwie) oceniajace czytelnosc i zwodniczosc wiadomosci, potwierdzajace, ze wygenerowane e-maile sa bardzo czytelne i skutecznie oszukuja ludzi, czesto przewyzszajac pod tym wzgledem realne e-maile phishingowe z zestawu Nigerian.

Autorzy wygenerowali korpus **1 000 e-maili spear-phishingowych** (50 wirtualnych studentow i 50 wirtualnych pracownikow, kazdy z 10 roznymi strategiami phishingowymi) i deklaruja udostepnienie kodu, modeli obroncow oraz datasetu do celow badawczych. Praca ma jednoznacznie ofensywno-defensywny charakter: ujawnia zagrozenie, by uzasadnic potrzebe silniejszych mechanizmow obronnych i szkolen swiadomosciowych.

## Kluczowe Wnioski

- **Petla generator-krytyk drastycznie zwieksza zwodniczosc**: bez krytyka detektor ICL wykrywa 70,3% e-maili; z jednym krytykiem GPT-4 spada do 59,4%; z pelnym zestawem wielu krytykow SpearBot osiaga najnizsza wykrywalnosc (Findings 4).
- **Jailbreak promptowy jest wysoce skuteczny**: 66% e-maili udaje sie wygenerowac od razu za pierwszym razem, 91% w ciagu pieciu prob - mimo ze GPT-4 bez jailbreaka wprost odmawia generowania phishingu.
- **E-maile SpearBota niemal calkowicie omijaja obroncow ML i PLM**: najlepszy obronca ML (XGBoost) osiaga zaledwie 21,70% accuracy, a obroncy PLM (BERT/GPT-2/RoBERTa) spadaja do 3,00% / 1,00% / 2,20% accuracy - to oznaka silnego przeuczenia (overfitting) do starych zbiorow.
- **Obroncy LLM sa najlepsi, ale wciaz slabi**: in-context learning (ICL) osiaga najwyzsze 45,00% accuracy wobec SpearBota, chain-of-thought 22,00%, ChatSpamDetector 21,30% (Findings 2). ICL jest najskuteczniejsza metoda detekcji.
- **Strategia phishingowa wplywa na wykrywalnosc**: dla CoT najtrudniejsza do wykrycia jest "Confirmation of Personal Information" (17%), a najlatwiejsza "Offering Help" (27%); dla ICL relacja sie odwraca - wzorce rozpoznawania LLM mozna zmieniac demonstracjami ICL (Findings 3).
- **Wysoka czytelnosc i zwodniczosc dla ludzi**: czytelnosc e-maili SpearBota przewyzsza nawet realne e-maile Nigerian; wynik zwodniczosci (Q3) wynosi 2,2 vs 1,3 dla Nigerian-Phish i jest na poziomie legalnych e-maili (Findings 5). Manualna kontrola: oceniajacy uznali 93%, 89% i 95% e-maili za phishing (Findings 1).
- **Bardzo niski koszt ataku**: sredni koszt wygenerowania jednego e-maila to 0,1518 USD (student) i 0,1278 USD (pracownik) - nieporownywalnie taniej niz reczne tworzenie przez czlowieka.

## Metodologia

Framework SpearBot (Algorithm 1) sklada sie z dwoch glownych faz:

1. **Przygotowanie danych** - aby nie wykorzystywac danych realnych osob, GPT-4 generuje wirtualne profile (Name, Age, Gender, Hobby, Job/Company dla pracownikow, Educational qualification/University dla studentow), inspirowane cechami z Xu et al. (2023). Powstaje 50 profili studentow i 50 pracownikow z zachowaniem rownowagi plci. Rownolegle GPT-4 generuje **10 strategii phishingowych** (m.in. Authority Impersonation, Scarcity and Urgency, Curiosity Provocation, Fake Notifications, Confirmation of Personal Information, Tailored Content).

2. **Inicjalizacja przez jailbreak (Mg)** - wieloturowy prompt promptowego (nie tokenowego) jailbreaku: atakujacy podszywa sie pod studenta cyberbezpieczenstwa prowadzacego "badania naukowe", najpierw pytajac o motywacje i strategie psychologiczne (zapytania nieszkodliwe), a nastepnie zadajac wygenerowania e-maila z konkretnymi danymi osobowymi i strategia, z falszywym, "autentycznie wygladajacym" linkiem (http/www). Model, "wierzac" w cel edukacyjny, generuje poczatkowy e-mail y^0_i.

3. **Optymalizacja oparta na krytyce (critique-based optimization)** - wygenerowany e-mail jest oceniany przez wielu krytykow LLM (M_jk), kazdy zwraca decyzje (p_k in {True, False}) wraz z uzasadnieniem (r_k) w formacie XML. Jesli ktorykolwiek krytyk uzna e-mail za phishing, uzasadnienia trafiaja do generatora przez prompt regeneracyjny ("ukryj intencje subtelniej, by uniknac detekcji, ale zachowaj atrakcyjnosc linku"). Petla iteruje do momentu, gdy wszyscy krytycy zwroca False, lub do limitu T = 10 iteracji.

**Konfiguracja**: generator i krytycy to GPT-4 (gpt-4-1106-preview), Claude-3-Sonnet (claude-3-sonnet-20240229) oraz ChatGPT (gpt-3.5-turbo-1106); temperatura = 1.0 dla zwiekszenia roznorodnosci.

**Ewaluacja maszynowa**: obroncy trenowani na zmiksowanych szesciu publicznych zbiorach (split 8:1:1), metryki Precision/Recall/F1/Accuracy. PLM trenowane na pojedynczym GPU Tesla V100, Adam, lr 3e-5, batch 16, max dlugosc 256.

**Ewaluacja ludzka**: 20 uczestnikow, kwestionariusz z trzema pytaniami (czytelnosc, "czy maszyna", zagrozenie/zwodniczosc) w skali 0-4; kazdy ocenia 15 e-maili Nigerian-phish, 15 Nigerian-legit i 15 wygenerowanych przez SpearBota.

## Glowne Koncepcje

- **Spear-phishing** - wysoce ukierunkowana, spersonalizowana forma phishingu wymierzona w konkretne osoby/podmioty; tradycyjnie kosztowna do recznego tworzenia, co LLM radykalnie obnizaja.
- **Generative-Critique (generator-krytyk)** - adwersarialna petla, w ktorej jeden LLM generuje tresc, a inne LLM ja krytykuja, napedzajac iteracyjne ulepszanie az do ominiecia detekcji; rdzen wkladu pracy.
- **Jailbreak promptowy (prompt-level)** - obejscie zabezpieczen LLM przez semantycznie sensowne, socjotechniczne prompty (kontra jailbreak tokenowy, kosztowny i nieinterpretowalny); SpearBot stosuje wersje promptowa.
- **Safety alignment / RLHF / safety filter** - mechanizmy "wyrownania" LLM z wartosciami ludzkimi, ktore jailbreak ma obejsc.
- **Strategia phishingowa** - czynnik psychologiczny obnizajacy czujnosc ofiary (np. pilnosc, ciekawosc, autorytet, wzajemnosc); 10 strategii wygenerowanych przez GPT-4.
- **Obroncy maszynowi (machine-based defenders)** - trzy klasy detektorow: ML (TF-IDF + SVM/XGBoost/RF), PLM (BERT/RoBERTa/GPT-2 z warstwa klasyfikacji), LLM (ICL, CoT, ChatSpamDetector).
- **Overfitting detektorow** - wytrenowane modele osiagaja ~97-99% na starych zbiorach, ale zalamuja sie na nowych, LLM-owych e-mailach, co ujawnia kruchosc obecnych obroncow.

## Wyniki

**Obroncy ML (accuracy na SpearBot vs srednia na 6 zbiorach):**
- SVM: 16,00% (vs 97,85%), XGBoost: 21,70% (vs 97,80%), Random Forest: 9,70% (vs 97,71%). Precyzja zawsze 100% (SpearBot zawiera wylacznie e-maile phishingowe).

**Obroncy PLM (accuracy na SpearBot vs srednia):**
- BERT: 3,00% (vs 99,26%), GPT-2: 1,00% (vs 99,65%), RoBERTa: 2,20% (vs 99,53%) - dramatyczny spadek wskazujacy na przeuczenie.

**Obroncy LLM (accuracy na SpearBot vs srednia):**
- In-context Learning: 45,00% (vs 80,85%) - najlepszy obronca wobec SpearBota.
- Chain-of-Thought: 22,00% (vs 88,87%).
- ChatSpamDetector: 21,30% (vs 93,32%).

**Ablacja krytykow (detektor ICL):** brak krytyka 70,3% wykrywalnosci -> GPT-4 jako krytyk 59,4% -> pelny SpearBot najnizsza wartosc.

**Analiza generacji:** jailbreak skuteczny w 66% za pierwszym razem, 91% w ciagu 5 prob; tylko 11% e-maili omija krytykow w jednej rundzie, wiekszosc wymaga do 5 rund krytyki (rozklad: 1 runda 11,0%, 2 rundy 43,5%, 3 rundy 30,0%, 4 rundy 13,2%, 5 rund 2,3%).

**Koszt:** srednio 6 618 tokenow (generacja) / 972 (detekcja) na e-mail studencki; 5 462 / 927 na e-mail pracowniczy; koszt jednostkowy 0,1518 / 0,1278 USD.

**Ewaluacja ludzka (srednie wyniki):** czytelnosc (Q1) SpearBota 2,8 przewyzsza Nigerian-Phish (2,3) i jest blisko Nigerian-Legi (2,7); "nie wyglada jak maszyna" (Q2) 2,5 vs 2,0; zwodniczosc/zagrozenie (Q3, wyzsze = postrzegane jako bezpieczniejsze) 2,2 vs 1,3 dla Nigerian-Phish - e-maile SpearBota sa postrzegane jako bezpieczne na rowni z legalnymi, czyli skutecznie maskuja zagrozenie.

**Studium przypadku:** e-mail podszywajacy sie pod "Google Developers Team" (strategia Authority Impersonation) skierowany do developera Google omija WSZYSTKIE zaimplementowane modele obronne, kazdy klasyfikuje go jako legalny. Dodatkowe przyklady (Appendix A): zaproszenie na "Bridge Builders Webinar" dla inzyniera budownictwa oraz zaproszenie do "Chemistry Community".

## Przydatne Cytaty

- "When a phishing email is identified by the critic, SpearBot refines the generated email based on the critique feedback until it can no longer be recognized as phishing, thereby enhancing its deceptive quality." (Abstract, s. 1)
- "Considering the weakness of token-level jailbreak, we adopt the idea of prompt-level jailbreak, and propose specific prompts for spear-phishing email generation." (Sec. 2.2, s. 3)
- "If any of Mjk respond with pk = True together with the reason rk, the reasons are fed into the model Mg to regenerate the spear-phishing emails considering the reasons... Then the procedure would be iterated until all pk equal False or the iteration time equals the predefined limit T." (Sec. 4.4, s. 6)
- "Adjust the message content for the reasons, hide its intent more subtly to prevent detection by malicious content detectors, and make sure it is still attractive enough for the recipient to click on the link." (Regeneration Prompt, s. 6)
- "The XGBoost defender registers only a 21.70% accuracy rate when confronted with phishing emails produced by SpearBot... This poor performance suggests that the model fails to recognize spear-phishing emails as malicious, instead mistaking them for legitimate communications." (Sec. 5.5, s. 8)
- "We observe a percent of 66% in the phishing emails can be directly generated within one time. By repeating to query GPT-4, the emails are mostly generated within five times (91%)." (Sec. 5.9, s. 10)
- "The deception scores for SpearBot are significantly higher than those for Nigerian-Phish (scoring 2.2 compared to 1.3) and are on par with legitimate Nigerian emails." (Sec. 6.2, s. 12)

## Datasety

Zbiory publiczne wykorzystane do **treningu obroncow** (statystyki z Table 4):
- **CEAS_08** (2008): 21 842 phish / 17 312 legit / 39 154 total
- **Enron** (2006): 12 411 / 4 005 / 16 416
- **Ling** (2000): 2 401 / 458 / 2 859
- **Nazario** (2005-2022): 1 565 / 1 500 / 3 065
- **Nigerian** (1998-2008): 3 331 / 3 000 / 6 331 - zrodlo e-maili odniesienia w badaniu z ludzmi
- **Assassin / SpamAssassin** (2002-2006): 1 718 / 4 091 / 5 809

**Dataset wygenerowany w pracy**: korpus **1 000 e-maili spear-phishingowych** (50 wirtualnych studentow + 50 wirtualnych pracownikow x 10 strategii), z syntetycznymi profilami osobowymi wygenerowanymi przez GPT-4. Autorzy deklaruja publiczne udostepnienie kodu, modeli obroncow i datasetu (Sec. 8 Availability).

*(Brak odpowiadajacych plikow w `datasets/` - kandydaci do utworzenia: `ceas-08.md`, `enron-email.md`, `ling-spam.md`, `nazario-phishing.md`, `nigerian-fraud.md`, `spamassassin.md`, `spearbot-generated-emails.md`.)*

## Powiazane Tematy

- Jailbreaking LLM (prompt-level vs token-level): Chao et al. 2023 (PAIR), Liu et al. 2023, Shah et al. 2023 (persona modulation), Deng et al. 2024 (Masterkey)
- LLM-generated phishing: Roy et al. 2023 (From chatbots to phishbots), Bethany et al. 2024 (lateral spear phishing w organizacji), Heiding et al. 2023 (LLM vs human phishing)
- Detekcja phishingu oparta na LLM: Koide et al. 2024 (ChatSpamDetector), Champa et al. 2024 (punkty awarii detekcji)
- LLM jako krytycy: McAleese et al. 2024 (LLM critics help catch LLM bugs)
- Podatnosc na spear-phishing i personalizacja: Xu et al. 2023 (personalized persuasion), Wang et al. 2012, Rajivan & Gonzalez 2018
- Czynniki ludzkie w phishingu: Dhamija et al. 2006 (Why phishing works), Desolda et al. 2021
- Mechanizmy obrony / guardrails: RLHF (Ouyang et al. 2022), Safe RLHF (Dai et al. 2023), Llama Guard (Inan et al. 2023)
- Kierunki rozszerzen (future work): generowanie szkolen swiadomosciowych, phishing SMS/web, optymalizacja zlosliwych promptow/kodu przez petle krytyki

## Notatki
