from fastapi import FastAPI
from src.first_project.calculator import Calculator

app = FastAPI(title="Calculator API", version="1.0.0")
calc = Calculator()

@app.get("/")
async def root():
    return {"message": "Calculator API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/add")
async def add_numbers(x: float, y: float):
    result = calc.add(x, y)
    return {"result": result, "operation": "addition", "operands": [x, y]}

@app.get("/add/{x}/{y}")
async def add_numbers_get(x: float, y: float):
    result = calc.add(x, y)
    return {"result": result, "operation": "addition", "operands": [x, y]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)