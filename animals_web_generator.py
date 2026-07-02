import sys


def load_html_template(html_string):
    """loads the HTML template code from a file and replaces the placeholder with the actual HTML code"""
    with open("animals_template.html", "r") as template:
        template = template.read()
        website_text_animals = template.replace("__REPLACE_ANIMALS_INFO__", html_string)
        return website_text_animals


def write_error_html_message(animal):
    with open("animals.html", "w") as website:
        website.write(f'<h2>The animal "{animal}" is not existing.</h2>')
        sys.exit()


def write_new_html(html_string):
    """writes the HTML code to a new file"""
    with open("animals.html", "w") as website:
        website.write(html_string)
        return True


def serialize_animal(animals_data):
    """creates an HTML string of the animals data"""
    output = ""
    for animal in animals_data:
        try:
            output += f"""
            <li class="cards__item">
                <div class="card__title">{animal['name']}</div>
                <p class="card__text">
                    <strong>Diet:</strong> {animal['characteristics']['diet']}<br/>
                    <strong>Location:</strong> {animal.get('locations', None)}<br/>
                    <strong>Type:</strong> {animal['characteristics']['type']}<br/>
                </p>
            </li>
            """

        except KeyError:
            continue

    return output



