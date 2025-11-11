import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_html1(self):
        node = HTMLNode("a", "Click me", [],{"href": "https://example.com", "target": "_blank"})
        expected = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_html2(self):
        node = HTMLNode("p", "Hello", [], {})
        self.assertEqual(node.props_to_html(),"")

    def test_props_html3(self):
        node = HTMLNode("img", None, [], {"src":"image.png"})
        expected = ' src="image.png"'
        self.assertEqual(node.props_to_html(), expected)

    def test_leaf_to_html1(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html2(self):
        node = LeafNode("a", "Click me!",{"href": "www.google.com"})
        self.assertEqual(node.to_html(), '<a href="www.google.com">Click me!</a>')

    def test_leaf_to_html3(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html4(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()


if __name__ == "__main__":
    unittest.main()