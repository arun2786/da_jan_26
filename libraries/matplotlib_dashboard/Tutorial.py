import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

data = pd.read_csv("sales.csv")
# print(data)

# np.random.seed(42)

# data = pd.DataFrame({
#     'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
#     'Revenue': np.random.randint(100, 8000, 12),
#     'Orders': np.random.randint(100, 8000, 12),
#     'Customers': np.random.randint(100, 1500, 12),
#     'Marketing-Spend': np.random.randint(50, 150, 12),
#     'Returns': np.random.randint(15, 80, 12)
# })
# Task 1 - Analyse Revenue Trends (Month - Revenue)

plt.figure(figsize=(10,5))
# plt.plot(data['Month'],data['Revenue']) # Line chart
plt.plot(data['Month'],data['Revenue'], marker="o", linewidth=4, color='green') # Line chart
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid()
# plt.gca().set_xticks(range(len(data['Month'])))
# plt.gca().set_yticks(range(250, 450, 10))
plt.show()



# Task 2 - Customer vs Revenue
plt.figure(figsize=(10,5))
plt.scatter(data['Customers'],data['Revenue'])
plt.title("Customer vs Revenue Trend")
plt.xlabel("Customer")
plt.ylabel("Revenue")
plt.show()

# Task 3 - Month - Order Analysis
plt.figure(figsize=(10,5))
plt.bar(data['Month'],data['Orders']) # bar chart
plt.title("Month - Order Analysis")
plt.xlabel("Months")
plt.ylabel("Orders")
plt.grid()
plt.show()

# Task 4 - Revenue vs Marketing 
plt.figure(figsize=(10,5))
plt.plot(data['Month'],data['Revenue'], marker="o", color="green", label="Revenue") 
plt.plot(data['Month'],data['Marketing-Sp'], marker="s", color="red", label="Marketing") 
plt.title("Revenue vs Marketing Spends")
plt.xlabel("Months")
plt.ylabel("Values")
plt.grid()
plt.legend()
plt.show()

# Task 5 - Histogram - Revenue Distribution
plt.figure(figsize=(10,5))
plt.hist(data['Revenue']) # bar chart
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()


# Task 6 - Month - Returns Analysis
plt.figure(figsize=(10,5))
plt.fill_between(data['Month'],data['Returns']) # bar chart
plt.title("Month - Returns Analysis")
plt.xlabel("Months")
plt.ylabel("Returns")
plt.grid()
plt.show()