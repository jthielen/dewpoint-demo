import metpy.calc as mpcalc
from metpy.units import units

mixing = 10 * units('g/kg')
p0 = 350 * units.hPa

e = mpcalc.vapor_pressure(p0, mixing)
td = mpcalc.dewpoint(e)

print(e)
