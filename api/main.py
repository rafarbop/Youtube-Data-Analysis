from fastapi import FastAPI
from api.routes.analysis import router


def create_app():
    """Create and run fast api."""
    app = FastAPI()

    app.include_router(router)

    @app.get("/")
    def root() -> dict[str, str]:
        return {"status": "OK"}

    return app
