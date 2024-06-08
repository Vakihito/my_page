from fastapi import APIRouter
from backend.src.goals.service import UpdateGoalsService
from backend.src.goals.controller import UpdateGoalsController
from backend.src.goals.infra import GoalsRepository
from backend.src.shared.database_shared import get_db_session

db = next(get_db_session())


def update_goals_router_factory() -> APIRouter:
    repository = GoalsRepository(db)
    service = UpdateGoalsService(repository)
    controller = UpdateGoalsController(service)
    return controller.router
