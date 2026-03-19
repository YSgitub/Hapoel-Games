import requests
from datetime import datetime
from config import FOOTBALL_API_KEY, BASE_URL, LEAGUES, TEAM_TO_CITY


def get_matches_by_city(month_str, cities=None):
    """
    Fetch all home matches for the given month across all configured leagues,
    filtered by city.

    Args:
        month_str: "YYYY-MM" format, e.g. "2026-04"
        cities: list of city names to filter by, or None for all cities

    Returns:
        list of match dicts, each enriched with 'city' key
    """
    if not FOOTBALL_API_KEY:
        raise ValueError(
            "Missing API key. Create a .env file with:\n"
            "  FOOTBALL_API_KEY=your_key_here\n"
            "Register free at: https://www.football-data.org/client/register"
        )

    year, month = map(int, month_str.split("-"))
    date_from, date_to = _month_range(year, month)

    results = []
    headers = {"X-Auth-Token": FOOTBALL_API_KEY}

    for code, league_name in LEAGUES.items():
        url = f"{BASE_URL}/competitions/{code}/matches"
        params = {"dateFrom": date_from, "dateTo": date_to}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 401:
            raise ValueError("Invalid API key. Check your .env file.")
        if response.status_code == 403:
            raise ValueError(
                f"Access denied for {league_name}. "
                "This league may not be available on your plan."
            )
        if response.status_code != 200:
            print(f"Warning: could not fetch {league_name} ({response.status_code})")
            continue

        matches = response.json().get("matches", [])

        for match in matches:
            home_team = match["homeTeam"]["name"]
            city = TEAM_TO_CITY.get(home_team)

            if city is None:
                continue  # team not in our city map

            if cities and city.lower() not in [c.lower() for c in cities]:
                continue  # city not in filter

            results.append({
                "date": _parse_date(match),
                "home_team": home_team,
                "away_team": match["awayTeam"]["name"],
                "competition": league_name,
                "city": city,
                "status": match.get("status", ""),
            })

    results.sort(key=lambda m: m["date"])
    return results


def _month_range(year, month):
    import calendar
    last_day = calendar.monthrange(year, month)[1]
    return (
        f"{year:04d}-{month:02d}-01",
        f"{year:04d}-{month:02d}-{last_day:02d}",
    )


def _parse_date(match):
    date_str = match.get("utcDate", "")
    return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
