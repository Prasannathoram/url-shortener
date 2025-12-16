from pydantic import BaseModel, HttpUrl

class ShortenRequest(BaseModel):
    original_url: HttpUrl


class ShortenResponse(BaseModel):
    short_code: str


class StatsResponse(BaseModel):
    short_code: str
    total_clicks: int
