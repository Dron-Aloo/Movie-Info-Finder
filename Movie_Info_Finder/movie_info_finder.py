import requests
import os
from dotenv import load_dotenv

load_dotenv()  # reads the .env file and loads the variables into the environment

API_KEY = os.getenv("OMDB_API_KEY")  # fetches it from the environment

movie_name = input("Enter movie name: ")

url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    if data["Response"] == "True":
        print(f"\n🎬 Title       : {data['Title']}")
        print(f"📅 Year        : {data['Year']}")
        print(f"⭐ IMDb Rating : {data['imdbRating']}")
        print(f"🎭 Genre       : {data['Genre']}")
        print(f"👨‍👩‍👧‍👦 Actors      : {data['Actors']}")
        print(f"📝 Plot        : {data['Plot']}")
    else:
        print("Movie not found. Please check the title and try again.")
except requests.exceptions.Timeout:
    print("The request timed out. Please try again later.")
except requests.exceptions.ConnectionError:
    print("Network error. Please check your connection and try again.")
except requests.exceptions.HTTPError:
    print("HTTP error occurred. Please try again later.")
except requests.exceptions.RequestException:
    print("An error occurred while making the request. Please try again later.")