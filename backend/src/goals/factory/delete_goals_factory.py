from fastapi import APIRouter
from backend.src.goals.service import DeleteGoalsService
from backend.src.goals.controller import DeleteGoalsController
from backend.src.goals.infra import GoalsRepository
from backend.src.shared.database_shared import get_db_session

db = next(get_db_session())


def delete_goals_router_factory() -> APIRouter:
    repository = GoalsRepository(db)
    service = DeleteGoalsService(repository)
    controller = DeleteGoalsController(service)
    return controller.router
