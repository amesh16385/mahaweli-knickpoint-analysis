import rasterio
import matplotlib.pyplot as plt
import numpy as np

dem_path = 'data/mahaweli_dem.tif'

with rasterio.open(dem_path) as src:
    elevation = src.read(1)
    extent = [src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top]

    # 1. ඉතාම පහත් ම මිටියාවත් (ගංගා යහන් මාවත පමණක්) තෝරා ගැනීමට දැඩි සීමාවක් (Strict threshold) යෙදීම
    min_el = np.nanmin(elevation)
    max_el = np.nanmax(elevation)
    
    # 25 වෙනුවට 0.03 (සියයට 3ක් වැනි ඉතාම පහත් ම ගැඹුරුම ප්‍රදේශ පමණක්)
    river_mask = (elevation >= min_el) & (elevation <= (min_el + (max_el - min_el) * 0.04))

    # 2. බෑවුම ගණනය කිරීම
    dy, dx = np.gradient(elevation)
    slope = np.sqrt(dx**2 + dy**2)

    # 3. ගංගා මාවතට පමණක් බෑවුම සීමා කිරීම
    river_knicks = np.where(river_mask, slope, np.nan)

    # 4. සිතියම ඇඳීම
    fig, ax = plt.subplots(figsize=(8, 6))

    # පසුබිම් භූමිය පෙන්වීම
    ax.imshow(elevation, cmap='terrain', extent=extent, alpha=0.5)

    # හරියටම ගඟ ඇතුළේ ඇති Knickpoints තදින් පෙන්වීම
    im = ax.imshow(river_knicks, cmap='jet', extent=extent, alpha=1.0)
    
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Precise River Knickpoints Intensity')

    plt.title("Precise Mahaweli River Channel Knickpoints", fontsize=12, fontweight='bold')
    plt.xlabel("X Coordinate (Longitude)")
    plt.ylabel("Y Coordinate (Latitude)")
    
    plt.tight_layout()
    plt.savefig('mahaweli_knickpoints.png', dpi=300, bbox_inches='tight')