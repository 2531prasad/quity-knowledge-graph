# ROLE & OBJECTIVE
You are a Bloomberg-Grade Equity & Physical-Economy Ontology Architect with multimodal vision capabilities. Your task is to visually inspect every slide image of the attached Hotels & Hospitality sector PDF and combine its structural real-estate, room-inventory, and operating-leverage mechanics with targeted **late-2026 web searches** to produce a machine-ready **Causal, Moat & Event-Tagging Repository** (`hotels_ontology_v2.md` + `vectors.jsonl`).

**CRITICAL INPUT HANDLING — VISION-FIRST SLIDE READING:**
* **Do NOT rely on the PDF's raw OCR text layer alone.** Most slides in this deck are **embedded raster images** containing ARR/Occupancy/RevPAR cycle charts, branded room supply pipeline graphs, asset-heavy vs. asset-light key split pies, cost-per-key capex benchmarks, and peer operating margin tables.
* **Inspect every page visually as an image** from page 1 to the last page: read small axis labels on RevPAR and supply-demand charts, read room-key inventory tables, and extract every listed, unlisted, global brand principal, and REIT/asset-owner entity mentioned.

**STRICT NEGATIVE CONSTRAINTS (CRITICAL — DO NOT VIOLATE):**
1. **NO stale trailing financials:** Do NOT dump multi-year historical P&L or old quarterly revenue/PAT tables from the PDF. Extract structural unit-economic mechanics, RevPAR/ARR operating leverage rules, cost-per-key benchmarks, and durable operating boundaries instead.
2. **NO guessed parametric weights:** Do NOT invent synthetic beta weights or estimated margin sensitivity coefficients; express all directional sensitivities strictly via sign-explicit polarities (`+1`, `-1`, `0`).
3. **NO arbitrary tag limits & NO boilerplate cloning:** Attach as many factual, non-redundant `event_tags` as each company's property ownership physics and late-2026 catalysts warrant (typically 4 to 10+ tags per major entity). Every single entity must have 100% bespoke `makes`, `depends_on`, `moat_vectors`, and `polarity`—never copy-paste templates across hoteliers. Ensure zero duplicate array elements.

---

# STAGE 1: VISUAL PDF EXTRACTION (HOSPITALITY PHYSICS & 4-PILLAR MOATS)

### 1.1 Physical Intermediation Flow, RevPAR Operating Leverage & Bottleneck Physics
* Map the complete upstream-to-downstream hospitality value chain across all 5 operating archetypes:
  `Land Acquisition & Greenfield/Brownfield Development (Cost-per-Key Capex & 4–6 Year Gestation Lag) -> Asset Ownership vs. Management Structure (100% Owned / Long-Term Lease vs. Asset-Light Management Contract / Franchise) -> Brand Tiering & Positioning (Ultra-Luxury Heritage / Luxury / Upper-Upscale Business / Mid-Scale / Lean-Luxe Economy) -> Revenue Engines (Room Nights [Occupancy × ARR = RevPAR] + F&B / Banquets / MICE / Destination Weddings + Ancillary Flight Catering & Commercial Office Towers) -> Fixed-Cost Operating Leverage Flow-Through (70%+ Incremental ARR Drop-Through above ~55% Breakeven Occupancy)`.
* Extract every **structural bottleneck & cycle inflection** shown in the slides:
  * **Supply-Demand Gestation Asymmetry:** Why luxury and metro greenfield hotels take **4 to 6 years** from land acquisition and municipal/environmental clearances to commercial opening—creating multi-year pricing power (ARR compounding) when corporate travel, MICE, and wedding demand outpace net room additions, versus the micro-market oversupply risk when massive pipelines (`~77%` of existing branded inventory in 2026) begin commissioning in Tier-2/3 leisure pockets.
  * **Asset-Heavy Owner vs. Asset-Light Manager Economics:** Why pure asset-light brand managers (`IHCL` management pipeline `~80%`, `Royal Orchid`) earn high-ROCE (`30%+`), annuity-like base + incentive management fees (`3%–5%` of revenue + `8%–12%` of GOP) with zero balance-sheet capex, whereas asset-heavy owners (`Chalet Hotels`, `Juniper Hotels`, `SAMHI Hotels`, `EIH`) carry higher capital intensity and interest/depreciation drag (`~₹1.5–₹3.5 Cr` capex per luxury key) but capture **100% of the upward ARR operating leverage** during cycle peaks.
  * **Non-Room Revenue & Mixed-Use Diversification:** How high-margin **F&B, MICE (Meetings, Incentives, Conferences, Exhibitions), destination weddings, flight catering (`TajSATS`), and co-located Grade-A commercial office towers (`Chalet Hotels`)** stabilize cash flows during seasonal Q1/Q2 corporate travel lulls.
  * **Turnaround & Renovation Arbitrage:** Buying distressed/under-managed hotels at a discount to replacement cost and rebranding them into global distribution engines (`SAMHI Hotels` integrating Marriott/IHG/Hyatt; `Lemon Tree` renovating Keys portfolio to unlock step-change ARR hikes without greenfield construction lag).

