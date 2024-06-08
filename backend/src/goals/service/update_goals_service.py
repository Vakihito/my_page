from backend.src.goals.schema import UpdateGoalsInputSchema, UpdateGoalsResponseSchema
from backend.src.goals.model import GoalsModel
from backend.src.goals.infra import GoalsRepository


class UpdateGoalsService:
    def __init__(self, update_goals_repository: GoalsRepository) -> UpdateGoalsResponseSchema:
        self.update_goals_repository = update_goals_repository

    def update_goals(self, update_goals_input: UpdateGoalsInputSchema) -> UpdateGoalsResponseSchema:
        return {"created": True}
