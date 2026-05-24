#takes user created fn from helper file

import pandas as pd
from helper import cal_total,format_amt
df=pd.read_csv('D:\Projects ai\sales\Sales_Analysis\data\sales.csv')

#tot for each row
tot=[]
for idx,row in df.iterrows():
  tota=cal_total(row['Quantity'],row['Price'])
  tot.append(tota)

#add extra col of tot
df['Totals']=tot

#disp formatted totals
for idx,row in df.iterrows():
  form_tot=format_amt(row['Totals'])
  print(f"{row['Item']}:{form_tot}")

#to show grand total
grand_tot=df['Totals'].sum()
form_grand_total=format_amt(grand_tot)
print(f"grand total:{form_grand_total}")

#visualize 
import matplotlib.pyplot as plt
plt.title("Sales chart")
plt.bar(df['Item'],df['Totals'])
plt.xlabel('Items')
plt.ylabel('Total sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_chart.png')
plt.show()

