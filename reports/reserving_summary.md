# Reserving Summary – Chain Ladder Method (Critical Review)

## Objective
The objective of this analysis is to estimate ultimate claims and Incurred But Not Reported (IBNR) reserves for a General Insurance portfolio using the Chain Ladder (CL) method, based on historical claims development patterns.

---

## Data Overview
The reserving analysis is based on aggregated claims data structured by:

- Accident Year  
- Development Period (starting from 0)  
- Cumulative Incurred Losses, defined as:

Incurred Loss = Paid Loss + Case Reserves

The dataset spans Accident Years 2018 to 2025, covering both mature and immature underwriting years.

---

## Methodology

### Triangle Construction
- Incremental incurred losses were aggregated by Accident Year and Development Period
- Incremental values were converted into cumulative incurred loss triangles
- Basic data consistency checks were performed to ensure monotonic cumulative development

### Development Factor Selection
- Age-to-age development factors were calculated from the cumulative incurred triangle
- Factors were selected using volume-weighted averages
- Cumulative Development Factors (CDFs) were derived to project losses to ultimate

### Ultimate Loss Estimation
Ultimate losses were estimated using the standard Chain Ladder approach:

Ultimate Loss = Latest Observed Cumulative Loss × Corresponding CDF

### IBNR Calculation
IBNR was calculated as:

IBNR = Ultimate Loss − Latest Reported Loss

IBNR percentages were calculated relative to ultimate losses.

---

## Key Results

| Accident Year | Ultimate Loss | Latest Reported |       IBNR     |   IBNR % |
|---------------|---------------|-----------------|----------------|----------|
         | 2018 | 375,329,250   | 860,531,226     | -485,201,976   | -129.27% |
         | 2019 | 746,961,674   | 1,765,113,205   | -1,018,151,531 | -136.31% |
         | 2020 | 725,130,584   | 1,802,469,362   | -1,077,338,778 | -148.57% |
         | 2021 | 662,158,829   | 1,774,342,399   | -1,112,183,570 | -167.96% |
         | 2022 | 629,954,057   | 1,882,789,209   | -1,252,835,152 | -198.88% |
         | 2023 | 598,477,826   | 1,919,790,216   | -1,321,312,390 | -220.78% |
         | 2024 | 546,782,955   | 2,014,133,129   | -1,467,350,174 | -268.36% |
         | 2025 | 241,460,993   | 991,709,710     | -750,248,717   | -310.71% |

---

## Interpretation of Results
The Chain Ladder results indicate consistently negative IBNR across all accident years, with magnitudes increasing for more recent years. This implies that latest reported losses significantly exceed model-estimated ultimate losses, indicating systematic over-reserving according to the Chain Ladder model.

From an actuarial perspective, these results are not consistent with expected reserving behavior:

- Negative IBNR exceeding 100% of ultimate losses is not economically plausible
- The pattern persists across both mature and immature accident years
- Recent accident years show extreme negative IBNR despite incomplete development

---

## Root Cause Assessment
The results suggest that key Chain Ladder assumptions are violated for this dataset. Potential contributing factors include:

1. Inflated Case Reserves  
   Case reserves appear disproportionately high relative to historical paid development, leading to reported losses far exceeding Chain Ladder ultimates.

2. Inappropriateness of Chain Ladder for This Portfolio  
   The method assumes stable historical development patterns, which may not be representative of the observed claims experience.

3. Immaturity of Recent Accident Years  
   Limited development for recent years results in unreliable extrapolation and understated ultimate loss estimates.

4. Methodological Limitations  
   - No tail factor applied beyond observed development
   - Deterministic Chain Ladder used without variability estimation
   - No segmentation by line of business, claim size, or exposure characteristics

---

## Actuarial Conclusion
Based on the analysis, the Chain Ladder results are not appropriate for reserve estimation for this dataset without significant adjustment.

The magnitude and consistency of negative IBNR indicate that the model outputs are not reliable and should not be used for financial reporting or regulatory purposes in their current form.

---

## Recommended Next Steps
To improve reserving accuracy and actuarial credibility, the following actions are recommended:

- Apply Incurred Chain Ladder with credibility weighting
- Perform Paid versus Incurred development diagnostics
- Use Bornhuetter–Ferguson or Expected Loss Ratio methods for recent accident years
- Conduct case reserve runoff analysis
- Apply actuarial judgment in tail selection and reserve floors

---

## Limitations
- Deterministic Chain Ladder only (no variance estimation)
- No tail factor beyond observed development
- No segmentation by claim characteristics
- AI-simulated data used for educational and portfolio demonstration purposes

---

## Professional Statement
The results presented in this analysis are for educational and portfolio demonstration purposes only and should not be interpreted as actual reserve estimates for any real insurance portfolio.
