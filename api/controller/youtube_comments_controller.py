from controller.base_controller import BaseController


class YouTubeCommentsController(BaseController):
    def __init__(self):
        super().__init__()
        # self.youtube_comments_service = youtube_comments_service

    def get_kpis(self):
        return {"kpi1": 25, "kpi2": 58}

    # async def get_sentiment_analysis(self, video_id):
    #     return await self.youtube_comments_service.get_sentiment_analysis(video_id)

    # async def get_topic_extraction(self, video_id):
    #     return await self.youtube_comments_service.get_topic_extraction(video_id)
