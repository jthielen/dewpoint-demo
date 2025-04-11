import metpy.calc as mpcalc
from metpy.units import units

mixing = 14 * units('g/kg')
p0 = 1013 * units.hPa

e = mpcalc.vapor_pressure(p0, mixing)
td = mpcalc.dewpoint(e)

print(e)