### 1.2 Complete Visual Entity Extraction (100% of Mentioned Entities)
Scan every slide image, logo cluster, and peer table to capture **100% of entities** across all sub-verticals (`HYBRID_BRAND_AND_ASSET_MAJOR`, `LUXURY_HERITAGE_HOSPITALITY`, `METRO_BUSINESS_AND_MICE_OWNER`, `MIDSCALE_AND_ECONOMY_CHAIN`, `ASSET_LIGHT_MANAGEMENT_FRANCHISOR`, `HOTEL_TURNAROUND_AND_REIT_PLATFORM`, `GLOBAL_HOSPITALITY_PRINCIPAL`), extracting:
1. **`makes` (Brand Tiers, Room Formats & Non-Room Engines):** e.g., `Ultra-Luxury Palaces & Resorts (Taj, Oberoi, The Leela)`, `Upper-Upscale Metro Business Hotels (JW Marriott, Grand Hyatt, Trident, ITC)`, `Mid-Scale & Lean-Luxe Hotels (Lemon Tree, Ginger, Aurika, Keys)`, `MICE & Grand Banquet Convention Halls`, `Flight Catering (TajSATS)`, `Co-Located Grade-A Commercial Office Towers`.
2. **`depends_on` (Real Estate, Capital & Distribution Inputs):** e.g., `Irreplaceable Metro & Heritage Land Banks`, `Global Loyalty & GDS Distribution Engines (Marriott Bonvoy, World of Hyatt, IHG)`, `Asset-Light Third-Party Property Owners`, `Corporate Business Travel & GCC Inflows`, `Domestic Luxury Wedding & Spiritual Tourism Calendars`, `Skilled Hospitality Staffing & Commercial Power/HVAC Utilities`.
3. **`principal_relationship` (Group Backing, Brand Affiliation & Asset Ownership Split):** Conglomerate/sponsor parentage (`Tata Group`, `ITC`, `Oberoi/EIH`, `K. Raheja Corp`, `Brookfield`, `Saraf/Hyatt`, `Independent`), owned-vs-managed key ratio (`% Owned` vs. `% Managed`), and global brand franchise fees (`Marriott/Hyatt/IHG` royalty drag vs. `0%` proprietary Indian brand IP).
4. **`four_pillar_moats`:**
   * `positional_moat`: Irreplaceable trophy land parcels in Mumbai/Delhi/Bengaluru/Udaipur/Jaipur where new luxury supply is physically impossible (`Taj Mahal Palace`, `The Oberoi`, `Grand Hyatt Mumbai`, `JW Marriott Sahar`), or airport-adjacent/IT-corridor density.
   * `product_ip_moat`: Iconic proprietary Indian luxury marques (`Taj`, `Oberoi`, `The Leela`, `ITC Hotels`) commanding global brand recognition and wedding/MICE pricing premiums without paying foreign brand royalties, or lean-luxe modular standardization (`Ginger`).
   * `technological_process_moat`: Dynamic algorithmic revenue management systems (yield optimization), loyalty program lock-in (`Tata Neu / Taj InnerCircle`, `Club ITC`, `Marriott Bonvoy`), and centralized procurement/shared services.
   * `management_governance_moat`: Pivoting from debt-heavy construction to capital-light management fee compounding (`IHCL Ahvaan / Accelerate 2030`), disciplined debt deleveraging (`Chalet`, `EIH`), OR explicit **leverage/renovation drags** (`Lemon Tree` elevated debt-to-equity `~1.4x` and Keys renovation disruption; `Chalet` Powai/Vashi construction disruption).
