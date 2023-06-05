# constants.py

# ? enums

AGE_RATINGS = {
    1: "ESRB",
    2: "PEGI",
    3: "CERO",
    4: "USK",
    5: "GRAC",
    6: "CLASS_IND",
    7: "ACB",
}

GENDER = {
    0: "Male",
    1: "Female",
    2: "Other",
}

SPECIES = {
    1: "Human",
    2: "Alien",
    3: "Animal",
    4: "Android",
    5: "Unknown",
}

CATEGORY = {
    0: "Main Game",
    1: "DLC / Addon",
    2: "Expansion",
    3: "Bundle",
    4: "Standalone Expansion",
    5: "Mod",
    6: "Episode",
    7: "Season",
    8: "Remake",
    9: "Remaster",
    10: "Expanded Game",
    11: "Port",
    12: "Fork",
    13: "Pack",
    14: "Update",
}

STATUS = {
    0: "Released",
    2: "Alpha",
    3: "Beta",
    4: "Early Access",
    5: "Offline",
    6: "Cancelled",
    7: "Rumored",
    8: "Delisted",
}

PLATFORM = {
    1: "Console",
    2: "Arcade",
    3: "Platform",
    4: "Operating System",
    5: "Portable Console",
    6: "Computer",
}

REGION = {
    1: "Europe",
    2: "North America",
    3: "Australia",
    4: "New Zealand",
    5: "Japan",
    6: "China",
    7: "Asia",
    8: "Worldwide",
    9: "Korea",
    10: "Brazil",
}

# ? fields
EXCLUDED_FIELDS = [
    "alternative_names",
    "artworks",
    "checksum",
    "cover",
    "created_at",
    "follows",
    "forks",
    "hypes",
    "keywords",
    "multiplayer_modes",
    "player_perspectives",
    "ports",
    "first_release_date",
    "screenshots",
    "slug",
    "storyline",
    "summary",
    "tags",
    "themes",
    "updated_at",
    "url",
    "version_title",
    "videos",
    "websites",
]
