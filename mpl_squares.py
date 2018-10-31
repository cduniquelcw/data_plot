import matplotlib.pyplot as plt

input_value = [1,2,3,4,5,6]
squares = [1,4,9,16,25,36]

plt.plot(input_value,squares,linewidth = 3)#线条粗细

#标题，坐标标签
plt.title('Square Numbers',fontproperties = 'SimHei',fontsize = 24)
plt.xlabel('值',fontproperties = 'SimHei',fontsize=14)
plt.ylabel('平方',fontproperties="SimSun",fontsize = 14)

#刻度标记的大小
plt.tick_params(axis = 'both', labelsize = 12)
plt.show()