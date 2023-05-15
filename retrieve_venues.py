import requests
import argparse
from venue_db_management import Venue, create_database
from sqlalchemy import create_engine

import os
import json
from sqlmodel import Session

# As the v2 version is deprecated, I am not able to retrieve data using foursquare API but I am emplementing  
# this class which help to manage API
class FoursquareAPIManagement:
    def __init__(self, url, client_id, client_secret, version):
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.version = version

    def search_venues(self, lat, lng, radius, limit):
        endpoint = f"{self.url}/venues/search"
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "ll": f"{lat},{lng}",
            "radius": radius,
            "limit": limit,
            "v": self.version,
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        return data["response"]["groups"][0]["items"]


def collect_venues(args):

    # Extract relevant information from the JSON sample instead of foursquare API and insert into the database
    with open("file.json", encoding="utf-8") as file:
        data = json.load(file)

        venues = data["response"]["groups"][0]["items"][: args.num_venues]
        engine = create_engine("sqlite:///venues.db")
        with Session(engine) as session:
            for venue_data in venues:
                venue = Venue(
                    id=venue_data["venue"]["id"],
                    name=venue_data["venue"]["name"],
                    category=venue_data["venue"]["categories"][0]["name"],
                    address=venue_data["venue"]["location"].get("address"),
                    city=venue_data["venue"]["location"].get("city"),
                    country=venue_data["venue"]["location"].get("country"),
                    lat=venue_data["venue"]["location"].get("lat"),
                    lng=venue_data["venue"]["location"].get("lng"),
                )
                session.add(venue)
            session.commit()


parser = argparse.ArgumentParser()
parser.add_argument("address", help="Address argument")
parser.add_argument("num_venues", type=int, help="Num Venues argument")
parser.set_defaults(func=collect_venues)


def main():
    create_database()
    args = parser.parse_args()
    args.func(args)
