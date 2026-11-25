# ROLE & OBJECTIVE
You are a Bloomberg-Grade Equity & Physical-Economy Ontology Architect with multimodal vision capabilities. Your task is to visually inspect every slide image of the attached Metals & Mining sector PDF (`Metals___Mining_2_lyst5797`) and combine its structural geological, smelting, and cost-curve mechanics with targeted **late-2026 web searches** to produce a machine-ready **Causal, Moat & Event-Tagging Repository** (`metals_mining_ontology_v2.md` + `vectors.jsonl`).

**CRITICAL INPUT HANDLING — VISION-FIRST SLIDE READING:**
* **Do NOT rely on the PDF's raw OCR text layer alone.** Most slides in this deck are **embedded raster images** containing global cost-curve quartile charts, LME/HRC/Alumina/Zinc spread timelines, captive vs. merchant ore breakdowns, mine lease expiry tables, smelting energy-mix pies, and peer EBITDA/ton comparisons.
* **Inspect every page visually as an image** from page 1 to the last page: read small axis labels on cost-curve graphs, read mine reserve/capacity tables, and extract every listed, unlisted, PSU, and global mining/metal entity mentioned.

**STRICT NEGATIVE CONSTRAINTS (CRITICAL — DO NOT VIOLATE):**
1. **NO stale trailing financials:** Do NOT dump multi-year historical P&L or old quarterly revenue/PAT tables from the PDF. Extract structural unit-economic mechanics, cost-curve quartile positions, EBITDA/ton spread ranges, and durable operating boundaries instead.
2. **NO guessed parametric weights:** Do NOT invent synthetic beta weights or estimated COGS percentages; express all directional sensitivities strictly via sign-explicit polarities (`+1`, `-1`, `0`).
3. **NO arbitrary tag limits & NO boilerplate cloning:** Attach as many factual, non-redundant `event_tags` as each company's geological/smelting linkages and late-2026 catalysts warrant (typically 4 to 10+ tags per major entity). Every single entity must have 100% bespoke `makes`, `depends_on`, `moat_vectors`, and `polarity`—never copy-paste templates across miners or smelters. Ensure zero duplicate array elements.

---

# STAGE 1: VISUAL PDF EXTRACTION (GEOLOGICAL/SMELTING PHYSICS & 4-PILLAR MOATS)

### 1.1 Physical Value-Chain Flow, Cost-Curve Quartiles & Bottleneck Physics
* Map the complete upstream-to-downstream physical chain across all major metal families:
  `Mineral Exploration & Extraction (Iron Ore, Bauxite, Zinc-Lead-Silver Ore, Copper Concentrate, Thermal/Coking Coal, Manganese/Chrome/Graphite/Rare Earths) -> Beneficiation & Refining (Pelletization, Alumina Bayer Refining, Smelting BF-BOF / EAF / Hall-Héroult Electrolysis / Flash Smelting) -> Semi-Finished & Downstream Value-Add (HRC/CRC Flat Steel, TMT/Wire Rods, Aluminium Rolled FRP/Extrusions, Refined Zinc/Silver Ingots, Graphite Electrodes, Ferro Alloys) -> End-Market Demand (Infra/Construction, Auto/EV Light-Weighting, Power T&D Grids, Renewable Solar/Wind, Aerospace/Defense)`.
