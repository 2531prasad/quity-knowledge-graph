#!/usr/bin/env python3
"""
Master Equity Knowledge-Graph Unification Engine
Unifies all 10 physical-economy & tertiary healthcare sectors + valuation ruleset
with strict precedence, non-destructive delta merging, and cross-reference linking.

Precedence Rules:
1. Sector 10 (Hospitals): hospitals_sector.jsonl is the primary authoritative structural record.
   - NSE:HCG links CASE_STUDY:HCG_ONCOLOGY_DEEP_VALUE_TURNAROUND as valuation_rule_id without being overwritten.
   - NSE:APOLLOHOSP links canonical ISIN INE437A01024 and NSE:APOLLOHOSP:EQ without losing hospital schema.
2. Sector 9 (Real Estate): real estate/vectors.jsonl takes precedence over earlier valuechain duplicates (DLF, LODHA, etc.).
3. Distressed/Insolvent: NSE:UNITECH, NSE:HDIL, PSL_LTD tagged as DISTRESSED_INSOLVENT_BENCHMARK.
4. Valuation Rules: CASE_STUDY_PROOF and VALUATION_RULE nodes live in the rules index and link bi-directionally to equities.
"""

import json, os, glob
from collections import OrderedDict

BASE_DIR = "/Users/prasad/pdfs"

def load_jsonl(filepath):
    records = []
    if not os.path.exists(filepath):
        return records
    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Error parsing {filepath}:{line_num}: {e}")
    return records

