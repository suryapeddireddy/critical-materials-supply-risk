# Industrial Vulnerability Framework: CRM Supply Security & Substitution Urgency

## 🎯 Project Overview & Problem Statement
The transition to clean energy technologies (electric vehicles, wind turbines, and grid storage) requires unprecedented inputs of Critical Raw Materials (CRMs). However, these materials are exposed to severe geopolitical and industrial supply chain vulnerabilities. 

This project builds a multi-dimensional risk matrix tracking 5 essential transition metals: **Lithium, Cobalt, Nickel, Neodymium, and Graphite**. By programmatically synthesizing Geopolitical Concentration (via the Herfindahl-Hirschman Index - HHI), Economic Vulnerability, and End-of-Life Recycling Input Rates (EOL-RIR), this engine formulates a **Unified Vulnerability Index**. This framework allows systems engineers to prioritize which minerals present the most urgent supply chain risk and require targeted metallurgical substitution research under the European Green Deal frameworks.

---

## 📊 Core Analytical Insights

### 1. The Critical Raw Materials Risk Matrix
The computational engine evaluated the raw metrics to isolate the specific risk vectors across key green energy transition metals:

| Material | Primary Source Country | Geopolitical HHI Index | Economic Vulnerability (1-10) | EU Import Dependency % | Recycling Input Rate (EOL-RIR) | Unified Vulnerability Index |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Neodymium** | China | **6500** | 9.2 | 100.0% | **0.5%** | **8.25 (Critical)** |
| **Graphite** | China | 4800 | 7.5 | 95.0% | 2.0% | **6.72 (High)** |
| **Lithium** | Australia | 2800 | 8.5 | 98.0% | 1.2% | **6.42 (High)** |
| **Cobalt** | DR Congo | 4100 | 7.8 | 85.0% | 9.5% | **5.98 (Medium)** |
| **Nickel** | Indonesia | 1900 | 6.2 | 65.0% | 14.0% | **3.84 (Low)** |

### 2. Multi-Dimensional Visualizations

#### A. The Circularity Deficit Matrix (`crm_circularity_matrix.png`)
This multi-variable scatter plot maps Geopolitical Concentration (\(Y\)-axis) against actual Recycling Rates (\(X\)-axis). The individual bubble scale reflects absolute **EU Import Dependence**, while the color gradient marks the **Unified Vulnerability Index**. 
* **Key Finding:** **Neodymium** stands out in the dangerous upper-left quadrant, signaling a critical monopoly combined with a complete lack of secondary circular loops.

#### B. Substitution Priority Ranking (`crm_vulnerability_ranking.png`)
This ranked distribution index cleanly sorts the strategic metals by their mathematical vulnerability scores, giving researchers a direct roadmap for where metallurgical recycling and structural material substitution are most urgently required.

---

## ⚙️ Tech Stack & Methodology
* **Language:** Python 3.11
* **Data Processing:** `pandas`, `numpy` (Relational matrix grouping, multi-variable index formulations)
* **Data Presentation:** `matplotlib`, `seaborn` (Multi-variable bubble charting, sorted categorical distributions)
* **Environment:** VS Code Terminal Ecosystem

---

## 🚀 How to Run the Engine
1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Execute the visualization engine to regenerate the analytical charts:
   ```bash
   python plot_risk_dashboard.py
   ```
