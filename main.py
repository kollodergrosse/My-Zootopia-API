import requests
import sys
WEB_URL = "https://api.api-ninjas.com/v1/animals?name="


def load_html_template(html_string):
    """loads the HTML template code from a file and replaces the placeholder with the actual HTML code"""
    with open("animals_template.html", "r") as template:
        template = template.read()
        website_text_animals = template.replace("__REPLACE_ANIMALS_INFO__", html_string)
        return website_text_animals


def write_new_html(html_string):
    """writes the HTML code to a new file"""
    with open("animals.html", "w") as website:
        website.write(html_string)
        sys.exit()


def load_data(animal):
    """Loads data via API"""

    url = WEB_URL + animal
    response = requests.get(url, headers={"X-API-Key": "ZTT5l5Oxc2AGbxCm04MuiBS6zIjFpATPhkncljVe"})
    data = response.json()
    if data == []:
        error_html_message = f'<h2>The animal "{animal}" is not existing.</h2>'
        write_new_html(error_html_message)

    else:
        return data


def serialize_animal(animals_data):
    """creates an HTML string of the animals data"""
    output = ""
    for animal in animals_data:
        try:
            output += '<li class="cards__item">'
            output += f'<div class="card__title">{animal["name"]}</div>'
            output += '<p class="card__text">'
            output += f'<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
            output += f'<strong>Location:</strong> {animal["locations"][0]}<br/>\n'
            output += f'<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'
            output += "</p>\n"
            output += "</li>\n"

        except KeyError as e:
            continue

    return output


def main():
    """manages the functionality of the web generator and gets the animal selection from the user"""
    user_animal_selection = input("Enter a name of an animal: ")
    animals_data = load_data(user_animal_selection)
    animal_data_string = serialize_animal(animals_data)
    html_code = load_html_template(animal_data_string)
    write_website_success = write_new_html(html_code)
    if write_website_success:
        print("Website was successfully generated to the file animals.html.")


if "__main__" == __name__:
    main()