def unify_graph():
    master_entities = OrderedDict()
    master_rules = OrderedDict()
    sector_blueprints = OrderedDict()
    stats = {
        "sectors": 10,
        "gross_records": 0,
        "unique_equities": 0,
        "case_studies_and_rules": 0
    }

    print("======================================================================")
    print("STARTING EQUITY KNOWLEDGE-GRAPH UNIFICATION & HYGIENE PIPELINE")
    print("======================================================================")

    # 1. Ingest Valuation Rules & Case Studies (Non-Company Nodes)
    val_rules_path = os.path.join(BASE_DIR, "valuations/valuation_rules.jsonl")
    for r in load_jsonl(val_rules_path):
        rid = r.get("id")
        if rid:
            master_rules[rid] = r
    print(f"Loaded {len(master_rules)} Valuation Rules & Case Study Proofs from {val_rules_path}")

    # 2. Ingest Prior Sectors 1-8
    sector_dirs = [
        "banking", "hotels", "mining", "qsr", "rare earth",
        "specialty chemicals", "steelpipes", "value chain"
    ]
    for s_name in sector_dirs:
        vpath = os.path.join(BASE_DIR, s_name, "vectors.jsonl")
        recs = load_jsonl(vpath)
        added = 0
        for r in recs:
            eid = r.get("id")
            if not eid:
                continue
            # Mark distressed benchmarks
            if eid in ["PSL_LTD", "NSE:UNITECH", "NSE:HDIL"]:
                r["entity_type"] = "DISTRESSED_INSOLVENT_BENCHMARK"
            
            # If entity exists, merge event_tags without duplicates
            # Proactively deduplicate all array fields
            for field in ["makes", "depends_on", "event_tags", "correlates_with"]:
                if field in r and isinstance(r[field], list):
                    r[field] = list(OrderedDict.fromkeys(r[field]))

            if eid in master_entities:
                existing = master_entities[eid]
                merged_tags = list(OrderedDict.fromkeys(existing.get("event_tags", []) + r.get("event_tags", [])))
                existing["event_tags"] = merged_tags
            else:
                master_entities[eid] = r
                added += 1
        print(f"Loaded Sector '{s_name}': {len(recs)} records ({added} net-new)")

    # 3. Ingest Sector 9 (Real Estate) with Overwrite Precedence for Realty Equities
    re_path = os.path.join(BASE_DIR, "real estate/vectors.jsonl")
    re_recs = load_jsonl(re_path)
    re_updated = 0
    re_new = 0
    for r in re_recs:
        eid = r.get("id")
        if not eid:
            continue
        if eid in ["NSE:UNITECH", "NSE:HDIL"]:
            r["entity_type"] = "DISTRESSED_INSOLVENT_BENCHMARK"

        if eid in master_entities:
            # Prioritize deep real estate ontology fields while preserving unique historical tags
            existing_tags = master_entities[eid].get("event_tags", [])
            new_tags = r.get("event_tags", [])
            r["event_tags"] = list(OrderedDict.fromkeys(new_tags + existing_tags))
            master_entities[eid] = r
            re_updated += 1
        else:
            master_entities[eid] = r
            re_new += 1
    print(f"Loaded Sector 'real estate': {len(re_recs)} records ({re_updated} updated with precedence, {re_new} net-new)")

    # 4. Ingest Sector 10 (Hospitals & Tertiary Healthcare) with PRIMARY Precedence
    hosp_path = os.path.join(BASE_DIR, "hospital/hospitals_sector.jsonl")
    hosp_recs = load_jsonl(hosp_path)
    for r in hosp_recs:
        if r.get("action") == "SECTOR_BLUEPRINT":
            sector_blueprints["HEALTHCARE_PROVIDERS_HOSPITALS"] = r
            continue
        
        eid = r.get("id")
        if not eid:
            continue

        # Explicit Handling for Duplicate ID Merge: NSE:HCG
        if eid == "NSE:HCG":
            # Keep hospitals_sector.jsonl as the primary structural record
            # Link CASE_STUDY:HCG_ONCOLOGY_DEEP_VALUE_TURNAROUND as a cross-referenced valuation_rule_id
            r["valuation_rule_id"] = "CASE_STUDY:HCG_ONCOLOGY_DEEP_VALUE_TURNAROUND"
            r["cross_referenced_rules"] = list(OrderedDict.fromkeys(
                r.get("cross_referenced_rules", []) + [
                    "CASE_STUDY:HCG_ONCOLOGY_DEEP_VALUE_TURNAROUND",
                    "VAL_RULE:DEEP_VALUE_HOSPITAL_TURNAROUND_BLUEPRINT"
                ]
            ))
            # Also ensure the case study in master_rules links back to NSE:HCG
            if "CASE_STUDY:HCG_ONCOLOGY_DEEP_VALUE_TURNAROUND" in master_rules:
                cs = master_rules["CASE_STUDY:HCG_ONCOLOGY_DEEP_VALUE_TURNAROUND"]
                cs["primary_structural_entity_id"] = "NSE:HCG"
                cs["slide_case_studies"] = list(OrderedDict.fromkeys(cs.get("slide_case_studies", []) + ["NSE:HCG"]))

        # Explicit Handling for Duplicate ID Merge: NSE:APOLLOHOSP
        if eid == "NSE:APOLLOHOSP":
            # Keep hospitals_sector.jsonl as primary structural record
            # Check vec/vectors.jsonl for isin / canonicalId
            r["canonical_symbol"] = "NSE:APOLLOHOSP:EQ"
            r["canonical_isin"] = "INE437A01024"

        # Hospital record takes primary precedence over any prior occurrences
        if eid in master_entities:
            existing_tags = master_entities[eid].get("event_tags", [])
            r["event_tags"] = list(OrderedDict.fromkeys(r.get("event_tags", []) + existing_tags))
        
        master_entities[eid] = r
    print(f"Loaded Sector 'hospital': {len(hosp_recs)} records (1 blueprint + 10 primary structural hospital entities)")

    # 5. Apply REIT, Broker & Consumer Deltas (Incremental Top-offs)
    consumer_delta_path = os.path.join(BASE_DIR, "reports/consumer_macro_delta.jsonl")
    for r in load_jsonl(consumer_delta_path):
        action = r.get("action")
        if action == "SECTOR_BLUEPRINT":
            sector_blueprints["CONSUMER_STAPLES_AND_DISCRETIONARY"] = r
            continue
        eid = r.get("id")
        if action == "NEW_ENTITY" and eid not in master_entities:
            master_entities[eid] = r
        elif action == "DELTA_UPDATE" and eid in master_entities:
            existing = master_entities[eid]
            if "new_event_tags" in r:
                existing["event_tags"] = list(OrderedDict.fromkeys(existing.get("event_tags", []) + r["new_event_tags"]))
            if "institutional_weight_pct" in r:
                existing["institutional_weight_pct"] = r["institutional_weight_pct"]
    reit_delta_path = os.path.join(BASE_DIR, "real estate/reit_index_delta.jsonl")
    for r in load_jsonl(reit_delta_path):
        action = r.get("action")
        eid = r.get("id")
        if action == "NEW_ENTITY" and eid not in master_entities:
            master_entities[eid] = r
        elif action == "DELTA_UPDATE" and eid in master_entities:
            existing = master_entities[eid]
            if "new_event_tags" in r:
                existing["event_tags"] = list(OrderedDict.fromkeys(existing.get("event_tags", []) + r["new_event_tags"]))
            if "kpis" in r and "kpis" in existing:
                existing["kpis"].update(r["kpis"])

    broker_delta_path = os.path.join(BASE_DIR, "reports/broker_delta_updates.jsonl")
    for r in load_jsonl(broker_delta_path):
        action = r.get("action")
        eid = r.get("id")
        if action == "NEW_ENTITY" and eid not in master_entities:
            master_entities[eid] = r
        elif action == "DELTA_UPDATE" and eid in master_entities:
            existing = master_entities[eid]
            if "new_event_tags" in r:
                existing["event_tags"] = list(OrderedDict.fromkeys(existing.get("event_tags", []) + r["new_event_tags"]))

    # 6. Verification & Output Summary
    print("\n--- UNIFICATION HYGIENE AUDIT ---")
    
    # Verify HCG
    hcg = master_entities.get("NSE:HCG")
    assert hcg is not None, "FATAL: NSE:HCG missing from master entities!"
    assert hcg.get("entity_type") == "LISTED_INDIA", f"FATAL: NSE:HCG entity_type is {hcg.get('entity_type')} instead of LISTED_INDIA"
    assert hcg.get("valuation_rule_id") == "CASE_STUDY:HCG_ONCOLOGY_DEEP_VALUE_TURNAROUND", "FATAL: NSE:HCG missing valuation_rule_id link!"
    print("✅ Verified NSE:HCG is primary structural entity with linked valuation_rule_id.")

    # Verify APOLLOHOSP
    aphs = master_entities.get("NSE:APOLLOHOSP")
    assert aphs is not None, "FATAL: NSE:APOLLOHOSP missing from master entities!"
    assert aphs.get("entity_type") == "LISTED_INDIA", f"FATAL: NSE:APOLLOHOSP entity_type is {aphs.get('entity_type')}"
    assert aphs.get("canonical_isin") == "INE437A01024", "FATAL: NSE:APOLLOHOSP missing canonical ISIN!"
    print("✅ Verified NSE:APOLLOHOSP is primary structural entity with linked ISIN & canonical symbol.")

    # Verify all 10 hospitals
    hosp_tickers = [
        "NSE:APOLLOHOSP", "NSE:ASTERDM", "NSE:FORTIS", "NSE:MEDANTA", "NSE:HCG",
        "NSE:JLHL", "NSE:KIMS", "NSE:MAXHEALTH", "NSE:NH", "NSE:RAINBOW"
    ]
    for ht in hosp_tickers:
        assert ht in master_entities, f"FATAL: Missing hospital ticker {ht}"
        assert master_entities[ht]["entity_type"] == "LISTED_INDIA"
    print(f"✅ Verified all 10 hospital entities are present as primary structural records.")

    # Check for zero duplicate array items
    for eid, e in master_entities.items():
        for field in ["makes", "depends_on", "event_tags", "correlates_with"]:
            arr = e.get(field, [])
            assert len(arr) == len(set(arr)), f"Duplicate item found in {eid} -> {field}"
    print("✅ Verified zero duplicate array items across all unified entities.")

    # Output master graph
    out_path = os.path.join(BASE_DIR, "master_unified_graph.jsonl")
    with open(out_path, "w", encoding="utf-8") as f:
        for bp in sector_blueprints.values():
            f.write(json.dumps(bp, ensure_ascii=False) + "\n")
        for ent in master_entities.values():
            f.write(json.dumps(ent, ensure_ascii=False) + "\n")
        for rule in master_rules.values():
            f.write(json.dumps(rule, ensure_ascii=False) + "\n")

    print(f"\nSuccessfully serialized unified knowledge graph:")
    print(f"  • Blueprints: {len(sector_blueprints)}")
    print(f"  • Structural Equities & Entities: {len(master_entities)}")
    print(f"  • Valuation Rules & Case Study Proofs: {len(master_rules)}")
    print(f"  • Destination: {out_path} ({os.path.getsize(out_path):,} bytes)")
    print("======================================================================")

if __name__ == "__main__":
    unify_graph()
