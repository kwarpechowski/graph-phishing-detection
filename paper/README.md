# Paper sources

Elsevier **CAS** single-column manuscript (target journal: *Computers & Security*).

| File | Contents |
|------|----------|
| `main.tex` | Document entry point: front matter (title, authors, abstract inlined ≤250 words, highlights, keywords) + `\input{en/...}` + back-matter declarations + bibliography. |
| `en/introduction.tex` … `en/conclusion.tex` | The six manuscript sections. |
| `figures/` | 12 figures (PDF) referenced by the sections. |
| `bibliography.bib` | 94 cited references. |
| `highlights.txt` | Research highlights (each ≤85 characters), as a standalone submission file. |
| `cas-sc.cls`, `cas-common.sty`, `cas-model2-names.bst` | Elsevier CAS class and author-year bibliography style (bundled for self-contained build). |

## Build

```bash
pdflatex main
bibtex   main
pdflatex main
pdflatex main
```

## Notes for submission

- `main.tex` already contains the back-matter sections required by the journal: **CRediT statement**,
  **competing interests**, **funding**, **data availability**, and the **generative-AI declaration**.
  Two `% TODO` markers (funding source, data-repository URL/DOI) must be filled before submission.
- Citation style is Elsevier CAS author-year (`cas-model2-names`); *Computers & Security* accepts any
  consistent style.
- See `../SUBMISSION_CHECKLIST_CS.md` (repo root) for the full pre-submission checklist.
