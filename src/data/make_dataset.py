import logging
from pathlib import Path

import click
from dotenv import find_dotenv, load_dotenv
from igdb_api import main as populate_db


@click.command()
@click.argument("raw_input_filepath", type=click.Path(exists=True))
@click.argument("external_input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(raw_input_filepath, external_input_filepath, output_filepath):
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")
    populate_db(f"{external_input_filepath}/igdb_games.json")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = Path(__file__).resolve().parents[2]

    load_dotenv(find_dotenv())

    main()
