import logging
from pathlib import Path

import click
import spotipy
from dotenv import find_dotenv, load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials


def populate_db(sp, input_filepath, output_filepath):
    playlists = sp.user_playlists("spotify")
    output_filepath = Path(output_filepath) / "spotify.csv"
    with open(output_filepath, "w") as f:
        for playlist in playlists["items"]:
            if playlist["owner"]["id"] == "spotify":
                print(playlist["name"])
                results = sp.playlist(playlist["id"], fields="tracks,next")
                tracks = results["tracks"]
                for item in tracks["items"]:
                    track = item["track"]
                    f.write(
                        f"{track['artists'][0]['name']},{track['name']},{track['popularity']}\n"
                    )
                while tracks["next"]:
                    tracks = sp.next(tracks)
                    for item in tracks["items"]:
                        track = item["track"]
                        f.write(
                            f"{track['artists'][0]['name']},{track['name']},{track['popularity']}\n"
                        )
    return


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath, output_filepath):
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")

    # Authenticate with Spotify API
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    populate_db(sp, input_filepath, output_filepath)


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = Path(__file__).resolve().parents[2]

    load_dotenv(find_dotenv())

    main()
