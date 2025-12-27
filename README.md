# Actuarial Pricing and Reserving using GLM

## Overview
This repository presents an end-to-end actuarial pricing and reserving
framework for a general insurance portfolio using Generalized Linear Models (GLMs).

The project is designed to replicate industry-standard actuarial workflows,
covering experience analysis, pricing model development, reserving validation,
and regulatory documentation.
----
## ⚠️ IMPORTANT DISCLAIMER (PLEASE READ)

<div align="center">

<span style="font-size:26px; font-weight:bold; color:#D4AF37;">
THIS PROJECT IS FOR LEARNING & DEMONSTRATION PURPOSES ONLY
</span>

</div>

-----
---

### 📌 Data Source & Industry Relevance

The datasets used in this project were **synthetically generated using AI tools (Perplexity)** to simulate actuarial workflows in **Pricing and Reserving**.  
As a result:

- The data **does not represent real insurance portfolios**
- Claim development patterns **may not follow real-world industry behavior**
- Certain outputs (e.g., **negative IBNR or unusually high IBNR percentages**) are **expected artifacts of synthetic data**

---

### 📌 Purpose of This Project

This project was built to **demonstrate actuarial concepts and technical implementation**, including:

- 🔹 General Insurance **Pricing using GLM**
- 🔹 **Chain Ladder Reserving methodology**
- 🔹 Separation of **Pricing vs Reserving logic**
- 🔹 End-to-end actuarial workflow using **Python, Pandas, NumPy & Visualization**
- 🔹 Industry-standard documentation & GitHub structuring

⚠️ **The numerical results are not intended for business, regulatory, or reserving decisions.**

---

### 📌 Why Results May Look Unexpected

Some outcomes may appear unrealistic, such as:
- Negative IBNR in older accident years
- Extremely high IBNR percentages
- Inconsistent paid vs incurred development

These arise because:
- Synthetic data lacks **true claim settlement behavior**
- No expert judgment or manual reserving adjustments were applied
- No credibility weighting or tail factor calibration was performed
- The model strictly follows **deterministic actuarial formulas**

---

### 📌 Key Learning Takeaway

> **This repository focuses on *how actuarial models are built*, not on producing production-grade actuarial estimates.**

In real industry practice:
- Data undergoes extensive validation
- Actuarial judgment is applied
- Results are reviewed through multiple governance layers

---

### ✅ Reviewer Note

If real industry data were used, **the same framework and code structure would produce materially different and more stable results**.

This project should be evaluated based on:
- Methodological correctness
- Separation of pricing vs reserving logic
- Code quality & documentation
- Actuarial understanding demonstrated

---

<span style="color:#D4AF37; font-weight:bold;">
Actuarial modeling is as much about judgment as mathematics — this project emphasizes the foundation.
</span>
## Dataset Brief

### Three interlinked CSVs for end-to-end actuarial modeling:

policy_data.csv (500,000 rows): Policies with exposure, vehicle_age, region, channel, sum_insured, premium (1.5% data quality errors included for realism).

claims_data.csv (44,587 claims): Ultimate claim amounts, accident/development years, status (Open/Closed).

payment_data.csv (155,694 payments): Incremental payments + case reserves per claim.

Purpose: Train frequency/severity GLMs, compute pure premiums, loss ratios, reserving triangles. Synthetic scales are plausible (adjustable base_rate for India motor benchmarks).

-----

## Business Objective
To develop a transparent, regulator-friendly pricing model that:
- Estimates risk-based pure premiums
- Produces multiplicative rating factors
- Validates pricing assumptions using reserving outputs



## Methodology

### 1. Data Preparation
- Policy exposure aggregation
- Claims consolidation
- Feature engineering and risk banding

### 2. Experience Analysis
- Claim frequency and severity analysis
- Loss ratio diagnostics
- Stability checks across risk segments

### 3. Frequency Modeling
- Poisson GLM with log link
- Exposure used as offset
- Model diagnostics and goodness-of-fit checks

### 4. Severity Modeling
- Gamma GLM with log link
- Treatment of skewness and large losses

### 5. Pricing Framework
- Conversion of GLM coefficients into multiplicative relativities
- Base rate derivation
- Pure premium calculation (Frequency × Severity)
- Construction of rating structure

### 6. Reserving Validation
- Loss development triangles
- Chain Ladder reserve estimates
- Comparison of ultimate losses with priced expectations

### 7. Governance and Documentation
- Model assumptions and limitations
- Regulatory justification of GLM usage
- Reproducibility and audit readiness

---

## Tools and Technologies
- Python
- pandas, numpy
- statsmodels
- matplotlib
- chainladder

---

## Key Actuarial Concepts Demonstrated
- GLM-based pricing
- Frequency–severity modeling
- Exposure-based offsets
- Multiplicative rating factors
- Pricing and reserving consistency
- Actuarial governance

---

## Disclaimer
This project is a portfolio-based actuarial model developed for learning and
demonstration purposes. It does not represent the pricing strategy of any insurer.

---

## Author
Vaishnav
