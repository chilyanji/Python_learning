from  fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def products(
    category: str,
    min_price: int,
    max_price: int
):
    return {
        "category": category,
        "min_price": min_price,
        "max_price": max_price
    }


# Boolean Query Parameters

@app.get("/items")
def items(in_stock: bool = True):
    return {
        "in_stock": in_stock
    }