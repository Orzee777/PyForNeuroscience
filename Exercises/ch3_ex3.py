# Bradley Orzolek
# Chapter 3: Packages for Data Manipulation
# Exercise 3
# 5/17/2021

import pandas as pd

dementia_df = pd.read_csv("exercises/data/oasis_cross-sectional.csv")

avg_ses1 = demtentia_df[dementia_df['CDR'] == 0.0]['SES'].mean()
avg_ses2 = demtentia_df.loc[dementia_df['CDR'] == 0.0]['SES'].mean()

print(avg_ses1 == avg_ses2)
print(round(avg_ses1, 1))
