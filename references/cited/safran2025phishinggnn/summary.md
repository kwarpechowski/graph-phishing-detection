---
title: "PhishingGNN: Phishing Email Detection Using Graph Attention Networks and Transformer-Based Feature Extraction"
date: 2025-01-01
authors: "Mejdl Safran, Abdulbaset Musleh"
status: read
doi: "10.1109/ACCESS.2025.3592135"
category: "Security"
tags:
  - phishing-detection
  - email-security
  - graph-attention-networks
  - transformers
  - distilbert
  - gnn
  - project/graph-phishing-detection
---

# PhishingGNN: Phishing Email Detection Using Graph Attention Networks and Transformer-Based Feature Extraction

## Metadane
- **Autorzy**: Mejdl Safran, Abdulbaset Musleh (King Saud University; Al-Qalam University)
- **Rok**: 2025
- **Źródło**: IEEE Access
- **DOI/Link**: 10.1109/ACCESS.2025.3592135
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
PhishingGNN to hybrydowy model detekcji phishingowych e-maili, który integruje analizę semantyki tekstu z modelowaniem strukturalnym relacji w danych e-mailowych. Autorzy wychodzą z obserwacji, że phishing wymaga jednoczesnego ujęcia zarówno znaczenia treści, jak i zależności strukturalnych (metadane, relacje wewnątrz wiadomości), które tradycyjne klasyfikatory pomijają.

Architektura łączy DistilBERT do kontekstowej ekstrakcji cech tekstowych z grafowymi sieciami uwagi (Graph Attention Networks, GAT). Treść i metadane e-maila są przekształcane w struktury grafowe (relacyjne reprezentacje treści), a GNN analizuje interakcje tekstowe, zachowując efektywność obliczeniową. To pozwala wykrywać subtelne wzorce phishingowe trudne do uchwycenia metodami czysto tekstowymi.

Model oceniono na rozszerzonym zbiorze CEAS_08 (39 154 próbek: 17 312 nie-phishing i 21 842 phishing) osiągając: dokładność 0,9939, zrównoważone precision/recall/F1 na poziomie 0,99 oraz AUC 1,00. Walidacja krzyżowa na korpusie Nazario potwierdziła odporność (dokładność 0,9910) i przewagę nad współczesnymi podejściami few-shot. Wkłady to: architektura transformer-GNN łącząca rozumowanie semantyczne i strukturalne, nowa metoda grafowej reprezentacji e-maila oraz walidacja potwierdzająca skalowalność.

## Kluczowe Wnioski
- Połączenie DistilBERT (semantyka) i GAT (struktura) daje bardzo wysoką skuteczność detekcji phishingu.
- Grafowa reprezentacja treści e-maila ujmuje wzorce pomijane przez metody czysto tekstowe.
- Wysoka skuteczność cross-dataset (CEAS_08 → Nazario) świadczy o odporności i generalizacji.
- Architektura zachowuje efektywność obliczeniową przy zachowaniu modularności.

## Metodologia
Pipeline: ekstrakcja cech tekstowych przez DistilBERT, konstrukcja grafu z treści i metadanych e-maila, propagacja przez warstwy GAT z mechanizmem uwagi nad sąsiedztwem, klasyfikacja binarna phishing/legit. Ewaluacja na CEAS_08 (rozszerzony) z walidacją krzyżową na korpusie Nazario; metryki accuracy, precision, recall, F1, AUC.

## Główne Koncepcje
- **Graph Attention Network (GAT)**: ważona agregacja sąsiadów z uwagą.
- **Transformer-GNN hybrid**: fuzja reprezentacji semantycznej i strukturalnej.
- **Grafowa reprezentacja e-maila**: zamiana treści/metadanych w graf relacyjny.
- **Walidacja cross-dataset**: test generalizacji między korpusami.

## Relevancja dla graph-phishing-detection
To bezpośredni punkt odniesienia dla projektu — pokazuje, że grafowa detekcja phishingu (PhishingGNN) realnie przewyższa podejścia bazujące tylko na treści. Stanowi mocny baseline content+structure dla e-maili i wyznacza poprzeczkę metryczną (F1≈0,99, AUC≈1,0 na CEAS_08), którą projekt powinien analizować krytycznie — szczególnie pod kątem ryzyka przeszacowania na zbiorach o łatwym rozdzieleniu klas oraz testu na realnych etykietach BEC. W odróżnieniu od pojedynczego e-maila, projekt graph-phishing-detection celuje w grafy wieloźródłowe (komunikacja/domena/transakcje) i niezmienniki proweniencji/dynamiki kaskady; PhishingGNN dostarcza jednak gotowy wzorzec łączenia enkodera transformerowego z GAT, który można rozszerzyć o krawędzie temporalne i międzywiadomościowe.
