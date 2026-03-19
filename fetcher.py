import requests
from datetime import datetime, timezone
from config import FOOTBALL_API_KEY, HAPOEL_TEL_AVIV_ID, BASE_URL


def get_upcoming_matches(limit=None):
    """Fetch upcoming matches for Hapoel Tel Aviv from football-data.org."""
    if not FOOTBALL_API_KEY:
        raise ValueError(
            "חסר API key. צור קובץ .env עם השורה:\n  FOOTBALL_API_KEY=your_key_here\n"
            "הירשם חינם בכתובת: https://www.football-data.org/client/register"
        )

    url = f"{BASE_URL}/teams/{HAPOEL_TEL_AVIV_ID}/matches"
    params = {"status": "SCHEDULED"}
    headers = {"X-Auth-Token": FOOTBALL_API_KEY}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 401:
        raise ValueError("API key שגוי. בדוק את הקובץ .env")
    if response.status_code == 404:
        raise ValueError("לא נמצא מידע על הקבוצה. בדוק את מזהה הקבוצה.")
    if response.status_code != 200:
        raise ValueError(f"שגיאה בשליפת נתונים: {response.status_code} {response.text}")

    data = response.json()
    matches = data.get("matches", [])

    now = datetime.now(timezone.utc)
    upcoming = [m for m in matches if _parse_date(m) >= now]
    upcoming.sort(key=_parse_date)

    if limit:
        upcoming = upcoming[:limit]

    return upcoming


def _parse_date(match):
    date_str = match.get("utcDate", "")
    return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
