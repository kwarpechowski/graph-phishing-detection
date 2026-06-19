---
title: "Checklista submisji — Computers & Security"
tags:
  - project/graph-phishing-detection
  - submission
---

# Checklista submisji do *Computers & Security*

Na podstawie **Guide for Authors** (sugestie.pdf, ISSN 0167‑4048).
Status odnosi sie do **`release/paper/main.tex`** (wersja EN, klasa `cas-sc`, kompiluje sie 0 bledow, 94 ref).

Legenda: 🔴 blokujace / 🟡 wymagane przed submisja / 🟢 zalecane · `[ ]` do zrobienia · `[x]` zrobione

> **Stan na 2026‑06‑18 (zweryfikowany na plikach `release/paper/`):**
> ✅ Abstract przyciety do **~250 slow** (licznik surowy 254, `texcount` ≈245) · ✅ wszystkie **5 highlightow ≤85 znakow**
> (zmierzone: 83/84/77/69/81) · ✅ back‑matter w `main.tex` komplet: **CRediT**, **competing interests**, **funding**,
> **data availability**, **deklaracja generatywnej AI** · ✅ pisownia **konsekwentnie amerykanska** (brak form brytyjskich)
> · ✅ bibliografia 120 wpisow, **113 z identyfikatorem** (59 DOI + 54 arXiv); 7 bez DOI to USENIX/NDSS/NeurIPS/SNAP,
> ktore realnie nie maja DOI · ✅ zlozony kompletny folder repo (`release/`) z kodem, LaTeX i referencjami.
>
> **POZOSTAJE blokujace:** (1) decyzja o moratorium AI/ML; (2) 2 znaczniki `% TODO` w `main.tex` wymagajace danych
> od autora: **zrodlo finansowania** (l. 91) + **URL/DOI repozytorium** dla data availability (l. 96).

---

## 0. 🔴 KRYTYCZNE — decyzja o zakresie (PRZED dalsza praca)

- [ ] **🔴 Moratorium na AI/ML.** Guide (str. 2–3): *„we have instituted a moratorium on
  consideration of submissions that feature AI or ML as significant components."* Nasza praca stosuje
  **GNN / temporalny GNN (TGN‑lite) / LightGBM** — pod scislym czytaniem **ryzyko desk‑reject**. Decyzja:
  - [x] Opcja A: **przeramowano** narracje na *koncept grafu wiedzy domenowej* + *pomiar podatnosci* +
    *metodologia leak‑aware*. Dodane w `introduction.tex` jawne zdanie: modele uczone (TGN‑lite, gradient
    boosting) = *„off‑the‑shelf measurement instruments"*, wklad pojeciowo‑metodologiczny, NIE nowa
    architektura ML. Metodologia juz ramuje modele jako porownywane detektory. **(decyzja venue dalej otwarta)**
  - [ ] Opcja B: **alternatywny venue** bez moratorium ML (sprawdzic w `venues/`).
  - [ ] Skonsultowac z promotorem (B. Ksiezopolski) przed wyborem.
- [ ] **🟢 Kryptologia** — nie eksponowac watku blockchainowego w related work
  (`daluwatta2022cgraph`, `edirimannage2022phishchain` zostawic jako marginalia).

---

## 1. 🟡 Limit dlugosci (twardy)

- [x] **≤ 12 000 slow** lacznie — zmierzono ~10,6k (8,1k tekst + ~2,5k bib). **Miesci sie** (margines ~1,4k).
- [x] **Abstract ≤ 250 slow** — **przyciety** (`en/absbody.tex`, ~245 wg texcount). Zachowana teza 98/2% +
  2 niezmienniki + podatnosc + leak‑aware.
