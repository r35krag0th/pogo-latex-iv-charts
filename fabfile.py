from invoke import task
import os
import requests

GAMEMASTER_FILES = [
    "https://cdn.rawgit.com/pokemongo-dev-contrib/pokemongo-json-pokedex/4ffd90b0/output/pokemon.json",
    "https://cdn.rawgit.com/pokemongo-dev-contrib/pokemongo-json-pokedex/4ffd90b0/output/avatar-customization.json",
    "https://cdn.rawgit.com/pokemongo-dev-contrib/pokemongo-json-pokedex/4ffd90b0/output/move.json",
    "https://cdn.rawgit.com/pokemongo-dev-contrib/pokemongo-json-pokedex/4ffd90b0/output/type.json"
]


@task
def download_gamemaster_data(ctx):
    for file in GAMEMASTER_FILES:
        filename = os.path.split(file)[-1]
        response = requests.get(file)
        with open(os.path.join('data', filename), 'w') as fp:
            fp.write(response.text)

