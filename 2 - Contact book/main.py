import argparse
from sqlalchemy.orm import Session

from models import Contact
from database import engine
from database import create_contact, show_contacts, show_contact_by_id


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='cmd')

    create_parser = subparser.add_parser('create')
    create_parser.add_argument('--name', type=str)
    create_parser.add_argument('--phone', type=int)
    create_parser.add_argument('--is_favorite', type=bool)
    
    list_parser = subparser.add_parser('list')
    list_parser.add_argument('--limit', type=int)

    search_parser = subparser.add_parser('search')
    search_parser.add_argument('--id', type=int)

    args = parser.parse_args()

    if args.cmd == 'create':
        with Session(engine) as session:
            create_contact(
                session=session,
                name=args.name,
                phone=args.phone,
                is_favorite=args.is_favorite,
            )
            print(' [+] New contact was created.')
    elif args.cmd == 'list':
        with Session(engine) as session:
            contacts: list[Contact] = show_contacts(session=session, limit=args.limit)
            
            for contact in contacts:
                print(contact)
    elif args.cmd == 'search':
        with Session(engine) as session:
            contact: Contact = show_contact_by_id(session=session, contact_id=args.id)
            print(contact)


if __name__ == '__main__':
    main()
