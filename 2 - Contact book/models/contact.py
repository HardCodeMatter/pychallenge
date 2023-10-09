from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from . import Base


class Contact(Base):
    __tablename__ = 'contact'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    phone: Mapped[int] = mapped_column(Integer)
    is_favorite: Mapped[bool] = mapped_column(Boolean)

    def __str__(self) -> str:
        return f"Contact #{self.id}:\n - name: {self.name}\n - phone: {self.phone}\n - favorite: {self.is_favorite}"
    
    def __repr__(self) -> str:
        return str(self)
