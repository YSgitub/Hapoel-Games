import os
from dotenv import load_dotenv

load_dotenv()

FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY", "")
HAPOEL_TEL_AVIV_ID = 11163  # Hapoel Tel Aviv FC on football-data.org
BASE_URL = "https://api.football-data.org/v4"
