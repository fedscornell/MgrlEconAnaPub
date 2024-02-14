# This is for class demonstration

import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

WorkingDir = r"D:\Dropbox\UW\Teaching\AAE625\AAE625_2024\Slides\Demand"
df = pd.read_excel(WorkingDir + '/MarketDemand.xlsx',sheet_name='Correct')

plt.plot(df.Q_Tot, df.P)
plt.xlabel('Q')
plt.ylabel('P')
plt.title('Market Demand')
plt.show()

from datetime import datetime
def convert_date(date_string):
    # Replace the non-standard hyphen with a standard one
    date_string = date_string.replace('–', '-')
    parsed_date = datetime.strptime(date_string, '%b-%Y')
    formatted_date = parsed_date.strftime('%Y-%m')
    return formatted_date

WorkingDir = r"D:\Dropbox\UW\Teaching\AAE625\AAE625_2024\AAE625Git\PublicRep\MgrlEconAnaPub\Demand"
df = pd.read_excel(WorkingDir + '/IronOre/IronOre.xlsx',sheet_name='Price')
df['Date'] = df['Date'].apply(lambda x: convert_date(x))
df['Earning'] = df['Price'] * df['ExpCHN'] 

plt.scatter(df.Date, df.Earning)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


fig, axs = plt.subplots(1,2)


import statsmodels.api as sm
from statsmodels.formula.api import ols
md_1 = ols('Price ~ExpCHN', data=df).fit()
print(md_1.summary())


# Demand curve: 
df = pd.read_excel(WorkingDir + '/DemandCurve.xlsx')
df = pd.read_excel(WorkingDir + '/DemandCurve/MarketDemand.xlsx',sheet_name='Correct')

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


df['Q_Tot']=df['Q1']+df['Q2']+df['Q3']

df_melted = pd.melt(df, id_vars=['P'], value_vars=['Q1', 'Q2', 'Q3'], var_name='ID', value_name='Q')
cols = ['ID'] + [col for col in df_melted.columns if col != 'ID']
df_melted = df_melted[cols]
df_melted['ID'] = df_melted['ID'].str.replace('Q','ID_')

# group
df_melted_ag =  df_melted.groupby('P')['Q'].sum().reset_index()

# milk:
df_m = pd.read_excel(WorkingDir +'/Milk/dyfluid.xlsx',sheet_name='Proc')
plt.plot(df_m.Year, df_m.WholeMilk)
plt.xlabel('Year')
plt.ylabel('Consumption (PerCap)')
plt.savefig(WorkingDir+'/fig.png')
plt.show()

plt.plot(df_m.Year, df_m.TotFMilk)
plt.xlabel('Year')
plt.ylabel('Consumption (PerCap)')
plt.savefig(WorkingDir+'/figTotF.png')
plt.show()
