import numpy as np 
import pandas as pd

np.random.seed(42)

data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Revenue': np.random.randint(200, 500, 12),
    'Orders': np.random.randint(800, 2000, 12),
    'Customers': np.random.randint(500, 1500, 12),
    'Marketing-Spend': np.random.randint(50, 150, 12),
    'Returns': np.random.randint(15, 80, 12)
})

print(data)
