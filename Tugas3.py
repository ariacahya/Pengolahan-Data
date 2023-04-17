import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [6.50,3.00]
plt.rcParams["figure.autolayout"] = True

df = pd.read_csv("company_sales_data.csv")
print(df["total_profit"].tolist())

df.set_index("total_profit").plot ()
plt.show ()