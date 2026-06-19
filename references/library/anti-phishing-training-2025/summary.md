---
title: "Anti-Phishing Training (Still) Does Not Work: A Large-Scale Reproduction Study"
date: 2025-01-01
authors: "Andrew T. Rozema, James C. Davis"
status: read
category: "Security"
tags: []
---
# Anti-Phishing Training (Still) Does Not Work: A Large-Scale Reproduction Study

## Metadane
- **Autorzy**: Andrew T. Rozema, James C. Davis
- **Rok**: 2025
- **Źródło**: arXiv:2506.19899v3 [cs.CR]
- **DOI/Link**: https://arxiv.org/abs/2506.19899v3
- **Status**: read
- **Kategoria główna**: Security
- **Podkategorie**: Human Factors, Cybersecurity Training
- **Tagi**: #phishing-training #ineffectiveness #nist-phish-scale #human-factors #cybersecurity-awareness #reproduction-study #organizational-security

## Streszczenie

To large-scale reproduction study (N=12,511) w US-based fintech firm potwierdza nieefektywność szkoleń anti-phishing. Badanie wykorzystuje dwa różne podejścia treningowe (lecture-based vs interactive) i po raz pierwszy waliduje NIST Phish Scale na poziomie enterprise.

Kluczowe odkrycia: (1) Training nie wykazał statystycznie istotnych efektów na click rates (p=0.450) ani reporting rates (p=0.417), z negligible effect sizes (η²<0.01). (2) NIST Phish Scale successfully predicted user behavior - click rates wzrosły z 7.0% (easy lures) do 15.0% (hard lures), F(2,12086)=41.415, p<0.001. (3) Wprowadzono Organizational Inoculation Index - novel metric measuring organizational temporal resilience: 36-55% kampanii osiągnęło "inoculation" patterns (reports before clicks), niezależnie od individual training effectiveness.

Badanie potwierdza wcześniejsze wyniki Lain et al. (19,000+ employees) i Ho et al. (19,500+ healthcare) w nowym kontekście organizacyjnym, używając standardized difficulty measure. Implikacje: current phishing training approaches provide minimal protection; organizations need realistic expectations and should complement training with technical controls and incident response preparedness.

## Kluczowe Wnioski

- **Training nie działa**: Żadna training modality (lecture-only, interactive) nie wykazała statistically significant improvements w click reduction (p=0.450) lub reporting (p=0.417)
- **Effect sizes negligible**: Wszystkie training effects miały η²<0.01, indicating minimal practical value nawet gdy statistically significant
- **NIST Phish Scale works**: Pierwszy large-scale validation - difficulty strongly predicted behavior (7.0%→15.0% clicks easy→hard)
- **Organizational resilience exists**: 36-55% template-group combinations achieved "inoculation" (reports before clicks), independent of training
- **Interactive training nie lepszy**: Treatment B (lecture+interactive) nie wykazał higher reporting rates niż Treatment A (lecture-only)
- **Vendors can game metrics**: Używając low-difficulty lures można osiągnąć artificially low click rates (~2%) nie reprezentujące real threats
- **Compliance ≠ Security**: Regulation-compliant training zapewnia minimal operational security improvement

## Metodologia

**Study Design:**
- Two-factor between-subjects experiment
- Factor 1: Training Modality (3 conditions)
  - Treatment A: Lecture-based videos + quiz (n=6,023)
  - Treatment B: Lecture + interactive phishing exercises (~20 templates) (n=6,026)
  - Control Group: No training (n=462)
- Factor 2: Phishing Lure Complexity (NIST Phish Scale)
  - Easy: High cues/low alignment (5,721 emails)
  - Medium: Some cues/some alignment (2,279 emails)
  - Hard: Few cues/high alignment (4,511 emails)

**Subjects:**
- 12,511 full-time employees w US fintech firm
- Diverse cross-section: finance, technology, operations, customer service, admin
- Mandatory training (regulatory compliance)
- Stratified random sampling across departments
- Completion rates: 87.3%-89.1% (balanced across conditions)

**Procedure:**
1. Random assignment to training condition
2. 1-month window for training completion
3. Phishing simulations distributed within 3 months post-training
4. Each participant received ONE phishing email (randomly assigned template)
5. Metrics collected: open rate, click rate, report rate, timing

**NIST Phish Scale Assessment:**
- 19 phishing templates from vendor library
- Expert review: 3 IT security staff independently rated
- Two dimensions:
  - Phishing Cues: observable errors/inconsistencies (spelling, suspicious URLs, formatting)
  - Premise Alignment: relevance to organizational context
- Disagreements resolved through discussion + third rater

**Metrics:**
- Standard: Open Rate, Click-Through Rate (CTR), Reporting Rate
- Novel Temporal Metrics:
  - Individual Reporting Timeliness: time from deployment to report
  - Campaign Inoculation Status: binary (1 if first report < first click)
  - Organizational Inoculation Index (OII): t_first_click - t_first_report

