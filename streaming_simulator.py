import time
import json
import random
import uuid
import pandas as pd
from datetime import datetime

ZONES = ["Indiranagar", "Koramangala", "HSR Layout", "Whitefield", "MG Road"]


def generate_telemetry_batch(num_records=1200):
    records = []
    print("Simulating real-time geospatial telemetry stream...")

    for _ in range(num_records):
        pickup_zone = random.choice(ZONES)
        drop_zone = random.choice([z for z in ZONES if z != pickup_zone])
        hour_of_day = random.randint(0, 23)

        # Peak traffic hours simulation
        is_peak = 1 if hour_of_day in [8, 9, 10, 17, 18, 19, 20] else 0

        # Supply vs Demand dynamics
        demand_requests = random.randint(50, 250) if is_peak else random.randint(10, 70)
        available_drivers = random.randint(10, 80) if is_peak else random.randint(30, 100)

        supply_demand_ratio = round(demand_requests / max(available_drivers, 1), 2)

        # Trip distance and base time
        distance_km = round(random.uniform(2.0, 22.0), 2)
        traffic_delay = random.uniform(5.0, 25.0) if is_peak else random.uniform(0.0, 8.0)
        actual_eta_mins = round((distance_km * 2.8) + traffic_delay + random.normalvariate(2.0, 1.0), 2)

        # Surge pricing multiplier rule
        if supply_demand_ratio > 2.5:
            surge_multiplier = round(1.0 + (supply_demand_ratio * 0.35), 2)
        elif supply_demand_ratio > 1.2:
            surge_multiplier = round(1.0 + (supply_demand_ratio * 0.15), 2)
        else:
            surge_multiplier = 1.0

        record = {
            "ride_id": str(uuid.uuid4())[:8],
            "timestamp": datetime.utcnow().isoformat(),
            "pickup_zone": pickup_zone,
            "drop_zone": drop_zone,
            "hour_of_day": hour_of_day,
            "is_peak_hour": is_peak,
            "demand_requests": demand_requests,
            "available_drivers": available_drivers,
            "supply_demand_ratio": supply_demand_ratio,
            "distance_km": distance_km,
            "surge_multiplier": surge_multiplier,
            "actual_eta_mins": actual_eta_mins
        }
        records.append(record)

    df = pd.DataFrame(records)
    df.to_csv("rapido_telemetry.csv", index=False)
    print(f"Stream simulation complete. Saved {len(df)} records to 'rapido_telemetry.csv'.")


if __name__ == "__main__":
    generate_telemetry_batch()