- [ ] 🟢 Margines na tabele: rozwazyc przeniesienie 2–4 tabel sweepowych do **Appendix/Supplementary**
  (`tab:pinf`, `tab:hopper`, `tab:blindspot`, `tab:labelnoise`, `tab:baserate`, `tab:topo`) — opcjonalne,
  gdyby licznik podbil sie po korekcie. ~17 tabel to duzo (Guide: *„use tables sparingly"*).

---

## 2. 🟡 Wymagane deklaracje

- [x] **Deklaracja generatywnej AI** — dodana (`main.tex`, sekcja „Declaration of generative AI…",
  formula Elsevier: tlumaczenie + copy‑edit Claude, pelna odpowiedzialnosc autorow).
- [x] **Declaration of competing interests** — dodana (autorzy nie maja konfliktow). 🟡 Przy submisji
  wypelnic tez *declarations tool* i wgrac wynikowy `.docx`.
- [x] **CRediT author statement** — dodany jako sekcja back‑matter + `\credit{}` w froncie (oba autorzy).
- [~] **Funding** — zdanie obecne (default „did not receive any specific grant"). 🔴 **`% TODO` l. 91:
  potwierdzic z NASK/promotorem, czy grant finansowal prace** — jesli tak, podmienic.
- [~] **Data availability** — statement gotowy, odwoluje sie do DOI Zenodo. **Pakiet Zenodo przygotowany:**
  `.zenodo.json` (metadane), `CITATION.cff` (cytowanie), `make_zenodo_archive.ps1` → czysty zip **1.77 MB**
  (`paper/`+`code/`, **bez `references/` i cudzych PDF** — copyright). **POZOSTAJE Twoja akcja (3 kroki):**
  - [ ] 1. Zenodo → New upload → **Reserve DOI** (przed publikacja).
  - [ ] 2. Wgrac `graph-phishing-spear-detection-zenodo-v1.0.0.zip` (zbudowany skryptem) + Publish.
  - [ ] 3. Wstawic zarezerwowany DOI w **3 miejscach** `10.5281/zenodo.XXXXXXX`: `main.tex` (Data
    availability), `CITATION.cff`, `README.md`. (ORCID autorow w `.zenodo.json`/`CITATION.cff` — opcjonalnie.)
- [ ] 🟢 **Acknowledgements** — dodac jesli sa podziekowania.

## 3. 🟡 Strona tytulowa i front matter

- [x] Tytul zwiezly, informatywny, bez skrotow (EN title).
- [x] Autorzy + kolejnosc (Warpechowski, Ksiezopolski); afiliacje + kraj (Kozminski, NASK; Poland); e‑maile.
- [x] Autor korespondencyjny oznaczony (`\cormark[1]`, `\cortext`).
- [ ] **🟡 Sprawdzic**, czy kolejnosc autorow == kolejnosc w systemie submisji (nieodwracalne po submisji).

## 4. 🟡 Abstract / Keywords / Highlights

- [x] Abstract bez `\cite` — OK.
- [x] **Abstract ≤250 slow** — zrobione (~245).
- [x] Keywords: 8, po angielsku.
- [x] **Highlights: 5 punktow, KAZDY ≤85 znakow** — zweryfikowane (83/84/77/69/81), w `\begin{highlights}` +
  `highlights.txt`.
- [ ] 🟢 Graphical abstract (opcjonalny, 531×1328 px) — rozwazyc.

## 5. 🟡 Struktura artykulu

- [x] Sekcje numerowane (CAS) + `Section~\ref` daja numery (10 odwolan, zweryfikowane).
- [x] Abstract poza numeracja sekcji (CAS).
- [ ] 🟡 **Introduction** — sprawdzic, czy nie powiela related work (Guide: wstep bez szczegolowego przegladu lit.).
- [x] 🟡 **Discussion** — przyciete **8 → 4 cytowania** (Guide str. 16). Zostaly ho2019detecting +
  stringhini2015thataint (interpretacja) i bethany2024evaluating + pendlebury2019tesseract (future work);
  usuniete luo/butavicius/halevi/sturman (sa w related work, wiec nie znikaja z bib).
- [x] **Conclusion** standalone — OK.
- [ ] 🟢 **Vitae** — krotki bio ≤100 slow + zdjecie kazdego autora (osobny plik).

## 6. 🟡 Matematyka / Tabele / Rysunki

- [x] Rownania edytowalne (LaTeX), numerowane.
- [x] Tabele: booktabs, bez pionowych linii i cieniowania.
- [x] 🟡 **Kazda tabela i rysunek ma odwolanie** `\ref` — zweryfikowane skryptem; naprawiono 2 sieroty
  (`tab:fielddist` rozklad pol person + `fig:realgraph` graf 3D) dodajac odwolania w `methodology.tex`.
- [ ] **🟡 Rysunki jako OSOBNE pliki** przy submisji z numeracja `Figure_1…` wg kolejnosci.
  Mamy 12 wektorowych PDF w `release/paper/figures/` (juz angielskie) — zebrac/przenumerowac do pakietu submisji.
- [x] Format wektor PDF — OK.
- [x] 🟡 **Dostepnosc kolorow** (color‑blind) — zweryfikowane: slupki czerwien/niebieski
  (`#d62728`/`#1f77b4`, rozroznialne przy deuteranopii), heatmapa **RdYlBu** (nie RdYlGn), kategorie z
  etykietami tekstowymi. Brak kodowania czerwien/zielen → OK, regeneracja zbedna.

## 7. 🟡 Bibliografia

- [x] **Styl spojny** — author‑year `cas-model2-names` akceptowalny (Guide: dowolny spojny styl).
- [x] Cytowania w tekscie spojne (`\citep`/`\citet`).
- [x] **Identyfikatory**: **116/120** wpisow ma DOI/eprint. Wyszukano przez crossref/openalex
  (`paper-search`) i dodano 3 prawdziwe DOI: `halevi2015spearphishing`→`10.2139/ssrn.2544742` (SSRN),
  `zhang2018link`→`10.48550/arXiv.1802.09691`, `arp2022dos`→`10.48550/arXiv.2010.09470` (arXiv DOI, bo
  proceedings NeurIPS/USENIX bez DOI). Pozostale **4 bez DOI** (`cidon2019high`, `lin2021phishpedia` —
  USENIX; `egele2013compa` — NDSS; `leskovec2014snap` — kolekcja datasetow Krevl) **realnie nie maja DOI**
  (crossref potwierdzil „no doi"); DOI biblioteki SNAP `10.1145/2898361` dot. INNEJ pracy (Sosic), wiec
  NIE przypisany. Brak nie jest luka — wpisy maja komplet autor/tytul/rok/venue.
- [ ] 🟢 >6 autorow → pierwszych 6 + „et al." (sprawdzic dlugie listy w `.bib`).
- [ ] 🟢 @article: 21 bez `pages`, @inproceedings: 69 bez `pages` — uzupelnic gdzie latwo dostepne.

## 8. 🟢 Jezyk i inkluzywnosc

- [x] **Pisownia jednolita** — konsekwentnie **amerykanska** (organiz‑, behavior, labeled; 0 form brytyjskich).
- [ ] **🟡 Korekta jezykowa native** — tlumaczenie wierne, zalecany przeglad native/Elsevier Language Editing.
- [x] Single‑blind → autor NIE anonimizowany. OK.

## 9. 🟡 Pakiet submisji

- [ ] Jeden autor korespondencyjny z pelnymi danymi (e‑mail, adres, telefon).
- [ ] **Pliki zrodlowe**: `main.tex` + `en/*.tex` + `bibliography.bib` + `.bbl` + `cas-sc.cls` +
  `cas-common.sty` + `cas-model2-names.bst` + rysunki (osobne). PDF nie jest akceptowalnym zrodlem.
- [ ] Spell/grammar check.
- [x] Wszystkie ref cytowane (94 cytowane z 120 w `.bib`; bibtex drukuje tylko cytowane).
- [ ] Pozwolenia na materialy chronione prawem autorskim (jesli sa).
- [ ] APC / open access — ustalic model.
- [ ] 🟢 Rozwazyc preprint na **SSRN** (nie liczy sie jako prior publication).

---

## Podsumowanie priorytetow (stan 2026‑06‑18)

| # | Zadanie | Priorytet | Status |
|---|---------|-----------|--------|
| 1 | Decyzja: moratorium AI/ML — przeramowanie vs inny venue | 🔴 blokujace | ⏳ czeka na decyzje + promotora |
| 2 | `% TODO` zrodlo finansowania (NASK/grant?) | 🔴 | ⏳ czeka na dane autora |
| 3 | DOI repozytorium (Zenodo) → data availability | 🔴 | 🟡 pakiet gotowy; czeka na reserve+upload (3 kroki) |
| 4 | Abstract ≤250 slow | 🔴 | ✅ zrobione |
| 5 | Highlights ≤85 znakow ×5 | 🔴 | ✅ zrobione |
| 6 | Deklaracja generatywnej AI + competing interests + CRediT | 🔴/🟡 | ✅ zrobione |
| 7 | Przyciac cytowania w Discussion (8 → 4) | 🟡 | ✅ zrobione |
| 8 | Kazda tabela/rysunek ma `\ref` (2 sieroty naprawione) | 🟡 | ✅ zrobione |
| 9 | Dostepnosc kolorow rysunkow (color‑blind) | 🟡 | ✅ zweryfikowane |
| 10 | Reframe pod moratorium (modele = narzedzia, nie wklad ML) | 🔴 | ✅ zrobione (Opcja A) |
| 11 | Korekta native EN | 🟡 | ⏳ przed submisja (human/Elsevier) |
| 12 | Pakiet submisji (osobne rysunki Figure_1.., pliki .tex) | 🟡 | ⏳ przy submisji (venue) |

> Legenda statusu: ✅ zrobione · ⏳ otwarte · `[~]` = statement obecny, ale z otwartym `% TODO`.
