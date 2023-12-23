from typing import Any
from fastapi import APIRouter, status, Response
from api.controller.youtube_comments_controller import YouTubeCommentsController

router = APIRouter(prefix="/youtube")

youtube_comments = YouTubeCommentsController()


@router.get("/video/{source_id}", status_code=status.HTTP_201_CREATED)
async def add_video_service(source_id: str, response: Response) -> Any:
    """Route to add requests for get video youtube comments analysis."""
    info = youtube_comments.add_comments_for_analysis(source_id, "video")
    if info["status"] == "FAILED":
        response.status_code = status.HTTP_400_BAD_REQUEST
    return info


@router.get("/channel/{source_id}", status_code=status.HTTP_201_CREATED)
async def add_channel_service(source_id: str, response: Response) -> Any:
    """Route to add requests for get channel youtube comments analysis."""
    info = youtube_comments.add_comments_for_analysis(source_id, "channel")
    if info["status"] == "FAILED":
        response.status_code = status.HTTP_400_BAD_REQUEST
    return info
