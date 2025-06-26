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

def serialize_animal(animal_name,animals_data):
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
    """data = load_data('animals_data.json')
    output=''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    generate_animals_html(output)"""




animal_name = input('Enter a name of an animal: ')
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
animals_data = requests.get(api_url, headers={'X-Api-Key': 'luW0O9X/K73+K1fUBJ0kGw==lkpJau798Isalh8o'})
if animals_data.status_code == requests.codes.ok:
    print(animals_data.text)
else:
    print("Error:", animals_data.status_code, animals_data.text)
output = serialize_animal(animals_data, animal_name)
if __name__ == '__main__':
    main()

