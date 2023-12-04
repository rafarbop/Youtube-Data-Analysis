from typing import Any
from fastapi import APIRouter
from controller.youtube_comments_controller import YouTubeCommentsController

router = APIRouter(prefix="/analysis")

youtube_comments = YouTubeCommentsController()


@router.get("/youtube_comments/{resource_id}")
async def add_service_analysis(resource_id: str) -> Any:
    info = youtube_comments.get_comments(resource_id)
    return info
