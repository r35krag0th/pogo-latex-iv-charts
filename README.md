# Pokémon Go - IV Chart Generator

Something quick and dirty I made for my own needs.  This project uses GAMEMASTER data from Pokémon Go Dev's Contribs that has been normalized.  It will then make LaTeX and PDF copies of the IV chart.

## Installation

You might need to install pipenv.

```sh
# Checkout the code and "cd" to directory
$ pipenv install

# Probably good to install those dev deps if you're going to run this
$ pipenv install -d
```

### LaTeX and PDFs
You'll need to have LaTeX installed.  Since I already use TexPad, I've got MacTex installed.  So you will want to make sure that `/Library/TeX/texbin` is in your `$PATH`.

## Usage

Generated LaTeX files go in `latex/POKEMON_NAME.tex`, and PDF files go in `pdf/POKEMON_NAME.pdf`.  This will generate data for ALL pokemon contained in the GAMEMASTER dumps.  So this can take a short bit.

If you've not recently updated the GAMEMASTER data.  You should run `fab download-gamemaster-data` from the project root.

```sh
# ==> From the project root
# --> NOTE: Only if you're not inside a "pipenv shell" session
$ pipenv run python app.py
```
