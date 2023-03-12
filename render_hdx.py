import geopandas as gpd
import matplotlib.pyplot as plt

df = gpd.read_file('data/hdx/lka_rapidsl_rvr_250k_sdlka.geo.json')
df.plot(figsize=(10,10), aspect=1,edgecolor=(0,0.2,0.6),linewidth=0.4)
plt.show()
