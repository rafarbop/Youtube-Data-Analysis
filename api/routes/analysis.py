from fastapi import APIRouter
from controller.youtube_comments_controller import YouTubeCommentsController

router = APIRouter(prefix="/analysis")

youtube_comments = YouTubeCommentsController()


@router.get("/youtube_comments")
async def add_service_analysis() -> dict[str, int]:
    return youtube_comments.get_kpis()
