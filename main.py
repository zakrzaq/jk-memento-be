from fastapi import FastAPI
from utils.init_models import init_models
from routes import todo

init_models()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Memento API", "version": "0.1"}


app.include_router(todo.router, prefix="/todo")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
