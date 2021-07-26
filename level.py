import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
ds = xr.open_mfdataset('*_spring_*.nc')
co2 = ds.co2.mean('time')
co2graph = co2.isel(level=1)
ax = plt.axes(projection=ccrs.PlateCarree())
#ax = co2graph.plot( cmap='jet', extend='max', vmax=440, vmin=390))
ax.coastlines()
co2graph.plot(cmap='coolwarm',vmax=440, vmin=390)
plt.title('Spring 2010-18', pad=1)
# plt.xlabel('latitude')
# plt.ylabel('longitude')

#plt.savefig('Mean variation 2010-18.png level 1', dpi=300, bbox_inches='tight')
plt.show()
