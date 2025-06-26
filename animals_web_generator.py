import data_fetcher

def generate_animals_html(output):
    """Reads the HTML template and writes the final HTML file"""
    with open('animals_template.html', 'r') as file:
        html_content = file.read()

    updated_html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output)

    with open('animals.html', 'w') as file:
        file.write(updated_html_content)

    print("animals.html generated successfully")

def serialize_animal(animal):
    """Turns one animal dict into a card"""
    output = '<li class="cards__item">\n'
    if 'name' in animal:
        name = animal['name'].upper()
        output += f"<div class=\"card__title\">{name}</div>\n"
    output += '<p class="card__text">\n'
    if 'characteristics' in animal:
        if 'diet' in animal['characteristics']:
            output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
        if 'type' in animal['characteristics']:
            output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
    if 'locations' in animal and animal['locations']:
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
    output += '</p>\n</li>\n'
    return output

def main():
    animal_name = input('Enter the name of an animal: ')
    animals_data = data_fetcher.fetch_data(animal_name)

    if not animals_data:
        output = f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
    else:
        output = ''
        for animal in animals_data:
            output += serialize_animal(animal)

    generate_animals_html(output)

if __name__ == '__main__':
    main()
