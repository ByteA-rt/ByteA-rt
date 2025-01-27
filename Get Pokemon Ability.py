import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException, HTTPError, ConnectionError
from urllib3.util.retry import Retry

def get_pokemon_ability(ability_id):
    try:
        # creates a persistant session object as PokeAPI only has HTTP GET available on resources
        session = requests.Session()

        #Retries failed connection up to 3 times and confirms the wait time between retries
        #retry = Retry(connect=3, backoff_factor=0.5)

        # Handles the low-level details of how requests are made
        #adapter = HTTPAdapter(max_retries=retry)
        adapter = HTTPAdapter()

        #Tells the session to use this adaptor for http and https requests
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        #Creates the API URL to insert ability_id        
        api = f"https://pokeapi.co/api/v2/ability/{ability_id.lower()}/"
        
        #Makes the get response using the above defined session
        response = session.get(api)
        #response.raise_for_status()

        #Takes the API response and converts from JSON format to Python dictionary
        pokemon_data = response.json()

        #Creates a new dictionary and takes specific peices of data from the laterger pokemon_data library
        pokemon_info = {
            "identification": pokemon_data["id"],
            "nameof": pokemon_data["name"],
            "Originated from main series" : pokemon_data["is_main_series"],
            #"Pokemons" : pokemon_data["pokemon"]
            "Pokemons": [],
            "Website" : []
        }

        # Loop collects all pokemon names
        # i is each item in the list of pokemon data
        # i["pokemon"]["name"] gets just the name
        # Adds each name to the Pokemon list
        for i in pokemon_data["pokemon"]:
            pokemon_info["Pokemons"].append(i["pokemon"]["name"])

        # Loop collects all pokemon URL
        # i is each item in the list of pokemon data
        # i["pokemon"]["url"] gets just the URL
        # Adds each URL to the Website  list
        for j in pokemon_data["pokemon"]:
            pokemon_info["Website"].append(j["pokemon"]["url"])

        #Returns dictionary created
        return pokemon_info
    
    # Catches specific connection related errors
    except ConnectionError as conn_err: 
            print(f'Connection Error! {conn_err}.')

    #Catches HTTP specific errors
    except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')

pokemon_ability = input("Enter the pokemon ability: ")

#Calls the function amd returns that dictionary
pokemon_info = get_pokemon_ability(pokemon_ability)

#Calls the function amd prints that dictionary
print (get_pokemon_ability(pokemon_ability))

print(pokemon_info)
