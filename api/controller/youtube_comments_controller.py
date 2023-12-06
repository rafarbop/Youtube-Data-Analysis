from api.controller.base_controller import BaseController
from api.service.youtube_api_service import YouTubeApiService


class YouTubeCommentsController(BaseController):
    """Class Controller for Youtube Comments Requests."""

    def __init__(self):
        super().__init__()
        self.youtube_service = YouTubeApiService()
        # self.youtube_comments_service = youtube_comments_service

    def get_comments(self, source_id: str):
        """Get comments for video_id or channel_id of youtube."""
        data = self.youtube_service.get_comments_info(
            source_id=source_id, related_to="video"
        )
        return data

    # async def get_sentiment_analysis(self, video_id):
    #     return await self.youtube_comments_service.get_sentiment_analysis(video_id)

    # async def get_topic_extraction(self, video_id):
    #     return await self.youtube_comments_service.get_topic_extraction(video_id)
