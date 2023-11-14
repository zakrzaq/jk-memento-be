from fastapi import FastAPI
from utils.init_models import init_models
from routes import todo, user

init_models()

app = FastAPI()


@app.get("/", tags=["root"])
async def root():
    return {"message": "Memento API", "version": "0.1"}


app.include_router(todo.router, prefix="/todo", tags=["todos"])
app.include_router(user.router, prefix="/user", tags=["users"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
