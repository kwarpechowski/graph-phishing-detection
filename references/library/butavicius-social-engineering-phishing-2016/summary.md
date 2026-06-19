---
title: "Breaching the Human Firewall: Social Engineering in Phishing and Spear-Phishing Emails"
date: 2016-01-01
authors: "Marcus Butavicius, Kathryn Parsons, Malcolm Pattinson, Agata McCormac"
status: read
doi: ""
category: "Security"
tags:
  - phishing-detection
  - spear-phishing
  - social-engineering
  - human-factors
  - authority-principle
  - cialdini
  - signal-detection-theory
  - cognitive-impulsivity
  - user-study
  - project/spear-phishing-context
---

# Breaching the Human Firewall: Social Engineering in Phishing and Spear-Phishing Emails

## Metadane
- **Autorzy**: Marcus Butavicius, Kathryn Parsons, Malcolm Pattinson, Agata McCormac
- **Rok**: 2015 (ACIS 2015, Adelaide; opublikowano 2016)
- **Źródło**: Australasian Conference on Information Systems (ACIS) 2015 (Defence Science and Technology Group / University of Adelaide)
- **DOI/Link**: brak (open-access proceedings ACIS 2015)
- **Status**: read
- **Kategoria główna**: Security
- **Tagi**: `#phishing-detection` `#spear-phishing` `#social-engineering` `#human-factors` `#authority-principle` `#cialdini` `#signal-detection-theory` `#cognitive-impulsivity` `#user-study`

## Streszczenie

Artykuł bada wpływ trzech strategii inżynierii społecznej (ang. social engineering) na ocenę bezpieczeństwa linków w emailach przez użytkowników. Badanie opiera się na taksonomii Cialdiniego (2007): trzy testowane strategie to **autorytet** (authority), **niedobór** (scarcity) i **dowód społeczny** (social proof). Badanie kontrolowane z 121 studentami australijskiego uniwersytetu — uczestnicy oceniali 12 emaili (genuine, phishing, spear-phishing) z każdą z 4 warunków inżynierii społecznej (authority, scarcity, social proof, none) na 5-punktowej skali bezpieczeństwa linku.

