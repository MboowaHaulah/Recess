# import requests
# from bs4 import BeautifulSoup

# url = 'http://xeno.canto.org'
# response = requests.get(url)

# # GET TITLE OF THE WEBSITE
# soup = BeautifulSoup(response.content, 'html.parser')

# title = soup.find('title')

# print(title.text)


#EXERCISE
#-EXTRACT ALL BIRD SPECIES FROM THIIS WEBSITE AND GENERATE A CSV FILE FOR THE BIRD SPECIES
#use this API to get data . The endpoint for the web service is at 
#http://xeno.canto.org/api/2/recordings.


import requests
import csv
import json
from bs4 import BeautifulSoup

#API 
'https://xeno-canto.org/collection/species/latest'

#I also extracted a json file for further referal of my work

#EXTRACTION OF INFO
def extract_bird_species():
    url = 'https://xeno-canto.org/collection/species/latest'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        species_data = []
        for row in soup.select('table.results tr'):
            species_name = row.select_one('span.common-name')
            AddedBy_name = row.select_one('span.sci-name')
            if species_name and AddedBy_name:
                species_data.append({
                    'species_name': species_name.text.strip(),
                    'AddedBy_name': AddedBy_name.text.strip()
                })
        return species_data
    else:
        print('Failed to fetch data .')
        return []

# Function to generate CSV file
def generate_csv(data):
    csv_filename = 'bird_species.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['species_name', 'AddedBy_name']
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
        print('CSV and JSON files were generated successfully.')
