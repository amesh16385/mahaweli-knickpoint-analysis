import rasterio
import matplotlib.pyplot as plt
from rasterio.plot import show


dem_path = "Data/mahaweli_dem.tif"


with rasterio.open(dem_path) as src:
    print("DEM file is successfully execuated!")
    print(f"Size (Width x Height): {src.width} x {src.height}")
    print(f"coordinate system (CRS): {src.crs}")
    
    
    fig, ax = plt.subplots(figsize=(8, 6))
    show(src, ax=ax, cmap='terrain')  
    
    plt.title("Geology Research: Peradeniya DEM Elevation Map")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    
  
    plt.show()