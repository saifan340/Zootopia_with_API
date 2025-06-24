import json

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

def serialize_animal(animal_obj):
    """ Loops through the animal info and creates outputs for the cards in the HTML page """
    output =''
    if animal_obj:
           output +=f'<li class="cards__item">\n'
           if 'name' in animal_obj:
               name = animal_obj['name'].upper()
               output += f"<div class=\"card__title\">{name}</div>\n"
           output += f'<p class="card__text">\n'
           if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
               output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"
           if 'locations' in animal_obj:
               locations=animal_obj["locations"]
               output += f"<strong>Location:</strong> {locations[0]}<br/>\n"
           if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
               output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n"
           output += '</p>'
           output += '</li>'
    return output

def main():
    data = load_data('animals_data.json')
    output=''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    generate_animals_html(output)

if __name__ == '__main__':
    main()

