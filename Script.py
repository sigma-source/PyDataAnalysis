"""
Question:
1.How many sales have they made with amounts more than 1000
2.How many sales have they made that belong to the Category "Tops" and have a Quantity of 3.
3.The Total Sales by Category
4.Average Amount by Category and Status
5.Total Sales by Fulfilment and Shipment Type

"""
import numpy as np
import pandas as pd

sales_data= pd.read_excel("sales_data.xlsx")

#summary
sales_data.info()
sales_data.describe()

#column names
print(sales_data.columns)

#first few Rows
print(sales_data.head())

# type 
print(sales_data.dtypes)


# =============================================================================
# Cleaning the Data
# =============================================================================

# Check null Values
print(sales_data.isnull().sum())

#Drop Any rows
sales_data_dropped=sales_data.dropna()   #lost too much data


#drop only values which have only missing amounts
sales_data_cleaned = sales_data.dropna(subset=['Amount'])
print(sales_data_cleaned.isnull().sum())

#How many sales have they made with amounts more than 1000
Sales_greater_th=sales_data_cleaned[sales_data_cleaned['Amount']>1000]['Order ID'].count()
print(Sales_greater_th)

#How many sales have they made that belong to the Category "Tops" and have a Quantity of 3.
sales_tops_grt=sales_data_cleaned[(sales_data_cleaned['Category']=="Top") & (sales_data_cleaned['Qty']==3)]['Order ID'].count()
print(sales_tops_grt)

#The Total Sales by Category
Category_total=sales_data_cleaned.groupby('Category')['Amount'].sum()
print(Category_total)
Category_total=sales_data_cleaned.groupby('Category', as_index= False)['Amount'].sum()

Category_total=Category_total.sort_values("Amount", ascending=False)

#Average Amount by Category and Status
Category_avg=sales_data_cleaned.groupby(['Category', 'Status'])['Amount'].mean()
Category_avg=sales_data_cleaned.groupby(['Category', 'Fulfilment'], as_index=False)['Amount'].mean()
Category_avg=Category_avg.sort_values('Amount', ascending=False)

#Total Sales by Fulfilment and Shipment Type
Sales_total_SF=sales_data_cleaned.groupby(['Courier Status','Fulfilment'],as_index=False)['Amount'].sum()
Sales_total_SF=Sales_total_SF.sort_values('Amount', ascending=False)
Sales_total_SF=Sales_total_SF.rename(columns={'Courier Status' : 'Shipment'}, inplace=False)

#Export 
Sales_total_SF.to_excel('Sales total by ful and ship.xlsx', index=False)
Category_avg.to_excel('catavg.xlsx',index=False)


