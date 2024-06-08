from backend.src.goals.service import SearchGoalsService
from backend.src.goals.schema import SearchGoalsInputSchema, SearchGoalsResponseSchema
from starlette import status
from fastapi import APIRouter, Body, Depends


class SearchGoalsController:
    def __init__(self, search_goals_service: SearchGoalsService):
        self.search_goals_service = search_goals_service
        self.router = APIRouter()
        self.router.add_api_route(
            "/search_goals/{text_title}",
            self.handle,
            methods=["GET"],
            status_code=status.HTTP_200_OK,
            response_model=SearchGoalsResponseSchema,
            name="",
        )

    async def handle(self, text_title: str):
        return self.search_goals_service.search_goals(text_title)
