---
title: "PhishChain: A Decentralized and Transparent System to Blacklist Phishing URLs"
date: 2022-01-01
authors: "Shehan Edirimannage, Mohamed Nabeel, Charith Elvitigala, Chamath Keppitiyagama"
status: read
tags: []
---
# PhishChain: A Decentralized and Transparent System to Blacklist Phishing URLs

## Metadane
- **Autorzy**: Shehan Edirimannage, Mohamed Nabeel, Charith Elvitigala, Chamath Keppitiyagama
- **Rok**: 2022
- **Źródło**: WWW (The Web Conference 2022), April 25-29, 2022
- **DOI/Link**: arXiv:2202.07882v1 [cs.CR]
- **Status**: read
- **Tagi**: #blockchain #phishing-blacklist #decentralization #crowd-sourcing #truth-discovery #smart-contracts #quorum #transparency #consortium-blockchain

## Streszczenie

PhishChain to zdecentralizowany i transparentny system do blacklistingu phishingowych URLi wykorzystujący technologię blockchain. Adresuje fundamentalne ograniczenia istniejących centralized blacklists (PhishTank, CryptoScamDB, APWG): (1) single point of failure, (2) brak transparentności w decision-making, (3) brak incentive dla uczestników, (4) podatność na manipulacje. System wykorzystuje Quorum consortium blockchain z Istanbul Byzantine Fault Tolerance consensus, smart contracts (Solidity), i novel PageRank-based truth discovery algorithm.

Kluczowa innowacja to truth discovery algorithm oparty na verifier-verifier graph construction wykorzystując "follower" relationships (verifier v1 follows v2 jeśli v1 weryfikuje URL przed v2). PageRank applied na tym grafie oblicza verifier importance (ranks 0-1), które są używane do weighted voting dla URL phishing score. Evaluacja na PhishTank data (17k phishing, 6k non-phishing, Jan-Dec 2020) pokazuje 95.45% accuracy, 96.74% precision, 94.31% recall - outperforming EM (93.71%) i GLAD (93.98%) truth discovery algorithms.

System incentivizes participation przez skill points (nie cryptocurrency) based on verifier reputation i proportion of correctly labeled URLs, inspirowane StackOverflow gamification. Consortium blockchain (7 validation nodes w demo) zapewnia decentralization gdzie każdy może participate, ale no single authority kontroluje blacklist.

## Kluczowe Wnioski

- **Decentralization Achievable**: Blockchain consortium (Quorum) eliminates single point of failure; 7 validation nodes w demo, envisioned deployment: organizations targeted by phishers (PayPal, Apple, Microsoft, Facebook)
- **Transparency vs Existing Systems**: PhishTank shows inconsistent labeling (URL marked phishing despite all 5 verifiers saying phishing; URL marked safe despite no verification) - PhishChain records all operations immutably w distributed ledger
- **PageRank Truth Discovery Superior**: Novel PR-based algorithm outperforms traditional truth discovery (EM, GLAD) on real PhishTank data: 95.45% acc vs 93.71-93.98%, addressing sparse verification problem (handful verifiers per URL, nie majority)
- **Skill Points Incentive Model**: Non-monetary gamification (like StackOverflow) encourages voluntary participation; skill points based on reputation score + accuracy of labels
- **Smart Contract Functionality**: Three categories: (1) user management, (2) URL management, (3) URL verification; implemented in Solidity 0.5.0 on Quorum
- **Real-World Dataset Validation**: PhishTank 2020 data (23k URLs, Jan-Dec) used for evaluation; cleaned dataset: 6k phishing + 6k non-phishing (balanced)
- **Dynamic Phish Score**: Score changes z każdym nowym vote (truth discovery re-invoked); timeline pokazuje evolution (e.g., 0.64 after 3rd vote → 0.35 after 4th vote)

## Metodologia

### System Architecture
1. **Blockchain Network Module**:
   - **Quorum consortium blockchain**: Private/permissioned dla targeted organizations
   - **Istanbul Byzantine Fault Tolerance (IBFT)** consensus: Assumes potentially malicious participants
   - **Validator nodes** vs **normal nodes**: Validators validate transactions (blockchain block verification), normal nodes read-only
   - **Tessera**: Transaction management dla Quorum network
   - **Demo setup**: 7 validation nodes, each with copy of blockchain ledger

