import argparse
from sqlalchemy.orm import Session

from api import BoredAPI
from models import Base
from database import engine, save_activity, get_activities


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='cmd')

    new_parser = subparser.add_parser('new')
    new_parser.add_argument('--type', type=str)
    new_parser.add_argument('--participants', type=int)
    new_parser.add_argument('--price_min', type=float)
    new_parser.add_argument('--price_max', type=float)
    new_parser.add_argument('--accessibility_min', type=float)
    new_parser.add_argument('--accessibility_max', type=float)
    new_parser.add_argument('--key', type=str)

    list_parser = subparser.add_parser('list')
    list_parser.add_argument('--limit', type=int, default=5)

    args = parser.parse_args()

    api = BoredAPI()

    Base.metadata.create_all(bind=engine)
    
    if args.cmd == 'new':
        params: dict[str, str | int | float] = {
            'type': args.type,
            'participants': args.participants,
            'minprice': args.price_min,
            'maxprice': args.price_max,
            'minaccessibility': args.accessibility_min,
            'maxaccessibility': args.accessibility_max,
            'key': args.key,
        }

        with Session(engine) as session:
            activity: dict[str, str | int | float] = api.get_activity(**params)

            if activity:
                save_activity(session, **activity)
                print(repr(activity))

    if args.cmd == 'list':
        with Session(engine) as session:
            activities: list = get_activities(session, args.limit)

            for activity in activities:
                print(f'{activity}\n')


if __name__ == '__main__':
    main()
