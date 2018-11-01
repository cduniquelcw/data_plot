import matplotlib.pyplot as plt

x_value=list(range(1,1001))
y_value=[x**2 for x in x_value]
plt.scatter(x_value,y_value,c=y_value,
	cmap=plt.cm.Blues,edgecolor='none',s=40)

#标题，坐标标签
plt.title('散点',fontproperties='simhei',fontsize=24)
plt.xlabel('值',fontproperties='simsun',fontsize=20)
plt.ylabel('平方',fontproperties='kaiti',fontsize=20)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1000,0,1000000])
plt.savefig('scatter_plot.png',bbox_inches='tight')