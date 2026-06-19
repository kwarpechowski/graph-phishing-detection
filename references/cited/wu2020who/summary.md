---
title: "Who Are the Phishers? Phishing Scam Detection on Ethereum via Network Embedding"
date: 2020-01-01
authors: "Jiajing Wu, Qi Yuan, Dan Lin, Wei You, Weili Chen, Chuan Chen, Zibin Zheng"
status: read
doi: "10.1109/TSMC.2020.3016821"
category: "Security"
tags:
  - ethereum
  - phishing-detection
  - network-embedding
  - trans2vec
  - blockchain
  - project/graph-phishing-detection
---

# Who Are the Phishers? Phishing Scam Detection on Ethereum via Network Embedding

## Metadane
- **Autorzy**: Jiajing Wu, Qi Yuan, Dan Lin, Wei You, Weili Chen, Chuan Chen, Zibin Zheng
- **Rok**: 2020
- **Źródło**: IEEE Transactions on Systems, Man, and Cybernetics: Systems
- **DOI/Link**: 10.1109/TSMC.2020.3016821
- **Status**: read
- **Kategoria główna**: Security

## Streszczenie
Praca proponuje metodę wykrywania oszustw phishingowych na Ethereum poprzez eksplorację rekordów transakcji. Phishing stanowi ponad 50% cyberprzestępstw na Ethereum od 2017 r. i jest poważnym zagrożeniem dla bezpieczeństwa handlu w ekosystemie blockchain. Autorzy najpierw zbierają oznakowane adresy phishingowe z dwóch autoryzowanych witryn i rekonstruują sieć transakcji na podstawie zebranych rekordów.

Następnie, uwzględniając kwotę transakcji i znacznik czasu, proponują nowy algorytm osadzania sieci o nazwie trans2vec, który wydobywa cechy adresów na potrzeby późniejszej identyfikacji phishingu. Wreszcie stosują jednoklasową maszynę wektorów nośnych (one-class SVM) do klasyfikacji węzłów na normalne i phishingowe. Wyniki eksperymentów pokazują, że metoda działa skutecznie na Ethereum oraz że trans2vec przewyższa istniejące algorytmy SOTA w ekstrakcji cech sieci transakcyjnych. Jest to pierwsze badanie detekcji phishingu na Ethereum z wykorzystaniem osadzania sieci, dostarczające wglądu w to, jak osadzać cechy wielkoskalowych sieci transakcyjnych.

## Kluczowe Wnioski
- Pierwsza praca o detekcji phishingu na Ethereum oparta na osadzaniu sieci (network embedding).
- trans2vec włącza kwotę i czas transakcji do losowych spacerów, poprawiając jakość osadzeń.
- One-class SVM skutecznie klasyfikuje węzły w warunkach silnej nierównowagi klas.
- trans2vec przewyższa wcześniejsze metody osadzania w ekstrakcji cech sieci transakcyjnych.

## Metodologia
Zbieranie oznakowanych adresów phishingowych i rekonstrukcja sieci transakcji Ethereum; algorytm trans2vec rozszerzający losowe spacery o wagi oparte na kwocie i znaczniku czasu transakcji w celu uczenia osadzeń wierzchołków; klasyfikacja adresów za pomocą one-class SVM. Ewaluacja porównawcza z istniejącymi metodami osadzania.

## Główne Koncepcje
- **trans2vec**: osadzanie sieci ważone kwotą i czasem transakcji.
- **Sieć transakcji Ethereum**: graf adresów połączonych transakcjami.
- **One-class SVM**: klasyfikacja przy silnej nierównowadze klas.
- **Network embedding**: uczenie reprezentacji wierzchołków grafu.

## Relevancja dla graph-phishing-detection
Praca jest podstawowym, często cytowanym baseline dla detekcji phishingu na grafach transakcyjnych Ethereum i bezpośrednim poprzednikiem metod grafowo-uczonych (TSGN, GNN). Dla projektu istotne jest włączenie atrybutów czasowych i ilościowych do uczenia reprezentacji wierzchołków oraz traktowanie detekcji jako problemu silnie niezbalansowanego (one-class). Stanowi punkt odniesienia, który projekt stara się przewyższyć nowoczesnymi modelami GNN na grafie wiedzy domenowej, oraz inspirację dla ważenia krawędzi atrybutami transakcji.