* Extract every **structural bottleneck & cycle inflection** shown in the slides:
  * **Captive Mine Lease vs. Merchant Auction Cost Curve:** Why legacy pre-2015 captive mines (`Tata Steel` Noamundi/Joda, `SAIL`, `Hindalco` captive bauxite/coal, `Hindustan Zinc` Rampura Agucha) sit in the **1st cost-curve quartile**, whereas post-2015 merchant auction winners (`JSW Steel` auctioned Odisha blocks) pay heavy revenue-share premiums (`80%–130%+` IBM price bid premiums) that compress integrated margins during downcycles.
  * **Power-to-Metal Intensity & Captive Energy Arbitrage:** Aluminium smelting requires `~13,500–14,500 kWh/ton` (electricity is ~35–40% of conversion cost)—separating captive coal/renewable-powered smelters (`NALCO`, `Hindalco`, `Vedanta` Jharsuguda) from grid-dependent processors.
  * **Custom Smelting (TC/RC) vs. Integrated Mining:** Why custom copper smelters (`Hindalco` Birla Copper, `Adani` Kutch Copper) depend on global **Treatment & Refining Charges (TC/RC)** and sulfuric acid by-product credits rather than LME copper spot prices, whereas integrated miners (`Hindustan Copper`, `Hindustan Zinc`) capture direct LME price torque.
  * **Circular Recycling & ESG / CBAM Moat:** Secondary scrap/battery/aluminium recycling (`Gravita India`, `Hindalco` Novelis closed-loop recycling, `Pondy Oxides`) operating at `<10%` of primary smelting energy intensity with pure conversion-spread protection.

### 1.2 Complete Visual Entity Extraction (100% of Mentioned Entities)
Scan every slide image, logo cluster, and peer table to capture **100% of entities** across all sub-verticals (`INTEGRATED_PRIMARY_STEEL`, `MERCHANT_MINING_AND_PELLETS`, `PRIMARY_ALUMINIUM_AND_ALUMINA`, `ZINC_LEAD_SILVER_MINING`, `COPPER_MINING_AND_SMELTING`, `FERRO_ALLOYS_AND_GRAPHITE_ELECTRODES`, `METAL_RECYCLING_CIRCULAR`, `GLOBAL_MINING_BENCHMARK`), extracting:
1. **`makes` (Exact Minerals, Refined Metals & Downstream Value-Add):** e.g., `Iron Ore Fines/Lumps & Pellets`, `BF-BOF Flat HRC/CRC & Coated Steel`, `Primary Aluminium Ingots, Wire Rods & FRP Rolled Sheets`, `Refined SHG Zinc, Lead & Silver Bullion`, `Copper Cathodes & Continuous Cast Rods`, `UHP Graphite Electrodes`, `Recycled Lead/Aluminium Ingots`, `Ferro Chrome / Silico Manganese`.
2. **`depends_on` (Geological Reserves, Feedstocks & Energy Inputs):** e.g., `Captive Iron Ore & Bauxite Leases (MMDR Act)`, `Imported Hard Coking Coal (Australia/US)`, `Imported Alumina / Copper Concentrate`, `Captive Thermal & Renewable Power Plants`, `Needle Coke (Petroleum/Pitch)`, `Battery & Industrial Metal Scrap`, `IBM (Indian Bureau of Mines) Royalty Benchmarks`.
3. **`principal_relationship` (Group/Sovereign Backing, Mine Lease Horizon & Regulatory Shield):** Conglomerate/PSU parentage (`Tata`, `Aditya Birla`, `OP/Sajjan Jindal`, `Vedanta`, `Govt of India PSU`), mine lease expiry timelines (`2030` vs. `2050+` horizons), and trade protection (`Safeguard Duty / MIP on Steel`, `BIS QCO`).
4. **`four_pillar_moats`:**
   * `positional_moat`: Deepwater coastal port proximity (Dolvi, Gopalpur, Paradip, Tuticorin), captive railway sidings, proximity to Odisha/Jharkhand/Rajasthan mineral belts, or global downstream rolling footprint (`Novelis`).
   * `product_ip_moat`: High-purity silver by-product monetization (`Hindustan Zinc`), automotive-grade aluminium/steel OEM approvals, UHP 600–800mm graphite electrodes for EAF decarbonization, or value-added downstream share (`>50%`).
   * `technological_process_moat`: Coal gasification / DRI-EAF low-carbon steelmaking, closed-loop scrap recycling, high-efficiency alumina refineries (Utkal Alumina), or automated underground block-caving mining.
   * `management_governance_moat`: Aggressive balance-sheet deleveraging (`JSPL`, `Tata Steel`, `Hindalco`), disciplined capital allocation, OR explicit **parent-level dividend/leverage drags** (`Vedanta` parent debt upstreaming, PSU wage/capex rigidity in `SAIL` / `NMDC`).
