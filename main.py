import argparse
import sys
from fetcher import get_upcoming_matches
from display import print_matches


def cmd_fetch(args):
    try:
        matches = get_upcoming_matches(limit=args.next)
        print_matches(matches)
    except ValueError as e:
        print(f"\n❌  {e}\n", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="מעקב משחקים — הפועל תל אביב"
    )
    subparsers = parser.add_subparsers(dest="command")

    fetch_parser = subparsers.add_parser("fetch", help="הצג משחקים עתידיים")
    fetch_parser.add_argument(
        "--next", type=int, metavar="N",
        help="הצג רק N משחקים הקרובים"
    )

    args = parser.parse_args()

    if args.command == "fetch":
        cmd_fetch(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
