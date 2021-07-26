import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
ds = xr.open_mfdataset('*_summer_*.nc')
co2 = ds.co2.mean('time')
co2graph = co2.isel(level=0)
plt.figure(figsize= (12,4))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
co2graph.plot(cmap='coolwarm',vmax=440, vmin=390)
plt.title('summer 2010-18', pad=1)
plt.show()