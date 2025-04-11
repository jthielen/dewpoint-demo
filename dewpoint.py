import metpy.calc as mpcalc
from metpy.units import units

mixing = 15 * units('g/kg')
p0 = 850 * units.hPa

e = mpcalc.vapor_pressure(p0, mixing)
td = mpcalc.dewpoint(e)

print(e)
