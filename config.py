import os
from dotenv import load_dotenv

load_dotenv()

FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY", "")
BASE_URL = "https://api.football-data.org/v4"

# Competition codes supported by the free tier
LEAGUES = {
    "PL":  "Premier League (England)",
    "PD":  "La Liga (Spain)",
    "BL1": "Bundesliga (Germany)",
    "SA":  "Serie A (Italy)",
}

# Mapping: city → list of home team names (as they appear in football-data.org)
CITY_TEAMS = {
    # England
    "London": [
        "Arsenal FC", "Chelsea FC", "Tottenham Hotspur FC",
        "West Ham United FC", "Crystal Palace FC", "Fulham FC",
        "Brentford FC", "AFC Wimbledon",
    ],
    "Manchester": [
        "Manchester United FC", "Manchester City FC",
    ],
    "Liverpool": [
        "Liverpool FC", "Everton FC",
    ],
    "Birmingham": [
        "Aston Villa FC", "Birmingham City FC", "Wolverhampton Wanderers FC",
    ],
    "Newcastle": ["Newcastle United FC"],
    "Leeds": ["Leeds United FC"],
    "Leicester": ["Leicester City FC"],
    "Brighton": ["Brighton & Hove Albion FC"],
    "Southampton": ["Southampton FC"],
    "Nottingham": ["Nottingham Forest FC"],

    # Spain
    "Madrid": [
        "Real Madrid CF", "Club Atlético de Madrid", "Getafe CF",
        "Rayo Vallecano de Madrid", "CD Leganés",
    ],
    "Barcelona": ["FC Barcelona", "RCD Espanyol de Barcelona"],
    "Seville": ["Sevilla FC", "Real Betis Balompié"],
    "Valencia": ["Valencia CF", "Villarreal CF", "Levante UD"],
    "Bilbao": ["Athletic Club"],
    "San Sebastian": ["Real Sociedad de Fútbol"],

    # Germany
    "Munich": ["FC Bayern München", "TSV 1860 München"],
    "Dortmund": ["Borussia Dortmund"],
    "Frankfurt": ["Eintracht Frankfurt"],
    "Leipzig": ["RB Leipzig"],
    "Berlin": ["Hertha BSC", "1. FC Union Berlin"],
    "Hamburg": ["Hamburger SV", "FC St. Pauli"],
    "Stuttgart": ["VfB Stuttgart"],
    "Leverkusen": ["Bayer 04 Leverkusen"],
    "Bremen": ["Werder Bremen"],
    "Mönchengladbach": ["Borussia Mönchengladbach"],
    "Freiburg": ["SC Freiburg"],
    "Augsburg": ["FC Augsburg"],
    "Wolfsburg": ["VfL Wolfsburg"],
    "Bochum": ["VfL Bochum 1848"],
    "Hoffenheim": ["TSG 1899 Hoffenheim"],
    "Mainz": ["1. FSV Mainz 05"],
    "Cologne": ["1. FC Köln"],

    # Italy
    "Milan": ["AC Milan", "FC Internazionale Milano"],
    "Rome": ["AS Roma", "SS Lazio"],
    "Turin": ["Juventus FC", "Torino FC"],
    "Naples": ["SSC Napoli"],
    "Florence": ["ACF Fiorentina"],
    "Bologna": ["Bologna FC 1909"],
    "Genoa": ["Genoa CFC", "UC Sampdoria"],
    "Venice": ["Venezia FC"],
    "Bergamo": ["Atalanta BC"],
    "Verona": ["Hellas Verona FC", "AC ChievoVerona"],
    "Udine": ["Udinese Calcio"],
    "Lecce": ["US Lecce"],
    "Cagliari": ["Cagliari Calcio"],
    "Parma": ["Parma Calcio 1913"],
    "Como": ["Como 1907"],
    "Monza": ["AC Monza"],
}

# Build reverse mapping: team name → city (for fast lookup)
TEAM_TO_CITY = {
    team: city
    for city, teams in CITY_TEAMS.items()
    for team in teams
}
