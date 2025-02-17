import unittest

from htmlnode import LeafNode

class TestLEAFNode(unittest.TestCase):
    def test_true(self):
        node = LeafNode("div", "Hello, World!")
        print(node.__repr__())
        print(node.to_html())
        self.assertTrue(node)

    def test_true2(self):
        node = LeafNode("div", None, {"Hi": "Bye",})
        self.assertTrue(node)

    def test_true3(self):
        node = LeafNode(None, "Hello, World!", {"Hi": "Bye",})
        print(node.__repr__())
        print(node.to_html())
        self.assertTrue(node)

    def test_true4(self):
        node = LeafNode("div", "Hello, World!", {"Hi": "Bye",})
        print(node.__repr__())
        print(node.to_html())
        self.assertTrue(node)

    def test_true5(self):
        node = LeafNode("div", "Hello, World!")
        print(node.__repr__())
        print(node.to_html())
        self.assertTrue(node)

if __name__ == "__main__":
    unittest.main()