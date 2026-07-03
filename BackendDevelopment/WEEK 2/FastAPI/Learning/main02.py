from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# @app.get("/hello")

# def hello(name: str):
#     return {
#         "message": f"Hello {name}"
#     }

@app.get("/search")
def search(q: str, page: int):
    return {
        "query": q,
        "page": page
    }


# Optional Query Parameters


@app.get("/hello")
def hello(name: Optional[str] = None):
    if name:
        return {"message": f"Hello {name}"}
    return {"message": "Hello Guest"}

# Default Values

@app.get("/products")
def products(page: int = 1):
    return {
        "page": page
    }

# Multiple Default Parameters

@app.get("/products")
def products(page: int = 1, limit: int = 10):
    return {
        "page": page,
        "limit": limit
    }