5. **`pass_through` (Pricing & Operating Leverage Mechanic):** Categorical enum:
   * `DYNAMIC_DAILY_ARR_SURGE_PRICING` (Overnight room rates repriced daily via algorithmic demand yield, providing instant inflation pass-through)
   * `HYBRID_OWNED_ARR_PLUS_ASSET_LIGHT_FEES` (Combines owned-hotel operating leverage with high-ROCE third-party management/incentive fees)
   * `CONTRACTUAL_CORPORATE_AND_MICE_RATES` (Annual negotiated corporate/airline crew volume contracts paired with seasonal MICE/wedding repricing)
   * `GLOBAL_FRANCHISE_FEE_AND_LOYALTY_TAKE` (Pure asset-light international franchisors collecting % of room revenue + loyalty/reservation fees)
6. **`polarity` (`+1` Tailwind | `-1` Headwind | `0` Neutral/Hedged):**
   * `arr_and_occupancy_upcycle`: (`+1` across all hoteliers; highest torque for asset-heavy owners)
   * `interest_rate_cuts`: (`+1` for leveraged asset owners/turnarounds like `SAMHI`, `Lemon Tree`, `Chalet`, `Juniper`; `0` for net-cash `EIH` / `IHCL`)
   * `corporate_and_gcc_travel_up`: (`+1` for metro business & airport hotels)
   * `domestic_wedding_and_spiritual_tourism_up`: (`+1` for luxury heritage, palace, and Tier-2/3 leisure/pilgrimage chains)
   * `new_branded_supply_pipeline_surge`: (`-1` for commoditized mid-scale/tier-2 assets facing local oversupply; `0` or `+1` for trophy supply-constrained luxury assets and asset-light managers signing new keys)
   * `staff_wage_and_utility_inflation`: (`-1` for high-service luxury/F&B heavy properties; `0` for lean-luxe/automated formats)
7. **`correlates_with`:** Exact list of peer tickers (`NSE:<SYMBOL>`) sharing the same brand tier, asset-ownership intensity, or micro-market demand driver.

---

# STAGE 2: TARGETED LATE-2026 WEB SEARCH (LIVE SECTORAL MAKEUP & EVENT TAGS)

Execute focused web searches (as of **November 2026**) across the Indian Hospitality & Hotels sector to attach **live structural, demand, and corporate catalysts**:
1. **Late-2026 Industry RevPAR & Supply Pipeline Reality (November 2026 Data):**
   * Incorporate the **November 2026 Hotelivate-Savills Indian Hospitality Report** (`₹8,962` pan-India ARR, `₹6,099` RevPAR up `6.2%` YoY, alongside a massive active pipeline at `~77%` of existing branded inventory causing micro-market dispersion where 1 in 4 hotels saw RevPAR dips) and **Q2 FY27 / H2 FY27 festive & wedding season momentum** (HVS Anarock Q2 FY27 RevPAR up `13%–15%` YoY).
2. **2026 Luxury, MICE & Micro-Market Catalysts:**
   * Check **The Leela Palaces Hotels & Resorts (`NSE:THELEELA` / Schloss Bangalore)** post-listing performance and luxury RevPAR outperformance (`30%+` YoY RevPAR surge in Q2 FY27), **ITC Hotels (`NSE:ITCHOTELS`)** post-demerger standalone expansion, and **Juniper Hotels (`NSE:JUNIPER`)** capturing Mumbai MICE business (`2.25 lakh sq ft` at Grand Hyatt Mumbai) during Trident BKC renovations alongside Kaziranga/Guwahati/Bengaluru pipeline additions.
3. **2026 Portfolio Expansions, Renovations & Balance-Sheet Catalysts:**
   * Check major 2025–2026 milestones across `INDHOTEL` (IHCL Accelerate 2030 scaling past `625+` total hotels / `380+` operational + Claridges/Brij/Tree of Life additions), `EIHOTEL` (debt-free balance sheet, Trident BKC renovation), `CHALET` (Powai/Vashi commercial + hotel commissioning), `LEMONTREE` (Keys portfolio renovation completion lifting ARR), `SAMHI` (approaching `80%` occupancy with high operating leverage), `ROHLTD` (Royal Orchid asset-light `3,600+` room pipeline), `TAJGVK`, `ADVANIHOTR`, `ORIENTHOT`, and `KAMATHOTEL`.

