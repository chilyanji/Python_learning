from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user

@app.get("/")
def home():
    return {"message": "Hello World! My name is Ayush Singh"}
@app.get("/about")
def about():
    return {"message": "About Page"}
@app.get("/contact")
def contact():
    return{"message": "Contact US"}
@app.get("/user/{user_id}/post/{post_id}")
def get_user(user_id: int, post_id: int):
    return {
        "user_id": user_id, 
        "post_id": post_id
    }

# Quary Parameters

@app.get("/products")
def get_products(category: str):
    return {"category": category}


@app.get("/search")
def search(q: str, page: int):
    return {
        "query": q,
        "page": page
    }

