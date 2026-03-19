from datetime import timezone, timedelta
from tabulate import tabulate

ISRAEL_TZ = timezone(timedelta(hours=3))


def print_matches(matches, month_str):
    if not matches:
        print(f"\nNo matches found for {month_str}.\n")
        return

    print(f"\n⚽  European Home Matches — {month_str}")
    print("=" * 70)

    # Group by city
    by_city = {}
    for m in matches:
        by_city.setdefault(m["city"], []).append(m)

    for city in sorted(by_city.keys()):
        print(f"\n📍 {city}")
        print("-" * 60)

        rows = []
        for m in by_city[city]:
            date_il = m["date"].astimezone(ISRAEL_TZ)
            date_str = date_il.strftime("%d/%m/%Y")
            time_str = date_il.strftime("%H:%M")
            home = _short(m["home_team"])
            away = _short(m["away_team"])
            rows.append([date_str, time_str, home, "vs", away, m["competition"]])

        headers = ["Date", "Time (IL)", "Home", "", "Away", "League"]
        print(tabulate(rows, headers=headers, tablefmt="simple"))

    print(f"\nTotal: {len(matches)} matches in {len(by_city)} cities\n")


def _short(name):
    """Remove common suffixes for cleaner display."""
    for suffix in [" FC", " CF", " AC", " SC", " BC", " United", " City",
                   " Calcio", " Balompié", " de Fútbol"]:
        name = name.replace(suffix, "")
    return name.strip()
