"""Build index.html from the EV market CSV.
Usage: python build.py data/ev_market_test.csv
Aggregates 100k rows into small cubes (year/region/category/battery etc.) and
embeds them in template.html so the dashboard runs without a server."""
import sys, json
import pandas as pd

src = sys.argv[1] if len(sys.argv) > 1 else "data/ev_market_test.csv"
df = pd.read_csv(src)

# ---- cleaning ----
df = df.drop_duplicates("vehicle_id")
df["sales"] = df["annual_sales_units"].fillna(0)          # missing sales -> 0 units
for c in ["customer_rating", "battery_cycle_life", "resale_value_pct_3yr"]:
    df[c + "_n"] = df[c].notna().astype(int)               # keep counts so averages ignore blanks
    df[c + "_s"] = df[c].fillna(0)

METRICS = dict(
    n=("vehicle_id", "count"), sales=("sales", "sum"),
    range_s=("range_km", "sum"), price_s=("price_usd", "sum"),
    rat_s=("customer_rating_s", "sum"), rat_n=("customer_rating_n", "sum"),
    dc_s=("charging_dc_fast_time_min", "sum"), deg_s=("battery_degradation_pct_5yr", "sum"),
    cyc_s=("battery_cycle_life_s", "sum"), cyc_n=("battery_cycle_life_n", "sum"),
    res_s=("resale_value_pct_3yr_s", "sum"), res_n=("resale_value_pct_3yr_n", "sum"),
    co2_s=("co2_saved_tons_per_year", "sum"))

def cube(data, dims):
    keys = {d: sorted(data[d].unique().tolist()) for d in dims}
    g = data.groupby(dims, observed=True).agg(**METRICS).reset_index()
    for d in dims:
        g[d] = g[d].map({v: i for i, v in enumerate(keys[d])})
    cols = dims + list(METRICS)
    rows = [[round(float(x), 1) if i >= len(dims) else int(x) for i, x in enumerate(r)]
            for r in g[cols].itertuples(index=False)]
    for r in rows:
        r[len(dims):] = [int(v) if float(v).is_integer() else v for v in r[len(dims):]]
    return {"d": dims, "k": keys, "r": rows}

df["model_year"] = df["model_year"].astype(str)
top = df.groupby("manufacturer")["sales"].sum().nlargest(20).index
data = {
    "main": cube(df.rename(columns={"model_year": "year", "market_region": "region", "battery_type": "battery"}),
                 ["year", "region", "category", "battery"]),
    "country": cube(df.rename(columns={"model_year": "year", "manufacturing_country": "country", "battery_type": "battery"}),
                    ["country", "year", "category", "battery"]),
    "mfr": cube(df[df.manufacturer.isin(top)].rename(columns={"model_year": "year", "manufacturer": "mfr"}),
                ["mfr", "year", "category"]),
}
html = open("template.html", encoding="utf-8").read().replace("__DATA__", json.dumps(data, separators=(",", ":")))
open("index.html", "w", encoding="utf-8").write(html)
print("rows:", len(df), "| cells:", {k: len(v["r"]) for k, v in data.items()}, "| index.html KB:", len(html) // 1024)
