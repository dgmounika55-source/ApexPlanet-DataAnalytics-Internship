import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
orders = pd.read_csv("Task1/cleaned_orders.csv")
products = pd.read_csv("Task1/cleaned_products.csv")
payments = pd.read_csv("dataset/olist_order_payments_dataset.csv")

# Display first rows
print("\nORDERS DATA")
print(orders.head())

print("\nPAYMENTS DATA")
print(payments.head())

# Basic statistics
print("\nPAYMENT STATISTICS")
print(payments['payment_value'].describe())
# Payment distribution chart
plt.figure(figsize=(10,5))

sns.histplot(payments['payment_value'], bins=50)

plt.title("Payment Value Distribution")
plt.xlabel("Payment Value")
plt.ylabel("Frequency")
plt.show()
# Payment method analysis
payment_method_counts = payments['payment_type'].value_counts()

print("\nPAYMENT METHOD COUNTS")
print(payment_method_counts)

# Payment method chart
plt.figure(figsize=(8,5))

sns.countplot(x='payment_type', data=payments)

plt.title("Payment Methods Used")
plt.xlabel("Payment Type")
plt.ylabel("Count")

plt.show()
# Convert purchase timestamp to datetime
orders['order_purchase_timestamp'] = pd.to_datetime(
    orders['order_purchase_timestamp']
)

# Extract month and year
orders['order_month'] = orders['order_purchase_timestamp'].dt.to_period('M')

# Count orders per month
monthly_orders = orders['order_month'].value_counts().sort_index()

print("\nMONTHLY ORDER COUNTS")
print(monthly_orders)

# Monthly orders trend chart
plt.figure(figsize=(14,6))

monthly_orders.plot()

plt.title("Monthly Order Trend")
plt.xlabel("Month")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)

plt.show()
# Order status analysis
order_status_counts = orders['order_status'].value_counts()

print("\nORDER STATUS COUNTS")
print(order_status_counts)

# Order status chart
plt.figure(figsize=(8,5))

sns.countplot(
    x='order_status',
    data=orders,
    order=orders['order_status'].value_counts().index
)

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.show()
# Top 10 highest payment values
top_payments = payments.sort_values(
    by='payment_value',
    ascending=False
).head(10)

print("\nTOP 10 HIGHEST PAYMENTS")
print(top_payments[['order_id', 'payment_type', 'payment_value']])

# Top payments chart
plt.figure(figsize=(12,5))

sns.barplot(
    x='order_id',
    y='payment_value',
    data=top_payments
)

plt.title("Top 10 Highest Payment Orders")
plt.xlabel("Order ID")
plt.ylabel("Payment Value")

plt.xticks(rotation=90)

plt.show()