**Analysis:**
- Two-way ANOVA: training modality × phishing difficulty
- Confirmatory: logistic regression for binary outcomes
- Both approaches yielded consistent conclusions

## Główne Koncepcje

- **NIST Phish Scale**: Standardized measure of phishing lure difficulty. Two dimensions: (1) Phishing Cues - observable errors that alert users (spelling, suspicious URLs, formatting), (2) Premise Alignment - relevance to recipient's organizational context. Higher alignment + fewer cues = most deceptive.

- **Organizational Inoculation Index (OII)**: Novel metric measuring organizational-level temporal security. OII = t_first_click - t_first_report. Positive values = "inoculation" (reports preceded clicks, enabling threat mitigation). Addresses Steves et al.'s research question: "Is time to first report sooner than time to first click?"

- **Training Modalities**: (1) Lecture-based - passive videos/readings + quiz, (2) Interactive - videos + scenario-based exercises identifying suspicious elements, (3) Just-in-time - real-time alerts during risky behavior. Study compared (1) vs (2).

- **Reproduction vs Replication**: Reproduction tests generalizability of phenomenon across different contexts (organizational, training approaches). Replication repeats identical procedures. This study = reproduction of training ineffectiveness findings.

- **Effect Size vs Statistical Significance**: Statistical significance (p<0.05) ≠ practical significance. Effect sizes (η²) measure variance explained. η²<0.01 = negligible practical value despite statistical significance due to large N.

- **Ecological Validity**: Lab studies have high experimental control but may lack real-world applicability. Real-world studies (like this) sacrifice some control for ecological validity - findings generalize better to operational environments.

## Wyniki

**H1 (Phish Scale Effect): SUPPORTED ✓**
- NIST Phish Scale strongly predicted user behavior
- F(2, 12086) = 41.415, p < 0.001, η² = 0.007
- Click rates by difficulty:
  - Easy: 7.0%
  - Medium: 8.7%
  - Hard: 15.0%
- First large-scale enterprise validation of NIST framework

**H2 (Training Impact - General): NOT SUPPORTED ✗**
- No significant training effect on click rates: F(2, 12086) = 0.800, p = 0.450
- No significant training effect on report rates: F(2, 12086) = 0.874, p = 0.417
- Click rates comparison:
  - Control Group: 9.8%
  - Training Only: 10.6%
  - Training + Exercise: 10.4%
- Report rates comparison:
  - Control Group: 8.9%
  - Training Only: 9.5%
  - Training + Exercise: 9.9%

**H3 (Interactive Training Effect): NOT SUPPORTED ✗**
- Interactive training (Treatment B) did NOT produce significantly higher reporting rates
- Differences were numerically modest and non-significant
- Contrasts with some prior work [16] but aligns with recent large-scale studies [43]

**H4 (Interaction Effect): NOT SUPPORTED ✗**
- No significant training × difficulty interaction for clicks: F(4, 12086) = 3.135, p = 0.014
- No significant training × difficulty interaction for reports: F(4, 12086) = 0.517, p = 0.723
- Marginal interaction: training may provide SOME protection against hardest emails
  - Training Only × Hard: -9.67 percentage points (p=0.002)
  - Training + Exercise × Hard: -9.09 percentage points (p=0.004)

**H5 (Reporting Timeliness): PARTIALLY SUPPORTED ~**
- Individual behavior: median time-to-report = 21 minutes (0.35 hours)
- 90% of reports within 18.8 hours
- Organizational Inoculation Index results (17 templates with both clicks & reports):
  - Overall: 52.9% achieved inoculation, median OII = +0.4 hours
  - Control: 66.7% inoculation, median OII = +0.3 hours
  - Training Only: 75% inoculation, median OII = +1.37 hours
  - Training + Exercise: 28.6% inoculation, median OII = -0.2 hours
- Differences NOT statistically significant (limited sample size)
- Successfully inoculated templates: median OII ~30 minutes

**Effect Sizes Summary:**
- Training effect: η² = 0.000 (negligible)
- Difficulty effect: η² = 0.007 (meaningful for prediction, though statistically "small")
- Training × Difficulty: η² = 0.001 (negligible)

**Key Pattern:**
- Overall click rate: 10.4%
- Overall report rate: 9.6%
- Click rates doubled (7.0% → 15.0%) as difficulty increased
- Training effects: all below η² = 0.01 (minimal practical impact)

## Przydatne Cytaty

> "After deploying regulation-compliant training programs to over 12,000 employees, we found no statistically significant main effects of training on either click rates (p=0.450) or report rates (p=0.417)." (str. 8)

> "The NIST Phish Scale successfully predicted user behavior. Phishing lure difficulty had a highly significant effect on click-through rates (F(2, 12086)=41.415, p < 0.001, η²=0.007), validating the scale's utility for measuring phishing complexity." (str. 6-7)

