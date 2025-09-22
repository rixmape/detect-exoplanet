import pandas as pd


def create_unified_schema():
    """Defines the mapping from original column names to a unified schema."""
    kepler_mapping = {
        "kepid": "star_id",
        "kepoi_name": "object_name",
        "koi_disposition": "disposition",
        "kepler_name": "alias",
        "koi_count": "num_planet_candidates",
        "ra": "ra_deg",
        "dec": "dec_deg",
        "koi_steff": "stellar_temp_k",
        "koi_srad": "stellar_radius_solar",
        "koi_slogg": "stellar_logg_cms2",
        "koi_kepmag": "stellar_mag",
        "koi_period": "orbital_period_days",
        "koi_prad": "planet_radius_earth",
        "koi_duration": "transit_duration_hours",
        "koi_depth": "transit_depth_ppm",
        "koi_teq": "planet_eq_temp_k",
        "koi_insol": "planet_insolation_earthflux",
        "koi_time0bk": "transit_midpoint_bjd",
        "koi_impact": "impact_parameter",
    }

    tess_mapping = {
        "tid": "star_id",
        "toi": "object_name",
        "tfopwg_disp": "disposition",
        "ctoi_alias": "alias",
        "pl_pnum": "num_planet_candidates",
        "ra": "ra_deg",
        "dec": "dec_deg",
        "st_teff": "stellar_temp_k",
        "st_rad": "stellar_radius_solar",
        "st_logg": "stellar_logg_cms2",
        "st_tmag": "stellar_mag",
        "pl_orbper": "orbital_period_days",
        "pl_rade": "planet_radius_earth",
        "pl_trandurh": "transit_duration_hours",
        "pl_trandep": "transit_depth_ppm",
        "pl_eqt": "planet_eq_temp_k",
        "pl_insol": "planet_insolation_earthflux",
        "pl_tranmid": "transit_midpoint_bjd",
        "st_dist": "stellar_distance_pc",
    }

    return kepler_mapping, tess_mapping


def load_and_preprocess_data(file_path, mission_name, mapping):
    """Loads a dataset, renames columns, consolidates labels, and adds a mission column."""
    df = pd.read_csv(file_path, low_memory=False)
    df = df.rename(columns=mapping)
    df["mission"] = mission_name

    label_map = {
        "CONFIRMED": "CONFIRMED",
        "CP": "CONFIRMED",
        "KP": "CONFIRMED",
        "CANDIDATE": "CANDIDATE",
        "PC": "CANDIDATE",
        "APC": "CANDIDATE",
        "FALSE POSITIVE": "FALSE POSITIVE",
        "FP": "FALSE POSITIVE",
        "FA": "FALSE POSITIVE",
    }
    if "disposition" in df.columns:
        df["disposition"] = df["disposition"].replace(label_map)

    for col in df.columns:
        if df[col].dtype == "object" and any(char.isdigit() for char in str(df[col].iloc[0])):
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def impute_missing_values(df):
    """Fills missing numerical values with the median of the column."""
    numeric_cols = df.select_dtypes(include=["number"]).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())
    return df


def main():
    """Main function to run the data preparation pipeline."""
    kepler_mapping, tess_mapping = create_unified_schema()

    kepler_df = load_and_preprocess_data("data/kepler.csv", "Kepler", kepler_mapping)
    tess_df = load_and_preprocess_data("data/tess.csv", "TESS", tess_mapping)

    common_cols = list(set(kepler_df.columns) & set(tess_df.columns))
    kepler_df_common = kepler_df[common_cols]
    tess_df_common = tess_df[common_cols]

    unified_df = pd.concat([kepler_df_common, tess_df_common], ignore_index=True)
    unified_df = impute_missing_values(unified_df)

    print(unified_df.info())
    unified_df.to_csv("data/merged_data.csv", index=False)


if __name__ == "__main__":
    main()
