from sqlalchemy import and_, distinct
from sqlalchemy import update as dbUpdate
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.sql import func, literal_column
from starlette import status
from backend.src.goals.schema import CreateGoalInputSchema, CreateGoalResponseSchema
from backend.src.goals.model import GoalsModel
from loguru import logger
from backend.src.main.exceptions import ApplicationException
from datetime import date, datetime


class GoalsRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_goal(self, create_goal_input: CreateGoalInputSchema):
        create_goal_input.start_date = datetime.strptime(create_goal_input.start_date, "%Y-%m-%d")
        create_goal_input.end_date = datetime.strptime(create_goal_input.end_date, "%Y-%m-%d")

        new_goal = GoalsModel(**create_goal_input.model_dump())
        try:
            logger.info("create new goal")
            self.db.add(new_goal)
            self.db.commit()
            self.db.refresh(new_goal)
        except IntegrityError:
            self.db.rollback()
            logger.info("goal duplicated, returning goal existent")
            return None
        except SQLAlchemyError:
            self.db.rollback()
            raise ApplicationException(status_code=500, key="postgres_keyword_error_to_create")
        finally:
            self.db.close()

        logger.info("created new goal")

        return new_goal
