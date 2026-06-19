---
title: "Evaluating Large Language Models' Capability to Launch Fully Automated Spear Phishing Campaigns: Validated on Human Subjects"
date: 2024-01-01
authors: "Fred Heiding, Simon Lermen, Andrew Kao, Bruce Schneier, Arun Vishwanath"
status: read
doi: "arXiv:2412.00586"
category: "Security"
tags:
  - spear-phishing
  - large-language-models
  - social-engineering
  - phishing-detection
  - osint
  - ai-automation
  - project/graph-phishing-detection
---

# Evaluating Large Language Models' Capability to Launch Fully Automated Spear Phishing Campaigns: Validated on Human Subjects

## Metadane
- **Autorzy**: Fred Heiding, Simon Lermen, Andrew Kao, Bruce Schneier, Arun Vishwanath (uwaga: w reference.md klucz `bethany2024evaluating`, lecz PDF wskazuje powyższych autorów)
- **Rok**: 2024
- **Źródło**: arXiv (Harvard Kennedy School / Avant Research Group)
- **DOI/Link**: https://arxiv.org/abs/2412.00586
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca empirycznie ocenia zdolność dużych modeli językowych (LLM) do prowadzenia w pełni zautomatyzowanych kampanii spear phishing, walidując wyniki na 101 ludzkich uczestnikach. Porównano cztery grupy e-maili: grupa kontrolna (zwykły spam, 12% click-through), e-maile pisane przez ludzkich ekspertów (54%), w pełni zautomatyzowane przez AI (54%) oraz AI z human-in-the-loop (56%). Ataki AI wypadły na równi z ekspertami i 350% lepiej niż grupa kontrolna — istotny postęp względem badań sprzed roku, gdy AI wymagało interwencji człowieka.

Autorzy zbudowali własne narzędzie automatyzujące cały proces: rekonesans OSINT (scraping cyfrowego śladu celu przez agenta GPT-4o), tworzenie spersonalizowanych profili podatności, generowanie e-maili (głównie Claude 3.5 Sonnet z technikami perswazji Cialdiniego i V-Triad) oraz śledzenie kliknięć. Zebrane informacje OSINT były trafne i użyteczne w 88% przypadków, błędne tylko w 4%. Praca wyróżnia trzy poziomy personalizacji (brak/semi/hiper); narzędzie celuje w hiper-personalizację (Kategoria 3).

W części obronnej autorzy testują LLM do detekcji intencji e-maili. Claude 3.5 Sonnet osiągnął 97,25% wykrywalności na 363 e-mailach phishingowych przy zerowym poziomie fałszywych alarmów; "priming for suspicion" (pytanie wprost o podejrzliwość) poprawia detekcję bez wzrostu FP. Analiza ekonomiczna pokazuje, że AI zwiększa rentowność phishingu nawet 50-krotnie; pełna automatyzacja jest zawsze najbardziej opłacalna, a koszt to ~4 centy/e-mail.

## Kluczowe Wnioski
- W pełni zautomatyzowane AI spear phishing dorównuje ekspertom (54% vs 54% click-through), 350% nad grupą kontrolną.
- Rekonesans OSINT przez AI jest trafny w 88% przypadków; human-in-the-loop staje się zbędny jakościowo.
- LLM (Claude 3.5 Sonnet) wykrywa phishing z 97,25% trafnością i zerowym FP, zwłaszcza przy "priming for suspicion".
- AI obniża koszty i zwiększa rentowność phishingu do 50x; guardraile łatwo obchodzić prostą zmianą promptu.
- Detekcja sygnaturowa (signature detection) staje się przestarzała wobec unikatowo personalizowanych e-maili.

## Metodologia
Eksperyment z ludźmi (n=101, IRB, analiza mocy, alpha=0,05, power=0,80), randomizacja do 4 grup. Metryka: click-through rate. Część detekcyjna: 5 LLM na 20 e-mailach, następnie Claude/GPT-4o na 381 e-mailach (18 legit, 363 phishing, 9 kategorii). Analiza ekonomiczna: model rentowności z parametrem konwersji q, koszty czasu/API, t-testy.

## Główne Koncepcje
- **Hiper-personalizacja**: e-mail oparty na konkretnych projektach, zainteresowaniach i współpracownikach celu.
- **OSINT-driven reconnaissance**: agent LLM buduje profil podatności z publicznego śladu cyfrowego.
- **Priming for suspicion**: pytanie modelu wprost o podejrzliwość podnosi detekcję bez wzrostu fałszywych alarmów.
- **Personalized vulnerability profile**: obosieczny — atak i obrona mogą korzystać z tego samego profilu.

## Relevancja dla graph-phishing-detection
Praca jest mocną motywacją dla projektu: pokazuje, że AI-generowany spear phishing/BEC jest tani, skalowalny i nieodróżnialny od legalnych wiadomości, co podważa detekcję sygnaturową i treściową — dokładnie luka, którą podejście grafowe ma wypełnić (struktura komunikacji/proweniencja zamiast samej treści). Pipeline OSINT→profil→generacja jest bezpośrednio zbieżny z założeniami projektu personalized-phishing-defense (rodzic GP). Hiper-personalizowane, syntetyczne ataki stanowią realistyczny model zagrożenia (threat model) i materiał do generowania adwersarialnych przykładów do testowania odporności GNN, a wnioski o detekcji LLM (Claude 97% Recall, zerowy FP) wyznaczają silny baseline treściowy, który model grafowy musi uzupełnić sygnałem strukturalnym, zwłaszcza w ewaluacji Recall@FPR1%.
