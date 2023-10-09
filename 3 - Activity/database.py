from typing import Iterable
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

import config
from models import Activity


engine = create_engine(
    url=config.SQLALCHEMY_URL, 
    echo=config.SQLALCHEMY_ECHO
)


def save_activity(session: Session, **params: dict[str, str | int | float]) -> None:
    activity: Activity = Activity(**params)

    session.add(activity)
    session.commit()

def get_activities(session: Session, limit: int) -> list[dict[str, str | int | float]]:
    statement = select(Activity).order_by(Activity.id.desc()).limit(limit)
    activities: Iterable[Activity] = session.scalars(statement)

    return activities
