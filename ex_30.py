class Node:
	def __init__(self, k):
		self.l = None
		self.r = None
		self.k = k

class Tree:
	def cn(self, k):
		return Node(k)

	def ins(self, n, k):
		if n is None:
			return self.cn(k)

		if k < n.k:
			n.l = self.ins(n.l, k)

		if k > n.k:
			n.r = self.ins(n.r, k)

		return n

	def inO(self, n):
		if n is not None:
			self.inO(n.l)
			print(n.k)
			self.inO(n.r)

	def sr(self, n, k):
		if n is None:
			print('not found')
			return

		if k == n.k:
			print('found')
			return

		if k < n.k:
			self.sr(n.l, k)

		if k > n.k:
			self.sr(n.r, k)

	def min(self, n):
		if n is None:
			return

		while n:
			cn = n
			n = n.l

		print('min is : ' + str(cn.k))

	def max(self, n):
		if n is None:
			return

		while n:
			cn = n
			n = n.r

		print('max is : ' + str(cn.k))

	def BFS(self, n):
		if n is None:
			return

		q = []
		q.append(n)
		while len(q) > 0:
			n = q.pop(0)
			print n.k

			if n.l:
				q.append(n.l)
			if n.r:
				q.append(n.r)
t = Tree()
r = t.ins(None, 0)
t.ins(r, 10)
t.ins(r, 5)
t.ins(r, -1)
t.ins(r, 90)
t.ins(r, 100)
print('sorted order')
t.inO(r)
t.sr(r, 6)
t.sr(r, 5)
		
t.min(r)
t.max(r)

print('BFS')
t.BFS(r)
