import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import seaborn as sns
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly as plotly
from botocore.client import Config
import ibm_boto3

WorkingDir = r'D:\Dropbox\UW\Teaching\AAE625\AAE625_2024\AAE625Git\PublicRep\MgrlEconAnaPub\Demand'
# Import data
# df = pd.read_excel(WorkingDir + '/DemandCurve/MarketDemand.xlsx',sheet_name='Correct')
df = pd.read_csv(WorkingDir + '/DemandCurve/MarketDemand.csv',sep = '|')
df = df.rename(columns={'Q_Tot':'Q'})
model_linear = ols('Q ~ P', data=df).fit()
print(model_linear.summary())
plt.scatter(df.Q, df.P)
plt.title('My First Python Plot - Demand Curve')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='P', y='Q', data=df, color='blue', label='Observations')
sns.lineplot(x='P', y=md_Tot.predict(df), data=df, color='red', label='Fitted Line')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.title('Fitted Line and Observations')
plt.legend()
plt.show()

#  95% confidence interval shaded around the regression line
sns.regplot(x='P', y='Q', data=df, color='blue', label='Observations')
plt.xlabel('P')
plt.ylabel('Q')
plt.title('Original Data with Fitted Regression Line')
plt.legend()
plt.grid(True)
plt.show()
# constant elasticity: 
df['lgP'] = np.log(df['P'])
df['lgQ'] = np.log(df['Q'])
model_log = ols('lgQ ~ lgP', data=df).fit()
print(model_log.summary())

# ------------Point estimation-------------
df = df[['P','Q']]
# pct:
df['P_pct'] = df['P'].pct_change()
df['Q_pct'] = df['Q'].pct_change()
df['Point_Elas'] = df['Q_pct']/df['P_pct']
x1 = df['P']
y1 = df['Q']
z1 = df['Point_Elas']


trace1 = go.Scatter(
    x=x1,
    y=y1,
    name='Demand Curve'
)
trace2 = go.Scatter(
    x=x1,
    y=z1,
    name='Elasticity',
    yaxis='y2'
)
data = [trace1, trace2]
layout = go.Layout(
    title='Price Elasticity of Demand and the Demand Schedule',
    yaxis=dict(
        title='Quantity'
    ),
    yaxis2=dict(
        title='Price Elasticity of Demand',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    ),
        xaxis=dict(
        title='Price',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
))
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig, filename='shapes-lines')

df['Rev'] = df['P'] * df['Q']
z1=df['Rev']
# revenue 
trace1 = go.Scatter(
    x=x1,
    y=y1,
    name='Demand Curve'
)
trace2 = go.Scatter(
    x=x1,
    y=z1,
    name='Revenue',
    yaxis='y2'
)
data = [trace1, trace2]
layout = go.Layout(
    title='Revenue, Quantity and Price',
    yaxis=dict(
        title='Quantity'
    ),
    yaxis2=dict(
        title='Revenue',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    ),
        xaxis=dict(
        title='Price',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
))
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig, filename='shapes-lines')