# Electric Vehicle Market Performance & Insights

An interactive dashboard built from a 100,000-row EV market dataset. It shows sales, manufacturers, battery technology, range, pricing, charging, degradation and customer ratings, with filters for model year, market region, vehicle category and battery type.

**Live demo:** https://your-project.vercel.app
**Repository:** https://github.com/your-username/ev-market-dashboard

---

## Who it is for

| Persona | Role | What the dashboard gives them |
|---|---|---|
| Emily Johnson | EV Market Strategy Director | Category sales, leading manufacturers, customer satisfaction by segment, growth by model year |
| David Chen | Automotive BI Manager | Manufacturer share, battery type distribution, manufacturing country and region analysis, ratings |
| Dr. Sarah Williams | Sustainable Mobility Researcher | Battery comparison (range, degradation, charging), adoption over time, CO₂ saved |

---

## Dataset

`ev_market_test.csv` has **100,000 EV models**, **36 columns**, **200 manufacturers**, model years **2018–2026**, **15 vehicle categories**, **5 battery types**, **10 manufacturing countries** and **7 market regions**.

Main columns used: `manufacturer`, `model_year`, `manufacturing_country`, `market_region`, `category`, `battery_type`, `battery_degradation_pct_5yr`, `battery_cycle_life`, `range_km`, `charging_dc_fast_time_min`, `price_usd`, `resale_value_pct_3yr`, `co2_saved_tons_per_year`, `annual_sales_units`, `customer_rating`.

### Data cleaning

| Issue | Handling |
|---|---|
| Missing `annual_sales_units` (989 rows) | Counted as 0 units in sales totals |
| Missing `customer_rating` (1,931), `battery_cycle_life` (2,028), `resale_value_pct_3yr` (3,057) | Left out of those averages only |
| Duplicate vehicle IDs | Removed (none found) |
| Extreme sales values (max 772,442) | Kept, since they are valid high-volume models |
| `efficiency_wh_per_km` has extreme outliers | Not used in the dashboard |

---

## Dashboard contents

- **Filters:** model year, market region, vehicle category, battery type, reset button
- **KPI cards:** models, total sales, average range, average price, customer rating, DC fast-charge time, CO₂ saved
- **12 charts:** sales by year, battery share of sales, battery adoption over time, sales by region, sales by category, top 15 manufacturers, range by battery type, range by category, rating by category, sales by manufacturing country, 5-year degradation, DC fast-charge time
- **Category scorecard:** sortable table of models, sales, price, range, rating and resale value
- **Auto-generated insights** that update with the filters

Two charts respond to fewer filters because they come from separate summary tables: top manufacturers (year and category) and manufacturing country (year, category and battery).

---

## Key findings

- **Total sales:** about **772.6 million units** across all model years, with no strong upward trend (roughly 82–88 million units per year).
- **Categories:** Two-Wheeler Scooters lead with **11.0%** of sales, followed by Sedans (**10.1%**) and Compact SUVs (**9.9%**). Sales are spread fairly evenly across all 15 categories.
- **Battery technology:** NMC (**33.5%**) and LFP (**32.2%**) hold about two thirds of sales. NCA has **17.3%**, Sodium-Ion **9.8%** and Solid-State **7.2%**.
- **Durability:** Solid-State has the lowest 5-year degradation (**7.4%**), then LFP (**10.1%**). NMC, NCA and Sodium-Ion are all near **14%**.
- **Range:** Luxury Sedans have the longest average range (**549 km**) and Two-Wheeler Scooters the shortest (**105 km**). Average range is almost identical across battery types (about 321–325 km).
- **Customer satisfaction:** Ratings are high and close together (average **4.08 / 5**), from **4.07** for Electric Trucks to **4.10** for Crossovers.
- **Manufacturing:** China, Japan and Vietnam lead by sales, each around **10%**. Europe is the top market region (**14.6%**).
- **Competition:** The market is fragmented. The largest manufacturers (SurgeWorks, CurrentMobility, ElektraMobility) each hold only about **0.6%** of sales.

---

## Project structure

```
ev-market-dashboard/
├── index.html        # finished dashboard (data embedded), deployed to Vercel
├── template.html     # dashboard code with a data placeholder
├── build.py          # cleans the CSV and builds index.html
├── data/             # put ev_market_test.csv here (ignored by Git)
├── .gitignore
└── README.md
```

## Run locally

```bash
git clone https://github.com/your-username/ev-market-dashboard.git
cd ev-market-dashboard
npx serve .          # or just open index.html in a browser
```

## Rebuild with new data

```bash
pip install pandas
python build.py data/ev_market_test.csv
```

This reads the CSV, aggregates it into small summary tables and writes a new `index.html`.

## Deploy on Vercel

1. Push the repo to GitHub.
2. Import it at [vercel.com](https://vercel.com), set the framework preset to **Other**, leave build settings empty.
3. Click **Deploy**.

## Tech stack

Python (pandas) for data preparation, HTML, CSS and JavaScript, Chart.js for charts, Vercel for hosting.

## Author

**Your Name**, GitHub: [@your-username](https://github.com/your-username)

## License

MIT
