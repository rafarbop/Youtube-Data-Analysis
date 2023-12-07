from typing import Any
from googleapiclient import discovery
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()


class YouTubeApiService:
    """Class for handler all youtube services requests."""

    def __init__(self):
        self.youtube_service = discovery.build(
            serviceName="youtube",
            version="v3",
            developerKey=os.getenv("youtubeApiKey"),
        )

    def _get_comment_threads(self, options: dict[str, str | int]) -> Any:
        request = self.youtube_service.commentThreads().list(**options)
        return request.execute()

    def _join_comments(self, response: dict[str, Any]) -> list[Any]:
        comments: list[Any] = []
        total_replies = 0
        for item in response["items"]:
            comment_id = item["snippet"]["topLevelComment"]["id"]
            comment = item["snippet"]["topLevelComment"]["snippet"]
            total_reply_count = item["snippet"]["totalReplyCount"]
            comments.append(
                [
                    comment_id,
                    comment["channelId"],
                    comment["videoId"],
                    comment["authorDisplayName"],
                    comment["publishedAt"],
                    comment["updatedAt"],
                    total_reply_count,
                    comment["textDisplay"],
                ]
            )
            total_replies += total_reply_count
        print(f"Total replies: {total_replies}")
        return comments

    def _comments_to_json(self, comments: list[Any]):
        # Convert the list of lists to a list of dictionaries
        json_comments = []
        for comment in comments:
            data_row = {
                "comment_id": comment[0],
                "channel_id": comment[1],
                "video_id": comment[2],
                "author": comment[3],
                "published_at": comment[4],
                "updated_at": comment[5],
                "reply_count": comment[6],
                "text": comment[7],
            }
            json_comments.append(data_row)
        return json_comments

    def _dataframe_info_comments(self, comments: list[Any]) -> pd.DataFrame:
        df = pd.DataFrame(
            comments,
            columns=[
                "comment_id",
                "channel_id",
                "video_id",
                "author",
                "published_at",
                "updated_at",
                "reply_count",
                "text",
            ],
        )
        return df

    def get_comments_info(
        self,
        source_id: str,
        related_to: str = "",
        page_token: str = "",
        all_comments: list[Any] = [],
    ):
        """Get top level comments for a especify video or channel."""
        comments = []
        if not page_token:
            all_comments = []
        options: dict[str, str | int] = {
            "part": "snippet",
            "maxResults": 100,
            "textFormat": "plainText",
        }
        if related_to == "video":
            options["videoId"] = source_id
        elif related_to == "channel":
            options["channelId"] = source_id
        if page_token:
            options["pageToken"] = page_token
        try:
            response = self._get_comment_threads(options)
        except Exception as e:
            print("Erro na solicitação")
            print(f"Detalhe do erro: {e}")
        comments = self._join_comments(response)
        all_comments.extend(comments)
        next_page_token = response.get("nextPageToken")
        if next_page_token:
            print(
                f"Buscando dados da próxima página - nextPageToken: {next_page_token}"
            )
            return self.get_comments_info(
                source_id, related_to, next_page_token, all_comments.copy()
            )
        comments_json = self._comments_to_json(all_comments)
        # df: pd.DataFrame = self._dataframe_info_comments(comments)
        # df.info()
        # print(df['reply_count'].sum())
        # return json.loads(df.to_json(orient='records'))
        return comments_json
