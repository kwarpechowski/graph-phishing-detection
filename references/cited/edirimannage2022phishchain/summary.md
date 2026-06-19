---
title: "PhishChain: A Decentralized and Transparent System to Blacklist Phishing URLs"
date: 2022-01-01
authors: "Shehan Edirimannage, Mohamed Nabeel, Charith Elvitigala, Chamath Keppitiyagama"
status: read
doi: "arXiv:2202.07882"
category: "Security"
tags:
  - phishing-urls
  - blacklisting
  - blockchain
  - crowdsourcing
  - truth-inference
  - pagerank
  - project/graph-phishing-detection
---

# PhishChain: A Decentralized and Transparent System to Blacklist Phishing URLs

## Metadane
- **Autorzy**: Shehan Edirimannage, Mohamed Nabeel, Charith Elvitigala, Chamath Keppitiyagama
- **Rok**: 2022
- **Zrodlo**: The Web Conference 2022 (WWW), demo
- **DOI/Link**: https://arxiv.org/abs/2202.07882
- **Status**: read
- **Kategoria glowna**: Security

## Streszczenie
Praca prezentuje PhishChain - przejrzysty i zdecentralizowany system blacklistowania adresow URL phishingowych. Autorzy wskazuja ograniczenia istniejacych crowdsourcingowych blacklist (PhishTank, CryptoScamDB, APWG): scentralizowana architektura z pojedynczym punktem awarii, brak przejrzystosci procesu etykietowania, brak zachet do uczestnictwa oraz podatnosc na manipulacje. Ilustruja niespojnosci w przypisywaniu etykiet w PhishTank (URL oznaczony jako phishing mimo zgodnej weryfikacji, lub odwrotnie - oznaczenie bez zadnej weryfikacji).

PhishChain wykorzystuje technologie blockchain dla zapewnienia przejrzystosci i decentralizacji - zaden pojedynczy podmiot nie kontroluje listy, a wszystkie operacje sa zapisywane w niezmiennym, rozproszonym rejestrze. System stosuje algorytm odkrywania prawdy (truth discovery) oparty na PageRank, ktory przypisuje kazdemu URL score phishingowy na podstawie crowdsourcingowych ocen. Jako zacheta do dobrowolnego uczestnictwa uzytkownikom przyznawane sa punkty umiejetnosci (skill points) za udzial w weryfikacji.

## Kluczowe Wnioski
- Scentralizowane blacklisty maja pojedynczy punkt awarii i brak przejrzystosci.
- Blockchain zapewnia niezmienny, audytowalny rejestr decyzji blacklistowych.
- Algorytm truth discovery oparty na PageRank agreguje crowdsourcingowe oceny w score phishingu.
- Mechanizm skill points motywuje rzetelne uczestnictwo i ogranicza manipulacje.

## Metodologia
Architektura zdecentralizowana na blockchain ze smart kontraktami; crowdsourcingowa weryfikacja URL; algorytm rankingowy PageRank-based do truth inference przypisujacy scoring phishingu; system reputacji/zachet (skill points). Implementacja demonstracyjna.

## Glowne Koncepcje
- **Blacklisting** - lista zablokowanych URL phishingowych.
- **Truth discovery / inference** - agregacja sprzecznych ocen w wiarygodna etykiete.
- **PageRank-based scoring** - rankingowanie wiarygodnosci/zlosliwosci.
- **Skill points** - reputacyjna zacheta dla uczestnikow crowdsourcingu.

## Relevancja dla graph-phishing-detection
PhishChain pokazuje grafowe/rankingowe podejscie (PageRank) do oceny zlosliwosci URL - pokrewne propagacji sygnalow w grafie wiedzy domenowej. Mechanizm truth inference z zaszumionych, sprzecznych ocen jest analogiczny do reżimu rzadkich i niepewnych etykiet w projekcie, gdzie modele GNN musza radzic sobie z niedoskonalym ground truth. Praca (wspolautorzy pokrywaja sie z cGraph) dostarcza kontekstu dla baseline opartych na rankingu grafowym oraz uwypukla problem jakosci etykiet phishingowych, kluczowy dla ewaluacji leak-aware.