> "Organizations setting specific performance targets (such as click-through rates around 2%) may achieve these by using low-difficulty lures that fail to represent sophisticated attacks organizations actually face. This creates a misalignment between perceived and actual security posture." (str. 8)

> "These findings provide the first empirical measurement of organizational temporal security dynamics, responding to Steves et al.'s research question about whether 'time to first report is sooner than time to first click'. The results suggest that organizational-level protective behaviors operate independently of individual training effectiveness." (str. 7-8)

> "The small effect sizes we observed (η² < 0.01 for all main effects) indicate that even statistically significant improvements translate to minimal operational impact." (str. 8)

> "In security-sensitive environments, models with extremely high recall may overwhelm security teams with false positives. Organizations should complement training with other defense mechanisms rather than relying on awareness programs as primary protection." (str. 8)

## Datasety

- [NIST Phish Scale](../../datasets/nist-phish-scale.md) - First large-scale enterprise validation (N=12,511); click rates: 7.0% (easy) → 8.7% (medium) → 15.0% (hard); F(2,12086)=41.415, p<0.001
- **Vendor Phishing Template Library** - ~20 professional phishing templates used for interactive training and simulation (proprietary)
- **19 Evaluated Templates** - Expert-rated templates used in simulation (see Table 6 in paper for full breakdown)
  - 8 Easy templates (high cues/low alignment)
  - 3 Medium templates (some cues/some alignment)
  - 8 Hard templates (few cues/high alignment)

*Uwaga: Study uses proprietary vendor data and organizational training data - NIST Phish Scale is the only public framework/dataset*

## Powiązane Tematy

- Phishing training effectiveness measurement
- NIST Phish Scale validation and application
- Human factors in cybersecurity
- Security awareness training vs technical controls
- Organizational resilience and collective security behaviors
- Compliance-driven training vs risk reduction
- Real-world vs lab studies in security research
- Phishing simulation platforms and vendor ecosystems
- Gamification in cybersecurity training
- Just-in-time security interventions
- Secure Email Gateway (SEG) configurations
- SIEM/SOAR integration for phishing response
- Feedback loops in email security architecture
- Social engineering attack evolution
- LLM-generated phishing threats
- Temporal dynamics of threat detection and reporting
- User reporting mechanisms ("Report Phish" buttons)
- Incident response and automated hunting
- Zero-Hour Auto Purge (ZAP) systems
- Email authentication protocols (SPF, DKIM, DMARC, BIMI, ARC)

## Notatki

**Strengths:**
- Largest NIST Phish Scale validation to date (N=12,511)
- Real-world operational environment (not lab)
- Compared multiple training modalities systematically
- Introduced novel organizational-level metrics (OII)
- Reproduction study addressing generalizability
- Rigorous experimental design (stratified random sampling, controlled difficulty)
- High completion rates (87-89%) across conditions
- Comprehensive threat landscape coverage (19 templates, 3 difficulty levels)

**Limitations (acknowledged by authors):**
- **Construct validity**: Depends on specific vendor training (though regulation-compliant)
- **Internal validity**: Small control group due to compliance requirements
- **Measurement concerns**:
  - False positive clicks (automated security scanners, prefetch)
  - False negative reports (alternative reporting channels like help-desk)
- **External validity**:
  - Fintech context (higher baseline security awareness?)
  - US-based organization
  - Immediate post-training effects only (no long-term follow-up)
- **Template constraints**: Excluded high-distress scenarios per organizational request
- **Sample size**: Limited templates with both clicks AND reports (n=17) for OII analysis

**Practical Implications:**
- Organizations should set realistic (low) expectations for training outcomes
- Technical controls should be primary defense, not training
- Vendors can manipulate perceived effectiveness by difficulty selection
- NIST Phish Scale enables benchmarking and honest assessment
- Organizational feedback loops (user reports → IT response) may provide protection independent of training
- Compliance ≠ Security: mandatory training checks box but doesn't reduce risk significantly

**Future Work Directions (authors suggest):**
- Refinement of Organizational Inoculation Index
- AI-generated phishing and NIST Phish Scale relevance
- LLM-crafted attacks lack traditional flaws (grammar, unsecured sites) - questions framework validity
- Long-term training effects and recency
- Spear phishing vs mass phishing (OII utility unclear for targeted attacks)

**Comparison to Prior Work:**
- Echoes Lain et al. [48, 49]: 19,000+ employees, training ineffective
- Aligns with Ho et al. [43]: 19,500+ healthcare, minimal effectiveness
- Contrasts with vendor claims and some lab studies showing short-term benefits

**Key Takeaway:**
After rigorous large-scale testing, phishing training (lecture or interactive) provides negligible protection. NIST Phish Scale works. Organizational behaviors (collective reporting) may matter more than individual training.

