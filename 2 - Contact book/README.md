# Contact Book in bash

## Stack

`Python == 3.11.4`

`argparse == 3.12.0`

`SQLAlchemy == 2.0.21`

## Using

Create new contact:

`python3 main.py create --name [STRING] -- phone [NUMBER] --is_favorite [TRUE/FALSE]`

Show all contact's list:

`python3 main.py list`

Show limited contact's list:

`python3 main.py list --limit [NUMBER]`

Search by id:

`python3 main.py search --id [NUMBER]`
