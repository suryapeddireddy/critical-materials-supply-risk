import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the manual data file
try:
    df = pd.read_csv('critical_materials_risk_data.csv')
    print("✓ Successfully loaded critical_materials_risk_data.csv")
except FileNotFoundError:
    print("❌ Error: Could not find 'critical_materials_risk_data.csv' in this folder!")
    exit()

# Set up clean, professional engineering grid styling
sns.set_theme(style="whitegrid")

# =========================================================================
# GRAPH 1: MULTI-DIMENSIONAL CIRCULARITY DEFICIT SCATTER MATRIX
# =========================================================================
plt.figure(figsize=(10, 6))

# X-Axis: Recycling Rate, Y-Axis: Concentration Monopoly Risk, Bubble Size: Import Dependence
scatter = plt.scatter(
    x=df['Current_Recycling_Rate_EOL_RIR'],
    y=df['Geopolitical_Concentration_HHI'],
    s=df['EU_Import_Dependency_Pct'] * 8, # Multiply to make bubble differences distinct
    c=df['Unified_Vulnerability_Index'],
    cmap='YlOrRd', alpha=0.85, edgecolors='black', linewidth=1.5
)

# Dynamically annotate the points with bold metal labels
for i, txt in enumerate(df['Material']):
    plt.annotate(txt, (df['Current_Recycling_Rate_EOL_RIR'].iloc[i] + 0.3, df['Geopolitical_Concentration_HHI'].iloc[i] - 100), 
                 fontsize=11, weight='bold')

# Formatting aesthetics
plt.colorbar(scatter, label='Unified Material Vulnerability Index (Risk Score)')
plt.title('Circularity Deficit Matrix: Supply Concentration vs. Recycling Recovery Rates', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('End-of-Life Recycling Input Rate (EOL-RIR %)', fontsize=11, fontweight='bold')
plt.ylabel('Geopolitical Sourcing Monopoly (HHI Index)', fontsize=11, fontweight='bold')
plt.xlim(-1, 17) # Give padding to read labels
plt.ylim(1000, 7500)

plt.tight_layout()
chart1_name = 'crm_circularity_matrix.png'
plt.savefig(chart1_name, dpi=300)
print(f"✓ Visual Dimension 1 Exported: Saved as '{chart1_name}'")
plt.show()

# =========================================================================
# GRAPH 2: STRATEGIC PRIORITIZATION & SUBSTITUTION URGENCY RANKING
# =========================================================================
plt.figure(figsize=(10, 5))

# Sort from highest risk index to lowest to establish priority ranking
df_sorted = df.sort_values('Unified_Vulnerability_Index', ascending=False)
sns.barplot(data=df_sorted, x='Material', y='Unified_Vulnerability_Index', palette='flare', edgecolor='black')

# Formatting aesthetics
plt.title('Prioritizing Metallurgy Alternatives: Unified Vulnerability Ranking of Critical Metals', fontsize=12, fontweight='bold', pad=15)
plt.ylabel('Unified Vulnerability Index Score (Max Risk)', fontsize=11, fontweight='bold')
plt.xlabel('Target Strategic Transition Mineral', fontsize=11, fontweight='bold')
plt.ylim(0, 10) # Risk index scaled out of 10 max

plt.tight_layout()
chart2_name = 'crm_vulnerability_ranking.png'
plt.savefig(chart2_name, dpi=300)
print(f"✓ Visual Dimension 2 Exported: Saved as '{chart2_name}'")
plt.show()

print("\n🚀 Complete multi-dimensional dashboard generated successfully!")
