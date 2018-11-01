from random import choice

class RandomWalk():
	"""一个生成随机漫步的类"""

	def __init__(self,num_points=5000):
		self.num_points = num_points

		#
		self.x_values = [0]
		self.y_values = [0]

	def get_step(self):
		""""""
		direction = choice([1,-1])
		distance = choice([0,1,2,3,4])
		step = direction * distance
		return step
	def fill_walk(self):
		"""计算随机漫步包含的所有点"""

		#到达条件前不停止
		while len(self.x_values) < self.num_points:

			#漫步方向
			x_step = self.get_step()
			y_step = self.get_step()

			#拒绝原地踏步
			if x_step == 0 and y_step == 0:
				continue

			#计算下一个点的x y
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)
