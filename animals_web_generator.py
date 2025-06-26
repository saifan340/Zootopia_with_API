import json
import requests
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def generate_animals_html(output):
     with open("animals_template.html", "r") as file:
          html_content =file.read()
     updated_html_content =html_content.replace("__REPLACE_ANIMALS_INFO__", output)
     with open('animals_data.html', 'w') as file:
         file.write(updated_html_content)
     print("Animals data has been generated")

def serialize_animal(animals_data):
    """ Loops through the animal info and creates outputs for the cards in the HTML page """
    output =''
    if animals_data:
       # for animal in animals_data:
           output +=f'<li class="cards__item">\n'
           if 'name' in animals_data:
               name = animals_data['name'].upper()
               output += f"<div class=\"card__title\">{name}</div>\n"
           output += f'<p class="card__text">\n'
           if 'characteristics' in animals_data and 'diet' in animals_data['characteristics']:
               output += f"<strong>Diet:</strong> {animals_data['characteristics']['diet']}<br/>\n"
           if 'locations' in animals_data:
               locations=animals_data["locations"]
               output += f"<strong>Location:</strong> {locations[0]}<br/>\n"
           if 'characteristics' in animals_data and 'type' in animals_data['characteristics']:
               output += f"<strong>Type:</strong> {animals_data['characteristics']['type']}<br/>\n"
           output += '</p>'
           output += '</li>'
    return output

def main():
    animal_name = input('Enter the name of an animal: ')

    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': 'luW0O9X/K73+K1fUBJ0kGw==lkpJau798Isalh8o'})

    if response.status_code == requests.codes.ok:
        animals_data = response.json()

        if not animals_data:
            output = f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
            print(f" The animal \"{animal_name}\" doesn't exist.")
        else:
            output = ''
            for animal in animals_data:
                output += serialize_animal(animal)

        generate_animals_html(output)
    else:
        print("Error:", response.status_code, response.text)

if __name__ == '__main__':
    main()

