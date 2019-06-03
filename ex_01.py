class ListNode:
	def __init__(self, v):
		self.v = v
		self.n = None

class Solution:
	def add(self, l1, l2):
		dh = ListNode(0)
		cn = dh
		cr = 0
		while l1 and l2:
			sum = cr + l1.v + l2.v
			cr = int(sum / 10)
			cn.n = ListNode(int(sum % 10))
			cn = cn.n
			l1 = l1.n if l1.n else None
			l2 = l2.n if l2.n else None
		if cr > 0:
			cn.n = ListNode(cr)

		return dh.n

x = ListNode(2)
x.n = ListNode(4)
x.n.n = ListNode(3)

y = ListNode(5)
y.n = ListNode(6)
y.n.n = ListNode(4)

s = Solution()
r = s.add(x,y)

print(r.v, r.n.v, r.n.n.v)

x = ListNode(0)
y = ListNode(0)
r = s.add(x,y)
print(r.v, r.n.v)
