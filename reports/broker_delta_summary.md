# Broker Sector Delta Architecture: Capital Goods Q2 FY27
**Source Document:** `CapitalGoods-8-10-26-PL.pdf` (Prabhudas Lilladher Institutional Equities, Oct 8, 2026)  
**Deliverable:** [`broker_delta_updates.jsonl`](file:///Users/prasad/pdfs/reports/broker_delta_updates.jsonl) (65.8 KB, 26 Entities)  
**Mirror Path:** [`/Users/prasad/pdfs/broker_delta_updates.jsonl`](file:///Users/prasad/pdfs/broker_delta_updates.jsonl)

---

## 1. Executive Summary & Macro Infrastructure Currents

The October 2026 capital goods coverage report captures an acute divergence between **T&D-focused product equipment manufacturers** (super-cycle pricing power and volume scaling) and **turnkey infrastructure EPC players** (geopolitical shipping friction, logistics delays, and raw material pass-through lags):

```
                        ┌────────────────────────────────────────────────────────┐
                        │      CABINET GREEN ENERGY CORRIDOR PHASE-III           │
                        │               (₹1.86 Lakh Cr Outlay)                   │
                        └───────────────────────────┬────────────────────────────┘
                                                    │
                 ┌──────────────────────────────────┴──────────────────────────────────┐
                 ▼                                                                     ▼
┌─────────────────────────────────┐                                   ┌─────────────────────────────────┐
│     T&D PRODUCT SPECIALISTS     │                                   │       TURNKEY INFRA EPC         │
│  (ENRIN, GVTD, HITACHI, VAMP)   │                                   │        (LT, KEC, KPIL)          │
├─────────────────────────────────┤                                   ├─────────────────────────────────┤
│ • EHV Transformers & STATCOMs   │                                   │ • Record Inflows (LT ₹1.4 Trn)  │
│ • HVDC Barmer-Kalamb Corridor   │                                   │ • Middle East Shipping Friction │
│ • Favorable Mix & Scale Leverage│                                   │ • Slower Revenue Recognition    │
│ • Expanding EBITDA Margins      │                                   │ • Civil Cost Overrun Compression│
└─────────────────────────────────┘                                   └─────────────────────────────────┘
```

### Core Macro & Thematic Tailwinds:
1. **Green Energy Corridor Phase-III:** Union Cabinet approval of ₹1.86 Lakh Cr capital outlay providing multi-year visibility for 765 kV / 1200 kV transmission substations, STATCOM dynamic reactive power compensation, and inter-state renewable evacuation.
2. **HVDC Transmission Super-Cycle:** Key landmark project award of Barmer–South Kalamb HVDC-LCC package (`NSE:GVT&D`) cementing domestic DC transmission infrastructure alongside Khavda and Bhadla renewable corridor buildouts (`NSE:POWERINDIA`, `NSE:ENRIN`).
3. **Defense Indigenization Acceleration:** Defence Acquisition Council (DAC) Acceptance of Necessity (AoN) approvals crossing ₹1.1–1.6 Lakh Cr in FY27 YTD, paired with the 6th Positive Indigenisation List. Strategic awards include BEML's ₹5,400 Cr Mumbai-Ahmedabad High-Speed Rail (MAHSR) bullet train sets, BEL's ₹69,800 Cr order backlog, and Solar Industries' scaling of Pinaka rockets and Nagastra loitering munitions.
4. **Middle East Geopolitical Friction:** Regional shipping disruptions through the Red Sea / Persian Gulf creating elevated ocean freight and milestone revenue-recognition delays for project EPC contractors (`NSE:LT`, `NSE:KEC`, `NSE:KPIL`).

---

## 2. Partition Breakdown: 12 Incremental Deltas vs. 14 Net-New Baselines

| Group | Count | Entities Covered | Action Type | Schema Characteristics |
| :--- | :---: | :--- | :--- | :--- |
| **Existing Graph Tickers** | **12** | `ABB`, `APARINDS`, `BEL`, `BHEL`, `GVT&D`, `HAL`, `POWERINDIA`, `CUMMINSIND`, `LT`, `SIEMENS`, `THERMAX`, `VOLTAMP` | `DELTA_UPDATE` | Incremental `2026_Q4_` event tags, catalyst summaries, and non-destructive delta semantic updates. Zero structural core overwriting. |
| **Net-New Graph Tickers** | **14** | `ENRIN` (Siemens Energy), `BEML`, `SOLARINDS`, `KEC`, `KPIL`, `ENGINERSIN`, `ELGIEQUIP`, `INGERRAND`, `KIRLOSPNEU`, `PRAJIND`, `TRITURBINE`, `CARBORUNIV`, `GRINDWELL`, `HARSHA` | `NEW_ENTITY` | Full institutional master schema: `makes`, `depends_on`, `principal_relationship`, 4-pillar `moat_vectors`, `polarity`, `correlates_with`, and dated `event_tags`. |

---

## 3. Net-New Baseline Entities Registry (14 Stocks)

1. **Siemens Energy India Limited (`NSE:ENRIN`)**
   * *Sub-Vertical:* EHV Power Transmission, Grid Stabilization & HVDC Systems
   * *Moat & Mechanics:* Pure-play demerged energy powerhouse supplying 765 kV / 1200 kV power transformers, STATCOMs, and HVDC converter packages. Direct technology transfer from Siemens Energy AG; zero net debt.
2. **BEML Limited (`NSE:BEML`)**
   * *Sub-Vertical:* Rail & Metro Rolling Stock, Defense Heavy Mobility & Mining Equipment
   * *Moat & Mechanics:* Sole domestic manufacturer for MAHSR bullet train trainsets (₹5,400 Cr contract), Vande Bharat sleepers, and heavy missile transporter-launchers (Pinaka, BrahMos).
3. **Solar Industries India Limited (`NSE:SOLARINDS`)**
   * *Sub-Vertical:* Industrial Explosives, Defense Munitions, Propellants & Warheads
   * *Moat & Mechanics:* 28-30% domestic commercial explosives share scaling into high-margin military munitions: Pinaka rockets, Nagastra loitering drones, and Bhargavastra counter-drone hard-kill systems.
4. **KEC International Limited (`NSE:KEC`)**
   * *Sub-Vertical:* Power Transmission & Distribution EPC, Railways, Civil & Cables
   * *Moat & Mechanics:* RPG Group flagship operating across 100+ countries with in-house tower testing stations; navigating Middle East shipping friction and civil project cost overruns.
5. **Kalpataru Projects International Limited (`NSE:KPIL`)**
   * *Sub-Vertical:* Power Transmission EPC, Oil & Gas Pipelines, Buildings & Water EPC
   * *Moat & Mechanics:* Merged EPC major with ₹9,500+ Cr quarterly inflows (₹4,000 Cr UAE project); deploying proceeds from 30.2% Linjemontage stake sale to de-lever balance sheet.
6. **Engineers India Limited (`NSE:ENGINERSIN`)**
   * *Sub-Vertical:* Hydrocarbon & Industrial Engineering Consultancy & Turnkey EPC
   * *Moat & Mechanics:* Navratna engineering consultancy with virtual monopoly in Indian refinery design; secured USD 450M Dangote refinery expansion consultancy in Kenya; debt-free cash-rich model.
7. **Elgi Equipments Limited (`NSE:ELGIEQUIP`)**
   * *Sub-Vertical:* Industrial Air Compressors & Pneumatic Power Systems
   * *Moat & Mechanics:* Top-2 domestic compressor OEM with ~30% share; patented AB series oil-free compressors; operational cost rationalization and disciplined price hikes counteracting input inflation.
8. **Ingersoll-Rand (India) Limited (`NSE:INGERRAND`)**
   * *Sub-Vertical:* Premium Centrifugal & Rotary Industrial Air Compressors
   * *Moat & Mechanics:* Centac centrifugal market leader (>40% RoCE); operationalizing 50% capacity expansion at Naroda facility for customized heavy compressors; debt-free MNC.
9. **Kirloskar Pneumatic Company Limited (`NSE:KIRLOSPNEU`)**
   * *Sub-Vertical:* Gas & Refrigeration Compressors, Air Compressors & Marine Gears
   * *Moat & Mechanics:* ~60% domestic market share in City Gas Distribution (CGD) CNG compressor packages; precision marine propulsion gearboxes for the Indian Navy.
10. **Praj Industries Limited (`NSE:PRAJIND`)**
    * *Sub-Vertical:* Bio-Energy Engineering, Critical Process Equipment & HiPurity Systems
    * *Moat & Mechanics:* 65% domestic share in bio-ethanol plants; scaling "GenX" modular process skids for energy transition, Sustainable Aviation Fuels (SAF), and data center cooling.
11. **Triveni Turbine Limited (`NSE:TRITURBINE`)**
    * *Sub-Vertical:* Industrial Steam Turbines (<100 MW) & Clean Energy Turbomachinery
    * *Moat & Mechanics:* ~60% domestic market share in sub-30 MW steam turbines; temporary margin compression from zero-margin utility NTPC contract resolving into high-margin export and aftermarket rebound in H2 FY27.
12. **Carborundum Universal Limited (`NSE:CARBORUNIV`)**
    * *Sub-Vertical:* Abrasives, Engineered Ceramics, Refractories & Electrominerals
    * *Moat & Mechanics:* Murugappa Group materials flagship; high-margin engineered ceramics (metallized switchgear cylinders, ballistic armor) offsetting electromineral subsidiary weakness.
13. **Grindwell Norton Limited (`NSE:GRINDWELL`)**
    * *Sub-Vertical:* High-Performance Abrasives, Silicon Carbide & Engineered Ceramics/Plastics
    * *Moat & Mechanics:* Saint-Gobain subsidiary with dominant abrasives leadership; rapid growth in performance plastics and ceramics; zero-debt balance sheet and superior cost competitiveness.
14. **Harsha Engineers International Limited (`NSE:HARSHA`)**
    * *Sub-Vertical:* Precision Bearing Cages & Specialized Stamping Components
    * *Moat & Mechanics:* ~50-60% domestic and ~6-7% global market share in brass bearing cages; mission-critical supplier to Timken, SKF, Schaeffler; scaling new Advantek manufacturing facility.

---

## 4. Verification & Negative Constraint Compliance

1. **Strict Exclusion of Broker Ratings & Targets:** Zero broker recommendations (`Buy`, `Hold`, `Accumulate`, `Reduce`), zero target prices (`TP`), and zero quarterly forward EPS/PAT estimates are included in the JSONL dataset.
2. **Preservation of Structural Cores:** Existing tickers receive targeted `2026_Q4_` delta tags and semantic catalyst updates without overwriting historical baseline properties.
3. **Array Uniqueness:** Set-based deduplication verified 100% uniqueness across all lists (`makes`, `depends_on`, `correlates_with`, `event_tags`).
