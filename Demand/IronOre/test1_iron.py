import pandas as pd
import matplotlib.pyplot as plt
WorkingDir = r"D:\Dropbox\UW\Teaching\AAE625\AAE625_2024\Slides\Demand"

df = pd.read_excel(WorkingDir + '/MarketDemand.xlsx',sheet_name='Correct')

plt.plot(df.Q1, df.P)
plt.xlabel('Q1')
plt.ylabel('P')
plt.show()

fig, axs = plt.subplots(2,2)
axs.set_xlabel('Q')  # Set x-axis label for each subplot
axs.set_ylabel('P')
axs[0,0].plot(df.Q1, df.P)
axs[0,0].set_title('Q1')
axs[0, 0].set_xlabel('Q1')
axs[0, 0].set_ylabel('P')
axs[0,1].plot(df.Q2, df.P)
axs[0,1].set_title('Q2')
axs[0, 1].set_xlabel('Q2')
axs[0, 1].set_ylabel('P')
axs[1,0].plot(df.Q3, df.P)
axs[1,0].set_title('Q3')
axs[1, 0].set_xlabel('Q3')
axs[1, 0].set_ylabel('P')
axs[1,1].plot(df.Q_Tot, df.P)
axs[1,1].set_title('Market Demand')
axs[1, 1].set_xlabel('Q')
axs[1, 1].set_ylabel('P')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()

# ----------together:------
data = [(df.Q1, df.P), (df.Q2, df.P), (df.Q3, df.P), (df.Q_Tot, df.P)]

# Loop through data to create each subplot
for ax, (y, title) in zip(axs.flat, data):
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel('Q')  # Set x-axis label for each subplot
    ax.set_ylabel('P')  # Set y-axis label for each subplot

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()


df_w = pd.read_excel(WorkingDir + '/MarketDemand.xlsx',sheet_name='Wrong')
df = df_w
plt.plot(df.Q1, df.P)
plt.xlabel('Q1')
plt.ylabel('P')
plt.show()

df_melted = pd.melt(df, id_vars=['P'], value_vars=['Q1', 'Q2', 'Q3'], var_name='ID', value_name='Q')
cols = ['ID'] + [col for col in df_melted.columns if col != 'ID']
df_melted = df_melted[cols]
df_melted['ID'] = df_melted['ID'].str.replace('Q','ID_')
df_melted_ag =  df_melted.groupby('P')['Q'].sum().reset_index()
plt.plot(df_melted_ag.Q, df_melted_ag.P)
plt.show()

# model
import statsmodels.api as sm
from statsmodels.formula.api import ols
md_1 = ols('Q ~ P', data=df_melted_ag).fit()
print(md_1.summary())

# milk
# data: https://www.ers.usda.gov/data-products/food-availability-per-capita-data-system/

df_m = pd.read_excel(WorkingDir +'/Data/dyfluid.xlsx',sheet_name='Proc')
plt.plot(df_m.Year, df_m.WholeMilk)
plt.xlabel('Year')
plt.ylabel('Consumption (PerCap)')
plt.savefig(WorkingDir+'/fig.png')
plt.show()

