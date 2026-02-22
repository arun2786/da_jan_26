import pandas as pd

sales_data = pd.read_csv('orders.csv')

# print("Data ---------------")
# print(sales_data)

# print("Customers")
# print(sales_data["Customer"])


# print("Customers with order status")
# print(sales_data[["Customer", "Status"]])

# print("Select order by index")
# print(sales_data.iloc[:3])


# print("Cancelled orders")
# print(sales_data['Status']=='Cancelled')
# print(sales_data[sales_data['Status']=='Cancelled'])


# print("Prime orders")
# print(sales_data[sales_data['Amount']>=200])


# print("Prime & Cancelled orders")
# print(sales_data[
#     (sales_data['Status']=='Cancelled')
#     &
#     (sales_data['Amount']>=200)
#     ])

# modify first row - status

# sales_data.loc[0,'Status']="Delivered"

# print(f"Add 5% gst")

# sales_data['Bill'] = sales_data['Amount'] * 1.05
# print(sales_data)

# Delete column
# backup = sales_data.copy()
# backup = backup.drop('City', axis=1)
# print(backup)

# Delete row 
# backup = sales_data.copy()
# backup = backup.drop(1, axis=0)
# print(backup)


# Sorting - ascending
# print(sales_data.sort_values('Amount'))
# print(sales_data.sort_values('Amount', ascending=False))

# total_sale_by_status = sales_data.groupby('Status')['Amount'].sum()
# print(total_sale_by_status)

# total_sale_by_city = sales_data.groupby('City')['Amount'].sum()
# print(total_sale_by_city)


# sd = sales_data.groupby('Status')['Amount'].agg([
#     ('Total', 'sum'),
#     ('Average', 'mean')
# ])

# print(sd)


# print(sales_data.groupby('City')['Amount'].sum())