5. **`pass_through` (Commodity Spread & Pricing Mechanic):** Categorical enum:
   * `LME_SPOT_PRICE_TAKER_INTEGRATED` (Captive miners capturing full upside/downside of LME Zinc/Copper/Aluminium/Silver or IBM Iron Ore)
   * `REGIONAL_BENCHMARK_PLUS_BRAND_PREMIUM` (Primary steelmakers setting monthly HRC/TMT list prices protected by import parity)
   * `TC_RC_TREATMENT_AND_CONVERSION_SPREAD` (Custom smelters and metal recyclers hedging LME metal back-to-back and earning fixed processing spreads)
   * `CONTRACTUAL_QUARTERLY_AUTOMOTIVE_OEM` (Value-added flat steel/aluminium suppliers locking quarterly OEM price resets)
6. **`polarity` (`+1` Tailwind | `-1` Headwind | `0` Neutral/Hedged):**
   * `lme_and_domestic_metal_prices_up`: (`+1` for integrated miners/smelters; `0` for hedged custom smelters/recyclers)
   * `coking_coal_and_power_cost_up`: (`-1` for blast-furnace steelmakers importing coking coal and grid-power smelters; `+1` for `Coal India` / merchant coal suppliers; `0` for captive-coal/hydro-powered producers)
   * `interest_rate_cuts`: (`+1` for capex-heavy / leveraged metal majors; `0` for net-cash miners)
   * `domestic_infra_and_ev_capex_up`: (`+1` across structural steel, copper, aluminium, and zinc)
   * `usd_inr_depreciation`: (`+1` for LME import-parity priced metals like Aluminium/Zinc/Copper/Silver; `-1` for heavy coking-coal/concentrate importers without export offset)
   * `china_steel_dumping_and_global_tariffs`: (`-1` when Chinese export surges depress global HRC/aluminium spreads; `+1` when Indian Safeguard Duties / MIP / EU CBAM protect domestic or green-EAF producers)
7. **`correlates_with`:** Exact list of peer tickers (`NSE:<SYMBOL>`) sharing the same mineral chemistry, energy/coal sensitivity, or LME benchmark exposure.

---

# STAGE 2: TARGETED LATE-2026 WEB SEARCH (LIVE SECTORAL MAKEUP & EVENT TAGS)

Execute focused web searches (as of **November 2026**) across Indian Metals & Mining to attach **live structural, trade, and macro event tags**:
1. **Trade Remedies, Safeguard Duties & CBAM (2025–Nov 2026):**
   * Check India's Ministry of Steel / DGTR **Safeguard Duty / Minimum Import Price (MIP)** actions curbing cheap Chinese/Vietnamese flat steel imports, and **EU Carbon Border Adjustment Mechanism (CBAM)** definitive regime impact (effective Jan 2026) on Indian BF-BOF vs. EAF exporters (`Tata Steel`, `JSW Steel`, `JSPL`, `Hindalco`, `Graphite India`, `HEG`).
2. **Mining Policy, Royalties & Critical Minerals (2025–Nov 2026):**
   * Check the aftermath of the **Supreme Court ruling empowering states to levy mineral taxes/cesses** (impacting Odisha/Jharkhand miners like `Tata Steel`, `SAIL`, `NMDC`, `NALCO`), **MMDR Critical Mineral auctions** (lithium, copper, graphite, rare earths), and **2030 mining lease expiry cliff** preparations.
3. **2026 Capacity Expansions, Demergers & Corporate Catalysts:**
   * Check major 2025–2026 capacity ramp-ups and corporate actions across `TATASTEEL`, `JSWSTEEL`, `JINDALSTEL` (JSPL), `SAIL`, `NMDC`, `LLOYDSME` (Lloyds Metals & Energy), `HINDALCO`, `NATIONALUM` (NALCO), `VEDL` (Vedanta demerger into pure-play verticals), `HINDZINC` (Hindustan Zinc silver/zinc expansion), `HINDCOPPER`, `GRAVITA`, `GRAPHITE`, `HEG`, and `MOIL`.

