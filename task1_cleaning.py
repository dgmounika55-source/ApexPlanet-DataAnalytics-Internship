import pandas as pd

# Load datasets
customers = pd.read_csv("dataset/olist_customers_dataset.csv")
orders = pd.read_csv("dataset/olist_orders_dataset.csv")
payments = pd.read_csv("dataset/olist_order_payments_dataset.csv")
products = pd.read_csv("dataset/olist_products_dataset.csv")
order_items = pd.read_csv("dataset/olist_order_items_dataset.csv")

# Show first 5 rows
print("\nCUSTOMERS DATA")
print(customers.head())

print("\nORDERS DATA")
print(orders.head())

# Show dataset information
print("\nORDERS INFO")
print(orders.info())

# Check missing values
print("\nMISSING VALUES IN PRODUCTS")
print(products.isnull().sum())

# Check duplicate rows
print("\nDUPLICATES IN ORDERS")
print(orders.duplicated().sum())
# Fill missing product category names
products['product_category_name'] = products['product_category_name'].fillna("Unknown")

products['product_weight_g'] = products['product_weight_g'].fillna(
    products['product_weight_g'].median()
)

products['product_length_cm'] = products['product_length_cm'].fillna(
    products['product_length_cm'].median()
)

products['product_height_cm'] = products['product_height_cm'].fillna(
    products['product_height_cm'].median()
)

products['product_width_cm'] = products['product_width_cm'].fillna(
    products['product_width_cm'].median()
)
# Convert order dates to datetime
orders['order_purchase_timestamp'] = pd.to_datetime(
    orders['order_purchase_timestamp']
)

# Save cleaned datasets
products.to_csv("Task1/cleaned_products.csv", index=False)
orders.to_csv("Task1/cleaned_orders.csv", index=False)

print("\nDATA CLEANING COMPLETED SUCCESSFULLY!")