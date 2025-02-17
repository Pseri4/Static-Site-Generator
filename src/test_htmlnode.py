import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_true(self):
        node = HTMLNode("div", "Hello, World!")
        print(node.__repr__())
        self.assertTrue(node)

    def test_true2(self):
        node = HTMLNode("div", None, 3, {"Hi": "Bye",})
        print(node.__repr__())
        self.assertTrue(node)

    def test_true3(self):
        node = HTMLNode("div", "Hello, World!", None, {"Hi": "Bye",})
        print(node.__repr__())
        self.assertTrue(node)

    def test_true4(self):
        node = HTMLNode("div", "Hello, World!", None, {"Hi": "Bye",})
        print(node.__repr__())
        self.assertTrue(node)

    def test_true5(self):
        node = HTMLNode("div", "Hello, World!", 3)
        print(node.__repr__())
        self.assertTrue(node)

if __name__ == "__main__":
    unittest.main()