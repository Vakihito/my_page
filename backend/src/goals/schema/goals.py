from uuid import UUID
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict


class CreateGoalInputSchema(BaseModel):
    id: UUID
    title: str
    todo: str
    nottodo: str
    start_date: datetime = datetime.strptime("2024-06-07", "%Y-%m-%d")
    end_date: datetime = datetime.strptime("2024-06-20", "%Y-%m-%d")
    data_format: str = "weaks"
    model_config = ConfigDict(
        id="00000000-0000-0000-0000-000000000000",
        title="cool little text",
    )


class CreateGoalResponseSchema(BaseModel):
    created: bool