2. **Smart Contract Module**:
   - **Solidity version 0.5.0**
   - **Three categories**:
     1. User management contracts
     2. URL management contracts
     3. URL verification contracts
   - **Immutable recording**: All URL data (URLs, votes, status) consistent i hardened from unauthorized modifications

3. **Truth Discovery Module**:
   - **Problem**: Existing truth discovery algorithms (database community) assume majority of verifiers respond to each task ← NOT true dla URLs (PhishTank retrospective: handful verify każdy URL mimo thousands total verifiers)
   - **Solution**: PageRank-based algorithm on verifier-verifier graph
   - **Graph Construction**:
     - **Follower relationship**: Verifier v1 follows v2 dla URL jeśli v1 verifies BEFORE v2
     - **Directed edge**: v1 → v2 created
     - **Intuition**: More followers → more recognition from peers → higher importance
   - **PageRank Application**: Computes rank (0-1 real value) dla każdego verifier node
   - **Weighted Voting**: Ranks używane do calculate weighted score dla każdego URL
   - **Phishing Score**: Weighted score of phishing vs non-phishing verifiers; positive score = phishing URL
   - **Skill Points Assignment**: Based on (1) verifier reputation score from truth discovery + (2) proportion of correctly labeled URLs
   - **Minimum votes requirement**: At least 3 votes przed invoking truth discovery

4. **API Services Module**:
   - Facilitates communication z blockchain network
   - Demo web application consumes this API

### Evaluation Dataset
- **Source**: PhishTank URLs (January 1 - December 23, 2020)
- **Raw data**: 17,000 phishing URLs, 6,000 non-phishing URLs
- **Scraped additional info**: Verifiers i order of verification dla każdego URL
- **Balanced evaluation set**: 6,000 URLs from each class (12k total)
- **Comparison baselines**: EM, GLAD (popular truth discovery algorithms)

### Main Functions
1. **URL Submission**: Anyone can submit suspected phishing URL (requires accompanying valid email referencing URL to limit abuse)
2. **URL Verification**: Users verify if URL is phishing/non-phishing (Figure 4 UI)
3. **URL Lookup**: Query URL status, phish score, verification timeline

## Główne Koncepcje

- **Consortium Blockchain**: Permissioned blockchain where pre-selected organizations (consortium members) run validator nodes; balances decentralization with control (vs public blockchain like Bitcoin/Ethereum)

- **Truth Discovery**: Algorithm inferring ground truth from potentially conflicting crowd-sourced assessments; accounts for varying verifier expertise/reliability

- **PageRank-based Truth Discovery**: Novel adaptation of Google's PageRank dla verifier reputation; verifier-verifier graph constructed from temporal verification order ("follower" relationships); ranks represent verifier importance/trustworthiness

- **Verifier-Verifier Graph**: Directed graph where edge v1→v2 means v1 verified URL before v2 ("v1 follows v2"); captures real-world peer relationships i implicit trust signals

- **Skill Points (Non-Monetary Incentive)**: Gamification inspired by StackOverflow; participants earn points based on reputation + accuracy; addresses voluntary participation problem (PhishTank/APWG: only handful contribute despite thousands registered)

- **Immutable Ledger**: Blockchain property ensuring all operations (URL submissions, votes, status changes) permanently recorded i tamper-proof; enables full audit trail

- **Istanbul Byzantine Fault Tolerance (IBFT)**: Consensus algorithm tolerating up to (n-1)/3 malicious nodes in n-node network; suitable dla consortium where some members may be compromised

- **Smart Contracts**: Self-executing code on blockchain; implements PhishChain logic (user/URL management, verification) without central authority

- **Quorum**: Enterprise-focused Ethereum fork by ConsenSys; supports private transactions, consortium governance, higher throughput than public Ethereum

- **Phish Score**: Continuous value (not binary) representing phishing likelihood; computed as weighted score of verifier votes using PR-based ranks; positive = phishing, negative = legitimate

