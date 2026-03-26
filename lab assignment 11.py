import pandas as pd
import matplotlib.pyplot as plt

# Creating synthetic dataset
data = {
    'month_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'facecream': [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    'facewash': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    'toothpaste': [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
    'total_profit': [211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200]
}
df = pd.DataFrame(data)

# a) Line Plot of Total Profit
plt.figure(figsize=(10, 5))
plt.plot(df['month_number'], df['total_profit'], marker='o', color='b', label='Monthly Profit')
plt.title('Total Profit per Month')
plt.xlabel('Month Number')
plt.ylabel('Profit')
plt.grid(True)
plt.show()

# b) Multiline Plot for all product sales
plt.figure(figsize=(10, 5))
plt.plot(df['month_number'], df['facecream'], label='Face Cream', marker='o')
plt.plot(df['month_number'], df['facewash'], label='Face Wash', marker='o')
plt.plot(df['month_number'], df['toothpaste'], label='Toothpaste', marker='o')
plt.title('All Product Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.legend()
plt.show()

# c) Bar Chart for Face Cream and Face Wash
plt.figure(figsize=(10, 5))
plt.bar(df['month_number'] - 0.2, df['facecream'], width=0.4, label='Face Cream', align='center')
plt.bar(df['month_number'] + 0.2, df['facewash'], width=0.4, label='Face Wash', align='center')
plt.title('Face Cream vs Face Wash Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.xticks(df['month_number'])
plt.legend()
plt.show()

# d) Pie Chart for Total Yearly Sales per product
products = ['facecream', 'facewash', 'toothpaste']
sales_data = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum()]
plt.figure(figsize=(7, 7))
plt.pie(sales_data, labels=products, autopct='%1.1f%%', startangle=140)
plt.title('Total Yearly Sales Distribution')
plt.show()
