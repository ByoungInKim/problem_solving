import unittest

class quick_union:
    id = []
    sz = []
    def __init__(self, size):
        for i in range(size):
            self.id.append(i)
            self.sz.append(1)

    def union(self, p, q):
        p_root = self._find_root(p)
        q_root = self._find_root(q)

        if p_root == q_root:
            return
        
        if self.sz[p_root] < self.sz[q_root]:
            self.id[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]
        else:
            self.id[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]

    def connected(self, p, q):
        if self._find_root(p) == self._find_root(q):
            return True
        else:
            return False
    
    def _find_root(self, p):
        root_index = p
        while (root_index != self.id[root_index]):
            root_index = self.id[root_index]
        return root_index

class unit_test(unittest.TestCase):
    def setUp(self):
        self.data = quick_union(10)
        self.data.union(1, 2)
        self.data.union(3, 4)
        self.data.union(2, 8)
        self.data.union(0, 5)
        self.data.union(5, 6)
        self.data.union(7, 8)
        self.data.union(7, 9)

    def test_case(self):
        self.assertEqual(True, self.data.connected(1, 2))
        self.assertEqual(True, self.data.connected(2, 9))
        
        self.assertEqual(False, self.data.connected(0, 1))

