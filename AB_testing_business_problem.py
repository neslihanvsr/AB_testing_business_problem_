# AB-Testing: Business Problem

# AB Testing

# summary

#1. Set up Hypothesis
#2. Assumption Check
# - 1. Normality Assumption
# - 2. Variance Homogeneity
# 3. Implementation of the Hypothesis
# - 1. If assumptions are provided, t-test from two independent samples (parametric test)
# - 2. Mannwhitneyu test if absence of assumptions (non-parametric test)
# 4. Interpret results based on p-value
# Note:
# - Direct number 2 if the assumption of normality is not met. If variance homogeneity is not provided, argument number 1 is entered.
# - It may be helpful to examine and correct for outliers before examining normality.

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# There is an online course.
# Are the scores of those who watched the majority of a course different from those who did not?

# H0: M1 = M2 (.....there is no statistically significant difference between the means of the two groups.)
# H1: M1 != M2 (.....there is statistically significant difference between the means of the two groups.)

df = pd.read_csv(r'C:\Users\course_reviews.csv')
df.head()

df[(df['Progress'] > 75)]['Rating'].mean()
df[(df['Progress'] < 25)]['Rating'].mean()

test_stat, pvalue = shapiro(df[(df['Progress'] > 75)]['Rating'])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df[(df['Progress'] < 25)]['Rating'])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value<0.05; H0: M1 = M2 absence of normality assumption, reject the null hypothesis.

test_stat, pvalue = mannwhitneyu(df[(df['Progress'] > 75)]['Rating'],
                                 df[(df['Progress'] < 25)]['Rating'])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


# If we look at the final results; p-value<0.05 and that is why we should reject the null hypothesis; (H0: M1 = M2)
# Except the hypothesis; H1: M1 != M2 (.....there is statistically significant difference between the means of the two groups.)


