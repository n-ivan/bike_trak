import json
import matplotlib.pyplot as plt
import geopandas as gpd
import datetime

origin = [-79.619477, 43.577577]
end = [-79.12864, 43.84830]

def draw_to_png():
    df = gpd.read_file('data/rides.json')
    df.plot(color='black', linewidth=0.5)
    plt.axis("off")
    date = datetime.datetime.now().date().strftime("%Y-%m-%d")
    plt.savefig(f'pics/{date}.png',format='PNG', dpi=700)

def draw_to_png_fixed():
    df = gpd.read_file('data/rides.json')
    df.plot(color='black', linewidth=0.5)
    plt.ylim(43.577577, 43.84830)
    plt.xlim(-79.61947, -79.12864)
    plt.axis("off")
    date = datetime.datetime.now().date().strftime("%Y-%m-%d")
    plt.savefig(f"pics/{date}_fixed.png",format="PNG", dpi=700)  

def draw_to_png_tight():
    df = gpd.read_file('data/rides.json')
    df.plot(color='black', linewidth=0.5)
    plt.axis("off")
    date = datetime.datetime.now().date().strftime("%Y-%m-%d")
    plt.tight_layout()
    plt.savefig(f"pics/{date}_tight.png", format='PNG', dpi=700)
