from fastapi import APIRouter
from backend.src.goals.service import SearchGoalsService
from backend.src.goals.controller import SearchGoalsController
from backend.src.goals.infra import GoalsRepository
from backend.src.shared.database_shared import get_db_session

db = next(get_db_session())


def search_goals_router_factory() -> APIRouter:
    repository = GoalsRepository(db)
    service = SearchGoalsService(repository)
    controller = SearchGoalsController(service)
    return controller.router
