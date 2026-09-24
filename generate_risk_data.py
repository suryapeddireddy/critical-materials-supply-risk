import pandas as pd
import numpy as np

materials = ['Lithium', 'Cobalt', 'Nickel', 'Neodymium', 'Graphite']

# Defining the values separately to ensure they compile perfectly
hhi_values = [2800, 4100, 1900, 6500, 4800]

data = {
    'Material': materials,
    'Primary_Source_Country': ['Australia', 'DR Congo', 'Indonesia', 'China', 'China'],
    'Geopolitical_Concentration_HHI': hhi_values,
    'Economic_Vulnerability_Score': [8.5, 7.8, 6.2, 9.2, 7.5],
    'EU_Import_Dependency_Pct': [98.0, 85.0, 65.0, 100.0, 95.0],
    'Current_Recycling_Rate_EOL_RIR': [1.2, 9.5, 14.0, 0.5, 2.0]
}

df = pd.DataFrame(data)

df['Unified_Vulnerability_Index'] = (
    (df['Geopolitical_Concentration_HHI'] / 1000) * 0.4 + 
    df['Economic_Vulnerability_Score'] * 0.4 + 
    (df['EU_Import_Dependency_Pct'] / 10) * 0.2
) - (df['Current_Recycling_Rate_EOL_RIR'] * 0.05)

df['Unified_Vulnerability_Index'] = df['Unified_Vulnerability_Index'].round(2)
df.to_csv('critical_materials_risk_data.csv', index=False)
print("✓ CRM Risk Database successfully generated: 'critical_materials_risk_data.csv'")
