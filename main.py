import argparse
import sys
from datetime import datetime
from fetcher import get_matches_by_city
from display import print_matches


def cmd_fetch(args):
    month = args.month or datetime.now().strftime("%Y-%m")
    cities = args.cities or None

    try:
        _validate_month(month)
        matches = get_matches_by_city(month, cities)
        print_matches(matches, month)
    except ValueError as e:
        print(f"\nError: {e}\n", file=sys.stderr)
        sys.exit(1)


def _validate_month(month_str):
    try:
        datetime.strptime(month_str, "%Y-%m")
    except ValueError:
        raise ValueError(f"Invalid month format: '{month_str}'. Use YYYY-MM, e.g. 2026-04")


def main():
    parser = argparse.ArgumentParser(
        description="European football home matches by city and month"
    )
    subparsers = parser.add_subparsers(dest="command")

    fetch = subparsers.add_parser("fetch", help="List home matches for a given month")
    fetch.add_argument(
        "--month", metavar="YYYY-MM",
        help="Month to scan (default: current month)"
    )
    fetch.add_argument(
        "--cities", nargs="+", metavar="CITY",
        help="Filter by city, e.g. --cities London Madrid Munich"
    )

    args = parser.parse_args()

    if args.command == "fetch":
        cmd_fetch(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
