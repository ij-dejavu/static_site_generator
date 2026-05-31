import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_no_image(self):
        node = TextNode("Just plain text", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result, [node])

    def test_single_image(self):
        node = TextNode("Hello ![cat](https://cats.com) world", TextType.TEXT)
        result = split_nodes_image([node])
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "https://cats.com"),
            TextNode(" world", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_images(self):
        node = TextNode(
            "Start ![one](https://one.com) middle ![two](https://two.com) end",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        expected = [
            TextNode("Start ", TextType.TEXT),
            TextNode("one", TextType.IMAGE, "https://one.com"),
            TextNode(" middle ", TextType.TEXT),
            TextNode("two", TextType.IMAGE, "https://two.com"),
            TextNode(" end", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_image_at_start(self):
        node = TextNode("![start](https://start.com) then text", TextType.TEXT)
        result = split_nodes_image([node])
        expected = [
            TextNode("start", TextType.IMAGE, "https://start.com"),
            TextNode(" then text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_image_at_end(self):
        node = TextNode("text then ![end](https://end.com)", TextType.TEXT)
        result = split_nodes_image([node])
        expected = [
            TextNode("text then ", TextType.TEXT),
            TextNode("end", TextType.IMAGE, "https://end.com"),
        ]
        self.assertEqual(result, expected)

    def test_no_link(self):
        node = TextNode("Just plain text", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result, [node])

    def test_single_link(self):
        node = TextNode("Hello [boot](https://boot.dev) world", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("boot", TextType.LINK, "https://boot.dev"),
            TextNode(" world", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        node = TextNode(
            "Start [one](https://one.com) middle [two](https://two.com) end",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        expected = [
            TextNode("Start ", TextType.TEXT),
            TextNode("one", TextType.LINK, "https://one.com"),
            TextNode(" middle ", TextType.TEXT),
            TextNode("two", TextType.LINK, "https://two.com"),
            TextNode(" end", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_link_at_start(self):
        node = TextNode("[start](https://start.com) then text", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("start", TextType.LINK, "https://start.com"),
            TextNode(" then text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_link_at_end(self):
        node = TextNode("text then [end](https://end.com)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("text then ", TextType.TEXT),
            TextNode("end", TextType.LINK, "https://end.com"),
        ]
        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()