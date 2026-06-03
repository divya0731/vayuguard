from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "VayuGuard ML Service Running"}

@app.get("/health")
def health():
    return {"health": "ok"}