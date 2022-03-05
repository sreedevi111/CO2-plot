import matplotlib.pyplot as plt
from pylab import np
import xarray as xr
import geopandas as pd
f = pd.open_mfdataset('*.nc')
co2 = f.co2
lat = co2.latitude[:]
lon = co2.longitude[:]
l = co2.level[:]
where_lnid = np.where((lon >= 70) & (lon <= 90))[0]
where_ltid = np.where((lat >= 10) & (lon <= 25))[0]
where_level = np.where((l >= 1) & (1 <= 16))
slat_id = where_ltid[0]
elat_id = where_ltid[-1] + 1
slon_id = where_lnid[0]
elon_id = where_lnid[-1] + 1
co2_ind = co2[:, :, where_ltid[:], where_lnid[:]]
co2_ind = co2_ind.mean('latitude').mean('longitude').mean('time')
plt.plot(co2_ind[0:17], range(len(co2_ind))[0:17])
plt.show()
