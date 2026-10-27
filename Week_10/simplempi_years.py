from pathlib import Path
import numpy as np
from simplempi.parfor import parfor, pprint

output_dir = Path("simplempi_output")
output_dir.mkdir(exist_ok=True)
years = list(range(2000, 2012))

for year in parfor(years):
    rng = np.random.default_rng(year)
    precip = rng.gamma(shape=2.0, scale=4.0, size=365)
    summary = np.array([year, precip.mean(), np.quantile(precip, 0.95)])
    np.savetxt(output_dir / f"precip_summary_{year}.csv", summary[None, :], delimiter=",", header="year,mean,p95", comments="")
    pprint(f"completed {year}")
