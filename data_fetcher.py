import requests
import animals_web_generator


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
  url = main.WEB_URL + animal_name
  response = requests.get(url, headers={"X-API-Key": "ZTT5l5Oxc2AGbxCm04MuiBS6zIjFpATPhkncljVe"})
  data = response.json()
  if data == []:
      main.write_error_html_message(animal_name)

  else:
      return data