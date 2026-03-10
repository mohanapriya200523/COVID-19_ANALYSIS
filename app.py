import pandas as pd

# Load data
df = pd.read_csv("covid19.csv")

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

# Fill missing values
df.fillna(0, inplace=True)

# Create Active cases if not present
df['Active'] = df['Confirmed'] - df['Recovered'] - df['Deaths']

print(df.head())


country_cases = df.groupby('Country')[['Confirmed','Deaths','Recovered','Active']].sum()
print(country_cases.sort_values(by='Confirmed', ascending=False).head())


top10 = country_cases.sort_values(by='Confirmed', ascending=False).head(10)
print(top10)

import matplotlib.pyplot as plt

top10['Confirmed'].plot(kind='bar', figsize=(10,5))
plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.show()
