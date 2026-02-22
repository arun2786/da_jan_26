import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

data = pd.read_csv("sales.csv")

fig,matrix =  plt.subplots(2,2, figsize=(15,8))
# Revenue Trend
matrix[0,0].plot(data['Month'],data['Revenue'], marker="o", linewidth=4, color='green') # Line chart
matrix[0,0].set_title("Monthly Revenue Trend")
matrix[0,0].grid()

# Orders
matrix[0,1].bar(data['Month'],data['Orders']) # bar chart
matrix[0,1].set_title("Month - Order Analysis")
matrix[0,1].grid()


# Returns Trend
matrix[1,0].fill_between(data['Month'],data['Returns']) # bar chart
matrix[1,0].set_title("Month - Returns Analysis")

# Customer Vs Revenue 

matrix[1,1].scatter(data['Customers'],data['Revenue'])
matrix[1,1].set_title("Customer vs Revenue Trend")
matrix[1,1].grid()

fig.suptitle("Sales Dashboard", fontsize=24)
plt.tight_layout()
plt.savefig("sales_dashboard.png")
plt.show()

