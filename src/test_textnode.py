import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node3 = TextNode("This is a link", TextType.LINK, 'https://www.boot.dev/dashboard')
        node4 = TextNode("This is a link", TextType.LINK,'https://www.boot.dev/u/ij_dejavu')
        self.assertNotEqual(node3, node4)

    def test_eq_3(self):
        node5 = TextNode("This is a image", TextType.IMAGE)
        node6 = TextNode("This is a image", TextType.IMAGE)
        self.assertEqual(node5, node6)

    def test_eq_4(self):
        node7 = TextNode("This is a text", TextType.BOLD)
        node8 = TextNode("This is a text", TextType.ITALIC)
        self.assertNotEqual(node7, node8)

if __name__ == "__main__":
    unittest.main()