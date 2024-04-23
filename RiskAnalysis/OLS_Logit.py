# This script is developed for AAE 625.
#  Copyright: Jing Yi; jing.yi@wisc.edu

import pandas as pd
import statsmodels.api as sm
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('TkAgg')
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import scipy
from sklearn.metrics import accuracy_score
import numpy as np
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_row', 20)



Dir = r"D:\Dropbox\UW\Teaching\AAE625\AAE625_2024\AAE625Git\PublicRep\MgrlEconAnaPub\RiskAnalysis"
DataDir = r"D:\Dropbox\UW\Teaching\AAE625\AAE625_2024\AAE625Slides"

df = pd.read_excel(DataDir+'/W14_RiskAssessment.xlsx',sheet_name='DataOri')
sns.countplot(x='Default',data=df)
plt.show()
df['Default'].mean()
df.describe()
df.groupby('Default').mean()


Y = df['Default']
X = df[["WC/TA", "RE/TA","EBIT/TA","ME/TL","S/TA"]]
X = sm.add_constant(X)

model_ols = sm.OLS(Y,X,missing='drop')
model_ols = model_ols.fit()
model_ols.summary()

sm.graphics.plot_fit(model_ols,1, vlines=False)
plt.show()

# Logistic regression:
X = df[["WC/TA", "RE/TA","EBIT/TA","ME/TL","S/TA"]]
X = sm.add_constant(X)
model_logit_spe = sm.Logit(Y,X)
model_logit = model_logit_spe.fit()
model_logit.summary()
coefficients = pd.DataFrame(model_logit.params, columns=['coef'])

df_1 = df.copy()
df_1['Odds'] = coefficients.iloc[0, 0] +coefficients.iloc[1, 0]*df_1['WC/TA'] + coefficients.iloc[2, 0]* df_1['RE/TA'] + coefficients.iloc[3, 0]*df_1['EBIT/TA'] + coefficients.iloc[4, 0]*df_1['ME/TL']+coefficients.iloc[5, 0]*df_1['S/TA']
df_1['PD'] = 1/(1+ np.exp(-df_1['Odds']))

yhat = model_logit.predict(X)

# ==================model 2: ====================
Y = df['Default']
X = df[["RE/TA","EBIT/TA","ME/TL"]]
X = sm.add_constant(X)
model_logit_spe2 = sm.Logit(Y,X)
model_logit2 = model_logit_spe2.fit()
model_logit2.summary()
coefficients2 = pd.DataFrame(model_logit2.params, columns=['coef'])
model_logit2.llf
model_logit.llf

LR_statistic = -2*(model_logit2.llf-model_logit.llf)
p_val = scipy.stats.chi2.sf(LR_statistic, 2)

y_pred = model_logit2.predict(X)
