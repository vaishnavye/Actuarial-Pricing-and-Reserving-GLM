# Pricing Summary – General Insurance

### Objective
To estimate risk-based premium rates using historical policy and claims experience.

---

### Methodology

#### Exposure
- Exposure calculated based on policy coverage period
- Exposure capped at 1.0
- Used as offset in frequency modeling

#### Claim Frequency
- Poisson GLM used to model claim counts
- Risk factors include vehicle age, region, channel, and sum insured
- Exposure included as a log offset

#### Claim Severity
- Gamma GLM with log link used
- Model fitted on positive claim amounts only

---

### Premium Calculation

Pure Premium is calculated as:

Pure Premium = Frequency × Severity

Final premium indication can be obtained by loading for:
- Expenses
- Profit margin
- Risk margin (if applicable)

---

### Key Outputs
- Predicted frequency per policy
- Predicted severity per claim
- Pure premium
- Indicated risk premium

---

### Business Use
The pricing output supports:
- Risk-based pricing
- Portfolio segmentation
- Underwriting decisions
- Rate reviews and benchmarking