Kluczowy wynik: **autorytet** jest najskuteczniejszą strategią przekonywania użytkowników, że link jest bezpieczny. W warunku autorytetu uczestnicy nie byli w stanie w ogóle wykrywać spear phishingu (A'=0.5 — poziom przypadku). Spear phishing okazał się znacznie trudniejszy do wykrycia niż standardowy phishing: 71% emaili spear phishingowych oceniano błędnie jako bezpieczne (vs. 37% dla phishingu), a 45% uczestników nie wykryło żadnego z emaili spear phishingowych. Użytkownicy mniej impulsywni w podejmowaniu decyzji (wyższy wynik CRT) byli skuteczniejsi w obu rodzajach detekcji.

Autorzy zastosowali podejście Signal Detection Theory (SDT), co pozwoliło zmierzyć zarówno zdolność dyskryminacji (A') jak i bias (B''), w odróżnieniu od badań "real phishing", które mierzą tylko hits bez false alarms.

## Kluczowe Wnioski

- **Autorytet = poziom przypadku dla spear phishingu**: A'=0.5 przy strategii authority — uczestnicy nie mogą rozróżnić spear phishingu od genuine emaili gdy obecny jest autorytet
- **71% błędnych ocen spear phishingu**: użytkownicy oznaczają spear phishing jako bezpieczny znacznie częściej niż standardowy phishing (37%)
- **45% uczestników nie wykryło żadnego spear phishingu**: alarming failure rate w warunkach laboratoryjnych (gdzie czujność jest podwyższona)
- **Dowód społeczny najłatwiej wykrywalne**: A'=0.67 dla spear phishing (social proof) vs. 0.5 (authority) — paradoks: cecha najtrudniejsza do użycia przez atakujących jest najłatwiejsza do wykrycia
- **Impulsywność koreluje z podatnością**: CRT ρ=-.23 (spear-phishing) i ρ=-.30 (phishing) — mniej impulsywni = lepsze wykrywanie
- **Social engineering w phishingu = kontrproduktywne**: dla standardowego phishingu obecność jakiejkolwiek strategii SE obniżała skuteczność vs. brak strategii — efekt "inokulacji" (users are desensitized to generic SE in phishing)

## Metodologia

Badanie laboratoryjne (ACIS 2015): 121 studentów australijskiego uniwersytetu (finanse, rachunkowość, marketing, zarządzanie). 12 emaili × 4 warunki SE = każdy uczestnik oceniał 12 emaili (genuine × 4 warunki, phishing × 4 warunki, spear-phishing × 4 warunki — pero każdy email miał dokładnie jeden warunek SE). Emaile phishingowe: prawdziwe phishe z ostatnich 6 miesięcy dostarczone przez IT security uczelni. Emaile genuine + spear-phishing: bazowane na prawdziwych emailach studentów; spear-phishing różnił się od genuine tylko złośliwym linkiem.

Miara zależna: "Link Safety" judgment (5-pt Likert). Analiza: 4×3 Repeated Measures ANOVA + Signal Detection Theory (A' i B'' — nieparametryczne miary dyskryminacji i biasu). Indywidualne różnice: Cognitive Reflection Test (CRT, Frederick 2005) jako miara impulsywności poznawczej. Korelacja SDT–CRT przez Spearmana.

## Główne Koncepcje

- **Inżynieria społeczna (social engineering)**: psychologiczna manipulacja ludźmi w celu ujawnienia informacji lub wykonania akcji (Mitnick et al. 2002)
- **Cialdini's principles**: 6 zasad perswazji; badanie testuje 3: authority (autorytet), scarcity (niedobór), social proof (dowód społeczny)
- **Authority principle**: ludzie są skłonni wykonywać polecenia autorytetów (CEO, CIO) — najskuteczniejsza technika SE w phishingu
- **Scarcity principle**: ograniczona dostępność zwiększa atrakcję (oferty czasowe, limitowane miejsca)
- **Social proof**: inni już skorzystali → ty też powinieneś (np. "1000 studentów wyjedzie za granicę")
- **SDT (Signal Detection Theory)**: mierzy dyskryminację (A') i bias (B''); A'=0.5 = chance, A'=1.0 = perfect; B'' < 0 = bias ku "fraudulent", B'' > 0 = bias ku "genuine"
- **CRT (Cognitive Reflection Test)**: test mierzący tendencję do refleksyjnego (vs. impulsywnego) podejmowania decyzji
- **Dual processing**: "central" mode (analityczny) vs. "peripheral" mode (heurystyczny); CRT aktywuje central mode
- **Whaling**: spear phishing skierowany do senior executives i high-ranking staff

## Wyniki

| Email type | Strategia SE | A' (dyskryminacja) | B'' (bias) |
|-----------|-------------|-------------------|------------|
| Spear-phishing | Authority | **0.50** (chance) | 0.00 |
| Spear-phishing | Scarcity | 0.51 | 0.01 |
| Spear-phishing | Social Proof | **0.67** (best) | 0.25 |
| Spear-phishing | None | 0.59 | 0.07 |
| Phishing | Authority | 0.72 | 0.14 |
| Phishing | Scarcity | 0.82 | 0.03 |
| Phishing | Social Proof | **0.90** (best) | 0.06 |
| Phishing | None | 0.67 | 0.11 |

Średnie: spear-phishing A'=0.59 (słaba detekcja), phishing A'=0.78 (lepsza detekcja). Wszystkie B'' > 0 → bias ku "genuine".

Ogólne wskaźniki: genuine emails 77% poprawnie ocenione; spear-phishing 71% błędnie ocenione jako safe; phishing 37% błędnie ocenione jako safe.

Korelacja CRT: phishing ρ=-.30 (p=.001), spear-phishing ρ=-.23 (p=.014), genuine emails ρ=-.01 (n.s.).

## Przydatne Cytaty

> "When the fraudulent email used the authority strategy, participants were unable to reliably detect spear-phishing at all (A' = 0.5)." (str. 6)

> "Almost half the sample (45%) did not judge any of the links in the spear-phishing emails as unsafe." (str. 4)

> "The use of any social engineering technique in phishing emails appeared less effective than no technique at all. This may be due to an inoculation effect against this type of persuasion, whereby users have been exposed to so many generic phishing emails that attempt to use social engineering, that they have learnt to resist the persuasion attempt." (str. 7)

> "Participants who were less impulsive in decision making were more likely to judge the links in phishing emails as more dangerous." (str. 7)

> "the heightened effort and vigilance expected of users in a lab-based experiment should improve performance in comparison to real life" — co sprawia, że wyniki są tym bardziej alarmujące (str. 7)

## Datasety

Brak publicznych datasetów — badanie eksperymentalne z emailami dostarczonymi przez IT security australijskiego uniwersytetu (nie opublikowane).

## Powiązane Tematy

- Cialdini (2007) — taksonomia 6 zasad perswazji: baza teoretyczna dla inżynierii społecznej w phishingu
- Jagatic et al. (2007) — "Social Phishing": 4.5× wyższy sukces z kontekstem społecznym z Facebooka
- Parsons et al. (2013) — poprzednie badanie tej samej grupy z SDT do oceny detekcji phishingu
- CRT (Frederick 2005) — test impulsywności poznawczej jako predyktor podatności
- Dual processing theory (Chaiken et al. 1996) — central vs. peripheral mode: podstawa dla treningu odporności na SE
- Halevi et al. (2015) — spear phishing in the wild: personality traits a podatność na ataki
- Wright et al. (2014) — sprzeczne wyniki: authority jako najsłabsza technika SE (podczas gdy tu najsilniejsza)
- LLM-generated spear phishing: czy authority-framed AI-generated emails byłyby jeszcze skuteczniejsze?
- Impulsywność a trening: CRT jako narzędzie aktywujące analityczne przetwarzanie przed oceną emaila

## Notatki

