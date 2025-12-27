# Actuarial Model Note
## General Insurance Pricing and Reserving Project

### 1. Objective
The objective of this project is to develop an end-to-end actuarial framework for:
- General Insurance pricing using GLM-based frequency and severity models
- Loss reserving using the Chain Ladder methodology

The project demonstrates industry-standard actuarial practices using policy, claims, and payment data.

---

### 2. Data Overview

#### 2.1 Policy Data
Key fields:
- policy_id
- policy_start_date
- policy_end_date
- vehicle_age
- region
- channel
- sum_insured
- premium

#### 2.2 Claims Data
Key fields:
- policy_id
- claim_id
- accident_date
- accident_year
- development_year
- claim_amount
- claim_status

#### 2.3 Payment Data
Key fields:
- claim_id
- payment_date
- paid_amount
- case_reserve

---

### 3. Exposure Calculation
Exposure represents the proportion of time a policy is at risk during the observation period.

- Exposure is calculated as:
  
  Exposure = (Policy active days within observation window) / 365

- Exposure is capped at 1.0 in line with industry practice.
- Policies with zero exposure are excluded from pricing models.

---

### 4. Pricing Methodology

#### 4.1 Frequency Model
- Model: Poisson GLM
- Offset: log(exposure)
- Target: claim count per policy
- Purpose: Estimate expected claim frequency

#### 4.2 Severity Model
- Model: Gamma GLM with log link
- Target: claim amount (positive claims only)
- Purpose: Estimate expected claim severity

#### 4.3 Pure Premium
Pure Premium is calculated as:

Pure Premium = Predicted Frequency × Predicted Severity

---

### 5. Reserving Methodology

#### 5.1 Reserving Basis
- Method: Chain Ladder
- Triangle type: Incurred losses
- Development year starts from 0 (accident year)

#### 5.2 Outputs
- Reported claims
- Ultimate claims
- Incurred But Not Reported (IBNR)

IBNR = Ultimate − Reported

---

### 6. Assumptions & Limitations
- Historical loss development patterns are assumed to be stable
- No tail factor applied beyond observed development
- Inflation and discounting are not explicitly modeled
- Synthetic or anonymized data used for demonstration

---

### 7. Conclusion
The project successfully demonstrates an actuarially sound pricing and reserving workflow using reproducible Python-based models aligned with industry standards.
