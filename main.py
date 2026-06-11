import sys
import data_fetcher
import animals_web_generator


def main():
    """manages the functionality of the web generator and gets the animal selection from the user"""
    user_animal_selection = input("Enter a name of an animal: ")
    animals_data = data_fetcher.(user_animal_selection)
    animal_data_string = animals_web_generator.(animals_data)
    html_code = animals_web_generator.(animal_data_string)
    write_website_success = animals_web_generator.(html_code)
    if write_website_success:
        print("Website was successfully generated to the file animals.html.")

    sys.exit()


if "__main__" == __name__:
    main()