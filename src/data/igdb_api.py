import json
import sys

from igdb.wrapper import IGDBWrapper
from igdb_api_token import IGDBAccessToken

sys.path.append("src")
from constants import EXCLUDED_FIELDS


def get_all_games_features():
    features = []

    with open("data/external/igdb_games.json") as f:
        games = json.load(f)
        for game in games:
            features.extend(game.keys())

    return sorted(set(features))


def get_all_games(
    client_id,
    app_access_token,
    exclude=EXCLUDED_FIELDS,
    endpoint="games",
    fields="*",
    limit=500,
):
    offset = 0
    all_games = []

    print("Getting games from IGDB API...")

    while True:
        wrapper = IGDBWrapper(client_id, app_access_token)
        byte_array = wrapper.api_request(
            endpoint,
            f'fields {fields}; offset {offset}; limit {limit}; exclude {",".join(exclude)};',
        )

        # Parse into JSON
        game_data = json.loads(byte_array.decode("utf-8"))

        # Break if no more games are returned by the API
        if not game_data:
            break

        all_games.extend(game_data)

        # Increment the offset by the limit
        offset += limit

    print(f"Found {len(all_games)} games.")

    return all_games


def save_games_to_file(game_data, filename):
    with open(filename, "w") as outfile:
        json.dump(game_data, outfile)


def main(external_data_path):
    token_manager = IGDBAccessToken()
    access_token = token_manager.get_token()

    game_data = get_all_games(token_manager.client_id, access_token)
    save_games_to_file(game_data, f"{external_data_path}")


if __name__ == "__main__":
    # main()
    print(get_all_games_features())
    print(len(get_all_games_features()))
