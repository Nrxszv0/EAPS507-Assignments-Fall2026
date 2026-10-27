import os
import numpy as np

def analyze_station(station_id, n_days=3650):
    rng = np.random.default_rng(10_000 + station_id)
    day = np.arange(n_days)
    temperature = 25 + 7 * np.sin(2 * np.pi * day / 365.25) + rng.normal(0, 3, n_days)
    threshold = np.quantile(temperature, 0.95)
    return {"station": station_id, "p95": threshold, "exceedance_days": int((temperature > threshold).sum()), "pid": os.getpid()}
