import os
print(os.getcwd())
data_path="D:\Projects ai\sales\Sales_Analysis\data\sales.csv"
if os.path.exists(data_path):
  print(f"found:{data_path}")
else:
  print("not found")

#to read csv file 
import pandas as pd
df=pd.read_csv('D:\Projects ai\sales\Sales_Analysis\data\sales.csv')
print(df)
print(f"shape:{df.shape[0]}rows,{df.shape[1]}cols")

#to clacu total in each row 
df['total']=df['Quantity']*df['Price']
print(df)

#to create directory if not there 
#os.makedirs('output',exists_ok=True)   here it is already created

#to save as json format inside output
import json
df.to_json('D:\Projects ai\sales\Sales_Analysis\output\sales_data.json',orient='records')

#to save as excel file
#to open excel file left click>reveal in file explorer 
df.to_excel('D:\Projects ai\sales\Sales_Analysis\output\sales_data.xlsx',index=False)


#similarly save as csv as already did
#df.to_csv('D:\Projects ai\sales\Sales_Analysis\output\sales_data.csv',index=False)

#to read json 
df=pd.read_json('D:\Projects ai\sales\Sales_Analysis\output\sales_data.json')
#or for simple json:
with open('D:\Projects ai\sales\Sales_Analysis\output\sales_data.json','r') as f:
  data=json.load(f)

#read excel file
df=pd.read_excel('D:\Projects ai\sales\Sales_Analysis\output\sales_data.xlsx')

#txt files
with open('D:\Projects ai\sales\requirements.txt','r') as f:
  txt=f.read()

