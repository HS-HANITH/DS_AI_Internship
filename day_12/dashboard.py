# dashboard.py

import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for line plot (monthly sales trend example)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
monthly_sales = [200, 250, 300, 350, 400, 450]

# Create figure

# Subplot 1: Bar Chart
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Sales")

# Subplot 2: Line Plot
plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Prevent overlapping
plt.tight_layout()

# Show plot
plt.show()
