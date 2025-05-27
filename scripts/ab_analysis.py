import numpy as np
import pandas as pd
from scipy.stats import norm

from ab_generate_data import df_ab_test, n_exp, n_con

x_con = df_ab_test.groupby("group")["click"].sum().loc["con"]
x_exp = df_ab_test.groupby("group")["click"].sum().loc["exp"]
print("Number of clicks in Control: ", x_con)
print("Number of clicks in Control: ", x_exp)

p_con_hat = x_con/n_con
p_exp_hat = x_exp/n_exp

print("Click probability in control group: ", p_con_hat)
print("Click probability in experimental group: ", p_exp_hat)

p_pooled_hat = (x_con + x_exp) / (n_con + n_exp)

pooled_variance = p_pooled_hat * (1-p_pooled_hat) * (1/n_con + 1/n_exp)

print("p_^pooled ids: ", p_pooled_hat)
print("Pooled variance is: ", pooled_variance)

se = np.sqrt(pooled_variance)
print("Standard error is: ", se)

test_stat = (p_con_hat - p_exp_hat) / se
print("Test statistics for 2-sample Z-test is: ", test_stat)

alpha = 0.05 # We assume this was done before the test and that we agree significance level is 5%
print ("Alpha: significance level is: ", alpha)

z_crit = norm.ppf(1-alpha/2)
print ("Z-critical value from standard normal distribution: ", z_crit)

p_value = 2 * norm.sf(abs(test_stat))
print ("P-value of 2-sample Z-test is: ", round(p_value, 3))

# Since p_value = 0 and is lesss than alpha, we can state that null hypothesis can be rejected 
# And there is statistical diff b/w control version and experiment version of product

ci = [round((p_exp_hat - p_con_hat) - se * z_crit, 3), round((p_exp_hat - p_con_hat) + se * z_crit, 3)]
print ("Confiednce interval of the 2-sample Z-test is: ", ci)

df_ab_test.to_csv("ab_test_data.csv", index=False)
