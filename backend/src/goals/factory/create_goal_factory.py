from fastapi import APIRouter
from backend.src.goals.service import CreateGoalService
from backend.src.goals.controller import CreateGoalController
from backend.src.goals.infra import GoalsRepository
from backend.src.shared.database_shared import get_db_session

db = next(get_db_session())


def create_goal_router_factory() -> APIRouter:
    repository = GoalsRepository(db)
    service = CreateGoalService(repository)
    controller = CreateGoalController(service)
    return controller.router
