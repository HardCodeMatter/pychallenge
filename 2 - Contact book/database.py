from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

import config
from models import Base, Contact


engine = create_engine(config.SQLALCHEMY_URL, echo=config.SQLALCHEMY_ECHO)


def create_contact(session: Session, name: str, phone: int, is_favorite: bool) -> Contact:
    contact: Contact = Contact(
        name=name,
        phone=phone,
        is_favorite=is_favorite,
    )
    session.add(contact)
    session.commit()

def show_contacts(session: Session, limit: int) -> list[Contact]:
    statement = select(Contact).limit(limit)
    contacts: list[Contact] = session.scalars(statement)

    return contacts

def show_contact_by_id(session: Session, contact_id: int) -> Contact:
    statement = select(Contact).where(Contact.id == contact_id)
    contact: Contact | None = session.scalar(statement)
    
    return contact


def database():
    Base.metadata.create_all(bind=engine)


database()
