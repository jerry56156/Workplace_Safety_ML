import pandas as pd


df = pd.read_csv("osha2024.csv", encoding="latin1")

# List of relevant NAICS codes
keep_codes = [
    325311.00, 325311, 325311.0, # Nitrogenous Fertilizer Manufacturing
    325312.00, 325312, 325312.0, # Phosphatic Fertilizer Manufacturing
    325314.00, 325314, 325314.0, # Fertilizer (Mixing Only) Manufacturing
    212391.00, 212391, 212391.0, # Potash, Soda, and Borate Mineral Mining
    212392.00, 212392, 212392.0, # Phosphate Rock Mining
    212393.00, 212393, 212393.0, # Other Chemical and Fertilizer Mineral Mining
    325180.00, 325180, 325180.0, # Other Basic Inorganic Chemical Manufacturing
    325199.00, 325199, 325199.0  # Other Basic Organic Chemical Manufacturing
]

# If NAICS codes are stored as strings, convert them first
df['naics_code'] = df['naics_code'].astype(str)

# Filter to keep only rows where NAICS matches one of the codes
df_filtered = df[df['naics_code'].isin([str(code) for code in keep_codes])]

# Save filtered dataset
df_filtered.to_csv("filtered2024.csv", index=False)
