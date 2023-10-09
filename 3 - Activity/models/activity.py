from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from models import Base

class Activity(Base):
    __tablename__ = 'activities'

    id: Mapped[int] = mapped_column(primary_key=True)
    activity: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    participants: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float)
    accessibility: Mapped[float] = mapped_column(Float)
    link: Mapped[str] = mapped_column(String)
    key: Mapped[str] = mapped_column(String)

    def __str__(self) -> str:
        return f'Activity(id={self.id}, activity={self.activity}, type={self.type}, participants={self.participants}, price={self.price}, accessibility={self.accessibility}, link={self.link}, key={self.key})'
    
    def __repr__(self) -> str:
        return str(self)
