from fastapi import FastAPI
app = FastAPI()

@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}


@app.get("/multiply")
def multiply(a: int, b: int):
    return {
        "result": a * b
    }


@app.get("/student")
def student(name: str, age: int, city: str):
    return {
        "name": name,
        "age": age,
        "city": city
    }