- **Transparency Gap in PhishTank**: Demonstrates inconsistent labeling examples (Figure 1): URL marked phishing despite all verifiers agreeing it's phishing; URL marked safe despite zero verification - raises questions about decision process

## Wyniki

### Truth Discovery Algorithm Performance (Table 1)
**Dataset**: PhishTank 2020 balanced set (6k phishing + 6k non-phishing)

| Algorithm | Accuracy | Precision | Recall |
|-----------|----------|-----------|--------|
| **Our Approach (PR-based)** | **95.45%** | **96.74%** | **94.31%** |
| EM | 93.71% | 91.01% | 97.75% |
| GLAD | 93.98% | 91.72% | 97.39% |

**Analysis**:
- **Accuracy improvement**: +1.74% vs EM, +1.47% vs GLAD
- **Precision significantly higher**: 96.74% vs 91.01-91.72% (fewer false positives)
- **Recall slightly lower**: 94.31% vs 97.39-97.75% (trade-off: fewer false positives at cost of some false negatives)
- **Balanced performance**: F1-score likely highest (precision-recall balance)

**Why PR-based outperforms**:
- EM i GLAD assume majority verification per task ← violated w sparse crowd-sourcing
- PR-based leverages verifier relationships i temporal ordering ← captures implicit trust

### Demonstration Use Cases

**Use Case 1: URL Verification (Figure 4)**
- User submits verdict (phishing/non-phishing)
- Validator nodes validate transaction via IBFT consensus
- Transaction recorded on blockchain (Figure 5)
- Minimum 3 votes required before truth discovery invocation

**Use Case 2: URL Detailed Dashboard (Figure 6)**
- **Example scenario**:
  - User 1 submits URL
  - Users 3, 4 verify as phishing
  - Users 2, 5 verify as non-phishing
  - **System assigned phish score: 0.3452** (positive → phishing URL)
- Dashboard shows all votes, timestamps, phish score evolution

**Use Case 3: Verification Graph & Timeline (Figures 7, 8)**
- **Skill points**: User 1 has 153 points (highest in example)
- **Dynamic scoring example**:
  - After 3rd vote: phish score 0.64 (phishing)
  - After 4th vote: phish score 0.35 (still phishing, but lower confidence)
  - Score changes z każdym vote (truth discovery re-invoked)
- **Analyst transparency**: Can trace how system arrived at decision

### System Deployment (Figure 3 - Cakeshop Explorer)
- **7 validation nodes** running Quorum
- **5779 blocks** in demo blockchain (Figure 3 screenshot)
- **Consortium members** (envisioned): PayPal, Facebook, Microsoft, Apple, etc.
- **Real-world incentive**: Organizations targeted by phishers benefit from collective defense

## Przydatne Cytaty

> "While it [PhishTank] has been instrumental in maintaining a ledger of phishing URLs, it suffers from several limitations: (1) centralized architecture with a single point of failure, (2) lack of transparency, (3) lack of incentive to participate and (4) prone to manipulations." (str. 1)

> "Figure 1 shows inconsistent assignment of final labels to URLs in PhishTank. The figure on the left shows a URL marked as phishing even though all 5 crowd sourced verifiers ascertain it is phishing. The figure on the right, on the other hand, shows that a URL is marked as not phishing even though no one has verified it. It is not clear how PhishTank arrived at the final decision and raises concerns on the transparency." (str. 1)

> "We observe that existing truth discovery algorithms developed by the database community are performing poorly on our problem as these algorithms assume that the majority of the verifiers respond to each URL verification task, which is not true for verifying URLs. Our retrospective analysis of PhishTank URLs show that only a handful of verifiers verify a given URL even though there are thousands of them altogether." (str. 2)

> "We define verifier v1 follows v2 for a given URL if v1 verifies the URL before v2. A directed edge from v1 to v2 is created in this case. The generated graph represent real world relationships among users which captures how users are following others and how they are being followed." (str. 2)

> "Note that in PhishChain system, we enforce transparency and consistency on the data by following the consensus algorithm. In other words, all the data related to URLs (URLs themselves, votes, status) on the blockchain is consistent and hardened from unauthorized modifications." (str. 2)

