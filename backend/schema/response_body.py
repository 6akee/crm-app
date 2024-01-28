from pydantic import BaseModel, Field


class ResponseBody(BaseModel):
    FactMsg: dict | None = Field(default=None, description="Словарь с фактами")