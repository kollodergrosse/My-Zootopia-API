import requests
import os
import animals_web_generator
from dotenv import load_dotenv

load_dotenv()

WEB_URL = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = os.getenv("API_KEY")

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  url = WEB_URL + animal_name
  response = requests.get(url, headers={"X-API-Key": API_KEY})
  data = response.json()
  if data == []:
      animals_web_generator.write_error_html_message(animal_name)

  else:
      return data