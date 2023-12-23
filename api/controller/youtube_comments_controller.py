from api.service.youtube_api_service import YouTubeApiService
from typing import Any


class YouTubeCommentsController:
    """Class Controller for Youtube Comments Requests."""

    def __init__(self):
        self.youtube_service = YouTubeApiService()

    def get_status_analysis(self):
        """Get status of analysis in queue."""
        pass

    def _get_source_infos(self, source_id: str, type: str) -> dict[str, Any]:
        print("Getting info source...")
        return {"source_id": source_id, "type": type, "is_source_valid": True}

    def _add_item_analysis_queue(
        self, source_id: str, type: str, source_infos: dict[str, Any]
    ):
        print("Add source in queue...")
        pass

    def _export_comments(self, comments):
        print("Exporting comments...")
        pass

    def get_comments(self, source_id: str, type: str):
        """Get comments for video_id or channel_id of youtube."""
        data = self.youtube_service.get_comments_info(
            source_id=source_id, related_to=type
        )
        return data

    def add_comments_for_analysis(self, source_id: str, type: str) -> dict[str, Any]:
        """Add comments to analysis queue."""
        source_infos = self._get_source_infos(source_id, type)
        if source_infos.get("is_source_valid"):
            comments = self.get_comments(source_id, type)
            self._export_comments(comments)
            self._add_item_analysis_queue(source_id, type, source_infos)
            return {
                "Source ID": source_id,
                "status": "SUCCESS",
                "message": "Add in queue with success",
                "number_comments": len(comments),
                "example_comment": comments[0],
            }

        return {"Source ID": source_id, "status": "FAILED"}
