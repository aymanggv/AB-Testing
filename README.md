# A/B Test Analysis: Click-Through Rate on CTA Button

This repository contains a case study on an A/B test designed to measure the impact of a change on user click behavior. The A/B test involves a control group and an experimental group, with the primary metric being the click-through rate (CTR).

---

## 📁 Files Overview

- **`ab_generate_data.py`**: Script to simulate A/B testing data.
- **`ab_analysis_case_study.ipynb`**: Jupyter Notebook containing the analysis of the A/B test.
- **`ab_analysis.py`**: A Python file to initially practice A/B tetsing before moving on to the case study.  

---

## 📊 Objective

To determine whether a new version of a CTA (Call-To-Action) button increases click-through rate compared to the existing version, using both statistical and practical significance.

---

## 🧪 Data Generation (`ab_generate_data.py`)

- **Control Group (`con`)**: 10,000 users, click probability = 0.2
- **Experimental Group (`exp`)**: 10,000 users, click probability = 0.6
- **Total Users**: 20,000
- **Click Data**: Simulated using a binomial distribution
- **Additional Columns**:
  - `user_id`: Unique identifier for each user
  - `timestamp`: Simulated using 1-minute intervals

The data is saved to a CSV file: `ab_test_data.csv`

---

## 📈 Analysis Steps (`ab_analysis_case_study.ipynb`)

### 1. 📋 Summary Statistics & Visualization

- Grouped click data plotted using `seaborn` with yellow (no-click) and black (click) bars
- Percentage of clicks annotated for each group

### 2. 🧮 Statistical Testing

- **Test Type**: Two-sample Z-test for proportions
- **Hypotheses**:
  - Null: No difference in click rates between groups
  - Alternative: Significant difference in click rates

#### Calculated Metrics:
- Click Probability (CTR):
  - Control group: `p_con_hat`
  - Experimental group: `p_exp_hat`
- Pooled Probability: `p_pooled_hat`
- Standard Error: `se`
- Z-test Statistic: `test_stat`
- p-value: `p_value`
- Significance Level (α): 0.05

#### Results:
- ✅ **Statistical Significance** was found  
  (p-value < 0.05 and test statistic exceeds critical Z-value)

### 3. 🧠 Practical Significance

- **Minimum Detectable Effect (MDE)**: 10%
- **95% Confidence Interval** for difference in CTR:
  - Calculated as `(p_exp_hat - p_con_hat) ± Z * SE`
  - Example output: CI = (0.04, 0.06)

#### Decision:
- ✅ **Practical Significance Achieved**  
  (Lower bound of CI > MDE)

---

## 📌 Conclusions

- The new CTA button significantly increased the click-through rate.
- Both **statistical** and **practical** significance were achieved.
- The results are **unlikely due to chance**, and the **effect size is meaningful** for business impact.

---

## 📚 Tools & Libraries

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scipy.stats.norm`

---

## 💡 Notes

- Data simulation assumes no bias or systematic error in group assignment or data collection.
- Analysis is based on the central limit theorem and large sample approximation.
