# Actuarial-Pricing-Model---GI-Pricing
# Actuarial Pricing Model – General Insurance

## 📌 Project Overview
This project demonstrates an end-to-end actuarial pricing framework for a General Insurance portfolio 
using a frequency–severity approach. The model estimates pure premium, quantifies loss volatility, 
and derives a capital-aware technical premium.

---

## 🎯 Objectives
- Estimate expected losses using frequency–severity modeling
- Capture portfolio risk via aggregate loss simulation
- Derive risk-adjusted technical premium
- Demonstrate real-world actuarial pricing workflow

---

## 📂 Data Description
### Policy Data
- Policy ID
- Policy Start & End Date
- Sum Insured
- Written Premium

### Claims Data
- Accident Date
- Paid Amount
- Claim Status

---

## 🧹 Data Preparation
- Earned exposure calculation
- Data cleansing and validation
- Large loss identification
- Inflation-adjusted claims (optional)

---

## 📊 Methodology

### 1️⃣ Frequency Modeling
- Poisson distribution
- Exposure-normalized claim counts
- Estimation of expected claim frequency

### 2️⃣ Severity Modeling
- Lognormal distribution
- Tail-focused modeling
- Goodness-of-fit validation

### 3️⃣ Pure Premium
Pure Premium = Expected Frequency × Expected Severity

---

## 📈 Aggregate Loss Modeling
- Monte Carlo simulation
- Compound loss distribution
- Risk metrics:
  - Mean Loss
  - Value at Risk (VaR)
  - Tail Value at Risk (TVaR)

---

## 💰 Pricing Framework
Technical Premium includes:
- Expected Loss
- Risk Margin (VaR-based)
- Expense Loading
- Target Profit Margin

---

## 📊 Validation
- Actual vs Expected analysis
- Sensitivity testing
- Assumption documentation

---

## 📦 Deliverables
- Python pricing model
- Rate indication outputs
- Risk metrics dashboard (Power BI)
- Actuarial pricing report

---

## 🛠️ Tech Stack
- Python (pandas, numpy, scipy)
- Excel (reconciliation)
- Power BI (visualization)

---

## ⚠️ Disclaimer
This project is for academic and demonstrative purposes only and does not represent production pricing.
