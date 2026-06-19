"""cascadebench.features — ekstrakcja cech ze strumienia zdarzen (parametryzowana grafem).

Wspolne dla detektorow: cechy 1-hop, kontekst kaskady (burst/recency/propagacja), cechy wolumenowe
(COMPA), cechy strukturalne wezla. Rytm liczony przez graph.in_rhythm (realny lub syntetyczny).
"""
from __future__ import annotations

from collections import Counter, defaultdict
from typing import List

import numpy as np

from .graph import Graph, in_rhythm

WINDOW = 2


def index_traffic(events):
    recv = defaultdict(set); sent = defaultdict(set)
    for s, v, b, _l in events:
        recv[b].add(v); sent[b].add(s)
    return recv, sent


def onehop(graph: Graph, events: List, seed: int) -> np.ndarray:
    X = []
    for s, v, b, _l in events:
        cs = graph.neighbors(v)
        X.append([1.0 if s in cs else 0.0,
                  1.0 if in_rhythm(graph, s, b, seed) else 0.0,
                  float(len(cs)), float(len(graph.neighbors(s)))])
    return np.asarray(X, np.float32)


def context(graph: Graph, events: List, seed: int) -> np.ndarray:
    recv, sent = index_traffic(events)
    X = []
    for s, v, b, _l in events:
        cs = graph.neighbors(v); deg_v = max(1, len(cs))
        f1 = [1.0 if s in cs else 0.0, 1.0 if in_rhythm(graph, s, b, seed) else 0.0,
              float(len(cs)), float(len(graph.neighbors(s)))]
        recent = set()
        for bb in range(max(0, b - WINDOW), b + 1):
            recent |= recv.get(bb, set())
        burst = len((cs - {s}) & recent) / deg_v
        recency = 0.0
        for bb in range(max(0, b - WINDOW), b):
            if s in recv.get(bb, set()):
                recency = 1.0; break
        prop = len((cs - {s}) & {x for bb in range(max(0, b - WINDOW), b + 1)
                                 for x in sent.get(bb, set())}) / deg_v
        X.append(f1 + [burst, recency, prop])
    return np.asarray(X, np.float32)


def compa(events: List) -> np.ndarray:
    pair = Counter((s, v) for s, v, _b, _l in events)
    sb = Counter((s, b) for s, _v, b, _l in events)
    st = Counter(s for s, _v, _b, _l in events)
    X = []
    for s, v, b, _l in events:
        X.append([1.0 / (1.0 + pair[(s, v)]), 1.0 / (1.0 + sb[(s, b)]), float(st[s])])
    return np.asarray(X, np.float32)


def hopper(graph: Graph, events: List, seed: int) -> np.ndarray:
    """Cechy w duchu Hoppera (Ho i in. 2021): detekcja \emph{sciezki ruchu}. Zdarzenie podejrzane,
    gdy nadawca byl niedawno OSIAGNIETY (precursor przyczynowy --- czesc lancucha), RUSZA z~rozmachem
    do RZADKIEGO odbiorcy i~BEZ benign wyjasnienia (poza rytmem). Adaptacja do danych graf+czas ---
    bez tresci maila (URL/lure z~oryginalu sa niedostepne), wiec kodujemy strukturalno-czasowy rdzen
    sygnatury Hoppera."""
    recv, sent = index_traffic(events)
    dest_pop = Counter(v for _s, v, _b, _l in events)          # popularnosc v jako odbiorcy
    out_win = defaultdict(set)                                  # (s,b) -> zbior celow w oknie (rozmach ruchu)
    for s, v, b, _l in events:
        for bb in range(b, b + WINDOW + 1):
            out_win[(s, bb)].add(v)
    X = []
    for s, v, b, _l in events:
        precursor = 0.0                                        # czy s otrzymal cos w [b-W, b-1] (osiagniety)
        for bb in range(max(0, b - WINDOW), b):
            if s in recv.get(bb, set()):
                precursor = 1.0; break
        fan = float(len(out_win.get((s, b), ())))              # rozmach ruchu nadawcy w oknie
        rare_dest = 1.0 / (1.0 + dest_pop[v])                  # rzadki odbiorca (Hopper: rzadki cel)
        unexplained = 0.0 if in_rhythm(graph, s, b, seed) else 1.0   # brak benign wyjasnienia (poza rytmem)
        hop_sig = precursor * unexplained                      # sygnatura: ruch w lancuchu bez wyjasnienia
        X.append([precursor, fan, rare_dest, unexplained, hop_sig])
    return np.asarray(X, np.float32)


def node_features(graph: Graph, events: List) -> np.ndarray:
    import torch
    n = len(graph); idx = graph.index
    indeg = Counter(v for _s, v, _b, _l in events)
    outdeg = Counter(s for s, _v, _b, _l in events)
    X = torch.zeros(n, 3)
    for u, i in idx.items():
        X[i, 0] = len(graph.neighbors(u)); X[i, 1] = indeg.get(u, 0); X[i, 2] = outdeg.get(u, 0)
    X = torch.log1p(X)
    return (X - X.mean(0, keepdim=True)) / X.std(0, keepdim=True).clamp(min=1e-6)
