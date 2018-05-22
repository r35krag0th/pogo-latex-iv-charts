import json

from pylatex import Document, Section, MultiColumn, LineBreak, Tabular, TextColor
from pogoiv import Pokemon

DATAFILE = 'data/pokemon.json'

def rgb_to_dumb_string(r, g, b):
    xr = r / 255.0
    xg = g / 255.0
    xb = b / 255.0

    return f'{xr:0.2f}, {xg:0.2f}, {xb:0.2f}'


def color_by_iv(iv):
    if (iv == 100):
        return 'color100'
    elif (iv == 98):
        return 'color98'
    elif (iv == 96):
        return 'color96'
    elif (iv == 93):
        return 'color93'
    elif (iv == 91):
        return 'color91'
    else:
        return 'color91'


def compute_all_combinations(pokemon, level=20):
    output = []

    for attack in range(10, 16):
        for defense in range(10, 16):
            for stamina in range(10, 16):
                iv = pokemon.iv_from_stats(level, attack, defense, stamina)
                if (iv.perfection_percent >= 93 and attack in [13, 14, 15]) or (attack == 10 and defense == 10 and stamina == 10):
                    output.append(iv)

    output.sort(key=lambda x: x.cp, reverse=True)

    return output


def create_latex_iv_table(doc, name, list_of_ivs):
    with doc.create(Section(name)):
        for iv in list_of_ivs:
            doc.append(f'{iv.attack}/')


def create_latex_file(pokemon, list_of_normal_ivs, list_of_boosted_ivs):
    geometry_options = {
        "landscape": True,
        "margin": "0.5in",
        "headheight": "20pt",
        "headsep": "10pt",
        "includeheadfoot": True
    }

    doc = Document(page_numbers=True, geometry_options=geometry_options)

    doc.add_color('color100', 'rgb', rgb_to_dumb_string(0, 207, 194))
    doc.add_color('color98', 'rgb', rgb_to_dumb_string(60, 141, 1))
    doc.add_color('color96', 'rgb', rgb_to_dumb_string(72, 165, 6))
    doc.add_color('color93', 'rgb', rgb_to_dumb_string(242, 183, 8))
    doc.add_color('color91', 'rgb', rgb_to_dumb_string(246, 96, 0))

    section = Section(f'{pokemon.name} IV Chart')

    table = Tabular('|c|c|c|c|c|c|', row_height=1.5)
    table.add_hline()
    table.add_row(
        (
            MultiColumn(6, align='|c|', data=TextColor('white', pokemon.name), color='black'),
        ),
    )

    table.add_row((
        MultiColumn(1, align='|c', data='Lv20'),
        MultiColumn(1, align='c|', data='Lv25'),
        MultiColumn(3, align='c|', data='IV'),
        MultiColumn(1, align='|c|', data='%')
    ))

    for index in range(len(list_of_normal_ivs)):
        n_iv = list_of_normal_ivs[index]
        b_iv = list_of_boosted_ivs[index]

        row_data = (
            f'{n_iv.cp}',
            f'{b_iv.cp}',
            f'{n_iv.attack}',
            f'{n_iv.defense}',
            f'{n_iv.stamina}',
            f'{n_iv.perfection_percent_rounded}'
        )

        table.add_hline()
        table.add_row(
            row_data,
            color=color_by_iv(n_iv.perfection_percent_rounded)
        )

    section.append(table)
    doc.append(section)

    doc.generate_tex(f'latex/{pokemon.name}')
    doc.generate_pdf(f'pdf/{pokemon.name}')

if __name__ == '__main__':
    json_data = json.load(open(DATAFILE, 'r'))

    for poke_data in json_data:
        pokemon = Pokemon.from_json(poke_data)
        normal_ivs = compute_all_combinations(pokemon, 20)
        boosted_ivs = compute_all_combinations(pokemon, 25)

        create_latex_file(pokemon, normal_ivs, boosted_ivs)