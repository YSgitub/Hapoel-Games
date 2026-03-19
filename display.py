from datetime import datetime, timezone, timedelta
from tabulate import tabulate

ISRAEL_TZ = timezone(timedelta(hours=3))


def print_matches(matches):
    """Print upcoming matches as a formatted table."""
    if not matches:
        print("\nלא נמצאו משחקים עתידיים.\n")
        return

    print("\n⚽  משחקים קרובים — הפועל תל אביב")
    print("━" * 55)

    rows = []
    for i, match in enumerate(matches, 1):
        date_utc = datetime.fromisoformat(match["utcDate"].replace("Z", "+00:00"))
        date_il = date_utc.astimezone(ISRAEL_TZ)

        date_str = date_il.strftime("%d/%m/%Y")
        time_str = date_il.strftime("%H:%M")

        home = match["homeTeam"]["shortName"] or match["homeTeam"]["name"]
        away = match["awayTeam"]["shortName"] or match["awayTeam"]["name"]
        competition = match["competition"]["name"]

        if match["homeTeam"]["id"] == 11163:
            opponent = f"{away} (בית)"
        else:
            opponent = f"{home} (חוץ)"

        rows.append([i, date_str, time_str, opponent, competition])

    headers = ["#", "תאריך", "שעה", "יריב", "תחרות"]
    print(tabulate(rows, headers=headers, tablefmt="simple"))
    print()
