# Week 3: FastAPI CRUD API

A simple REST API built with **FastAPI**, **SQLAlchemy (ORM)**, and **PostgreSQL**. This project demonstrates how to perform full CRUD (Create, Read, Update, Delete) operations using Python.

## 🚀 Features
- **GET** `/products` - Fetch all products
- **POST** `/products` - Add a new product
- **PUT** `/products/{id}` - Update an existing product
- **DELETE** `/products/{id}` - Delete a product
- Data validation using **Pydantic**
- Clean database session management using FastAPI `Depends`

## 🛠️ Technologies Used
- Python 3.10+
- FastAPI
- SQLAlchemy (ORM)
- PostgreSQL
- Pydantic
- Uvicorn

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone git@github.com:TamannaEasmin/week-3-fastapi.git
   cd week-3-fastapi
