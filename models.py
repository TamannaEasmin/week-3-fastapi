from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Database connection URL (PostgreSQL)
# Format: postgresql://username:password@host:port/database_name
DATABASE_URL = "postgresql://postgres:12345@localhost:5432/shop_project"

# 2. Create the Database Engine (The core interface to the database)
engine = create_engine(DATABASE_URL)

# 3. Create a Base Class (All our models will inherit from this)
Base = declarative_base()

# 4. Define the Product Model (This Python class maps to the 'products' table)
class Product(Base):
    __tablename__ = "products"  # Name of the table in the database
    
    # Define the columns
    id = Column(Integer, primary_key=True)            # Unique ID for each product
    name = Column(String(100), nullable=False)        # Product name (cannot be empty)
    price = Column(Numeric(10, 2), nullable=False)    # Price with 2 decimal places
    stock = Column(Integer, default=0)                # Available stock (defaults to 0)

# 5. Create a Session Factory (Used to execute queries)
SessionLocal = sessionmaker(bind=engine)

print("✅ Models loaded successfully! The connection is ready.")
