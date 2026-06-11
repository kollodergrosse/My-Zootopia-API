import requests
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


def load_data(animal):
    """Loads data via API"""
    url = WEB_URL + animal
    response = requests.get(url, headers={"X-API-Key": "ZTT5l5Oxc2AGbxCm04MuiBS6zIjFpATPhkncljVe"})
    data = response.json()
    print(data)
    return data


def serialize_animal(animals_data):
    """creates an HTML string of the animals data"""
    output = ""
    for animal in animals_data:
        try:
            output += '<li class="cards__item">'
            output += f'<div class="card__title">{animal.get("name")}</div>'
            output += '<p class="card__text">'
            output += f'<strong>Diet:</strong> {animal.get("characteristics", {}).get("diet")}<br/>\n'
            output += f'<strong>Location:</strong> {animal.get("locations")[0]}<br/>\n'
            output += f'<strong>Type:</strong> {animal.get("characteristics").get("type")}<br/>\n'
            output += "</p>\n"
            output += "</li>\n"

        except KeyError as e:
            continue

    return output


def main():
    """manages the functionality of the web generator"""
    animals_data = load_data("fox")
    animal_data_string = serialize_animal(animals_data)
    html_code = load_html_template(animal_data_string)
    write_new_html(html_code)


if "__main__" == __name__:
    main()
