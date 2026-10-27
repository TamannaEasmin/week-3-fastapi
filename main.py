from fastapi import FastAPI, Depends, HTTPException
from models import SessionLocal, Product
from pydantic import BaseModel
from sqlalchemy.orm import Session

app = FastAPI(title="My First FastAPI App")

# Pydantic model
class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int = 0

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to my first FastAPI App!"}

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@app.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        name=product.name,
        price=product.price,
        stock=product.stock
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"message": "Product added successfully!", "product": new_product}

@app.put("/products/{product_id}")
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_product.name = product.name
    db_product.price = product.price
    db_product.stock = product.stock
    db.commit()
    db.refresh(db_product)
    return {"message": "Product updated successfully!", "product": db_product}

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return {"message": f"Product with ID {product_id} deleted successfully!"}
