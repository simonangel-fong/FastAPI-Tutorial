from fastapi import FastAPI

app = FastAPI(title="Demo")


@app.get("/")
async def root():
    return {"message": "This is a fastapi demo."}
