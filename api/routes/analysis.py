from typing import Any
from fastapi import APIRouter
from api.controller.youtube_comments_controller import YouTubeCommentsController

router = APIRouter(prefix="/analysis")

youtube_comments = YouTubeCommentsController()


@router.get("/youtube_comments/{resource_id}")
async def add_service_analysis(resource_id: str) -> Any:
    """Route to handler requests for get youtube comments."""
    info = youtube_comments.get_comments(resource_id)
    return info
