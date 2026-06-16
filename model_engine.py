def predict_event_impact(event_cause, expected_footfall, duration_hours, is_peak_hour):
    """
    Heuristic algorithm to quantify traffic impact and recommend resources.
    """
    # Base severity weights derived from typical traffic choke behavior
    base_severity = {
        'protest': 0.9,
        'procession': 0.8,
        'public_event': 0.7,
        'vip_movement': 0.6,
        'construction': 0.5
    }
    
    severity = base_severity.get(event_cause, 0.5)
    
    # Scale impact based on crowds and timing
    footfall_multiplier = min(expected_footfall / 10000, 2.5) 
    time_multiplier = 1.6 if is_peak_hour else 1.0
    duration_multiplier = 1.2 if duration_hours > 4 else 1.0
    
    # Calculate final impact score (Capped at 10)
    impact_score = min(severity * footfall_multiplier * time_multiplier * duration_multiplier * 5, 10.0)
    
    # Calculate the physical spillover radius
    impact_radius_km = max(0.5, impact_score * 0.3)
    
    # Intelligent Resource Allocation Formulas
    police_personnel = int(impact_score * 4) + (expected_footfall // 4000)
    barricades = int(impact_score * 12) + (expected_footfall // 1500)
    diversions_needed = max(1, int(impact_score // 2.5))
    
    return {
        "impact_score": round(impact_score, 1),
        "impact_radius_km": round(impact_radius_km, 2),
        "police_personnel": police_personnel,
        "barricades": barricades,
        "diversions_needed": diversions_needed
    }

def get_diversion_strategy(severity_score):
    if severity_score >= 8:
        return "CRITICAL: Implement hard road closures 2km from epicenter. Activate dynamic message signs on Outer Ring Road. Re-route heavy commercial vehicles."
    elif severity_score >= 5:
        return "HIGH: Create single-lane chokepoints. Deploy rapid response traffic units at adjacent major junctions. Limit U-turns."
    else:
        return "MODERATE: Monitor flow via CCTV. Place barricades on median gaps to prevent illegal crossings."