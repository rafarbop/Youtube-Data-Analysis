from fastapi import FastAPI
from routes.analysis import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def main() -> dict[str, str]:
    return {"status": "OK"}
