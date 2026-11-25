[banking](directory;file:///Users/prasad/pdfs/banking) 
# ROLE & OBJECTIVE
You are a Bloomberg-Grade Equity & Financial-Intermediation Ontology Architect with multimodal vision capabilities. Your task is to visually inspect every slide image of the attached Banking & NBFC sector PDF and combine its structural balance-sheet mechanics with targeted **late-2026 web searches** to produce a machine-ready **Causal, Moat & Event-Tagging Repository** (`banking_ontology_v2.md` + `vectors.jsonl`).

**CRITICAL INPUT HANDLING — VISION-FIRST SLIDE READING:**
* **Do NOT rely on the PDF's raw OCR text layer alone.** Most slides in this deck are **embedded raster images** containing CASA/NIM comparison charts, Loan-to-Deposit Ratio (LDR) graphs, GNPA/NNPA asset-quality cycle tables, RoA/RoE trees, and regional branch maps.
* **Inspect every page visually as an image** from page 1 to the last page: read small axis labels, segment pie charts (retail vs. wholesale vs. MSME vs. MFI), and institutional comparison matrices.

**STRICT NEGATIVE CONSTRAINTS (CRITICAL — DO NOT VIOLATE):**
1. **NO stale trailing financials:** Do NOT dump multi-year historical P&L or old quarterly NII/PAT tables from the PDF. Extract structural ratios, asset-liability mechanics, and durable operating boundaries instead.
2. **NO guessed parametric weights:** Do NOT invent synthetic beta weights or estimated NIM sensitivity coefficients; express all directional sensitivities strictly via sign-explicit polarities (`+1`, `-1`, `0`).
3. **NO arbitrary tag limits & NO boilerplate cloning:** Attach as many factual, non-redundant `event_tags` as each institution's balance-sheet physics and late-2026 catalysts warrant (typically 4 to 10+ tags per major entity). Every single entity must have 100% bespoke `makes`, `depends_on`, `moat_vectors`, and `polarity`—never copy-paste templates across banks.

---

# STAGE 1: VISUAL PDF EXTRACTION (BANKING PHYSICS & 4-PILLAR MOATS)

### 1.1 Financial Value-Chain Flow, Spread Pool & Bottleneck Physics
* Map the complete intermediation chain:
  `Liability Origination (CASA / Retail TD / Wholesale NCDs / Refinance) -> Risk Underwriting & Tech/Branch Distribution -> Asset Book Deployment (EBLR Floating vs. Fixed-Rate Retail/MSME/MFI/Gold) -> Collections, Recovery & Credit Cost Absorption -> RoA / RoE Compounding`.
* Extract every **structural bottleneck & cycle inflection** shown in the slides:
  * **Deposit & LDR Bottleneck:** CASA mobilization battles, Loan-to-Deposit Ratio (LDR) ceilings, and Term Deposit repricing lags.
  * **Asset-Liability Repricing Asymmetry:** How EBLR (External Benchmark Linked Rate) floating books reprice immediately on RBI Repo shifts vs. fixed-rate books (CV, Gold, MFI, Consumer Durables) where asset yields stay sticky while cost of funds moves.
  * **Regulatory & PSL Friction:** Priority Sector Lending (PSL) 40% (Universal Banks) vs. 75% (Small Finance Banks) mandates, RBI unsecured/MFI guardrails (50% FOIR cap, over-indebtedness norms), and LCR (Liquidity Coverage Ratio) buffers.
  * **Operating Leverage vs. Credit Cost Trap:** High-yield unsecured/MFI models (`20%+` yield, high opex/branch cost, sharp cyclical credit-cost spikes) vs. prime secured/corporate-backed models (`9–12%` yield, low credit cost, AAA borrowing edge).

### 1.2 Complete Visual Entity Extraction (100% of Mentioned Entities)
Scan every slide image, logo cluster, and peer table to capture **100% of institutions** across all tiers (`LARGE_PRIVATE_BANK`, `OLD_PRIVATE_BANK`, `PUBLIC_SECTOR_BANK`, `SMALL_FINANCE_BANK`, `NBFC_HFC`, `NBFC_VEHICLE_MSME`, `NBFC_MFI`, `NBFC_GOLD`, `FINTECH_CO_LENDER`), extracting:
1. **`makes` (Asset & Fee Products):** Exact loan books and fee engines (e.g., `Prime Home Loans`, `Used CV Finance`, `JLG Microfinance`, `Gold Collateral Loans`, `MSME Working Capital`, `Wealth & Bancassurance Fees`, `Co-Branded Credit Cards`).
2. **`depends_on` (Liabilities, Channels & Enablers):** Exact funding sources and operational dependencies (`Low-Cost Retail CASA Deposits`, `Wholesale NCDs & Commercial Paper`, `NHB / SIDBI Refinance Lines`, `Co-Lending / Direct Assignment Off-Balance-Sheet Pools`, `Physical Branch & Doorstep Collection Agents`, `Account Aggregator / Digital Underwriting Stack`).
3. **`principal_relationship` (Parentage & Regulatory Charter):** Sovereign PSU parentage, Corporate Conglomerate backing (Tata, Bajaj, Murugappa, Aditya Birla, Mahindra), Foreign/PE anchor, or Universal Bank transition status + regulatory license tier.
4. **`four_pillar_moats`:**
   * `positional_moat`: Liability franchise strength, branch density in semi-urban/rural catchments, corporate salary account lock-in, or regional community stickiness (e.g., Tamil Nadu/Kerala old private banks).
   * `product_ip_moat`: Niche underwriting mastery in informal/cash-flow borrowers (e.g., used truckers, small shopkeepers, gold valuation/auction velocity, no-cost POS consumer EMI ecosystems).
   * `technological_process_moat`: Core banking digital distribution (YONO, iMobile, InstaBIZ), sub-minute digital underwriting, tablet-based doorstep collections, or low Cost-to-Income operating efficiency.
   * `management_governance_moat`: Multi-cycle risk underwriting discipline, conservative PCR (Provision Coverage Ratio), smooth CEO/leadership continuity OR explicit **governance/asset-quality drags** (e.g., MFI over-leveraging, high LDR strain, audit/RBI supervisory restrictions, elevated Cost-to-Income >60% in SFBs).
5. **`pass_through` (Rate & Yield Repricing Mechanic):** Categorical enum:
   * `EBLR_INSTANT_FLOATING_BOOK` (reprices immediately with Repo; TD cost lags)
   * `FIXED_RATE_ASSET_STICKY_YIELD` (CV/MFI/Gold/Consumer NBFCs; expands NIM when rates fall, compresses when wholesale rates rise)
   * `HYBRID_MCLR_AND_RETAIL_FLOATING`
   * `ORIGINATE_TO_DISTRIBUTE_CO_LENDING`
6. **`polarity` (`+1` Tailwind | `-1` Headwind | `0` Neutral/Hedged):**
   * `rbi_repo_rate_hikes`: (`+1` for high-CASA EBLR banks in early hike phase; `-1` for wholesale-funded fixed-rate NBFCs/HFCs)
   * `system_liquidity_tightening_high_ldr`: (`-1` for high-LDR / deposit-starved banks; `0` or `+1` for deposit-surplus PSU/mega banks)
   * `rural_agri_cashflow_up`: (`+1` for MFI, tractor/CV, gold, and rural SFBs)
   * `urban_capex_and_msme_credit_up`: (`+1` for corporate/SME banks and LAP/SBL lenders)
   * `rbi_unsecured_mfi_regulatory_tightening`: (`-1` for MFI/unsecured personal loan heavy lenders; `+1` relative shift to secured gold/LAP lenders)
   * `gold_price_bull_run`: (`+1` for gold-loan NBFCs/banks via higher LTV headroom & lower LGD; `0` for non-gold lenders)
7. **`correlates_with`:** Exact list of peer tickers (`NSE:<SYMBOL>`) sharing the same liability structure, asset-class credit cycle, or regulatory sensitivity.

---

# STAGE 2: TARGETED LATE-2026 WEB SEARCH (LIVE SECTORAL MAKEUP & EVENT TAGS)

Execute focused web searches (as of **November 2026**) across Indian Banking, SFBs, and NBFCs to attach **live structural & macro event tags**:
1. **Late-2026 Monetary Policy, Liquidity & Inflation Regime:** Check current RBI Repo Rate (`5.50%` as of Oct 2026) and November 2026 CPI inflation breaching the 6% upper tolerance band (putting 25 bps rate hike risks on the Dec 2026 / Feb 2027 MPC radar), durable liquidity surplus, and system credit growth (~18–19% YoY).
2. **2026 Asset Quality & Regulatory Stress Pockets:** Check the ongoing MFI stress cycle (RBI's Nov 2026 refusal to relax the 50% FOIR cap, CRIF MicroLend portfolio moderation), unsecured personal loan/credit card seasoning, and the massive **+83% YoY surge in gold loans** (`₹5.59 Lakh Cr` bank gold loan book).
3. **2026 Institutional Catalysts & Corporate Actions:** Check major bank/NBFC developments across `HDFCBANK`, `ICICIBANK`, `SBIN`, `AXISBANK`, `KOTAKBANK`, `BAJFINANCE`, `CHOLAFIN`, `SHRIRAMFIN`, `MUTHOOTFIN`, `MANAPPURAM`, `AUBANK`, `EQUITASBNK`, `CREDITACC`, `FIVESTAR`, `FEDERALBNK`, `KARURVYSYA`, `IDFCFIRSTB`, and `INDUSINDBK` (e.g., SFB-to-Universal Bank license approvals, LDR compression milestones, promoter/management transitions, and subsidiary listings).

---

# REQUIRED OUTPUT FORMAT

### Part 1: Financial Intermediation Chain, Rate/Liquidity Physics & Late-2026 Live Sector Brief
(Concise ASCII money-flow diagram + bulleted summary of deposit/LDR bottlenecks, EBLR vs. fixed-rate NIM lag mechanics, and November 2026 RBI/inflation/MFI/gold-loan catalysts).

### Part 2: Bloomberg-Grade Financial Institution, Moat & Directional Matrix (All Covered Entities)
A clean structured table covering 100% of institutions visually extracted from the slides with:
`Institution (Ticker & Tier)` | `Makes (Asset/Fee Books)` | `Depends On (Liabilities/Channels)` | `4-Pillar Moat & Governance Signal` | `Rate Pass-Through Mechanic` | `Directional Polarity (+1/0/-1)` | `Late-2026 Live Event Tags (Unlimited)`

### Part 3: Machine-Ready JSON Export (`vectors.jsonl` Format)
Emit valid JSONL records matching this exact schema:
```json
{
  "id": "NSE:TICKER",
  "entity_type": "LISTED_INDIA",
  "name": "Institution Name",
  "sub_vertical": "LARGE_PRIVATE_BANK | OLD_PRIVATE_BANK | PUBLIC_SECTOR_BANK | SMALL_FINANCE_BANK | NBFC_HFC | NBFC_VEHICLE_MSME | NBFC_MFI | NBFC_GOLD",
  "makes": ["Asset Book 1", "Fee Stream 2", "..."],
  "depends_on": ["Liability Source 1", "Distribution/Collection Channel 2", "..."],
  "principal_relationship": {
    "backing": "CONGLOMERATE_OR_SOVEREIGN_OR_INDEPENDENT",
    "license_tier": "UNIVERSAL_BANK | SFB | NBFC_UPPER_LAYER | NBFC_MIDDLE_LAYER",
    "regulatory_drag": "40% PSL / 75% PSL / 50% MFI FOIR Cap"
  },
  "moat_vectors": {
    "positional": "...",
    "product": "...",
    "technological": "...",
    "governance": "..."
  },
  "pass_through": "EBLR_INSTANT_FLOATING_BOOK",
  "polarity": {
    "rbi_repo_rate_hikes": 1,
    "system_liquidity_tightening_high_ldr": -1,
    "rural_agri_cashflow_up": 0,
    "urban_capex_msme_credit_up": 1,
    "rbi_unsecured_mfi_tightening": 0,
    "gold_price_bull_run": 0
  },
  "correlates_with": ["NSE:PEER1", "NSE:PEER2", "..."],
  "event_tags": [
    "LIVE_NOV_2026_TAG_1",
    "LIVE_NOV_2026_TAG_2",
    "LIVE_NOV_2026_TAG_3",
    "LIVE_NOV_2026_TAG_4"
  ],
  "semantic_text": "Sign-explicit causal summary describing the institution's liability franchise, asset book mix, rate-repricing lag mechanics, 4-pillar moats or asset-quality drags, and macro/regulatory directional sensitivities."
}
