import json

import pygal.maps.world as pmw

from country_code import get_country_code1
from pygal.style import RotateStyle,LightColorizedStyle

filename = 'gdp.json'
with open(filename) as f:
	gdp_date = json.load(f)

#2016gdp
cc_gdp = {}
for gdp_dict in gdp_date:
	if gdp_dict['Year'] == 2016:
		country_name = gdp_dict['Country Name']
		gdp = int(float(gdp_dict['Value']))
		code = get_country_code1(country_name)
		if code:
			cc_gdp[code] = gdp


gdp_1,gdp_2,gdp_3,gdp_4 = {},{},{},{}
for cc,gdp in cc_gdp.items():
	if gdp < 100000000000:
		gdp_1[cc] = gdp
	elif gdp < 1000000000000:
		gdp_2[cc] = gdp
	elif gdp < 10000000000000:
		gdp_3[cc] = gdp
	else:
		gdp_4[cc] = gdp

wm_style = RotateStyle('#930322',base_style=LightColorizedStyle)
wm = pmw.World(style=wm_style)
wm.add('<100bn',gdp_1)
wm.add('<1tn',gdp_2)
wm.add('<10tn',gdp_3)
wm.add('10tn+',gdp_4)
wm.render_to_file('world_gdp.svg')

