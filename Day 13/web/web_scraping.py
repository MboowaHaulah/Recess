
import requests
import csv
import json
from bs4 import BeautifulSoup




# Function to extract bird species from the website
def extract_bird_species():
    url = 'https://xeno-canto.org/collection/species/latest'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        species_data = []
        for row in soup.select('table.results tr'):
            common_name = row.select_one('span.common-name')
            sci_name = row.select_one('span.sci-name')
            if common_name and sci_name:
                species_data.append({
                    'common_name': common_name.text.strip(),
                    'species_name': sci_name.text.strip()
                })
        return species_data
    else:
        print('Failed to fetch data from the website.')
        return []

# Function to generate CSV file
def generate_csv(data):
    csv_filename = 'bird_species.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['common_name', 'species_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Function to generate JSON file
def generate_json(data):
    json_filename = 'bird_species.json'
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    bird_species_data = extract_bird_species()
    if bird_species_data:
        generate_csv(bird_species_data)
        generate_json(bird_species_data)
        print('CSV and JSON files generated successfully.')