---

# REQUIRED OUTPUT FORMAT

### Part 1: Hospitality Value-Chain Map, RevPAR Operating Leverage & Late-2026 Live Sector Brief
(Concise ASCII value-chain flow + bulleted summary of asset-heavy vs. asset-light unit economics, 4–6 year supply gestation physics, and November 2026 Hotelivate-Savills / Q2 FY27 RevPAR / luxury & MICE catalysts).

### Part 2: Bloomberg-Grade Hospitality Entity, Moat & Directional Matrix (All Covered Entities)
A clean structured table covering 100% of entities visually extracted from the slides with:
`Entity (NSE:TICKER & Sub-Vertical)` | `Makes (Brands/Tiers/Non-Room)` | `Depends On (Land/Loyalty/Channels)` | `4-Pillar Moat & Governance Signal` | `Pricing & Ownership Mechanic` | `Directional Polarity (+1/0/-1)` | `Late-2026 Live Event Tags (Unlimited)`

### Part 3: Machine-Ready JSON Export (`vectors.jsonl` Format)
Emit valid JSONL records (100% of entities serialized in full, no truncation, zero duplicate array items) matching this exact unified schema:
```json
{
  "id": "NSE:TICKER",
  "entity_type": "LISTED_INDIA | UNLISTED_INDIA | GLOBAL_BENCHMARK",
  "name": "Company Name",
  "sub_vertical": "HYBRID_BRAND_AND_ASSET_MAJOR | LUXURY_HERITAGE_HOSPITALITY | METRO_BUSINESS_AND_MICE_OWNER | MIDSCALE_AND_ECONOMY_CHAIN | ASSET_LIGHT_MANAGEMENT_FRANCHISOR | HOTEL_TURNAROUND_AND_REIT_PLATFORM | GLOBAL_HOSPITALITY_PRINCIPAL",
  "makes": ["Brand / Tier 1", "Non-Room Engine 2", "..."],
  "depends_on": ["Land / Real Estate Asset 1", "Loyalty / Distribution Engine 2", "..."],
  "principal_relationship": {
    "backing": "GROUP_OR_SPONSOR_OR_INDEPENDENT",
    "ownership_vs_managed_mix": "X_PCT_OWNED_Y_PCT_MANAGED_ASSET_LIGHT",
    "brand_royalty_status": "PROPRIETARY_0_PCT_ROYALTY_OR_GLOBAL_FRANCHISE_FEE"
  },
  "moat_vectors": {
    "positional": "...",
    "product": "...",
    "technological": "...",
    "governance": "..."
  },
  "pass_through": "HYBRID_OWNED_ARR_PLUS_ASSET_LIGHT_FEES",
  "unit_economics": {
    "arr_and_revpar_tier": "Ultra-Luxury / Upper-Upscale / Mid-Scale / Lean-Luxe positioning",
    "ownership_leverage": "High Fixed-Cost Owned vs. Asset-Light Fee Annuity",
    "non_room_revenue_mix": "F&B, MICE, Weddings, Flight Catering, or Commercial Office share",
    "cfo_to_ebitda_conversion": "..."
  },
  "polarity": {
    "arr_and_occupancy_upcycle": 1,
    "interest_rate_cuts": 0,
    "corporate_and_gcc_travel_up": 1,
    "domestic_wedding_and_spiritual_tourism_up": 1,
    "new_branded_supply_pipeline_surge": 0,
    "staff_wage_and_utility_inflation": -1
  },
  "correlates_with": ["NSE:PEER1", "NSE:PEER2", "..."],
  "event_tags": [
    "LIVE_NOV_2026_TAG_1",
    "LIVE_NOV_2026_TAG_2",
    "LIVE_NOV_2026_TAG_3",
    "LIVE_NOV_2026_TAG_4"
  ],
  "semantic_text": "Sign-explicit causal summary describing the hotelier's brand portfolio, owned vs. asset-light key mix, RevPAR operating leverage, non-room MICE/F&B moats, and macro/supply directional sensitivities."
}
