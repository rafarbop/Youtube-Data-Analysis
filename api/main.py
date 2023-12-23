from fastapi import FastAPI
from api.routes import youtube


def create_app() -> FastAPI:
    """Create and run fast api."""
    app = FastAPI()

    app.include_router(youtube.router)

    @app.get("/")
    def main() -> dict[str, str]:
        return {"status": "OK"}

    return app
