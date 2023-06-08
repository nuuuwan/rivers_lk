from json import dumps

import shapefile

from src.rivers_lk._common import GEOJSON_PATH, SHP_PATH

def main():
    # read the shapefile
    reader = shapefile.Reader(SHP_PATH)
    fields = reader.fields[1:]
    field_names = [field[0] for field in fields]
    buffer = []
    for sr in reader.shapeRecords():
        atr = dict(zip(field_names, sr.record))
        geom = sr.shape.__geo_interface__
        buffer.append(dict(type="Feature", geometry=geom, properties=atr))

    # write the GeoJSON file
    geojson = open(GEOJSON_PATH, "w")
    geojson.write(
        dumps({"type": "FeatureCollection", "features": buffer}, indent=2)
        + "\n"
    )
    geojson.close()


if __name__ == "__main__":
    main()
