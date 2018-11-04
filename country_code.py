from pygal.maps.world import COUNTRIES

def get_country_code1(country_name):
	"""根据指定的国家， 返回Pygal使用的两个字母的国别码"""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
# 如果没有找到指定的国家， 就返回None
	return None

def get_country_code2(country_name):
	for code in sorted(COUNTRIES.keys()):
		if country_name == COUNTRIES[code]:
			return code
	return None