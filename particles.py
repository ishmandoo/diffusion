import random
import numpy as np

class Particle:
	def __init__(self, trap):
		self.trap = trap
		self.starting_trap = trap
	def getDisplacement(self):
		return self.trap.pos - self.starting_trap.pos
	def step(self):
		rand = random.uniform(0, 1)
		if rand < self.trap.left_prob:
			if not self.trap.left == None:
				self.trap = self.trap.left
			else:
				print "oops"
		elif rand > (1.-self.trap.right_prob):
			if not self.trap.right == None:
				self.trap = self.trap.right
			else:
				print "oops"


class Trap:
	def __init__(self, pos, left, right, left_prob, right_prob):
		self.pos = pos
		self.left = left
		self.right = right
		self.left_prob = left_prob
		self.right_prob = right_prob
		assert(left_prob + right_prob <= 1)
	def __repr__(self):
		return "pos %s, left prob %s, right prob %s" % (self.pos, self.left_prob, self.right_prob)
