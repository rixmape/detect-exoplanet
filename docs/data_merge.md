# Merging Kepler and TESS Datasets

This document outlines the strategy for merging the Kepler and TESS exoplanet datasets into a single, unified dataset for a machine learning model. The primary goal is to standardize disparate data formats and handle inconsistencies to create a clean, comprehensive source for analysis.

## 1. Unified Schema Creation

A master schema was created to standardize column names. This involved mapping columns from the `kepler.md` and `tess.md` documents that describe the same physical properties. The following is a list of the key columns that were merged:

| **Kepler (KOI) Column** | **TESS (TOI) Column** | **Unified Column Name** | **Description** |
| :--- | :--- | :--- | :--- |
| `kepid` | `tid` | `star_id` | A unique ID for the host star in its respective input catalog. |
| `kepoi_name` | `toi` | `object_name` | A number used to identify and track a transiting object of interest. |
| `koi_disposition` | `tfopwg_disp` | `disposition` | The classification of the object (e.g., Confirmed Planet, Planetary Candidate, or False Positive). |
| `ra`, `dec` | `ra`, `dec` | `ra_deg`, `dec_deg` | The celestial coordinates of the star in decimal degrees. |
| `koi_steff` | `st_teff` | `stellar_temp_k` | The effective temperature of the host star in Kelvin. |
| `koi_srad` | `st_rad` | `stellar_radius_solar` | The radius of the host star in units of solar radii. |
| `koi_period` | `pl_orbper` | `orbital_period_days` | The time the planet takes to make a complete orbit around its host star. |
| `koi_prad` | `pl_rade` | `planet_radius_earth` | The radius of the planet in units of Earth radii. |
| `koi_duration` | `pl_trandurh` | `transit_duration_hours` | The length of time from the beginning to the end of the planet's transit. |
| `koi_depth` | `pl_trandep` | `transit_depth_ppm` | The fractional decrease in the host star's flux caused by the transiting planet. |
| `koi_teq` | `pl_eqt` | `planet_eq_temp_k` | The equilibrium temperature of the planet as modeled by a black body. |

Columns unique to a single mission, like `stellar_distance_pc` from TESS, were also incorporated into the final schema to retain all available information.

## 2. Data Loading and Preprocessing

Each dataset was loaded from its source, and during this process, a `mission` column was added to each dataframe to identify the origin of the data (`Kepler` or `TESS`). To handle data corruption, the parser was configured to skip malformed rows, which prevented the script from failing on inconsistent line formats.

## 3. Handling Missing Data

Following the standardization of column names, numerical columns were checked for missing values. A simple imputation strategy was applied where any missing numerical data was filled with the median value of its respective column. This ensures that the dataset is complete for model training and that the imputation is robust to outliers.

## 4. Final Merging

The preprocessed dataframes were then concatenated, resulting in a single, unified dataset. This final dataset contains all the standardized columns from both missions, along with a `mission` flag for provenance, and is ready for feature engineering and model training.
