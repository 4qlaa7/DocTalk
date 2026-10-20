from fastapi import FastAPI

app = FastAPI()

@app.get("/sum")
def sum(a: int, b: int):
    return {"result": f'result is {a + b}'}