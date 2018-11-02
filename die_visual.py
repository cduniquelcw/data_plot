import pygal
import matplotlib.pyplot as plt

from die import Die

#创建2个Die
die_1 = Die()
die_2 = Die(8)

#掷几次骰子，并储存结果
results = []
for roll_num in range(10000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2,max_result + 1)]

# x_value = list(range(3,max_result + 1))
# plt.scatter(x_value,frequencies,linewidth=3)
# plt.show()

#可视化
hist = pygal.Bar()
title_original = 'D' + str(die_1.num_sides) + ' + D' + str(die_2.num_sides)
hist.title = 'Results of rolling ' + title_original +' 10000 times.'
hist.x_labels = list(range(2,max_result + 1))
hist.x_title = 'Result'

hist.y_title = 'Frenquency' 

hist.add(title_original,frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)
