import rasterio
import matplotlib.pyplot as plt
import numpy as np

dem_path = 'data/mahaweli_dem.tif'

with rasterio.open(dem_path) as src:
    elevation = src.read(1)
    extent = [src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top]


    min_el = np.nanmin(elevation)
    max_el = np.nanmax(elevation)
    
    river_mask = (elevation >= min_el) & (elevation <= (min_el + (max_el - min_el) * 0.04))

    
    dy, dx = np.gradient(elevation)
    slope = np.sqrt(dx**2 + dy**2)

    river_knicks = np.where(river_mask, slope, np.nan)

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.imshow(elevation, cmap='terrain', extent=extent, alpha=0.5)

    im = ax.imshow(river_knicks, cmap='jet', extent=extent, alpha=1.0)
    
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Precise River Knickpoints Intensity')

    plt.title("Precise Mahaweli River Channel Knickpoints", fontsize=12, fontweight='bold')
    plt.xlabel("X Coordinate (Longitude)")
    plt.ylabel("Y Coordinate (Latitude)")
    
    plt.tight_layout()
    plt.savefig('mahaweli_knickpoints.png', dpi=300, bbox_inches='tight')
