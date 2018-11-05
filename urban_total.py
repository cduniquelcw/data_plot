import csv

from country_code import get_country_code1 as gcc
from pygal.style import RotateStyle,LightColorizedStyle


import pygal.maps.world as pmw


fn = 'urban_total.csv'
with open(fn) as f:
	reader = csv.reader(f)
	
	country_name,urban_rate = [],[]

	cc_rate = {}

	count = 0
	for row in reader:
		count += 1
		if count > 5:
			try:
				name = row[0]
				rate= row[61]
				code = gcc(name)
				if code and rate:
					cc_rate[code] = float(rate)


			except IndexError:
				continue

	rate_1,rate_2,rate_3 = {},{},{}

	for cc,rate in cc_rate.items():
		if rate < 50:
			rate_1[cc] = rate
		elif rate < 75:
			rate_2[cc] = rate
		else:
			rate_3[cc] = rate
wm_style = RotateStyle('#190591',base_style=LightColorizedStyle)
wm = pmw.World(style=wm_style)
wm.add('<50',rate_1)
wm.add('<75',rate_2)
wm.add('>75',rate_3)
wm.render_to_file('world_urban_rate.svg')
