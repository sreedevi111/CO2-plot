import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
ds = xr.open_mfdataset('*_summer_*.nc')
co2 = ds.co2.mean('time')
co2graph = co2.isel(level=0)
ax = plt.axes(projection=ccrs.PlateCarree())
#ax = co2graph.plot( cmap='jet', extend='max', vmax=440, vmin=390))
ax.coastlines()
co2graph.plot(cmap='jet',vmax=430, vmin=390)
plt.title('summer', pad=1)
# plt.xlabel('latitude')
# plt.ylabel('longitude')
plt.show()
