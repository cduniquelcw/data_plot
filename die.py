from random import randint

class Die():
	"""创建一个骰子的类"""

	def __init__(self,num_sides=6):
		"""默认6面骰子"""
		self.num_sides = num_sides

	def roll(self):
		"""返回一个位于1和骰子面数之间的随机数"""
		return randint(1,self.num_sides)
