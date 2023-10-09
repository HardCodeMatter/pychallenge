import argparse
from random import randint


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('start', help='Start new game')
    parser.add_argument('--attempt', type=int, help='Attempt of guessing.')
    parser.add_argument('--between', type=int, help='Range FROM.', default=1)
    parser.add_argument('--to', type=int, help='Range TO', default=3)

    args = parser.parse_args()

    if args.start:
        if args.attempt is not None:
            target: int = randint(args.between, args.to)
            print(f'Target is between {args.between} and {args.to}.')

            i: int = 0
            while args.attempt > i:
                number: int = int(input(f'Enter the target number [{i + 1}/{args.attempt}]: '))

                if number >= args.between and number <= args.to:
                    if number > target:
                        print('Don\'t guess! Your answer is MORE than target.')
                    elif number < target:
                        print('Don\'t guess! Your answer is LESS than target.')
                    elif number == target:
                        print('You win! Your answer EQUAL to target.')
                        break

                i += 1
            else:
                print('You lose! You don\'t guess target number.')
        else:
            print('ATTEMPT is required.')


if __name__ == '__main__':
    main()
