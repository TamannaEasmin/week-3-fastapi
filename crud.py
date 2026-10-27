from models import SessionLocal, Product

# 1. Create a new session (connection to the database)
db = SessionLocal()

# ==========================================
# CREATE: Inserting a new product
# ==========================================
print("--- Creating a new product ---")

# Create a Python object
new_product = Product(name="Python Book", price=29.99, stock=50)

# Add it to the session and commit to save in the database
db.add(new_product)
db.commit()
db.refresh(new_product) # Refresh to get the auto-generated ID

print(f"✅ Added Product: {new_product.name} with ID: {new_product.id}")

# ==========================================
# READ: Fetching data from the database
# ==========================================
print("\n--- Reading all products ---")

# Query all products from the database
all_products = db.query(Product).all()

for p in all_products:
    print(f"ID: {p.id} | Name: {p.name} | Price: ${p.price} | Stock: {p.stock}")

# ==========================================
# UPDATE: Modifying existing data
# ==========================================
print("\n--- Updating product price ---")

# Find the product we just created (using its ID)
product_to_update = db.query(Product).filter(Product.id == new_product.id).first()

if product_to_update:
    product_to_update.price = 24.99  # Change the price
    db.commit() # Save changes
    print(f"✅ Updated {product_to_update.name}'s price to ${product_to_update.price}")

# ==========================================
# DELETE: Removing data
# ==========================================
print("\n--- Deleting the product ---")

# Delete the product
db.delete(product_to_update)
db.commit()
print(f"❌ Deleted product with ID: {new_product.id}")

# Close the session when done
db.close()
