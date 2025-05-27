import numpy as np
import pandas as pd

# At the end we'll assume that the data is how the engineers collect the data from the customers
# We'll also assume that ppl who were in control group only saw control version and ppl in experimental group only saw experimental version of the product
# We'll also assume there was no sytematic error when collecting the data from both groups of product


n_exp = 10000
n_con = 10000
total_rows = n_exp + n_con

# Generate click data
click_exp = pd.Series(np.random.binomial(1, 0.6, size= n_exp)) # Probability of success is 0.4 to have a diff between 2 groups
click_con = pd.Series(np.random.binomial(1, 0.2, size= n_con)) # Probability of success is 0.2 to have a diff between 2 groups

# Generate group identifier
exp_id =  pd.Series(np.repeat("exp", n_exp))
con_id =  pd.Series(np.repeat("con", n_con))

df_exp = pd.concat([click_exp, exp_id], axis= 1)
df_con = pd.concat([click_con, con_id], axis= 1)

df_exp.columns = ["click", "group"]
df_con.columns = ["click", "group"]

# print(df_exp)
# print(df_con)

df_ab_test = pd.concat([df_exp, df_con], axis= 0).reset_index(drop=True)

# Add timestamp column (1-minute intervals)
start_time = pd.Timestamp("2025-01-01 00:00:00")
df_ab_test["timestamp"] = pd.date_range(start=start_time, periods=total_rows, freq="T")

# Add user_id column
df_ab_test["user_id"] = range(1, total_rows + 1)
df_ab_test = df_ab_test[["user_id", "group", "click", "timestamp"]]

df_ab_test.to_csv("C:/Users/ayman/OneDrive/Documents/Code/AB Test/ab_test_data.csv", index=False)

print(df_ab_test)
