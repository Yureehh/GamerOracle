import os
import time

import requests
from dotenv import load_dotenv


class IGDBAccessToken:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Get environment variables
        self.client_id = os.getenv("GAMERORACLE_CLIENT_ID")
        self.client_secret = os.getenv("GAMERORACLE_CLIENT_SECRET")

        self.token_url = "https://id.twitch.tv/oauth2/token"
        self.access_token = None
        self.expires_at = 0

        # Get token at initialization
        self.get_token()

    def get_token(self):
        if self.access_token is None or time.time() > self.expires_at:
            self.refresh_token()
        return self.access_token

    def refresh_token(self):  # sourcery skip: raise-specific-error
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
        }

        response = requests.post(self.token_url, params=payload)

        if response.status_code != 200:
            raise Exception(
                f"Failed to refresh access token: {response.content}"
            )
        token_data = response.json()
        self.access_token = token_data["access_token"]
        self.expires_at = time.time() + token_data["expires_in"]
