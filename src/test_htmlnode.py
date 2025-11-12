import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_tag_error(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("p", "text")])
            node.to_html()

    def test_to_html_children_error(self):
        with self.assertRaises(ValueError):
            node = ParentNode("div", None)
            node.to_html()

    def test_to_html_empty_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("div", [])
            node.to_html()

    def test_to_html_with_props(self):
        child = LeafNode(None, "text")
        node = ParentNode("section", [child], {"class": "highlight"})
        self.assertEqual(node.to_html(), '<section class="highlight">text</section>')

    def test_to_html_mixed_children(self):
        children = [
            LeafNode("b", "Bold"),
            LeafNode(None, " and normal "),
            LeafNode("i", "Italic"),
        ]
        node = ParentNode("p", children)
        self.assertEqual(node.to_html(), "<p><b>Bold</b> and normal <i>Italic</i></p>")

    def test_to_html_deep_nesting(self):
        inner = ParentNode("span", [LeafNode("em", "deep")])
        outer = ParentNode("div", [inner])
        self.assertEqual(outer.to_html(), "<div><span><em>deep</em></span></div>")



if __name__ == "__main__":
    unittest.main()