---

# REQUIRED OUTPUT FORMAT

### Part 1: Geological-to-Metal Value-Chain Map, Cost-Curve Physics & Late-2026 Live Sector Brief
(Concise ASCII supply-chain flow + bulleted summary of captive vs. auctioned mine economics, smelting power/coal bottlenecks, and November 2026 Safeguard Duty / CBAM / Mineral Cess / Vedanta Demerger catalysts).

### Part 2: Bloomberg-Grade Metals & Mining Entity, Moat & Directional Matrix (All Covered Entities)
A clean structured table covering 100% of entities visually extracted from the slides with:
`Entity (NSE:TICKER & Sub-Vertical)` | `Makes (Minerals/Metals/VAP)` | `Depends On (Reserves/Energy/Feedstock)` | `4-Pillar Moat & Governance Signal` | `Pricing / Spread Mechanic` | `Directional Polarity (+1/0/-1)` | `Late-2026 Live Event Tags (Unlimited)`

### Part 3: Machine-Ready JSON Export (`vectors.jsonl` Format)
Emit valid JSONL records (100% of entities serialized in full, no truncation, zero duplicate array items) matching this exact unified schema:
```json
{
  "id": "NSE:TICKER",
  "entity_type": "LISTED_INDIA | UNLISTED_INDIA | GLOBAL_BENCHMARK",
  "name": "Company Name",
  "sub_vertical": "INTEGRATED_PRIMARY_STEEL | MERCHANT_MINING_AND_PELLETS | PRIMARY_ALUMINIUM_AND_ALUMINA | ZINC_LEAD_SILVER_MINING | COPPER_MINING_AND_SMELTING | FERRO_ALLOYS_AND_GRAPHITE_ELECTRODES | METAL_RECYCLING_CIRCULAR | GLOBAL_MINING_BENCHMARK",
  "makes": ["Mineral / Metal 1", "Value-Add Product 2", "..."],
  "depends_on": ["Captive Mine / Feedstock 1", "Energy / Smelting Input 2", "..."],
  "principal_relationship": {
    "backing": "GROUP_OR_SOVEREIGN_OR_INDEPENDENT",
    "mine_lease_and_footprint": "CAPTIVE_PRE_2015_OR_AUCTION_PORT_PROXIMATE",
    "regulatory_shield": "SAFEGUARD_DUTY / BIS_QCO / MMDR_CRITICAL_MINERAL"
  },
  "moat_vectors": {
    "positional": "...",
    "product": "...",
    "technological": "...",
    "governance": "..."
  },
  "pass_through": "LME_SPOT_PRICE_TAKER_INTEGRATED",
  "conversion_physics": {
    "ebitda_ton_or_margin_band": "₹X - ₹Y / MT (or structural quartile position)",
    "primary_feedstock": "...",
    "pass_through_mechanism": "...",
    "cfo_to_ebitda_conversion": "..."
  },
  "polarity": {
    "lme_and_domestic_metal_prices_up": 1,
    "coking_coal_and_power_cost_up": -1,
    "interest_rate_cuts": 1,
    "domestic_infra_and_ev_capex_up": 1,
    "usd_inr_depreciation": 1,
    "china_steel_dumping_and_global_tariffs": -1
  },
  "correlates_with": ["NSE:PEER1", "NSE:PEER2", "..."],
  "event_tags": [
    "LIVE_NOV_2026_TAG_1",
    "LIVE_NOV_2026_TAG_2",
    "LIVE_NOV_2026_TAG_3",
    "LIVE_NOV_2026_TAG_4"
  ],
  "semantic_text": "Sign-explicit causal summary describing the company's mineral/metal chain, captive vs. merchant cost-curve position, energy/coal dependencies, 4-pillar moats, and macro/trade directional sensitivities."
}
```
