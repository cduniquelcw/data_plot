import json

import pygal.maps.world as pmw
import country_code 
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle



filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

#2010年人口
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = country_code.get_country_code2(country_name)
		if code:
			cc_populations[code] = population
#按照人口数量进行分组
cc_pops1,cc_pops2,cc_pops3 ={},{},{}
for cc,pop in cc_populations.items():
	if pop < 10000000:
		cc_pops1[cc] = pop
	elif pop <1000000000:
		cc_pops2[cc] = pop
	else:
		cc_pops3[cc] = pop
wm_style = RotateStyle('#910106',base_style=LightColorizedStyle)
wm =pmw.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m',cc_pops1)
wm.add('10m-1bn',cc_pops2)
wm.add('1bn+',cc_pops3)

wm.render_to_file('world_populations.svg')