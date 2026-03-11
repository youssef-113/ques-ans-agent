# app/main.py
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
print("env loaded")
print("env ok")

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

# Optional: local run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
