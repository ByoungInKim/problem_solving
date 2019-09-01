import unittest

class quick_find:
    id = []
    def __init__(self, size):
        for i in range(size):
            self.id.append(i)

    def union(self, p, q):
        p_conn = self.id[p]
        q_conn = self.id[q]

        for i in range(len(self.id)):
            if q_conn != self.id[i]:
                continue
            self.id[i] = p_conn

    def connected(self, p, q):
        if self.id[p] == self.id[q]:
            return True
        else:
            return False

class unit_test(unittest.TestCase):
    def setUp(self):
        self.data = quick_find(10)
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

