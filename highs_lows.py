import csv
import matplotlib.pyplot as plt

from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates,highs,lows = [],[],[]

	for row in reader:
		try:
			current_date = datetime.strptime(row[0],'%Y/%m/%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)



	fig = plt.figure(dpi=128,figsize=(10,6))
	plt.plot(dates,highs,c='red',alpha=0.5,linewidth=1)
	plt.plot(dates,lows,c='blue',linewidth=1,alpha=0.5,)
	plt.fill_between(dates,highs,lows,facecolor='yellow',alpha=0.1)

	plt.title('日最高/最低气温 of 2014',fontproperties='SimHei',fontsize=24)
	plt.xlabel('',fontproperties='simsun',fontsize=12)
	fig.autofmt_xdate()
	plt.ylabel('气温',fontproperties='KaiTi',fontsize=12)
	plt.tick_params(axis='both',which='major',labelsize=12)

	plt.show()