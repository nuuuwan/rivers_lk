import colorsys

import geopandas as gpd
import matplotlib.pyplot as plt

ORIGINAL_PATH = 'data/hdx/lka_rapidsl_rvr_250k_sdlka.geo.json'
ANALYZED_PATH = 'data/hdx/lka_rapidsl_rvr_250k_sdlka.analyzed.geo.json'

LONGEST_RIVER_NAMES = [
    'Mahaweli Ganga',
    'Malwatu Oya',
    'Kala Oya',
    'Kelani Ganga',
    'Yan Oya',
    'Deduru Oya',
    'Welawe Ganga',
    'Maduru Oya',
    'Maha Oya',
    'Kalu Ganga',
]

NAME_MAP = {'Aruvi Aru': 'Malwatu Oya', 'Gallodai Aru': 'Maduru Oya'}


def get_name_to_color() -> dict:
    name_to_color = {}
    for i, name in enumerate(LONGEST_RIVER_NAMES):
        hue = i / len(LONGEST_RIVER_NAMES)
        sat = 0.5
        light = 0.5
        r, g, b = colorsys.hls_to_rgb(hue, light, sat)
        color = '#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))
        name_to_color[name] = color
    return name_to_color


NAME_TO_COLOR = get_name_to_color()


def get_color(name: str, code: int) -> str:
    if code != 1:
        return '#fcfcfc'
    name = NAME_MAP.get(name, name)
    return NAME_TO_COLOR.get(name, '#f8f8f8')


def main():
    df = gpd.read_file(ORIGINAL_PATH)
    colors = []
    data_list = df.to_dict('records')
    for d in data_list:
        name = d['NAME']
        code = d['CODE']
        color = get_color(name, code)
        colors.append(color)

        if name == 'Maha Oya':
            print(d)

    df['color'] = colors

    df.plot(figsize=(10, 10), aspect=1, linewidth=0.8, color=df['color'])
    plt.show()

    for name in sorted(NAME_TO_COLOR.keys()):
        print(name)


if __name__ == '__main__':
    main()
