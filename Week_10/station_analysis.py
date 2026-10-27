import os
import numpy as np

def analyze_station(station_id, n_days=3650):
    rng = np.random.default_rng(10_000 + station_id)
    day = np.arange(n_days)
    temperature = 25 + 7 * np.sin(2 * np.pi * day / 365.25) + rng.normal(0, 3, n_days)
    threshold = np.quantile(temperature, 0.95)
    thresh_90 = np.quantile(temperature, 0.90)
    mean_temp = np.mean(temperature)
    days_over_90 = int((temperature > thresh_90).sum())
    return {"station": station_id, "p95": threshold, "mean_temp": mean_temp, "95_exceedance_days": int((temperature > threshold).sum()), "90_exceedance_days": days_over_90, "pid": os.getpid()}
