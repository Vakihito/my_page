from backend.src.goals.schema import SearchGoalsInputSchema, SearchGoalsResponseSchema
from backend.src.goals.model import GoalsModel
from backend.src.goals.infra import GoalsRepository


class SearchGoalsService:
    def __init__(
        self, search_goals_repository: GoalsRepository
    ) -> SearchGoalsResponseSchema:
        self.search_goals_repository = search_goals_repository

    def search_goals(self, **args) -> SearchGoalsResponseSchema:
        serach_input = SearchGoalsInputSchema(**args)
        print(f"searching for : {serach_input}")
        searched_object = self.search_goals_repository.search_goals(serach_input)
        return searched_object
