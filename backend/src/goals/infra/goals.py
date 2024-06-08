from backend.src.goals.schema import CreateGoalInputSchema, UpdateGoalsResponseSchema
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
        if isinstance(create_goal_input.start_date, str):
            create_goal_input.start_date = datetime.strptime(
                create_goal_input.start_date, "%Y-%m-%d"
            )
        if isinstance(create_goal_input.end_date, str):
            create_goal_input.end_date = datetime.strptime(
                create_goal_input.end_date, "%Y-%m-%d"
            )

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
            raise ApplicationException(
                status_code=500, key="postgres_keyword_error_to_create"
            )
        finally:
            self.db.close()

        logger.info("created new goal")

        return new_goal

    def update_goals(self, update_goals_input: CreateGoalInputSchema):
        update_goals_dict = {}
        for field, value in update_goals_input.__dict__.items():
            if (value is not None) and (field != "id"):
                update_goals_dict[field] = value
        stmt = (
            dbUpdate(GoalsModel)
            .where(GoalsModel.id == update_goals_input.id)
            .values(**update_goals_dict)
        )
        try:
            logger.info("update goals ")
            result = self.db.execute(stmt)
            self.db.flush()
            self.db.commit()

        except IntegrityError:
            self.db.rollback()
            logger.info("error log")
            return None
        except SQLAlchemyError as exc:
            logger.error(
                f"Error updating existing relation of goal on database: error = {exc}"
            )
            self.db.rollback()
            raise ApplicationException(status_code=500, key="error doing something")
        finally:
            self.db.close()

        logger.info("update goals")
        return result