> "The motivation for introducing skill points is inspired from the question answering systems such as StackOverflow and StackExchange. Such systems show that even though participants do not receive any monetary benefits by contributing, these participants attain various 'expertise' levels that have far more significance in their respective domains." (str. 4)

## Datasety

- **PhishTank 2020 Dataset** (custom collection, 23k URLs):
  - Collection period: January 1 - December 23, 2020
  - Raw data: 17,000 phishing URLs, 6,000 non-phishing URLs
  - Scraped metadata: verifiers, verification order, timestamps
  - Evaluation set: Balanced 12k URLs (6k phishing + 6k non-phishing)
  - Used for: Truth discovery algorithm comparison (PR vs EM vs GLAD)

## Powiązane Tematy

- **Blockchain for Cybersecurity**: Decentralized threat intelligence sharing, immutable audit trails
- **Consortium Blockchain Governance**: Balancing decentralization with organizational control; validator node selection strategies
- **Truth Discovery i Crowd Wisdom**: Aggregating conflicting assessments from verifiers with varying expertise; Sybil attack resistance
- **Gamification for Security Participation**: Non-monetary incentives (skill points, reputation) vs cryptocurrency-based systems
- **Comparison to Existing Blockchain Blacklists**: PhishLedger (private, no crowd-sourcing), CrowdBC i ZebraLancer (rely on cryptocurrency)
- **Smart Contract Security**: Solidity vulnerabilities, gas optimization dla URL verification operations
- **PageRank Applications Beyond Search**: Reputation systems, social network analysis, fraud detection
- **Sparse Crowd-Sourcing Challenges**: Minority verification problem; existing algorithms assume majority participation
- **Transparency vs Privacy Trade-offs**: Public blockchain ledger (all votes visible) vs privacy concerns dla verifiers
- **Byzantine Fault Tolerance in Practice**: IBFT performance, validator selection, malicious node detection
- **Future Work - Manipulation Resistance**: Reputation/recommender system defenses against Sybil attacks, collusion, strategic voting
- **Integration with Browser/Email Clients**: Real-time URL checking against PhishChain blacklist
- **Scalability Considerations**: Blockchain throughput limitations, off-chain computation (truth discovery server), sharding strategies
- **Cross-Domain URL Blacklisting**: Extending beyond phishing (malware distribution, scam sites, copyright infringement)

## Notatki

**Strengths**:
- Novel PageRank-based truth discovery dla sparse crowd-sourcing (outperforms EM, GLAD)
- Demonstrates real-world transparency gap w PhishTank (Figure 1 examples)
- Practical consortium deployment model (targeted organizations form alliance)
- Non-monetary incentive (skill points) addresses voluntary participation problem
- Immutable audit trail enables verification of decision process

**Limitations (acknowledged in Discussion)**:
- **Assumes non-malicious users**: "we assume that users do not maliciously try to manipulate the truth discovery based system"
- **Future work needed**: Defending against manipulation using reputation/recommender system mechanisms [3]
- **4-page demo paper**: Limited technical depth on smart contract implementation, IBFT tuning, scalability analysis
- **Small-scale demo**: 7 validation nodes; real consortium deployment challenges not discussed
- **Email requirement for URL submission**: May limit submission volume, requires validation mechanism

**Observations**:
- **Sparse verification confirmed**: PhishTank retrospective shows handful verify każdy URL mimo thousands total verifiers
- **Dynamic scoring**: Phish score changes z każdym vote (0.64 → 0.35 example) - may cause instability in early stages
- **StackOverflow inspiration**: Proven gamification model dla voluntary participation
- **Consortium viability**: Organizations like PayPal, Facebook heavily targeted → strong incentive to participate

**Potential Research Directions**:
- Sybil attack resistance dla skill point manipulation
- Scalability testing: millions of URLs, thousands of concurrent verifiers
- Integration z automated phishing detection (ML models) - hybrid crowd+AI approach
- Longitudinal study: Does skill point system sustain participation over time?
- Cross-blockchain interoperability: Sharing blacklists across different consortium blockchains
- Privacy-preserving verification: Zero-knowledge proofs dla hiding verifier identities while maintaining accountability

