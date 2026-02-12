from fastapi import FastAPI

# uvicorn main:app --reload --port 8080

app = FastAPI(
    title="test-Insight",
    description="",
    version="1.0.0"
)

@app.get("/")
def hello():
    return {
        "message": "Hello, World!"
    }